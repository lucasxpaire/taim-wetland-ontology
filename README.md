# Ontologia do Banhado do Taim - Ecologia Rodoviária

Este projeto apresenta o desenvolvimento de uma ontologia em OWL para modelar o ecossistema do **Banhado do Taim** (RS) e analisar eventos de atropelamento de fauna na rodovia **BR-471**.

---

## 🚀 Como Executar o Projeto

Siga os passos abaixo para configurar o ambiente e rodar toda a pipeline da ontologia.

### 1. Pré-requisitos
Certifique-se de ter o **Python 3.8+** instalado em sua máquina.

### 2. Configurar o Ambiente Virtual
Abra o terminal na pasta do projeto e execute os comandos correspondentes ao seu sistema:

```bash
# Criar o ambiente virtual
python -m venv venv

# Ativar o ambiente virtual
# No Windows (PowerShell):
venv\Scripts\activate
# No Linux/macOS:
source venv/bin/activate
```

### 3. Instalar Dependências
Com o ambiente virtual ativado, instale as bibliotecas necessárias (`owlready2` e `rdflib`):
```bash
pip install -r requirements.txt
```

### 4. Executar os Scripts
Execute a sequência de comandos abaixo para gerar a ontologia base, povoá-la com dados reais da Wikipédia/simulações e rodar as consultas SPARQL:

```bash
# 1. Gerar a estrutura base da ontologia (.owl)
python ontology/ontologia_base.py

# 2. Coletar dados da Wikipédia e povoar a ontologia com indivíduos
python scripts/povoamento.py

# 3. Executar as 30 consultas SPARQL
python sparql_queries/executar_consultas.py
```

*Nota: O resultado da execução das consultas SPARQL será salvo no arquivo `docs/relatorio_sparql.md` (no formato markdown).*

---

## 📁 Estrutura da Pasta

* `ontology/`: Contém os arquivos da ontologia base e populada (`.owl`) e o script de modelagem.
* `scripts/`: Scripts para validação taxonômica via Wikipédia e povoamento automatizado de dados.
* `sparql_queries/`: Definições e execução das 30 consultas SPARQL.
* `docs/`: Contém o relatório acadêmico final em formato PDF (`relatorio.pdf`).

---

## 👥 Autores

* **Miguel Brondani**
* **Lucas Pairé**
