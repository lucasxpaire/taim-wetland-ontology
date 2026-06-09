# Relatório Final: Consultas SPARQL (Etapa 5)

Este documento apresenta as 30 consultas SPARQL implementadas sobre a ontologia populada, divididas nas 5 categorias exigidas.

## Categoria: Simples

### Consulta 1
**Descrição:** Listar todas as Capivaras registradas na ontologia.

**Código SPARQL:**
```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX taim: <http://www.exemplo.org/taim#>
SELECT ?capivara WHERE { ?capivara rdf:type taim:Capivara . }
```

**Resultados Obtidos:**
```text
Zero resultados encontrados.
```

---

### Consulta 2
**Descrição:** Listar todos os Jacarés-de-papo-amarelo registrados.

**Código SPARQL:**
```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX taim: <http://www.exemplo.org/taim#>
SELECT ?jacare WHERE { ?jacare rdf:type taim:Jacaré-de-papo-amarelo . }
```

**Resultados Obtidos:**
```text
Zero resultados encontrados.
```

---

### Consulta 3
**Descrição:** Listar todos os trechos de rodovia mapeados.

**Código SPARQL:**
```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
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
PREFIX taim: <http://www.exemplo.org/taim#>
SELECT ?evento ?animal ?trecho WHERE { ?evento rdf:type taim:EventoAtropelamento . ?evento taim:envolveAnimal ?animal . ?evento taim:ocorreEm ?trecho . }
```

**Resultados Obtidos:**
```text
evento: Acidente_Taim_001 | animal: Maçarico_2 | trecho: BR471_KM_28
evento: Acidente_Taim_002 | animal: Rã_5 | trecho: BR471_KM_26
evento: Acidente_Taim_003 | animal: Tachã_2 | trecho: BR471_KM_14
evento: Acidente_Taim_004 | animal: Capivara_1 | trecho: BR471_KM_13
evento: Acidente_Taim_005 | animal: Jacaré-de-papo-amarelo_2 | trecho: BR471_KM_24
evento: Acidente_Taim_006 | animal: Rã_5 | trecho: BR471_KM_11
evento: Acidente_Taim_007 | animal: Tuco-tuco_4 | trecho: BR471_KM_20
evento: Acidente_Taim_008 | animal: Cisne-de-pescoço-preto_3 | trecho: BR471_KM_11
evento: Acidente_Taim_009 | animal: Jacaré-de-papo-amarelo_3 | trecho: BR471_KM_10
evento: Acidente_Taim_0010 | animal: Capivara_3 | trecho: BR471_KM_18
... (e mais 50 resultados ocultados por brevidade)
```

---

### Consulta 8
**Descrição:** Descobrir em quais habitats os animais acidentados costumam viver.

**Código SPARQL:**
```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX taim: <http://www.exemplo.org/taim#>
SELECT DISTINCT ?animal ?habitat WHERE { ?evento rdf:type taim:EventoAtropelamento . ?evento taim:envolveAnimal ?animal . ?animal taim:viveEm ?habitat . }
```

**Resultados Obtidos:**
```text
animal: Maçarico_2 | habitat: Banhado_do_Nicola
animal: Rã_5 | habitat: Banhado_da_Mangueira
animal: Tachã_2 | habitat: Banhado_do_Nicola
animal: Capivara_1 | habitat: Banhado_Central
animal: Jacaré-de-papo-amarelo_2 | habitat: Banhado_do_Nicola
animal: Tuco-tuco_4 | habitat: Banhado_da_Mangueira
animal: Cisne-de-pescoço-preto_3 | habitat: Banhado_Central
animal: Jacaré-de-papo-amarelo_3 | habitat: Banhado_do_Nicola
animal: Capivara_3 | habitat: Banhado_da_Mangueira
animal: Capivara_2 | habitat: Banhado_Central
... (e mais 25 resultados ocultados por brevidade)
```

---

### Consulta 9
**Descrição:** Listar trechos de rodovia, seus acidentes e as condições climáticas exatas no momento.

**Código SPARQL:**
```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX taim: <http://www.exemplo.org/taim#>
SELECT ?trecho ?evento ?clima WHERE { ?evento taim:ocorreEm ?trecho . ?evento taim:ocorreSob ?clima . }
```

