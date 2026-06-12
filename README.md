# Banhado do Taim Wildlife & Road Ecology Ontology

This repository contains a Semantic Web and Knowledge Representation project developed for the Artificial Intelligence course. It features an **OWL (Web Ontology Language)** ontology designed to model the ecological ecosystem of the **Banhado do Taim** ecological reserve (located in Rio Grande do Sul, Brazil) and analyze wildlife-vehicle collisions (WVC) occurring on the federal highway **BR-471**.

---

## 📌 Project Overview

The Banhado do Taim is one of the most important wetland ecosystems in southern Brazil, hosting a rich biodiversity. The crossing of the BR-471 highway through the reserve leads to frequent animal vehicle collisions. 

This project structures the ecological, geographical, and operational domain knowledge into a queryable knowledge graph. It allows researchers and environmental managers to:
* Validate local fauna taxonomy dynamically using data extracted from real sources (Wikipedia).
* Model factors of risk like road traffic (vehicle volume) and weather visibility conditions.
* Run complex semantic queries (SPARQL) to investigate collision patterns under seasonal and environmental conditions.

---

## 🏗️ Ontology Architecture

The ontology was modeled using Protégé and Python (via the `owlready2` library). It contains **30 classes**, **10 object properties**, **13 data properties**, and formal **OWL class cardinality restrictions**.

### Core Classes (Taxonomy & Concepts)
* **Animal**: Taxonomical superclass containing `Mamifero`, `Ave`, `Reptil`, and `Anfibio`. Species (e.g., `Capivara`, `Jacaré-de-papo-amarelo`, `Tuco-tuco`, `Cisne-de-pescoço-preto`) are modeled as formal OWL subclasses.
* **Habitat**: Mapped into subclasses `Banhado`, `CorpoDagua`, and `Vegetacao` to represent ecosystem characteristics.
* **Rodovia & TrechoRodovia**: Models the highway network and specific 1-km road segments.
* **CondicaoAmbiental**: Models weather and atmospheric contexts (subclass `CondicaoClimatica`).
* **Evento & EventoAtropelamento**: Represents collision incidents.

### Key Properties & Relations
* **Object Properties**: Connect concepts, such as `envolveAnimal` (Event $\to$ Animal), `ocorreEm` (Event $\to$ Road Segment), `ocorreSob` (Event $\to$ Weather), and `viveEm`/`atravessa`.
* **Data Properties**: Store quantitative metrics like `kmRodovia`, `fluxoVeiculosHora` (traffic volume), `visibilidadeMetros` (fog/rain visibility), `estacaoAno` (seasons), `temperaturaCelsius`, and coordinates (`latitude`/`longitude`).
* **Cardinality Restrictions**: Enforce logical constraints, ensuring every `EventoAtropelamento` is linked to *exactly 1* animal, *exactly 1* road segment, and *exactly 1* weather condition.

---

## 🚀 Execution Pipeline

The project features an automated python pipeline to generate, populate, query, and report on the ontology.

```
[Wikipedia Scraping] -> [Ontology Base Gen] -> [Automated Population] -> [SPARQL Queries] -> [LaTeX Report]
```

1. **Wikipedia Species Validation** (`scripts/extracao_wikipedia.py`):
   Scrapes the official pt.wikipedia.org Banhado do Taim page to validate that the modeled species are biologically recorded in the reserve.
2. **Ontology Base Creation** (`ontology/ontologia_base.py`):
   Constructs the RDF/XML schema (`.owl`), sets up classes, properties, and restrictions.
3. **Automated Population** (`scripts/povoamento.py`):
   Instantiates 137 individuals, including habitats, road segments with traffic volume, weather conditions with visibility metrics, validated animal instances, and simulated collision events with season tags (Winter/Spring/Summer/Autumn).
4. **SPARQL Execution** (`sparql_queries/executar_consultas.py`):
   Runs **30 SPARQL queries** against the populated OWL file using `rdflib` and generates a query report.
5. **LaTeX Report Generation** (`scripts/gerar_latex.py`):
   Generates a fully detailed LaTeX academic report (`docs/relatorio.tex`) integrating all queries and execution outputs.

---

## 📊 SPARQL Queries

The queries are distributed across 5 categories in `sparql_queries/definicao_consultas.py`:
1. **Simple Queries**: Retrieving all road segments, weather conditions, or instances of specific species (e.g., Capybaras).
2. **Multiple Relations**: Correlating collisions with species habitats, weather, and proximity to water bodies.
3. **Filtering**: Filtering events by cold temperatures ($<15^\circ\text{C}$), high traffic volume, or low visibility.
4. **Aggregations**: Counting total accidents, grouping collisions by habitat type, or calculating average accident KMs.
5. **Scenario Queries**: Investigating critical risk zones (e.g., fatal accidents under heavy rain and low visibility near specific wetlands).

*Note: Since standard RDFLib lacks an OWL reasoner, queries on parent classes (like `Mamifero` or `Ave`) use transitive property paths (`rdf:type/rdfs:subClassOf*`) to correctly retrieve subclasses instances.*

---

## 💻 Installation & How to Run

### Prerequisites
Make sure you have **Python 3.8+** installed.

### Setup Environment
1. Clone this repository.
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On Unix/macOS:
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Run the Pipeline
To run the entire generation, population, query execution, and report compilation pipeline, run:
```bash
python ontology/ontologia_base.py
python scripts/povoamento.py
python sparql_queries/executar_consultas.py
python scripts/gerar_latex.py
```

---

## 📁 Repository Structure

* `ontology/`: Contains the base script and generated OWL files (`ontologia_base.owl`, `ontologia_populada.owl`).
* `scripts/`: Scraping, population, and report compilation python files.
* `sparql_queries/`: SPARQL query definitions and RDFLib query engine script.
* `docs/`: LaTeX academic report source files (`relatorio.tex`), output query results (`relatorio_sparql.md`), and the compiled PDF.
* `docs/images/`: Screenshots of Protégé showing class hierarchies, properties, and OntoGraf visual networks.

---

## 👥 Authors

* **Miguel Brondani**
* **Lucas Pairé**
