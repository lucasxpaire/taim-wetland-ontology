# Relatório Final: Consultas SPARQL (Etapa 5)

Este documento apresenta as 30 consultas SPARQL em OWL sobre a ontologia populada.

## Categoria: Simples

### Consulta 1
**Descrição:** Listar todas as Capivaras registradas na ontologia.

**Código SPARQL:**
```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX taim: <http://www.exemplo.org/taim#>
SELECT ?capivara WHERE { ?capivara rdf:type taim:Capivara . }
```

**Resultados Obtidos:**
```text
capivara: Capivara_1
capivara: Capivara_2
capivara: Capivara_3
capivara: Capivara_4
capivara: Capivara_5
```

---

### Consulta 2
**Descrição:** Listar todos os Jacarés-de-papo-amarelo registrados.

**Código SPARQL:**
```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX taim: <http://www.exemplo.org/taim#>
SELECT ?jacare WHERE { ?jacare rdf:type taim:Jacaré-de-papo-amarelo . }
```

**Resultados Obtidos:**
```text
jacare: Jacaré-de-papo-amarelo_1
jacare: Jacaré-de-papo-amarelo_2
jacare: Jacaré-de-papo-amarelo_3
jacare: Jacaré-de-papo-amarelo_4
jacare: Jacaré-de-papo-amarelo_5
```

---

### Consulta 3
**Descrição:** Listar todos os trechos de rodovia mapeados.

**Código SPARQL:**
```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX taim: <http://www.exemplo.org/taim#>
SELECT ?trecho WHERE { ?trecho rdf:type taim:TrechoRodovia . }
```

**Resultados Obtidos:**
```text
trecho: BR471_KM_10
trecho: BR471_KM_11
trecho: BR471_KM_12
trecho: BR471_KM_13
trecho: BR471_KM_14
trecho: BR471_KM_15
trecho: BR471_KM_16
trecho: BR471_KM_17
trecho: BR471_KM_18
trecho: BR471_KM_19
... (e mais 10 resultados ocultados por brevidade)
```

---

### Consulta 4
**Descrição:** Listar todos os Eventos de Atropelamento.

**Código SPARQL:**
```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX taim: <http://www.exemplo.org/taim#>
SELECT ?evento WHERE { ?evento rdf:type taim:EventoAtropelamento . }
```

**Resultados Obtidos:**
```text
evento: Acidente_Taim_001
evento: Acidente_Taim_002
evento: Acidente_Taim_003
evento: Acidente_Taim_004
evento: Acidente_Taim_005
evento: Acidente_Taim_006
evento: Acidente_Taim_007
evento: Acidente_Taim_008
evento: Acidente_Taim_009
evento: Acidente_Taim_0010
... (e mais 50 resultados ocultados por brevidade)
```

---

### Consulta 5
**Descrição:** Listar todas as Condições Climáticas registradas.

**Código SPARQL:**
```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX taim: <http://www.exemplo.org/taim#>
SELECT ?clima WHERE { ?clima rdf:type taim:CondicaoClimatica . }
```

**Resultados Obtidos:**
```text
clima: Clima_Chuva_Forte_0
clima: Clima_Neblina_Densa_1
clima: Clima_Ensolarado_2
clima: Clima_Nublado_3
```

---

### Consulta 6
**Descrição:** Listar todos os habitats do tipo Banhado.

**Código SPARQL:**
```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX taim: <http://www.exemplo.org/taim#>
SELECT ?banhado WHERE { ?banhado rdf:type taim:Banhado . }
```

**Resultados Obtidos:**
```text
banhado: Banhado_da_Mangueira
banhado: Banhado_do_Nicola
banhado: Banhado_Central
```

---

## Categoria: Múltiplas Relações

### Consulta 7
**Descrição:** Buscar eventos associados a um animal específico e o trecho onde ocorreu.

**Código SPARQL:**
```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX taim: <http://www.exemplo.org/taim#>
SELECT ?evento ?animal ?trecho WHERE { ?evento rdf:type taim:EventoAtropelamento . ?evento taim:envolveAnimal ?animal . ?evento taim:ocorreEm ?trecho . }
```