**Resultados Obtidos:**
```text
trecho: BR471_KM_28 | evento: Acidente_Taim_001 | clima: Clima_Neblina_Densa_1
trecho: BR471_KM_28 | evento: Acidente_Taim_0016 | clima: Clima_Chuva_Forte_0
trecho: BR471_KM_28 | evento: Acidente_Taim_0022 | clima: Clima_Chuva_Forte_0
trecho: BR471_KM_28 | evento: Acidente_Taim_0030 | clima: Clima_Chuva_Forte_0
trecho: BR471_KM_28 | evento: Acidente_Taim_0034 | clima: Clima_Neblina_Densa_1
trecho: BR471_KM_28 | evento: Acidente_Taim_0035 | clima: Clima_Ensolarado_2
trecho: BR471_KM_28 | evento: Acidente_Taim_0041 | clima: Clima_Neblina_Densa_1
trecho: BR471_KM_26 | evento: Acidente_Taim_002 | clima: Clima_Chuva_Forte_0
trecho: BR471_KM_26 | evento: Acidente_Taim_0011 | clima: Clima_Chuva_Forte_0
trecho: BR471_KM_26 | evento: Acidente_Taim_0026 | clima: Clima_Neblina_Densa_1
... (e mais 50 resultados ocultados por brevidade)
```

---

### Consulta 10
**Descrição:** Buscar trechos de rodovia que registraram acidentes e também estão próximos a um banhado.

**Código SPARQL:**
```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX taim: <http://www.exemplo.org/taim#>
SELECT ?trecho ?evento ?banhado WHERE { ?evento taim:ocorreEm ?trecho . ?trecho taim:proximoA ?banhado . ?banhado rdf:type taim:Banhado . }
```

**Resultados Obtidos:**
```text
trecho: BR471_KM_10 | evento: Acidente_Taim_009 | banhado: Banhado_da_Mangueira
trecho: BR471_KM_10 | evento: Acidente_Taim_0014 | banhado: Banhado_da_Mangueira
trecho: BR471_KM_10 | evento: Acidente_Taim_0017 | banhado: Banhado_da_Mangueira
trecho: BR471_KM_10 | evento: Acidente_Taim_0019 | banhado: Banhado_da_Mangueira
trecho: BR471_KM_10 | evento: Acidente_Taim_0024 | banhado: Banhado_da_Mangueira
trecho: BR471_KM_10 | evento: Acidente_Taim_0050 | banhado: Banhado_da_Mangueira
trecho: BR471_KM_10 | evento: Acidente_Taim_0058 | banhado: Banhado_da_Mangueira
trecho: BR471_KM_10 | evento: Acidente_Taim_0059 | banhado: Banhado_da_Mangueira
trecho: BR471_KM_13 | evento: Acidente_Taim_004 | banhado: Banhado_da_Mangueira
trecho: BR471_KM_15 | evento: Acidente_Taim_0031 | banhado: Banhado_da_Mangueira
... (e mais 50 resultados ocultados por brevidade)
```

---

### Consulta 11
**Descrição:** Listar animais que atravessaram a rodovia e se envolveram em um acidente.

**Código SPARQL:**
```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX taim: <http://www.exemplo.org/taim#>
SELECT ?animal ?evento WHERE { ?animal taim:atravessa ?trecho . ?evento taim:envolveAnimal ?animal . }
```

**Resultados Obtidos:**
```text
animal: Capivara_1 | evento: Acidente_Taim_004
animal: Capivara_1 | evento: Acidente_Taim_0031
animal: Capivara_1 | evento: Acidente_Taim_0052
animal: Capivara_1 | evento: Acidente_Taim_004
animal: Capivara_1 | evento: Acidente_Taim_0031
animal: Capivara_1 | evento: Acidente_Taim_0052
animal: Tuco-tuco_2 | evento: Acidente_Taim_0013
animal: Tuco-tuco_2 | evento: Acidente_Taim_0044
animal: Tuco-tuco_2 | evento: Acidente_Taim_0060
animal: Cisne-de-pescoço-preto_1 | evento: Acidente_Taim_0033
... (e mais 109 resultados ocultados por brevidade)
```

---

### Consulta 12
**Descrição:** Listar animais mamíferos, o evento associado e o trecho onde ocorreu.

**Código SPARQL:**
```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX taim: <http://www.exemplo.org/taim#>
SELECT ?mamifero ?evento ?trecho WHERE { ?mamifero rdf:type taim:Mamifero . ?evento taim:envolveAnimal ?mamifero . ?evento taim:ocorreEm ?trecho . }
```

