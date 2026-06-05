from google.adk.agents.llm_agent import Agent
from google.adk.tools.agent_tool import AgentTool
from google.adk.tools import google_search
from google.adk.code_executors import BuiltInCodeExecutor

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())  # Busca o .env subindo diretórios automaticamente

search_agent = Agent(
    model='gemini-3.5-flash',
    name='search_agent',
    description='Você é um agente especilizado em busca na web via Google Search.',
    instruction="""
        Você é um agente especilizado em busca na web via Google Search
        Use a ferramenta de busca para responder perguntas do usuário.
        """,
    tools=[google_search],
)

coding_agent = Agent(
    model='gemini-3.5-flash',
    name='coding_agent',
    description='Você é um agente especilizado em escrever código e executar codigo.',
    instruction="""
        Você é um agente especilizado em escrever código e executar codigo.
        Use a ferramenta de execução de código para executar o código que você escreveu.
        """,
    code_executor=BuiltInCodeExecutor(),
)

root_agent = Agent(
    model='gemini-3.5-flash',
    name='root_agent',
    description='Você é o agente principal e orquestrador.',
    instruction='Você é o agente principal e orquestrador',
    tools=[AgentTool(agent=search_agent), AgentTool(agent=coding_agent)],

)