**Resultados Obtidos:**
```text
evento: Acidente_Taim_001 | animal: Capivara_2 | trecho: BR471_KM_23
evento: Acidente_Taim_002 | animal: Jacaré-de-papo-amarelo_1 | trecho: BR471_KM_27
evento: Acidente_Taim_003 | animal: Ratão-do-banhado_3 | trecho: BR471_KM_22
evento: Acidente_Taim_004 | animal: Cisne-de-pescoço-preto_4 | trecho: BR471_KM_11
evento: Acidente_Taim_005 | animal: Cisne-de-pescoço-preto_3 | trecho: BR471_KM_15
evento: Acidente_Taim_006 | animal: Maçarico_5 | trecho: BR471_KM_18
evento: Acidente_Taim_007 | animal: Tachã_5 | trecho: BR471_KM_16
evento: Acidente_Taim_008 | animal: Tachã_4 | trecho: BR471_KM_14
evento: Acidente_Taim_009 | animal: Capivara_3 | trecho: BR471_KM_16
evento: Acidente_Taim_0010 | animal: Jacaré-de-papo-amarelo_4 | trecho: BR471_KM_15
... (e mais 50 resultados ocultados por brevidade)
```

---

### Consulta 8
**Descrição:** Descobrir em quais habitats os animais acidentados costumam viver.

**Código SPARQL:**
```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX taim: <http://www.exemplo.org/taim#>
SELECT DISTINCT ?animal ?habitat WHERE { ?evento rdf:type taim:EventoAtropelamento . ?evento taim:envolveAnimal ?animal . ?animal taim:viveEm ?habitat . }
```

**Resultados Obtidos:**
```text
animal: Capivara_2 | habitat: Banhado_do_Nicola
animal: Jacaré-de-papo-amarelo_1 | habitat: Banhado_Central
animal: Ratão-do-banhado_3 | habitat: Banhado_do_Nicola
animal: Cisne-de-pescoço-preto_4 | habitat: Banhado_do_Nicola
animal: Cisne-de-pescoço-preto_3 | habitat: Banhado_da_Mangueira
animal: Maçarico_5 | habitat: Banhado_Central
animal: Tachã_5 | habitat: Banhado_Central
animal: Tachã_4 | habitat: Banhado_do_Nicola
animal: Capivara_3 | habitat: Banhado_do_Nicola
animal: Jacaré-de-papo-amarelo_4 | habitat: Banhado_do_Nicola
... (e mais 27 resultados ocultados por brevidade)
```

---

### Consulta 9
**Descrição:** Listar trechos de rodovia, seus acidentes e as condições climáticas exatas no momento.

**Código SPARQL:**
```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX taim: <http://www.exemplo.org/taim#>
SELECT ?trecho ?evento ?clima WHERE { ?evento taim:ocorreEm ?trecho . ?evento taim:ocorreSob ?clima . }
```

**Resultados Obtidos:**
```text
trecho: BR471_KM_23 | evento: Acidente_Taim_001 | clima: Clima_Nublado_3
trecho: BR471_KM_23 | evento: Acidente_Taim_0012 | clima: Clima_Chuva_Forte_0
trecho: BR471_KM_23 | evento: Acidente_Taim_0026 | clima: Clima_Neblina_Densa_1
trecho: BR471_KM_23 | evento: Acidente_Taim_0031 | clima: Clima_Chuva_Forte_0
trecho: BR471_KM_23 | evento: Acidente_Taim_0032 | clima: Clima_Chuva_Forte_0
trecho: BR471_KM_23 | evento: Acidente_Taim_0043 | clima: Clima_Nublado_3
trecho: BR471_KM_23 | evento: Acidente_Taim_0052 | clima: Clima_Chuva_Forte_0
trecho: BR471_KM_23 | evento: Acidente_Taim_0058 | clima: Clima_Nublado_3
trecho: BR471_KM_27 | evento: Acidente_Taim_002 | clima: Clima_Ensolarado_2
trecho: BR471_KM_27 | evento: Acidente_Taim_0025 | clima: Clima_Nublado_3
... (e mais 50 resultados ocultados por brevidade)
```

---

### Consulta 10
**Descrição:** Buscar trechos de rodovia que registraram acidentes e também estão próximos a um banhado.

**Código SPARQL:**
```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX taim: <http://www.exemplo.org/taim#>
SELECT ?trecho ?evento ?banhado WHERE { ?evento taim:ocorreEm ?trecho . ?trecho taim:proximoA ?banhado . ?banhado rdf:type taim:Banhado . }
```