**Resultados Obtidos:**
```text
mamifero: Capivara_1 | evento: Acidente_Taim_004 | trecho: BR471_KM_13
mamifero: Capivara_1 | evento: Acidente_Taim_0031 | trecho: BR471_KM_15
mamifero: Capivara_1 | evento: Acidente_Taim_0052 | trecho: BR471_KM_22
mamifero: Capivara_2 | evento: Acidente_Taim_0012 | trecho: BR471_KM_27
mamifero: Capivara_2 | evento: Acidente_Taim_0054 | trecho: BR471_KM_19
mamifero: Capivara_3 | evento: Acidente_Taim_0010 | trecho: BR471_KM_18
mamifero: Tuco-tuco_1 | evento: Acidente_Taim_0057 | trecho: BR471_KM_24
mamifero: Tuco-tuco_2 | evento: Acidente_Taim_0013 | trecho: BR471_KM_22
mamifero: Tuco-tuco_2 | evento: Acidente_Taim_0044 | trecho: BR471_KM_22
mamifero: Tuco-tuco_2 | evento: Acidente_Taim_0060 | trecho: BR471_KM_15
... (e mais 11 resultados ocultados por brevidade)
```

---

## Categoria: Filtros

### Consulta 13
**Descrição:** Listar eventos ocorridos em clima frio (Temperatura Celsius < 15°C).

**Código SPARQL:**
```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX taim: <http://www.exemplo.org/taim#>
SELECT ?evento ?temp WHERE { ?evento taim:ocorreSob ?clima . ?clima taim:temperaturaCelsius ?temp . FILTER(?temp < 15) }
```

**Resultados Obtidos:**
```text
evento: Acidente_Taim_009 | temp: 9.772219606289214
evento: Acidente_Taim_0014 | temp: 9.772219606289214
evento: Acidente_Taim_0021 | temp: 9.772219606289214
evento: Acidente_Taim_0024 | temp: 9.772219606289214
evento: Acidente_Taim_0029 | temp: 9.772219606289214
evento: Acidente_Taim_0033 | temp: 9.772219606289214
evento: Acidente_Taim_0039 | temp: 9.772219606289214
evento: Acidente_Taim_0040 | temp: 9.772219606289214
evento: Acidente_Taim_0043 | temp: 9.772219606289214
evento: Acidente_Taim_0051 | temp: 9.772219606289214
... (e mais 1 resultados ocultados por brevidade)
```

---

### Consulta 14
**Descrição:** Listar acidentes de severidade 'Fatal'.

**Código SPARQL:**
```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX taim: <http://www.exemplo.org/taim#>
SELECT ?evento WHERE { ?evento taim:severidadeAcidente ?severidade . FILTER(str(?severidade) = 'Fatal') }
```

**Resultados Obtidos:**
```text
evento: Acidente_Taim_003
evento: Acidente_Taim_004
evento: Acidente_Taim_005
evento: Acidente_Taim_006
evento: Acidente_Taim_007
evento: Acidente_Taim_008
evento: Acidente_Taim_0010
evento: Acidente_Taim_0015
evento: Acidente_Taim_0018
evento: Acidente_Taim_0019
... (e mais 8 resultados ocultados por brevidade)
```

---

### Consulta 15
**Descrição:** Listar trechos de rodovia antes do KM 20.

**Código SPARQL:**
```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
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
PREFIX taim: <http://www.exemplo.org/taim#>
SELECT ?habitat ?nivel WHERE { ?habitat taim:nivelAguaMetro ?nivel . FILTER(?nivel > 2) }
```

**Resultados Obtidos:**
```text
habitat: Banhado_da_Mangueira | nivel: 2.1163792361009595
```

---

### Consulta 17
**Descrição:** Listar eventos envolvendo apenas Capivaras (filtragem por string no nome comum).

**Código SPARQL:**
```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX taim: <http://www.exemplo.org/taim#>
SELECT ?evento ?nome WHERE { ?evento taim:envolveAnimal ?animal . ?animal taim:nomeComum ?nome . FILTER(str(?nome) = 'Capivara') }
```

**Resultados Obtidos:**
```text
evento: Acidente_Taim_004 | nome: Capivara
evento: Acidente_Taim_0031 | nome: Capivara
evento: Acidente_Taim_0052 | nome: Capivara
evento: Acidente_Taim_0012 | nome: Capivara
evento: Acidente_Taim_0054 | nome: Capivara
evento: Acidente_Taim_0010 | nome: Capivara
```

---

### Consulta 18
**Descrição:** Listar eventos de atropelamento ocorridos em altas temperaturas (> 30°C).

**Código SPARQL:**
```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
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
PREFIX taim: <http://www.exemplo.org/taim#>
SELECT ?habitat (COUNT(?animal) AS ?totalAnimais) WHERE { ?animal taim:viveEm ?habitat . ?evento taim:envolveAnimal ?animal . } GROUP BY ?habitat
```

