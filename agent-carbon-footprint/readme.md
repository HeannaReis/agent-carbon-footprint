<!--START_SECTION:header-->
<div align="center">
  <p align="center">
    <img 
      alt="DIO Education" 
      src="https://raw.githubusercontent.com/digitalinnovationone/template-github-trilha/main/.github/assets/logo.webp" 
      width="100px" 
    />
    <h1>🤖 Agentes ADK — Pegada de Carbono & Automação de Tarefas</h1>
    <p>Documentação técnica dos agentes desenvolvidos com Google ADK e Gemini 2.5 Flash</p>
  </p>
</div>
<!--END_SECTION:header-->

<p align="center">
  <img src="https://img.shields.io/static/v1?label=Google%20ADK&message=Multi-Agent&color=4285F4&labelColor=202024&logo=google&logoColor=white" alt="Google ADK" />
  <img src="https://img.shields.io/static/v1?label=Gemini&message=2.5-flash&color=8E24AA&labelColor=202024" alt="Gemini" />
  <img src="https://img.shields.io/static/v1?label=Trello&message=API&color=0052CC&labelColor=202024&logo=trello&logoColor=white" alt="Trello" />
  <img src="https://img.shields.io/static/v1?label=Python&message=3.10%2B&color=3776AB&labelColor=202024&logo=python&logoColor=white" alt="Python" />
</p>

---

## 🌱 Agente 1 — Pegada de Carbono (`agentCoder/`)

Agente orquestrador que guia o usuário no cálculo, compreensão e redução da sua pegada de carbono pessoal.

### Arquitetura

```text
root_agent (orquestrador)
├── search_agent    → busca na web via Google Search
└── coding_agent    → escreve e executa código Python
```

### Fluxo do usuário

| Etapa | Agente responsável | Ação |
|---|---|---|
| Coleta de dados | Carbon Intake | Perguntas empáticas sobre transporte, energia, alimentação |
| Cálculo | Carbon Calculator | Soma emissões e gera baseline em tCO₂e/ano |
| Explicação | Carbon Explainability | Traduz números em linguagem humana com analogias |
| Recomendações | Carbon Advisor | Ações práticas classificadas por impacto × esforço |
| Metas | Carbon Goal | Define metas e acompanha progresso |

### Como executar

```bash
cd src/agent-carbon-footprint
adk web agentCoder
```

---

## ✅ Agente 2 — Tarefas Trello (`agents/agent04/agenttaskmanager/`)

Agente conversacional que gerencia tarefas no Trello via linguagem natural.

### Ferramentas disponíveis

| Ferramenta | Descrição |
|---|---|
| `get_temporal_context` | Retorna data e hora atual |
| `listar_boards` | Lista todos os boards disponíveis |
| `criar_lista` | Cria uma nova lista no board configurado |
| `adicionar_tarefa` | Adiciona card na lista "A Fazer" |
| `listar_tarefas` | Lista tarefas com filtro por status |
| `mudar_status_tarefa` | Move card entre listas |

### Status suportados

| Status | Lista no Trello |
|---|---|
| `a fazer` | A FAZER / TO DO |
| `em andamento` | EM ANDAMENTO / DOING |
| `concluido` | CONCLUÍDO / DONE |

### Como executar

```bash
cd src/agent-carbon-footprint/agents/agent04
adk web agenttaskmanager
```

> Para configurar as credenciais do Trello, consulte o [Guia de Registro no Trello](agents/agent04/readme.md).

---

## 📚 Pré-requisitos

| Habilidade | Nível |
|---|---|
| Python | Intermediário |
| APIs REST | Básico |
| Variáveis de ambiente (`.env`) | Básico |
| Conceitos de agentes de IA | Básico |
| Trello (uso básico) | Básico |

---

## 🛠️ Habilidades exercitadas

- Criação de agentes com `Agent` e orquestração com `AgentTool`
- Uso de ferramentas nativas: `google_search`, `BuiltInCodeExecutor`
- Integração com API do Trello via `py-trello`
- Gerenciamento de credenciais com `.env`
- Separação de responsabilidades entre agentes especializados

---

## 💬 Exemplo de Uso — Agente Trello em Ação

Vamos ver um fluxo completo de gerenciamento de tarefas, desde um board vazio até a alteração de status e prazos.

### 1. Começando: O Agente Confirma que Não Há Tarefas

A primeira interação mostra o agente verificando o board e confirmando que não há tarefas pendentes.


![Agente confirmando que não há tarefas](assets/sem_tarefa.png)


### 2. Criação: Adicionando Novas Tarefas

O usuário adiciona várias tarefas manualmente.

![Board do Trello com novas tarefas](assets/add_tarefas_tello.png)

Faz nova pergunta sobre as tarefas e o Agente retorna as tarefas adicionadas manualmente.

![Interface de consulta via pergunta](assets/nova_pergunta_com_tarefa.png)


### 3.  Ajuste Fino: Alterando o Prazo de uma Tarefa

O agente também pode ajustar detalhes como datas de vencimento.

**A conversa com o agente:**

![Conversa para alterar prazo](assets/alterar_prazo.png)


**O resultado no Trello:**

![Tarefa com prazo atualizado no Trello](assets/tarefa_com_prazo.png)


### 4.  Modificação: Alterando o Status de uma Tarefa

Em seguida, o usuário pede para mover uma tarefa para "Em Andamento".

**A conversa com o agente:**

![Conversa para alterar status](assets/alterar_para_andamento.png)


**O resultado no Trello:**

![Tarefa movida para Em Andamento no Trello](assets/tarefa_em_andamento_trello.png)

**Resposta do Agente:**

![Confirmação de alteração do Agente](assets/tarefa_alterada.png)


### 5. Remover Tarefas

Tentativa de remover uma tarefa
![Resultado de uma alteração complexa](assets/resulta_alterar_e_remover.png)


### 6. Criar Tarefas com o Agente 

Criando Tarefa com iteração via agente Trello
![Solicitação para criar Tarefa](assets/agente_criando_tarefa.png)

Interface do Trello com a tarefa criada pelo agente com descrição e prazo.

![Tarefa criada no Trello](assets/tarefa_criada_agente.png)

<!--START_SECTION:footer-->
<p align="center">
  <a href="https://www.dio.me/" target="_blank">
    <img align="center" src="https://raw.githubusercontent.com/digitalinnovationone/template-github-trilha/main/.github/assets/footer.png" alt="banner"/>
  </a>
</p>
<!--END_SECTION:footer-->