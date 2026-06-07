# Conceitos de Ontologia

**Ontologia**
Representação formal de um domínio de conhecimento através de conceitos e das relações entre eles.
* **Exemplo**: Um modelo lógico conectando fauna, clima e rodovias no Banhado do Taim.

**Classes**
Categorias amplas que agrupam entidades com características semelhantes.
* **Exemplo**: `Animal`, `Habitat`.

**Subclasses (Hierarquia)**
Especialização de uma classe mais ampla. Toda subclasse herda as propriedades de sua superclasse.
* **Exemplo**: `Capivara` é uma subclasse de `Animal`.

**Propriedades de Objeto (Object Properties)**
Relações semânticas que conectam dois indivíduos de classes (podem ser iguais ou diferentes).
* **Exemplo**: O evento de atropelamento `ocorreEm` um trecho de rodovia.

**Propriedades de Dados (Data Properties)**
Atributos que conectam um indivíduo a um tipo de dado primitivo (texto, número, data).
* **Exemplo**: A `velocidadeMaxima` de uma rodovia é `80` (inteiro).

**Indivíduos (Instâncias)**
Entidades concretas e específicas que pertencem a uma classe. São os dados reais que povoam a ontologia.
* **Exemplo**: `capivara_001` (um animal específico), `evento_045` (um acidente específico).

**Consultas SPARQL**
Linguagem estruturada para buscar informações na ontologia baseada na navegação de suas relações.
* **Exemplo**: Buscar os eventos de atropelamento (`?evento`) onde a condição climática (`ocorreSob`) é chuva forte.