**Resultados Obtidos:**
```text
trecho: BR471_KM_14 | evento: Acidente_Taim_008 | banhado: Banhado_da_Mangueira
trecho: BR471_KM_14 | evento: Acidente_Taim_0011 | banhado: Banhado_da_Mangueira
trecho: BR471_KM_14 | evento: Acidente_Taim_0033 | banhado: Banhado_da_Mangueira
trecho: BR471_KM_14 | evento: Acidente_Taim_0036 | banhado: Banhado_da_Mangueira
trecho: BR471_KM_21 | evento: Acidente_Taim_0016 | banhado: Banhado_da_Mangueira
trecho: BR471_KM_21 | evento: Acidente_Taim_0021 | banhado: Banhado_da_Mangueira
trecho: BR471_KM_21 | evento: Acidente_Taim_0049 | banhado: Banhado_da_Mangueira
trecho: BR471_KM_22 | evento: Acidente_Taim_003 | banhado: Banhado_da_Mangueira
trecho: BR471_KM_22 | evento: Acidente_Taim_0053 | banhado: Banhado_da_Mangueira
trecho: BR471_KM_25 | evento: Acidente_Taim_0037 | banhado: Banhado_da_Mangueira
... (e mais 50 resultados ocultados por brevidade)
```

---

### Consulta 11
**Descrição:** Listar animais que atravessaram a rodovia e se envolveram em um acidente.

**Código SPARQL:**
```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX taim: <http://www.exemplo.org/taim#>
SELECT ?animal ?evento WHERE { ?animal taim:atravessa ?trecho . ?evento taim:envolveAnimal ?animal . }
```

**Resultados Obtidos:**
```text
animal: Capivara_1 | evento: Acidente_Taim_0045
animal: Ratão-do-banhado_2 | evento: Acidente_Taim_0023
animal: Cisne-de-pescoço-preto_1 | evento: Acidente_Taim_0044
animal: Capivara_2 | evento: Acidente_Taim_001
animal: Capivara_5 | evento: Acidente_Taim_0052
animal: Ratão-do-banhado_3 | evento: Acidente_Taim_003
animal: Ratão-do-banhado_3 | evento: Acidente_Taim_0026
animal: Ratão-do-banhado_4 | evento: Acidente_Taim_0048
animal: Ratão-do-banhado_4 | evento: Acidente_Taim_0058
animal: Tachã_5 | evento: Acidente_Taim_007
... (e mais 107 resultados ocultados por brevidade)
```

---

### Consulta 12
**Descrição:** Listar animais mamíferos, o evento associado e o trecho onde ocorreu.

**Código SPARQL:**
```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX taim: <http://www.exemplo.org/taim#>
SELECT ?mamifero ?evento ?trecho WHERE { ?mamifero rdf:type/rdfs:subClassOf* taim:Mamifero . ?evento taim:envolveAnimal ?mamifero . ?evento taim:ocorreEm ?trecho . }
```

**Resultados Obtidos:**
```text
mamifero: Capivara_1 | evento: Acidente_Taim_0045 | trecho: BR471_KM_10
mamifero: Capivara_2 | evento: Acidente_Taim_001 | trecho: BR471_KM_23
mamifero: Capivara_3 | evento: Acidente_Taim_009 | trecho: BR471_KM_16
mamifero: Capivara_4 | evento: Acidente_Taim_0021 | trecho: BR471_KM_21
mamifero: Capivara_4 | evento: Acidente_Taim_0059 | trecho: BR471_KM_29
mamifero: Capivara_5 | evento: Acidente_Taim_0052 | trecho: BR471_KM_23
mamifero: Tuco-tuco_2 | evento: Acidente_Taim_0033 | trecho: BR471_KM_14
mamifero: Tuco-tuco_2 | evento: Acidente_Taim_0053 | trecho: BR471_KM_22
mamifero: Ratão-do-banhado_2 | evento: Acidente_Taim_0023 | trecho: BR471_KM_10
mamifero: Ratão-do-banhado_3 | evento: Acidente_Taim_003 | trecho: BR471_KM_22
... (e mais 4 resultados ocultados por brevidade)
```

---

## Categoria: Filtros

### Consulta 13
**Descrição:** Listar eventos ocorridos em clima frio (Temperatura Celsius < 15°C).

**Código SPARQL:**
```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX taim: <http://www.exemplo.org/taim#>
SELECT ?evento ?temp WHERE { ?evento taim:ocorreSob ?clima . ?clima taim:temperaturaCelsius ?temp . FILTER(?temp < 15) }
```

**Resultados Obtidos:**
```text
Zero resultados encontrados.
```

