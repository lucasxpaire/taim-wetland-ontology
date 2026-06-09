# Rascunho do Relatório Final: Ontologia do Banhado do Taim

Este documento servirá como a **base do seu Relatório Final em PDF**. Conforme formos avançando no projeto, nós preencheremos as seções abaixo. Assim, quando o trabalho terminar, o seu relatório já estará praticamente escrito!

---

## 1. Conceitos Aplicados (Fundamentação)
* **Ontologia:** Representação formal conectando fauna, clima e infraestrutura no Banhado do Taim.
* **Classes:** Categorias amplas (`Animal`, `Habitat`).
* **Subclasses (Hierarquia):** Especialização (`Capivara` é subclasse de `Animal`).
* **Propriedades de Objeto:** Relações semânticas (O evento de atropelamento `ocorreEm` um trecho de rodovia).
* **Propriedades de Dados:** Atributos primitivos (A `velocidadeVia` de uma rodovia é `80`).
* **Indivíduos:** Instâncias reais (`capivara_001`, `evento_045`).

---

## 2. Decisões de Modelagem (Requisito Obrigatório)

Nesta etapa inicial de estruturação (`base_ontology.py`), nós tomamos as seguintes decisões para garantir a coerência do modelo ecológico mantendo a simplicidade:

### 2.1 Justificativas das Classes Escolhidas
Optou-se por atingir a marca de exatamente 15 classes utilizando a estrutura ecológica mais relevante para o Banhado do Taim:
1. **Animal** e suas ramificações (`Mamifero`, `Ave`, `Reptil`, `Anfibio`). Justificativa: Permite herança de propriedades e facilita o povoamento com espécies nativas do Banhado.
2. **Habitat** (`Banhado`, `CorpoDagua`, `Vegetacao`). Justificativa: Essencial para mapear de onde o animal vem antes de cruzar a pista.
3. **Rodovia** (`TrechoRodovia`). Justificativa: O acidente ocorre em um quilômetro específico, não na via inteira.
4. **CondicaoAmbiental** (`CondicaoClimatica`). Justificativa: Fatores externos que afetam o risco (como visibilidade e comportamento animal).
5. **Evento** (`EventoAtropelamento`). Justificativa: O foco central da ontologia, que atua como o "nó" que liga o animal, a via e o clima.

### 2.2 Alternativas de Modelagem Descartadas (Requisito Obrigatório)
Para chegar ao modelo atual, consideramos e descartamos outras abordagens:

* **Alternativa Descartada 1: Usar "Infraestrutura" como Superclasse Genérica**
  * *O que era:* Criar a superclasse genérica `Infraestrutura` e colocar `Rodovia` dentro dela.
  * *Por que foi descartada:* O escopo do projeto foca exclusivamente em atropelamentos na estrada (BR-471). Manter uma classe `Infraestrutura` seria um excesso sem utilidade prática (não mapearíamos prédios ou fazendas). Assim, simplificamos promovendo `Rodovia` a superclasse.
* **Alternativa Descartada 2: Tratar o Clima e o Horário como "Classes" Separadas**
  * *O que era:* Criar uma classe chamada `Horario` e uma chamada `CondicaoAmbiental`.
  * *Por que foi descartada:* O horário não é uma entidade física do ecossistema, é uma medida de tempo. Foi muito mais coerente transformá-lo em uma *Propriedade de Dados* (`dataHora` do tipo datetime) atrelada ao `Evento`. Isso simplificou as consultas SPARQL temporais exigidas no escopo.

---

## 3. Povoamento da Ontologia (A fazer nas próximas etapas)
*(Nesta seção, documentaremos como o script `povoamento.py` foi feito, como geramos os 100 indivíduos automaticamente usando Python e quais os possíveis vieses ou limitações desses dados gerados).*

* Lembrete: Inserir capturas de tela do Protégé mostrando os 100 indivíduos gerados.

---

## 4. Consultas SPARQL (A fazer nas últimas etapas)
*(Nesta seção, listaremos as nossas consultas SPARQL respondendo ao requisito de descrever o código, o objetivo em linguagem natural e o resultado obtido).*
