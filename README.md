<!--START_SECTION:header-->
<div align="center">
  <p align="center">
    <img 
      alt="DIO Education" 
      src="https://raw.githubusercontent.com/digitalinnovationone/template-github-trilha/main/.github/assets/logo.webp" 
      width="100px" 
    />
    <h1>🤖 Agente de Automação de Fluxo de Trabalho com Trello e Google ADK</h1>
    <p>Desafio DIO — Criando um Agente para Automatizar um Fluxo de Trabalho em Python</p>
  </p>
</div>
<!--END_SECTION:header-->

<p align="center">
  <img src="https://img.shields.io/static/v1?label=DIO&message=Education&color=E94D5F&labelColor=202024" alt="DIO Project" />
  <a href="NIVEL"><img src="https://img.shields.io/static/v1?label=Nivel&message=Intermediário&color=E94D5F&labelColor=202024" alt="Nivel"></a>
  <img src="https://img.shields.io/static/v1?label=Python&message=3.10%2B&color=3776AB&labelColor=202024&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/static/v1?label=Google%20ADK&message=Multi-Agent&color=4285F4&labelColor=202024&logo=google&logoColor=white" alt="Google ADK" />
  <img src="https://img.shields.io/static/v1?label=Gemini&message=2.5-flash&color=8E24AA&labelColor=202024" alt="Gemini" />
  <img src="https://img.shields.io/static/v1?label=Trello&message=API&color=0052CC&labelColor=202024&logo=trello&logoColor=white" alt="Trello" />
</p>

<!--  -->
<table align="center">
<thead>
  <tr>
    <td align="center">
      <p><strong>Autor do Projeto</strong></p>
      <a href="https://github.com/HeannaReis">
        <img
          src="https://avatars.githubusercontent.com/u/67883256?v=4"
          width="120"
          alt="Joel Heanna Reis"
        />
      </a>
      <br/>
      <strong>Joel Heanna Reis</strong>
    </td>
    <td>
      <p>
        🎯 Desenvolvedor Back-End com foco em Java, Python, Inteligência Artificial e Automação de Processos.
        <br/><br/>
        🏆 1º Lugar no Desafio de Projetos de IA da Stefanini Brasil.
        <br/><br/>
        💼 Atuação em projetos SAP Ariba — SLP, Procurement, Master Data e integrações corporativas.
        <br/><br/>
        🤖 Experiência no desenvolvimento de assistentes inteligentes, automações com Python, APIs REST e integração com modelos de IA.
        <br/><br/>
        ⚙️ Entusiasta de Arquitetura de Software, Engenharia de Dados e soluções que geram impacto real nos negócios.
        <br/><br/>
        ⚽ Voluntário em projeto social de formação esportiva infantil.
      </p>
      <a href="https://www.linkedin.com/in/joel-heanna-reis/">
        <img alt="LinkedIn" src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white">
      </a>
      <a href="https://github.com/HeannaReis">
        <img alt="GitHub" src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white">
      </a>
      <a href="https://www.instagram.com/heannareis/">
        <img alt="Instagram" src="https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white">
      </a>
    </td>
  </tr>
</thead>
</table>
<!--  -->

<br/>
<br/>

## 💻 Sobre o Projeto

Este projeto implementa um sistema **multi-agente com Google ADK** para automação de fluxo de trabalho, desenvolvido como solução do desafio da DIO.

São dois agentes independentes:

- **Agente de Pegada de Carbono** — guia o usuário no cálculo e redução da sua pegada de carbono pessoal
- **Agente de Tarefas Trello** — gerencia tarefas no Trello via linguagem natural

Ambos utilizam **Gemini 2.5 Flash** como motor de linguagem e são executados via `adk web`.

---

## 🗂️ Estrutura do Repositório

```text
src/agent-carbon-footprint/
├── agentCoder/
│   ├── __init__.py
│   └── agent.py                          # Agente de carbono (search + code executor)
├── agents/
│   ├── 00.agent-orquestrador.md          # Spec: Orquestrador de agentes
│   ├── 01.agent-carbon-Intake.md         # Spec: Coleta de dados pessoais
│   ├── 03.agent-Carbon-Calculator.md     # Spec: Cálculo da pegada de carbono
│   ├── 04.agent-Carbon-Explainability.md # Spec: Explicação dos resultados
│   ├── 05.agent-Carbon-Advisor.md        # Spec: Recomendações personalizadas
│   ├── 06.agent-Carbon-Goal.md           # Spec: Metas e gamificação
│   └── agent04/
│       ├── agenttaskmanager/
│       │   ├── __init__.py
│       │   └── agent.py                  # Agente de tarefas Trello
│       ├── readme.md                     # Guia de configuração do Trello
│       └── requirements.txt
└── readme.md                             # Documentação detalhada do sistema de carbono
```

---

## 🤖 Agentes do Projeto