**Resultados Obtidos:**
```text
habitat: Banhado_Central | totalAnimais: 17
habitat: Banhado_da_Mangueira | totalAnimais: 19
habitat: Banhado_do_Nicola | totalAnimais: 24
```

---

### Consulta 21
**Descrição:** Contar o número de acidentes agrupados por Trecho de Rodovia.

**Código SPARQL:**
```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX taim: <http://www.exemplo.org/taim#>
SELECT ?trecho (COUNT(?evento) AS ?totalAcidentes) WHERE { ?evento taim:ocorreEm ?trecho . } GROUP BY ?trecho
```

**Resultados Obtidos:**
```text
trecho: BR471_KM_28 | totalAcidentes: 7
trecho: BR471_KM_26 | totalAcidentes: 6
trecho: BR471_KM_14 | totalAcidentes: 2
trecho: BR471_KM_13 | totalAcidentes: 1
trecho: BR471_KM_24 | totalAcidentes: 3
trecho: BR471_KM_11 | totalAcidentes: 5
trecho: BR471_KM_20 | totalAcidentes: 2
trecho: BR471_KM_10 | totalAcidentes: 8
trecho: BR471_KM_18 | totalAcidentes: 4
trecho: BR471_KM_27 | totalAcidentes: 2
... (e mais 8 resultados ocultados por brevidade)
```

---

### Consulta 22
**Descrição:** Descobrir a temperatura máxima registrada nos eventos.

**Código SPARQL:**
```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX taim: <http://www.exemplo.org/taim#>
SELECT (MAX(?temp) AS ?maxTemp) WHERE { ?evento taim:ocorreSob ?clima . ?clima taim:temperaturaCelsius ?temp . }
```

**Resultados Obtidos:**
```text
maxTemp: 24.478338955648415
```

---

### Consulta 23
**Descrição:** Descobrir o KM médio onde os acidentes ocorrem.

**Código SPARQL:**
```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX taim: <http://www.exemplo.org/taim#>
SELECT (AVG(?km) AS ?kmMedio) WHERE { ?evento taim:ocorreEm ?trecho . ?trecho taim:kmRodovia ?km . }
```

**Resultados Obtidos:**
```text
kmMedio: 19.68333333333333333333333333
```

---

### Consulta 24
**Descrição:** Contar o número de acidentes que foram fatais.

**Código SPARQL:**
```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX taim: <http://www.exemplo.org/taim#>
SELECT (COUNT(?evento) AS ?fatais) WHERE { ?evento taim:severidadeAcidente ?sev . FILTER(str(?sev) = 'Fatal') }
```

**Resultados Obtidos:**
```text
fatais: 18
```

---

## Categoria: Cenário

### Consulta 25
**Descrição:** Cenário de Risco Crítico: Quais rodovias acumularam chuva forte (Temperatura < 20°C) e tiveram acidentes fatais?

**Código SPARQL:**
```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX taim: <http://www.exemplo.org/taim#>
SELECT ?trecho ?temp ?sev WHERE { ?evento taim:ocorreEm ?trecho . ?evento taim:ocorreSob ?clima . ?clima taim:temperaturaCelsius ?temp . ?evento taim:severidadeAcidente ?sev . FILTER(?temp < 20 && str(?sev) = 'Fatal') }
```

**Resultados Obtidos:**
```text
trecho: BR471_KM_13 | temp: 15.191119079497632 | sev: Fatal
trecho: BR471_KM_11 | temp: 15.191119079497632 | sev: Fatal
trecho: BR471_KM_20 | temp: 15.191119079497632 | sev: Fatal
trecho: BR471_KM_10 | temp: 15.191119079497632 | sev: Fatal
trecho: BR471_KM_26 | temp: 15.191119079497632 | sev: Fatal
trecho: BR471_KM_14 | temp: 18.509518090974588 | sev: Fatal
trecho: BR471_KM_24 | temp: 18.509518090974588 | sev: Fatal
trecho: BR471_KM_11 | temp: 18.509518090974588 | sev: Fatal
trecho: BR471_KM_18 | temp: 18.509518090974588 | sev: Fatal
trecho: BR471_KM_29 | temp: 18.509518090974588 | sev: Fatal
... (e mais 5 resultados ocultados por brevidade)
```

---

### Consulta 26
**Descrição:** Cenário de Deslocamento Animal: Quais animais aquáticos (Aves) sofreram acidentes em KMs próximos ao Banhado da Mangueira?