---

### Consulta 14
**Descrição:** Listar acidentes de severidade 'Fatal'.

**Código SPARQL:**
```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX taim: <http://www.exemplo.org/taim#>
SELECT ?evento WHERE { ?evento taim:severidadeAcidente ?severidade . FILTER(str(?severidade) = 'Fatal') }
```

**Resultados Obtidos:**
```text
evento: Acidente_Taim_001
evento: Acidente_Taim_002
evento: Acidente_Taim_005
evento: Acidente_Taim_008
evento: Acidente_Taim_009
evento: Acidente_Taim_0010
evento: Acidente_Taim_0012
evento: Acidente_Taim_0013
evento: Acidente_Taim_0017
evento: Acidente_Taim_0021
... (e mais 18 resultados ocultados por brevidade)
```

---

### Consulta 15
**Descrição:** Listar trechos de rodovia antes do KM 20.

**Código SPARQL:**
```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX taim: <http://www.exemplo.org/taim#>
SELECT ?trecho ?km WHERE { ?trecho taim:kmRodovia ?km . FILTER(?km < 20) }
```

**Resultados Obtidos:**
```text
trecho: BR471_KM_10 | km: 10.0
trecho: BR471_KM_11 | km: 11.0
trecho: BR471_KM_12 | km: 12.0
trecho: BR471_KM_13 | km: 13.0
trecho: BR471_KM_14 | km: 14.0
trecho: BR471_KM_15 | km: 15.0
trecho: BR471_KM_16 | km: 16.0
trecho: BR471_KM_17 | km: 17.0
trecho: BR471_KM_18 | km: 18.0
trecho: BR471_KM_19 | km: 19.0
```

---

### Consulta 16
**Descrição:** Listar habitats com nível de água perigosamente alto (Nível > 2 metros).

**Código SPARQL:**
```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX taim: <http://www.exemplo.org/taim#>
SELECT ?habitat ?nivel WHERE { ?habitat taim:nivelAguaMetro ?nivel . FILTER(?nivel > 2) }
```

**Resultados Obtidos:**
```text
habitat: Banhado_da_Mangueira | nivel: 2.113643153299371
habitat: Banhado_do_Nicola | nivel: 2.48964383916167
```

---

### Consulta 17
**Descrição:** Listar eventos envolvendo apenas Capivaras (filtragem por string no nome comum).

**Código SPARQL:**
```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX taim: <http://www.exemplo.org/taim#>
SELECT ?evento ?nome WHERE { ?evento taim:envolveAnimal ?animal . ?animal taim:nomeComum ?nome . FILTER(str(?nome) = 'Capivara') }
```

**Resultados Obtidos:**
```text
evento: Acidente_Taim_0045 | nome: Capivara
evento: Acidente_Taim_001 | nome: Capivara
evento: Acidente_Taim_009 | nome: Capivara
evento: Acidente_Taim_0021 | nome: Capivara
evento: Acidente_Taim_0059 | nome: Capivara
evento: Acidente_Taim_0052 | nome: Capivara
```

---

### Consulta 18
**Descrição:** Listar eventos de atropelamento ocorridos em altas temperaturas (> 30°C).

**Código SPARQL:**
```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX taim: <http://www.exemplo.org/taim#>
SELECT ?evento ?temp WHERE { ?evento taim:ocorreSob ?clima . ?clima taim:temperaturaCelsius ?temp . FILTER(?temp > 30) }
```

**Resultados Obtidos:**
```text
Zero resultados encontrados.
```

---

## Categoria: Agregação

### Consulta 19
**Descrição:** Contar o número total de eventos de atropelamento.

**Código SPARQL:**
```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX taim: <http://www.exemplo.org/taim#>
SELECT (COUNT(?evento) AS ?totalAcidentes) WHERE { ?evento rdf:type taim:EventoAtropelamento . }
```

**Resultados Obtidos:**
```text
totalAcidentes: 60
```

---

### Consulta 20
**Descrição:** Contar o número de animais vitimados agrupados por habitat em que vivem.

**Código SPARQL:**
```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX taim: <http://www.exemplo.org/taim#>
SELECT ?habitat (COUNT(?animal) AS ?totalAnimais) WHERE { ?animal taim:viveEm ?habitat . ?evento taim:envolveAnimal ?animal . } GROUP BY ?habitat
```

