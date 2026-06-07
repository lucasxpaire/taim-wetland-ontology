## 1. O que é uma Ontologia?
É uma representação formal do conhecimento de um domínio específico. Ela define os conceitos (classes), as propriedades desses conceitos e as relações entre eles. 
No nosso projeto, a ontologia organiza o conhecimento sobre o ecossistema do **Banhado do Taim** e os **eventos de atropelamento de fauna**, permitindo que computadores (e algoritmos de IA) "entendam" as relações ecológicas e espaciais.

## 2. Componentes Principais da Nossa Ontologia

### 2.1 Classes (Conceitos)
Classes são os conjuntos ou categorias de coisas no nosso domínio. Elas formam uma hierarquia (taxonomia).
* **Superclasses (Classes Gerais):**
  * `Animal`: Representa qualquer ser vivo da fauna.
  * `Habitat`: Representa os diferentes tipos de ambientes ecológicos.
  * `Infraestrutura`: Elementos construídos pelo homem.
  * `Evento`: Acontecimentos no domínio (como os atropelamentos).
  * `FatorAmbiental`: Condições que influenciam o ambiente e os eventos.
* **Subclasses (Classes Específicas):**
  * `Capivara`, `Ave` herdam de `Animal`. (Ou seja, toda Capivara é um Animal).
  * `Banhado`, `CorpoDagua` herdam de `Habitat`.
  * `Rodovia`, `TrechoRodovia` herdam de `Infraestrutura`.
  * `EventoAtropelamento` herda de `Evento`.
  * `CondicaoClimatica` herda de `FatorAmbiental`.

> **Por que modelamos assim? (Justificativa de Modelagem)**: Esta estrutura modular permite separar claramente a biologia (Animais/Habitats) da infraestrutura (Rodovias) e dos acontecimentos dinâmicos (Eventos). Se no futuro o projeto quiser focar em poluição em vez de atropelamento, basta criar uma nova subclasse de `Evento`, reaproveitando todo o resto.

### 2.2 Propriedades de Objeto (Object Properties)
As Propriedades de Objeto ligam um indivíduo de uma classe a um indivíduo de outra classe (relação entre duas entidades).
* `envolveAnimal`: Relaciona um `EventoAtropelamento` a um `Animal`.
* `ocorreEm`: Relaciona um `EventoAtropelamento` a um `TrechoRodovia`. (Relação Espacial)
* `ocorreSob`: Relaciona um `EventoAtropelamento` a uma `CondicaoClimatica`. (Relação de Contexto/Temporal/Clima)
* `proximoA`: Relaciona um `TrechoRodovia` a um `Habitat`. (Relação Espacial)
* `viveEm`: Relaciona um `Animal` a um `Habitat`.
* `atravessa`: Relaciona um `Animal` a uma `Rodovia`.

### 2.3 Propriedades de Dados (Data Properties)
As Propriedades de Dados ligam um indivíduo a um valor primitivo (texto, número, data, etc).
* `nomeCientifico` (string): Nome biológico de um animal.
* `kmRodovia` (float): O quilômetro exato do TrechoRodovia.
* `velocidadeMaxima` (int): Velocidade da via.
* `dataHoraEvento` (datetime): Quando o atropelamento ocorreu. (Relação Temporal)
* `temperatura` (float): A temperatura exata no momento.
* `riscoCalculado` (float): Propriedade reservada para ser preenchida pelo algoritmo de Machine Learning.

### 2.4 Indivíduos (Instâncias)
Os indivíduos são os dados reais que povoam a ontologia. Enquanto `Capivara` é uma classe teórica, `capivara_001` é um animal específico que sofreu um acidente.
Exemplo no nosso modelo:
* **Indivíduo**: `evento_045` (Instância de `EventoAtropelamento`)
  * *envolveAnimal*: `capivara_001` (Instância de `Capivara`)
  * *ocorreEm*: `trecho_BR471_km32` (Instância de `TrechoRodovia`)
  * *ocorreSob*: `chuva_forte` (Instância de `CondicaoClimatica`)

## 3. Consultas SPARQL (O poder da inferência)
O SPARQL é uma linguagem de consulta (como o SQL para bancos de dados), mas feita para ontologias e grafos.
Como nossa ontologia liga tudo semanticamente, podemos fazer perguntas complexas como: *"Quais animais foram atropelados em trechos próximos a banhados durante a chuva?"*.

A ontologia vai navegar pelos links: 
`Evento` -> `ocorreSob` -> `Chuva` 
`Evento` -> `ocorreEm` -> `Trecho` -> `proximoA` -> `Banhado`
`Evento` -> `envolveAnimal` -> `?animal`

## 4. Integração com Machine Learning (IA Explicável)
A integração proposta funciona assim:
1. Um modelo preditivo de ML (ex: Random Forest, Rede Neural) recebe dados (km 32, horário, chuva) e diz: **"Risco de Atropelamento: 85%"**. O modelo é uma "caixa preta", ele apenas cospe o número.
2. A **Ontologia entra para explicar o porquê**. Consultando a ontologia no KM 32, o sistema infere: "No KM 32 há um banhado próximo, que é habitat de capivaras, e a condição de chuva reduz a visibilidade".
3. Resultado: A IA se torna Explicável (Explainable AI - XAI).

## 5. Como o Owlready2 funciona?
Usaremos a biblioteca `owlready2` no Python para não precisarmos clicar manualmente 100 vezes no software Protégé. O Python criará as classes dinamicamente e salvará o arquivo `taim_ontology.owl`. Depois, nosso script de povoamento poderá ler arquivos CSV ou extrair da Wikipedia e criar instâncias automaticamente usando código Python limpo e rápido.

## Alternativas de Modelagem Descartadas (Para o Requisito)
* **Alternativa 1:** Colocar as condições climáticas e espaciais como simples "Data Properties" (texto) dentro do evento. (ex: `clima="chuva"`). *Por que foi descartada?* Porque perderíamos a semântica. Ao modelar `CondicaoClimatica` como uma **Classe** e usar `ocorreSob`, podemos criar hierarquias de clima e conectar outras propriedades ao clima em si, permitindo inferências mais ricas nas consultas SPARQL.
* **Alternativa 2:** Modelar cada espécie de animal (ex: Capivara) como um indivíduo da classe `Animal`, em vez de criar subclasses. *Por que foi descartada?* Se a espécie for apenas um indivíduo, não podemos ter "várias capivaras reais". Criando `Capivara` como uma subclasse de `Animal`, podemos instanciar `capivara_001`, `capivara_002`, representando as vítimas reais dos eventos e permitindo o povoamento de 100+ indivíduos.
