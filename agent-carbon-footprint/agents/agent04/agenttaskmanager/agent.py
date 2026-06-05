# src\agent-carbon-footprint\agents\agent04\agenttaskmanager\agent.py

from google.adk.agents.llm_agent import Agent
from trello import TrelloClient
from dotenv import load_dotenv
from datetime import datetime
import os

load_dotenv()

API_KEY = os.getenv('TRELLO_API_KEY')
API_SECRET = os.getenv('TRELLO_API_SECRET')
TOKEN = os.getenv('TRELLO_TOKEN')
BOARD_NAME = os.getenv('TRELLO_BOARD_NAME', 'Agente CSC_Roboot')


def get_temporal_context():
    now = datetime.now()
    return now.strftime('%Y/%m/%d %H:%M:%S')


def _get_board():
    client = TrelloClient(api_key=API_KEY, api_secret=API_SECRET, token=TOKEN)
    boards = client.list_boards()
    matches = [b for b in boards if b.name == BOARD_NAME]
    if not matches:
        raise ValueError(f"Board '{BOARD_NAME}' não encontrado.")
    return matches[0]


def listar_boards() -> list:
    """Lista todos os boards disponíveis para diagnóstico."""
    try:
        client = TrelloClient(api_key=API_KEY, api_secret=API_SECRET, token=TOKEN)
        boards = client.list_boards()
        return [{"nome": b.name, "id": b.id} for b in boards]
    except Exception as e:
        return [{"erro": str(e)}]


def criar_lista(nome_da_lista: str) -> str:
    """Cria uma nova lista no board configurado."""
    try:
        board = _get_board()
        listas_existentes = board.list_lists()
        ja_existe = any(l.name.upper() == nome_da_lista.upper() for l in listas_existentes)
        if ja_existe:
            return f"⚠️ A lista '{nome_da_lista}' já existe no board '{BOARD_NAME}'."
        board.add_list(nome_da_lista)
        return f"✅ Lista '{nome_da_lista}' criada com sucesso no board '{BOARD_NAME}'."
    except Exception as e:
        return f"❌ Erro ao criar lista: {str(e)}"


def adicionar_tarefa(nome_da_task: str, descricao_da_task: str, due_date: str) -> str:
    try:
        board = _get_board()
        listas = board.list_lists()
        candidatas = [l for l in listas if l.name.upper() in ['TO DO', 'A FAZER']]
        if not candidatas:
            return "❌ Nenhuma lista 'A Fazer' ou 'To Do' encontrada. Crie a lista primeiro."
        minha_lista = candidatas[0]
        minha_lista.add_card(name=nome_da_task, desc=descricao_da_task, due=due_date)
        return f"✅ Tarefa '{nome_da_task}' criada na lista '{minha_lista.name}'."
    except Exception as e:
        return f"❌ Erro ao adicionar tarefa: {str(e)}"


def listar_tarefas(status: str = "todas") -> list:
    try:
        board = _get_board()
        listas = board.list_lists()

        if status.lower() == "todas":
            listas_filtradas = listas
        elif status.lower() == "a fazer":
            listas_filtradas = [l for l in listas if l.name.upper() in ['A FAZER', 'TO DO', 'TODO']]
        elif status.lower() == "em andamento":
            listas_filtradas = [l for l in listas if l.name.upper() in ['EM ANDAMENTO', 'DOING']]
        elif status.lower() == "concluido":
            listas_filtradas = [l for l in listas if l.name.upper() in ['CONCLUÍDO', 'CONCLUIDO', 'DONE']]
        else:
            listas_filtradas = listas

        tarefas = []
        for lista in listas_filtradas:
            for card in lista.list_cards():
                tarefas.append({
                    "nome": card.name,
                    "descricao": card.desc,
                    "vencimento": card.due,
                    "status": lista.name,
                    "id": card.id
                })
        return tarefas
    except Exception as e:
        return [{"erro": str(e)}]


def mudar_status_tarefa(nome_da_task: str, novo_status: str) -> str:
    try:
        board = _get_board()
        listas = board.list_lists()

        status_map = {
            "a fazer": "A FAZER",
            "em andamento": "EM ANDAMENTO",
            "concluido": "CONCLUÍDO"
        }

        nome_lista_destino = status_map.get(novo_status.lower())
        if not nome_lista_destino:
            return "❌ Status inválido. Use: 'a fazer', 'em andamento' ou 'concluido'"

        lista_destino = next(
            (l for l in listas if l.name.upper() == nome_lista_destino.upper()), None
        )
        if not lista_destino:
            return f"❌ Lista '{nome_lista_destino}' não encontrada. Crie a lista primeiro."

        card_encontrado = None
        lista_origem = None
        for lista in listas:
            card_encontrado = next(
                (c for c in lista.list_cards() if c.name.lower() == nome_da_task.lower()), None
            )
            if card_encontrado:
                lista_origem = lista
                break

        if not card_encontrado:
            return f"❌ Card '{nome_da_task}' não encontrado."

        card_encontrado.change_list(lista_destino.id)
        return f"✅ '{nome_da_task}': {lista_origem.name} → {lista_destino.name}"
    except Exception as e:
        return f"❌ Erro: {str(e)}"


root_agent = Agent(
    model='gemini-3.5-flash',
    name='root_agent',
    description='Agente de Organização de Tarefas',
    instruction=f"""
        Você é um agente de organização de tarefas integrado ao Trello.
        O board configurado atualmente é: '{BOARD_NAME}'.

        Suas funções:
        1. Listar todos os boards disponíveis (diagnóstico) via listar_boards
        2. Criar listas no board quando o usuário pedir (ex: "cria a lista A Fazer")
        3. Adicionar novas tarefas com nome, descrição e data de vencimento
        4. Listar todas as tarefas ou filtrar por status
        5. Mudar o status de uma tarefa entre listas
        6. Informar a data e hora atual via get_temporal_context

        Regras importantes:
        - Se o usuário pedir para ver os boards disponíveis, use listar_boards() imediatamente.
        - Se o usuário pedir para criar uma lista, use criar_lista() imediatamente.
        - Se o usuário tentar adicionar uma tarefa e não houver lista 'A Fazer',
          pergunte se deseja criá-la antes.
        - Nunca invente listas ou tarefas que não existam no board.
        - Sempre confirme ações realizadas com o resultado retornado pela tool.

        Ao iniciar a conversa, use get_temporal_context para informar a data atual
        e pergunte como pode ajudar com as tarefas do dia.
    """,
    tools=[
        get_temporal_context,
        listar_boards,
        criar_lista,
        adicionar_tarefa,
        listar_tarefas,
        mudar_status_tarefa,
    ],
)