### 1. Agente de Pegada de Carbono (`agentCoder/agent.py`)

Agente orquestrador que guia o usuário no cálculo, compreensão e redução da sua pegada de carbono pessoal.

**Motor de IA:** Gemini 2.5 Flash  
**Interface:** `adk web`

| Sub-agente | Responsabilidade |
|---|---|
| `search_agent` | Busca informações na web via Google Search |
| `coding_agent` | Escreve e executa código Python dinamicamente |
| `root_agent` | Orquestra os demais agentes |

---

### 2. Agente de Tarefas Trello (`agenttaskmanager/agent.py`)

Agente conversacional que gerencia tarefas no Trello via linguagem natural.

**Motor de IA:** Gemini 2.5 Flash  
**Interface:** `adk web`

#### Ferramentas disponíveis

| Ferramenta | Descrição |
|---|---|
| `get_temporal_context` | Retorna data e hora atual |
| `listar_boards` | Lista todos os boards do Trello |
| `criar_lista` | Cria uma nova lista no board configurado |
| `adicionar_tarefa` | Adiciona um card na lista "A Fazer" |
| `listar_tarefas` | Lista tarefas com filtro por status |
| `mudar_status_tarefa` | Move um card entre listas |

---

## 📚 Pré-requisitos de Habilidades e Níveis de Conhecimento

| Habilidade | Nível |
|---|---|
| Python | Intermediário |
| APIs REST | Básico |
| Variáveis de ambiente (`.env`) | Básico |
| Conceitos de agentes de IA | Básico |
| Trello (uso básico) | Básico |

---

## 🛠️ Habilidades que você vai exercitar neste projeto

- **Agentes de IA com Google ADK**
  - Criação de agentes especializados com `Agent`
  - Orquestração multi-agente com `AgentTool`
  - Uso de ferramentas nativas: `google_search`, `BuiltInCodeExecutor`
- **Integração com APIs externas**
  - Autenticação e uso da API do Trello com `py-trello`
  - Registro e autorização de aplicativo no Trello
- **Python**
  - Estruturação de projetos com múltiplos módulos
  - Gerenciamento de estado e contexto em agentes
- **Boas práticas**
  - Gerenciamento de credenciais com `.env`
  - Separação de responsabilidades entre agentes

---

## ⚙️ Configuração e Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/HeannaReis/agent-carbon-footprint.git
cd seu-repositorio
```

### 2. Instale as dependências

```bash
pip install -r requirements.txt
```

### 3. Configure as variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
# Google AI — obrigatório para ambos os agentes
GOOGLE_API_KEY=sua_chave_google_aqui

# Trello — obrigatório apenas para o agente de tarefas
TRELLO_API_KEY=sua_api_key_trello
TRELLO_API_SECRET=seu_api_secret_trello
TRELLO_TOKEN=seu_token_trello
TRELLO_BOARD_NAME=Agente CSC_Roboot
```

> Para obter as credenciais do Trello, siga o [Guia de Registro no Trello](src/agent-carbon-footprint/agents/agent04/readme.md).

---

## ▶️ Como Executar

### Agente de Pegada de Carbono

```bash
cd src/agent-carbon-footprint
adk web agentCoder
```

### Agente de Tarefas Trello

```bash
cd src/agent-carbon-footprint/agents/agent04
adk web agenttaskmanager
```

Acesse no navegador: `http://localhost:8000`

---

## 💬 Exemplo de Uso — Agente Trello

```
Você: cria a lista A Fazer no board
Agente: ✅ Lista 'A Fazer' criada com sucesso no board 'Agente CSC_Roboot'.

Você: adiciona a tarefa "Revisar relatório" com vencimento 2025-07-15
Agente: ✅ Tarefa 'Revisar relatório' criada na lista 'A Fazer'.

Você: lista todas as tarefas
Agente: Aqui estão suas tarefas:
  📋 Revisar relatório | Status: A Fazer | Vencimento: 2025-07-15

Você: muda o status de "Revisar relatório" para em andamento
Agente: ✅ 'Revisar relatório': A Fazer → Em Andamento
```

---

## 🎯 Objetivos e Resultados Esperados

Após explorar este projeto, você estará apto a:

- Criar agentes especializados com **Google ADK** e **Gemini**
- Orquestrar múltiplos agentes com **AgentTool**
- Integrar agentes com **ferramentas externas** (Google Search, Trello, execução de código)
- Autenticar e consumir a **API do Trello** com Python
- Estruturar um projeto de agentes com separação clara de responsabilidades

<!--START_SECTION:footer-->

<br />
<br />

<p align="center">
  <a href="https://www.dio.me/" target="_blank">
    <img align="center" src="https://raw.githubusercontent.com/digitalinnovationone/template-github-trilha/main/.github/assets/footer.png" alt="banner"/>
  </a>
</p>