**Código SPARQL:**
```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX taim: <http://www.exemplo.org/taim#>
SELECT ?ave ?trecho WHERE { ?ave rdf:type taim:Ave . ?evento taim:envolveAnimal ?ave . ?evento taim:ocorreEm ?trecho . ?trecho taim:proximoA ?habitat . FILTER(REGEX(str(?habitat), 'Mangueira', 'i')) }
```

**Resultados Obtidos:**
```text
ave: Cisne-de-pescoço-preto_1 | trecho: BR471_KM_15
ave: Cisne-de-pescoço-preto_2 | trecho: BR471_KM_20
ave: Cisne-de-pescoço-preto_2 | trecho: BR471_KM_10
ave: Cisne-de-pescoço-preto_5 | trecho: BR471_KM_10
ave: Maçarico_4 | trecho: BR471_KM_26
ave: Tachã_1 | trecho: BR471_KM_10
```

---

### Consulta 27
**Descrição:** Cenário de Prevenção: Obter a lista de trechos com acidentes de grandes mamíferos (Capivara) para possível instalação de placas.

**Código SPARQL:**
```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX taim: <http://www.exemplo.org/taim#>
SELECT DISTINCT ?trecho WHERE { ?evento taim:ocorreEm ?trecho . ?evento taim:envolveAnimal ?animal . ?animal rdf:type taim:Capivara . }
```

**Resultados Obtidos:**
```text
Zero resultados encontrados.
```

---

### Consulta 28
**Descrição:** Cenário Hidrológico: Animais atropelados perto de habitats com nível de água muito alto (risco de inundação forçando fuga).

**Código SPARQL:**
```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX taim: <http://www.exemplo.org/taim#>
SELECT ?animal ?nivel WHERE { ?evento taim:envolveAnimal ?animal . ?animal taim:viveEm ?habitat . ?habitat taim:nivelAguaMetro ?nivel . FILTER(?nivel >= 2.0) }
```

**Resultados Obtidos:**
```text
animal: Capivara_3 | nivel: 2.1163792361009595
animal: Tuco-tuco_3 | nivel: 2.1163792361009595
animal: Tuco-tuco_3 | nivel: 2.1163792361009595
animal: Tuco-tuco_4 | nivel: 2.1163792361009595
animal: Tuco-tuco_4 | nivel: 2.1163792361009595
animal: Ratão-do-banhado_1 | nivel: 2.1163792361009595
animal: Ratão-do-banhado_1 | nivel: 2.1163792361009595
animal: Ratão-do-banhado_3 | nivel: 2.1163792361009595
animal: Ratão-do-banhado_3 | nivel: 2.1163792361009595
animal: Cisne-de-pescoço-preto_1 | nivel: 2.1163792361009595
... (e mais 9 resultados ocultados por brevidade)
```

---

### Consulta 29
**Descrição:** Cenário de Rota Segura: Encontrar trechos da BR-471 (KM > 25) que não possuem banhados próximos com níveis altos de água.

**Código SPARQL:**
```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX taim: <http://www.exemplo.org/taim#>
SELECT ?trecho ?km WHERE { ?trecho taim:kmRodovia ?km . ?trecho taim:proximoA ?habitat . ?habitat taim:nivelAguaMetro ?nivel . FILTER(?km > 25 && ?nivel < 1.0) }
```

**Resultados Obtidos:**
```text
trecho: BR471_KM_29 | km: 29.0
```

---

### Consulta 30
**Descrição:** Cenário Investigativo: Resumo completo de um evento (Qual o animal envolvido, em qual km da rodovia e sob qual clima).

**Código SPARQL:**
```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX taim: <http://www.exemplo.org/taim#>
SELECT ?evento ?animal ?km ?temp WHERE { ?evento taim:envolveAnimal ?animal . ?evento taim:ocorreEm ?trecho . ?trecho taim:kmRodovia ?km . ?evento taim:ocorreSob ?clima . ?clima taim:temperaturaCelsius ?temp . } LIMIT 5
```

**Resultados Obtidos:**
```text
evento: Acidente_Taim_001 | animal: Maçarico_2 | km: 28.0 | temp: 15.191119079497632
evento: Acidente_Taim_0016 | animal: Maçarico_5 | km: 28.0 | temp: 18.509518090974588
evento: Acidente_Taim_0022 | animal: Ratão-do-banhado_5 | km: 28.0 | temp: 18.509518090974588
evento: Acidente_Taim_0030 | animal: Tachã_4 | km: 28.0 | temp: 18.509518090974588
evento: Acidente_Taim_0034 | animal: Jacaré-de-papo-amarelo_3 | km: 28.0 | temp: 15.191119079497632
```

---

