# Projeto Ontologia do Banhado do Taim

![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-blue)
![Disciplina](https://img.shields.io/badge/Disciplina-Intelig%C3%AAncia%20Artificial-brightgreen)
![Topico](https://img.shields.io/badge/Topico-Ontologia%20%26%20Web%20Sem%C3%A2ntica-orange)

## Sobre o Projeto

Este repositorio contem o desenvolvimento de uma **Ontologia para o Banhado do Taim**, localizado no Rio Grande do Sul. Este projeto e desenvolvido como parte da disciplina de Inteligencia Artificial, com o objetivo de aplicar tecnicas de representacao de conhecimento a um problema real de relevancia ambiental e social: **atropelamentos de fauna**.

O Banhado do Taim e uma das areas umidas mais importantes do RS, com rica biodiversidade e papel essencial na preservacao de ecossistemas. Ao estruturar o conhecimento sobre especies, habitats, condicoes ambientais e eventos de atropelamento, este trabalho busca organizar e integrar informacoes que hoje estao dispersas.

## Lista de Tarefas (To-Do List)

Esta lista contem todos os requisitos obrigatorios descritos na especificacao do trabalho para garantir a conclusao completa.

### 1. Modelagem da Ontologia
- [ ] Criar no minimo **15 classes** (Animais, Rodovias, Eventos de Atropelamento, Condicoes, etc.)
- [ ] Definir hierarquia de classes.
- [ ] Criar no minimo **10 propriedades de objeto** (Object Properties).
- [ ] Criar no minimo **10 propriedades de dados** (Data Properties).
- [ ] Definir restricoes de propriedade (dominio, alcance, cardinalidade, etc.).
- [ ] Modelar pelo menos **uma relacao temporal**.
- [ ] Modelar pelo menos **uma relacao espacial**.
- [ ] **OBRIGATORIO**: Documentar e justificar as principais decisoes de modelagem.
- [ ] **OBRIGATORIO**: Explicar pelo menos duas alternativas de modelagem que foram consideradas e descartadas.

### 2. Extracao de Conhecimento e Fontes
- [ ] Definir e documentar as fontes de informacao utilizadas (Wikidata, Wikipedia, DBpedia, OpenStreetMap, LLMs, etc.).
- [ ] Descrever a metodologia de extracao de dados no relatorio final.
- [ ] Discutir quaisquer limitacoes ou possiveis erros no processo de extracao.

### 3. Povoamento da Ontologia
- [ ] Povoar a ontologia com no minimo **100 individuos** (instancias).
- [ ] Desenvolver um script automatizado (ex.: Python, NLP, scripts de LLM) para coletar e modelar o conhecimento na ontologia.
- [ ] **OBRIGATORIO**: Explicar claramente como os dados e individuos foram gerados.
- [ ] Fornecer exemplos concretos das instancias criadas.
- [ ] Discutir possiveis inconsistencias ou limitacoes dos dados.

### 4. Consultas SPARQL
- [ ] Implementar um total de pelo menos **30 consultas SPARQL**.
- [ ] Garantir que as consultas cubram os seguintes tipos:
  - [ ] Consultas simples baseadas em classes.
  - [ ] Consultas envolvendo multiplas relacoes.
  - [ ] Consultas com filtros (ex.: por horario, condicoes climaticas).
  - [ ] Consultas com agregacoes.
  - [ ] Consultas representando cenarios relevantes do dominio.
- [ ] Para cada consulta, documentar: Descricao em linguagem natural, o codigo SPARQL e o resultado obtido.

### 5. Integracao com Machine Learning (Opcional)
- [ ] Explicar o modelo de ML utilizado (ex.: preditor de risco de atropelamento).
- [ ] Simular exemplos concretos de predicoes.
- [ ] Demonstrar como a ontologia foi utilizada para gerar explicacoes semanticas para as predicoes.

### 6. Entregas Finais
- [ ] O arquivo da ontologia (`.owl`).
- [ ] O codigo fonte dos scripts de povoamento.
- [ ] O codigo fonte dos algoritmos de ML (se utilizados).
- [ ] Protocolos de emprego de LLMs (se utilizados).
- [ ] **Relatorio Final em PDF** (Deve incluir: capturas de tela do Protege, trechos graficos da ontologia, execucoes SPARQL).
- [ ] **Video Pitch de 5 minutos** explicando a solucao.
- [ ] Preparacao para a apresentacao oral e defesa.

## Estrutura do Repositorio

```
├── docs/                # Documentacao do projeto, relatorios em PDF e apresentacoes
├── ontology/            # Arquivos da ontologia OWL e modelos relacionados
├── scripts/             # Scripts Python para extracao de dados (NLP, scraping) e povoamento
├── sparql_queries/      # Arquivos de texto contendo as consultas SPARQL
└── README.md            # Este arquivo
```

## Tecnologias e Ferramentas
- **Editor de Ontologia**: Protege
- **Linguagens/Frameworks**: Python, OWL, RDF, SPARQL
- **Bibliotecas**: `Owlready2`, `spaCy`, `BeautifulSoup`, `Requests`

## Contribuicao e Equipe
Desenvolvido para a disciplina de Inteligencia Artificial.
