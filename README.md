# Taim Wetland Ontology Project 🌿🐾

![Status](https://img.shields.io/badge/Status-In%20Development-blue)
![Course](https://img.shields.io/badge/Course-Artificial%20Intelligence-brightgreen)
![Topic](https://img.shields.io/badge/Topic-Ontology%20%26%20Semantic%20Web-orange)

## 📌 About The Project

This repository contains the development of an **Ontology for the Taim Ecological Reserve (Banhado do Taim)**, situated in Rio Grande do Sul, Brazil. This project is developed as part of an Artificial Intelligence academic curriculum, aiming to apply knowledge representation techniques to a real-world environmental and social issue: **wildlife roadkills**.

The Taim Wetland is one of the most important wetlands in southern Brazil, boasting rich biodiversity and playing an essential role in ecosystem preservation. By structuring knowledge regarding species, habitats, environmental conditions, and roadkill events, this project aims to organize and integrate currently dispersed information.

The developed ontology goes beyond an academic exercise—it creates a foundation for future intelligent systems focused on environmental monitoring, decision support, and conservation, connecting AI theory with real-world positive impact.

## 🎯 Objectives

The main goal is to develop an **OWL (Web Ontology Language)** ontology that represents the ecological and operational domain of the Taim Wetland. This model includes, at a minimum, the following core concepts:

- **Animals** (e.g., Capybaras, Birds)
- **Roads and Segments** (e.g., BR-471)
- **Roadkill Events**
- **Environmental Conditions** (e.g., weather, time, season)
- **Habitat Characteristics** (e.g., wetlands, vegetation, water bodies)
- **Risk Factors** (e.g., traffic, visibility, proximity to water)

## 🚀 Key Features

1. **Ontology Modeling**: Building a robust OWL ontology with classes, object properties, data properties, and spatial/temporal constraints, using tools like Protégé and Python libraries (`Owlready2`).
2. **Knowledge Extraction & Population**: 
   - Automating the extraction of domain knowledge using NLP, LLMs, and structured databases (Wikidata, DBpedia).
   - Populating the ontology with at least 100 individuals.
3. **SPARQL Queries**: Developing comprehensive queries to extract valuable inferences and investigate ecological patterns based on semantics, environment, and location.
4. **Machine Learning Integration (Explainable AI)**: Integrating predictive ML models (for roadkill risk assessment) with the ontology to provide semantic explanations for "black-box" model predictions.

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
- **Data Sources**: Wikidata, DBpedia, Wikipedia, OpenStreetMap

## 🤝 Contribution & Team

Developed for the Artificial Intelligence course.
