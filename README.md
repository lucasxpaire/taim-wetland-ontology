# Taim Wetland Ontology Project 🌿🐾

![Status](https://img.shields.io/badge/Status-In%20Development-blue)
![Course](https://img.shields.io/badge/Course-Artificial%20Intelligence-brightgreen)
![Topic](https://img.shields.io/badge/Topic-Ontology%20%26%20Semantic%20Web-orange)

## 📌 About The Project

This repository contains the development of an **Ontology for the Taim Ecological Reserve (Banhado do Taim)**, situated in Rio Grande do Sul, Brazil. This project is developed as part of an Artificial Intelligence academic curriculum, aiming to apply knowledge representation techniques to a real-world environmental and social issue: **wildlife roadkills**.

The Taim Wetland is one of the most important wetlands in southern Brazil, boasting rich biodiversity and playing an essential role in ecosystem preservation. By structuring knowledge regarding species, habitats, environmental conditions, and roadkill events, this project aims to organize and integrate currently dispersed information.

## 📋 Assignment To-Do List

This checklist contains all the mandatory requirements from the assignment specification to ensure full completion.

### 1. Ontology Modeling 🧠
- [ ] Create at least **15 classes** (Animals, Roads, Roadkill Events, Environments, etc.)
- [ ] Define the class hierarchy.
- [ ] Create at least **10 Object Properties**.
- [ ] Create at least **10 Data Properties**.
- [ ] Define property restrictions (domain, range, cardinality, etc.).
- [ ] Model at least **one temporal relation**.
- [ ] Model at least **one spatial relation**.
- [ ] **MANDATORY**: Document and justify the main modeling decisions.
- [ ] **MANDATORY**: Explain at least two alternative modeling approaches that were considered and discarded.

### 2. Knowledge Extraction & Sources 🌐
- [ ] Define and document the information sources used (Wikidata, Wikipedia, DBpedia, OpenStreetMap, LLMs, etc.).
- [ ] Describe the methodology for data extraction in the final report.
- [ ] Discuss any limitations or potential errors in the extraction process.

### 3. Ontology Population 📊
- [ ] Populate the ontology with at least **100 individuals** (instances).
- [ ] Develop an automated script (e.g., Python, NLP, LLM prompt scripts) to collect and model the knowledge into the ontology.
- [ ] **MANDATORY**: Clearly explain how the data and individuals were generated.
- [ ] Provide concrete examples of the instances created.
- [ ] Discuss possible data inconsistencies or limitations.

### 4. SPARQL Queries 🔎
- [ ] Implement a total of at least **30 SPARQL queries**.
- [ ] Ensure queries cover the following types:
  - [ ] Simple class-based queries.
  - [ ] Queries involving multiple relations.
  - [ ] Queries with filters (e.g., by time, weather conditions).
  - [ ] Queries with aggregations.
  - [ ] Queries representing relevant domain scenarios.
- [ ] For each query, document: Natural language description, the SPARQL code, and the obtained result.

### 5. Machine Learning Integration (Optional but Recommended) 🤖
- [ ] Explain the ML model used (e.g., roadkill risk predictor).
- [ ] Simulate concrete prediction examples.
- [ ] Demonstrate how the ontology was used to generate semantic explanations for the predictions.

### 6. Final Deliverables 📦
- [ ] The ontology file (`.owl`).
- [ ] The source code for population scripts.
- [ ] The source code for ML algorithms (if used).
- [ ] LLM employment protocols/prompts (if used).
- [ ] **Final PDF Report** (Must include: Protégé screenshots, graphical ontology snippets, SPARQL executions).
- [ ] **5-minute Pitch Video** explaining the solution.
- [ ] Prepare for the oral presentation and defense.

## 📁 Repository Structure

```
├── docs/                # Project documentation, PDF reports, and presentations
├── ontology/            # The OWL ontology files and related models
├── scripts/             # Python scripts for data extraction (NLP, scraping) and population
├── sparql_queries/      # Text files containing the SPARQL queries used for inference
└── README.md            # This file
```

## 🛠️ Technologies & Tools
- **Ontology Editor**: Protégé
- **Languages/Frameworks**: Python, OWL, RDF, SPARQL
- **Libraries**: `Owlready2`, `spaCy`, `BeautifulSoup`, `Requests`

## 🤝 Contribution & Team
Developed for the Artificial Intelligence course.