**Resultados Obtidos:**
```text
habitat: Banhado_da_Mangueira | totalAnimais: 9
habitat: Banhado_do_Nicola | totalAnimais: 22
habitat: Banhado_Central | totalAnimais: 29
```

---

### Consulta 21
**Descrição:** Contar o número de acidentes agrupados por Trecho de Rodovia.

**Código SPARQL:**
```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX taim: <http://www.exemplo.org/taim#>
SELECT ?trecho (COUNT(?evento) AS ?totalAcidentes) WHERE { ?evento taim:ocorreEm ?trecho . } GROUP BY ?trecho
```

**Resultados Obtidos:**
```text
trecho: BR471_KM_23 | totalAcidentes: 8
trecho: BR471_KM_27 | totalAcidentes: 3
trecho: BR471_KM_22 | totalAcidentes: 2
trecho: BR471_KM_11 | totalAcidentes: 4
trecho: BR471_KM_15 | totalAcidentes: 3
trecho: BR471_KM_18 | totalAcidentes: 3
trecho: BR471_KM_16 | totalAcidentes: 3
trecho: BR471_KM_14 | totalAcidentes: 4
trecho: BR471_KM_13 | totalAcidentes: 2
trecho: BR471_KM_19 | totalAcidentes: 4
... (e mais 10 resultados ocultados por brevidade)
```

---

### Consulta 22
**Descrição:** Descobrir a temperatura máxima registrada nos eventos.

**Código SPARQL:**
```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX taim: <http://www.exemplo.org/taim#>
SELECT (MAX(?temp) AS ?maxTemp) WHERE { ?evento taim:ocorreSob ?clima . ?clima taim:temperaturaCelsius ?temp . }
```

**Resultados Obtidos:**
```text
maxTemp: 27.464608200232902
```

---

### Consulta 23
**Descrição:** Descobrir o KM médio onde os acidentes ocorrem.

**Código SPARQL:**
```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX taim: <http://www.exemplo.org/taim#>
SELECT (AVG(?km) AS ?kmMedio) WHERE { ?evento taim:ocorreEm ?trecho . ?trecho taim:kmRodovia ?km . }
```

**Resultados Obtidos:**
```text
kmMedio: 19.53333333333333333333333333
```

---

### Consulta 24
**Descrição:** Contar o número de acidentes que foram fatais.

**Código SPARQL:**
```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX taim: <http://www.exemplo.org/taim#>
SELECT (COUNT(?evento) AS ?fatais) WHERE { ?evento taim:severidadeAcidente ?sev . FILTER(str(?sev) = 'Fatal') }
```

**Resultados Obtidos:**
```text
fatais: 28
```

---

## Categoria: Cenário

### Consulta 25
**Descrição:** Cenário de Risco Crítico: Quais rodovias acumularam chuva forte (Temperatura < 20°C) e tiveram acidentes fatais?

**Código SPARQL:**
```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX taim: <http://www.exemplo.org/taim#>
SELECT ?trecho ?temp ?sev WHERE { ?evento taim:ocorreEm ?trecho . ?evento taim:ocorreSob ?clima . ?clima taim:temperaturaCelsius ?temp . ?evento taim:severidadeAcidente ?sev . FILTER(?temp < 20 && str(?sev) = 'Fatal') }
```

**Resultados Obtidos:**
```text
trecho: BR471_KM_27 | temp: 15.801335913070272 | sev: Fatal
trecho: BR471_KM_16 | temp: 15.801335913070272 | sev: Fatal
trecho: BR471_KM_12 | temp: 15.801335913070272 | sev: Fatal
trecho: BR471_KM_15 | temp: 15.801335913070272 | sev: Fatal
trecho: BR471_KM_26 | temp: 15.801335913070272 | sev: Fatal
trecho: BR471_KM_13 | temp: 17.941515945987646 | sev: Fatal
trecho: BR471_KM_10 | temp: 17.941515945987646 | sev: Fatal
trecho: BR471_KM_23 | temp: 17.941515945987646 | sev: Fatal
trecho: BR471_KM_18 | temp: 17.941515945987646 | sev: Fatal
trecho: BR471_KM_16 | temp: 17.941515945987646 | sev: Fatal
... (e mais 3 resultados ocultados por brevidade)
```

---

### Consulta 26
**Descrição:** Cenário de Deslocamento Animal: Quais animais aquáticos (Aves) sofreram acidentes em KMs próximos ao Banhado da Mangueira?

**Código SPARQL:**
```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX taim: <http://www.exemplo.org/taim#>
SELECT ?ave ?trecho WHERE { ?ave rdf:type/rdfs:subClassOf* taim:Ave . ?evento taim:envolveAnimal ?ave . ?evento taim:ocorreEm ?trecho . ?trecho taim:proximoA ?habitat . FILTER(REGEX(str(?habitat), 'Mangueira', 'i')) }
```

**Resultados Obtidos:**
```text
ave: Cisne-de-pescoço-preto_3 | trecho: BR471_KM_21
ave: Maçarico_5 | trecho: BR471_KM_25
ave: Tachã_4 | trecho: BR471_KM_14
```

---

### Consulta 27
**Descrição:** Cenário de Prevenção: Obter a lista de trechos com acidentes de grandes mamíferos (Capivara) para possível instalação de placas.

**Código SPARQL:**
```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX taim: <http://www.exemplo.org/taim#>
SELECT DISTINCT ?trecho WHERE { ?evento taim:ocorreEm ?trecho . ?evento taim:envolveAnimal ?animal . ?animal rdf:type taim:Capivara . }
```

**Resultados Obtidos:**
```text
trecho: BR471_KM_10
trecho: BR471_KM_23
trecho: BR471_KM_16
trecho: BR471_KM_21
trecho: BR471_KM_29
```

---

### Consulta 28
**Descrição:** Cenário Hidrológico: Animais atropelados perto de habitats com nível de água muito alto (risco de inundação forçando fuga).

**Código SPARQL:**
```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX taim: <http://www.exemplo.org/taim#>
SELECT ?animal ?nivel WHERE { ?evento taim:envolveAnimal ?animal . ?animal taim:viveEm ?habitat . ?habitat taim:nivelAguaMetro ?nivel . FILTER(?nivel >= 2.0) }
```

**Resultados Obtidos:**
```text
animal: Capivara_1 | nivel: 2.113643153299371
animal: Capivara_5 | nivel: 2.113643153299371
animal: Cisne-de-pescoço-preto_3 | nivel: 2.113643153299371
animal: Cisne-de-pescoço-preto_3 | nivel: 2.113643153299371
animal: Cisne-de-pescoço-preto_3 | nivel: 2.113643153299371
animal: Maçarico_4 | nivel: 2.113643153299371
animal: Garça-moura_3 | nivel: 2.113643153299371
animal: Tartaruga_2 | nivel: 2.113643153299371
animal: Tartaruga_2 | nivel: 2.113643153299371
animal: Capivara_2 | nivel: 2.48964383916167
... (e mais 21 resultados ocultados por brevidade)
```

---

### Consulta 29
**Descrição:** Cenário de Rota Segura: Encontrar trechos da BR-471 (KM > 25) que não possuem banhados próximos com níveis altos de água.

**Código SPARQL:**
```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX taim: <http://www.exemplo.org/taim#>
SELECT ?trecho ?km WHERE { ?trecho taim:kmRodovia ?km . ?trecho taim:proximoA ?habitat . ?habitat taim:nivelAguaMetro ?nivel . FILTER(?km > 25 && ?nivel < 1.0) }
```

**Resultados Obtidos:**
```text
Zero resultados encontrados.
```

---

### Consulta 30
**Descrição:** Cenário Investigativo: Resumo completo de um evento (Qual o animal envolvido, em qual km da rodovia e sob qual clima).

**Código SPARQL:**
```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX taim: <http://www.exemplo.org/taim#>
SELECT ?evento ?animal ?km ?temp WHERE { ?evento taim:envolveAnimal ?animal . ?evento taim:ocorreEm ?trecho . ?trecho taim:kmRodovia ?km . ?evento taim:ocorreSob ?clima . ?clima taim:temperaturaCelsius ?temp . } LIMIT 5
```

**Resultados Obtidos:**
```text
evento: Acidente_Taim_001 | animal: Capivara_2 | km: 23.0 | temp: 27.464608200232902
evento: Acidente_Taim_0012 | animal: Jacaré-de-papo-amarelo_4 | km: 23.0 | temp: 26.046161909390044
evento: Acidente_Taim_0026 | animal: Ratão-do-banhado_3 | km: 23.0 | temp: 17.941515945987646
evento: Acidente_Taim_0031 | animal: Garça-moura_4 | km: 23.0 | temp: 26.046161909390044
evento: Acidente_Taim_0032 | animal: Tachã_5 | km: 23.0 | temp: 26.046161909390044
```

---

