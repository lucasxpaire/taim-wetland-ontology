Trabalho de Inteligência Artificial
Desenvolvimento de Ontologia para o Banhado do Taim

1. Contexto
Este trabalho da disciplina de Inteligência Artificial– IA está inserido em um projeto que
investiga fatores associados a atropelamentos de fauna na região do Banhado do Taim (RS).
A construção de uma ontologia para o Banhado do Taim é uma oportunidade de aplicar as
técnicas de representação de conhecimento da disciplina a um problema real de relevância
ambiental e social.
O Banhado do Taim é uma das áreas úmidas mais importantes do RS, com rica biodiver
sidade e papel essencial na preservação de ecossistemas. Ao estruturar o conhecimento sobre
espécies, habitats, condições ambientais e eventos como atropelamentos de fauna, o trabalho
pode contribuir para a organização e integração de informações que hoje estão dispersas.
A ontologia a ser desenvolvida neste trabalho não apenas favorece a compreensão do
domínio, mas também cria uma base para o desenvolvimento futuro de sistemas inteligentes
de monitoramento, apoio à decisão e conservação ambiental. Assim, o trabalho vai além do
exercício acadêmico: ele conecta teoria e prática, permitindo que a IA seja utilizada como
ferramenta para gerar impacto positivo no mundo real. Em especial, este trabalho focaliza a
representação de conhecimento, por meio da construção de uma ontologia do domínio.
O objetivo do trabalho é desenvolver uma ontologia em OWL que represente o domínio
ecológico e operacional relacionado ao Banhado do Taim. Este modelo poderá ser construído
utilizando a ferramenta Protégé e/ou outras bibliotecas Python para trabalhar com ontologias
(Owlready2, OWLAPY, etc). Ele deve contemplar, no mínimo, os seguintes conceitos:
• Animais
• Rodovias e trechos
• Eventos de atropelamento
• Condições ambientais (clima, horário, estação)
• Características do habitat (banhado, vegetação, água)
• Fatores de risco (tráfego, visibilidade, proximidade da água)
Os grupos podem ajustar ou expandir o escopo conforme necessidade

No exemplo da Figura 1, a classe Capivara é modelada como subclasse de Animal, en
quanto Banhado é subclasse de Habitat. A classe EventoAtropelamento se relaciona a en
tidades do domínio por propriedades como envolveAnimal, ocorreEm e ocorreSob. Além
das classes, o fragmento mostra indivíduos de exemplo, como capivara_001, evento_045 e
trecho_BR471_km32, ilustrando como a ontologia pode representar conhecimento especí
fico do domínio de forma estruturada e consultável. Considerando que a ontologia contém os
seguintes fatos:
• capivara_001 é instância de Capivara;
• evento_045 é instância de EventoAtropelamento;
• evento_045 envolveAnimal capivara_001;
• evento_045 ocorreEm trecho_BR471_km32;
• trecho_BR471_km32 proximoA banhado_do_taim;
• banhado_do_taim é instância de Banhado.
Exemplo de consulta:

PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX ex: <http://www.exemplo.org/taim#>
SELECT ?evento ?animal ?trecho ?condicao
WHERE {
?evento rdf:type ex:EventoAtropelamento .
?evento ex:envolveAnimal ?animal .
?evento ex:ocorreEm ?trecho .
?evento ex:ocorreSob ?condicao .
?animal rdf:type ex:Capivara .
?trecho ex:proximoA ?habitat .
?habitat rdf:type ex:Banhado .
}
Nesse caso, a consulta permite inferir operacionalmente que evento_045 corresponde a um
atropelamento de capivara ocorrido em um trecho rodoviário próximo a um habitat do tipo
banhado, sob uma determinada condição ambiental. Essa capacidade de relacionar múltiplos
conceitos do domínio é uma das vantagens centrais do uso de ontologias e consultas SPARQL.
Outro exemplo de consulta:
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX ex: <http://www.exemplo.org/taim#>
SELECT ?evento ?trecho
WHERE {
?evento rdf:type ex:EventoAtropelamento .
?evento ex:envolveAnimal ?animal .
?evento ex:ocorreEm ?trecho .
?evento ex:ocorreSob ?condicao .
?animal rdf:type ex:Capivara .
?condicao rdf:type ex:Clima .
?condicao ex:descricao "chuva_forte" .
}
Essa consulta recupera eventos de atropelamento envolvendo capivaras que ocorreram sob
condição climática de chuva forte. Com isso, torna-se possível investigar padrões do domínio
combinando semântica, contexto ambiental e localização.

2. Modelagem da Ontologia
A ontologia deve incluir:
• Classes (mínimo: 15, mas modelem quantas classes forem necessárias)
• Hierarquia de classes
• Propriedades de objeto (mínimo: 10, mas modelem quantas propriedades de objeto
forem necessárias)
• Propriedades de dados (mínimo: 10, mas modelem quantas propriedades de dados
forem necessárias)
• Restrições (domínio, alcance, cardinalidade, e outras restrições específicas que sejam
necessárias)
Além disso, deve incluir:
• Pelo menos uma relação temporal
• Pelo menos uma relação espacial
Requisito obrigatório:
• Justificar as principais decisões de modelagem
• Explicar pelo menos duas alternativas de modelagem que foram consideradas e descar
tadas

3. Povoamento da Ontologia
A ontologia deve ser populada com indivíduos utilizando:
• Inserção manual/automatizada de pelo menos 100 indivíduos no modelo da ontologia
no Protégé
• Desenvolvimento de script (Python ou similar) OU uso de ferramentas automatizadas
voltadas para a coleta e modelagem de conhecimento automatizada na ontologia
Conforme necessidade, o modelo da ontologia também pode ser construído, ajustado e
expandido com o apoio de algoritmos de ML devidamente explicados no trabalho.
Requisitos obrigatórios:
• Explicar claramente como os dados foram gerados
• Apresentar exemplos concretos das instâncias criadas
• Discutir possíveis inconsistências ou limitações dos dados

4. Fontes de Informação e Extração de Conhecimento
A construção da ontologia pode usar múltiplas fontes de informação, tanto estruturadas
quanto não estruturadas. A escolha dessas fontes é fundamental para garantir a qualidade
do conhecimento representado. No contexto do Banhado do Taim, é importante considerar
a diversidade de espécies, habitats e condições ambientais da região, incluindo mamíferos,
aves, répteis, corpos d’água, áreas alagadas, vegetação e infraestrutura viária.
4.1 Fontes de Informação
Os grupos podem utilizar diferentes tipos de fontes, incluindo:
• Bases abertas estruturadas:– Wikidata– DBpedia– Bases governamentais (ex.: dados ambientais, IBGE, ICMBio)
• Fontes textuais não estruturadas:– Wikipedia (páginas sobre espécies, habitats e ecossistemas)– Relatórios ambientais– Artigos científicos sobre fauna e ecologia do Taim
• Dados geográficos:– OpenStreetMap (rodovias, trechos, localização)– Mapas ambientais e hidrológicos
• Modelos de Linguagem (LLMs):– Extração de entidades e relações a partir de texto– Geração de exemplos de instâncias– Sugestão de classes e propriedades do domínio
Os grupos devem descrever claramente no relatório do trabalho:
• Quais fontes foram utilizadas
• Como os dados foram extraídos
• Limitações e possíveis erros do processo

4.2 Uso de LLMs
Modelos de linguagem podem ser utilizados como apoio para:
• Identificar conceitos relevantes (espécies, habitats, condições ambientais)
• Extrair relações ecológicas e espaciais
• Gerar exemplos de instâncias plausíveis
Contexto: "Aves aquáticas e capivaras são frequentemente encontradas em áreas alaga
das e próximas a lagoas no Banhado do Taim. Alguns animais atravessam rodovias nessas
regiões.". A partir desse contexto, um LLM pode auxiliar na extração de:
• Classes: Ave, Capivara, AreaAlagada, Lagoa, Rodovia
• Relações:– viveEm(Ave, AreaAlagada)– proximoA(Capivara, Lagoa)– atravessa(Animal, Rodovia)
Observação: Os resultados devem ser revisados, pois LLMs podem gerar informações
imprecisas ou generalizações incorretas.

4.3 Extração Automática de Conhecimento
Os grupos devem implementar ou descrever estratégias de extração automática de dados. A
seguir, alguns exemplos (não testados).
Exemplo 1: Extração de Wikipedia: extrair entidades e conceitos ecológicos
import requests
from bs4 import BeautifulSoup
url = "https://pt.wikipedia.org/wiki/Banhado_do_Taim"
html = requests.get(url).text
soup = BeautifulSoup(html, "html.parser")
texto = soup.get_text()
# Exemplo simples de identificação de termos relevantes
palavras_chave = ["água", "lagoa", "ave", "mamífero"]
for palavra in palavras_chave:
if palavra in texto:
print(f"Encontrado: {palavra}")

Exemplo 2: Extração com NLP: identificar relações semânticas em textos ecoló
gicos
import spacy
nlp = spacy.load("pt_core_news_sm")
texto = "Mamíferos e aves vivem próximos a áreas alagadas."
doc = nlp(texto)
for token in doc:
print(token.text, token.dep_)
Essa abordagem pode ajudar a identificar padrões como relações entre espécies e habitats.
Exemplo 3: Uso de LLM para extração estruturada: prompt exemplo
Extraia entidades e relações no formato:
(entidade1, relacao, entidade2)
Texto:
"Aves vivem próximas a lagoas e mamíferos cruzam rodovias."
Saída esperada:
(Ave, viveEm, Lagoa)
(Mamifero, cruza, Rodovia)
4.4 Integração com a Ontologia
Os dados extraídos devem ser convertidos para o modelo da ontologia, por exemplo:
• Criar indivíduos automaticamente
• Associar propriedades de objeto
• Preencher propriedades de dados
Exemplo:
ave_001 rdf:type Ave
ave_001 viveEm lagoa_01
lagoa_01 rdf:type CorpoDagua

5. Consultas SPARQL
Os grupos devem implementar pelo menos 30 consultas SPARQL, distribuídas em:
• Consulta simples (por classe)
• Consulta envolvendo múltiplas relações
• Consulta com filtros (ex.: horário, clima)
• Consulta com agregação
• Consulta representando um cenário relevante do domínio
Cada consulta deve incluir:
• Descrição em linguagem natural
• Código SPARQL
• Resultado obtido

6 Integração com Machine Learning (opcional)
Embora não seja obrigatório, os grupos podem propor uma integração entre a ontologia
desenvolvida e modelos de Machine Learning (ML), visando enriquecer a interpretação dos
resultados gerados por algoritmos preditivos.
6.1 Objetivo da integração
A ideia central é combinar:
• Modelos de ML: responsáveis por realizar predições (ex.: risco de atropelamento)
• Ontologia: responsável por fornecer explicações semânticas para essas predições
Essa integração permite transformar um modelo de “caixa-preta” em um sistema mais
interpretável.
6.2 Exemplo concreto no domínio do Taim
Considere um modelo de ML treinado para prever o risco de atropelamento de animais em
diferentes trechos da rodovia BR-471.
Entrada do modelo:
• Localização (km da rodovia)
• Horário
• Condições climáticas
• Proximidade de corpos d’água
• Tipo de habitat
Saída do modelo:
• Risco de atropelamento (ex.: 0.82 no km 32)
6.3 Uso da ontologia para explicação
A ontologia pode ser utilizada para explicar essa predição por meio de inferências e consultas
SPARQL.
Exemplo de fatos na ontologia:
• trecho_BR471_km32 proximoA banhado_do_taim
• banhado_do_taim rdf:type Banhado
• capivara viveEm banhado_do_taim
• capivara atravessa Rodovia
• condicao_climatica = chuva_forte
A partir desses dados, o sistema pode produzir uma explicação como:
“O risco de atropelamento é alto neste trecho porque:
• Otrecho está próximo a um habitat do tipo banhado
• Capivaras e outros animais são comuns nessa região
• Esses animais frequentemente atravessam rodovias
• Acondição climática (chuva forte) reduz a visibilidade
”
Neste cenário, a ontologia não realiza a predição, mas:
• Explica os fatores envolvidos
• Relaciona entidades do domínio
• Permite consultas estruturadas
• Aumenta a interpretabilidade do sistema
Se esta seção for explorada, os grupos devem:
• Descrever claramente o modelo de ML utilizado
• Simular exemplos concretos de predições (não precisa desenvolver o algoritmo preditivo)
• Demonstrar como a ontologia foi usada para gerar explicações
7. Entregas e apresentação
• Arquivo da ontologia (.owl)
• Código de scripts de povoamento
• Código de algoritmo de ML usados
• Protocolos de emprego de LLMs caso sejam usados
• Relatório em PDF (contendo, entre outros itens: capturas de tela do Protégé, trechos
gráficos da ontologia (OWL), execução das consultas SPARQL)
• Vídeo de até 5 minutos explicando a solução
Na apresentação oral do trabalho, os grupos poderão ser questionados sobre:
• Estrutura da ontologia
• Decisões de modelagem
• Coerência entre classes, propriedades e indivíduos
• Interpretação das consultas SPARQL
Observação: A avaliação considerará a coerência entre modelagem, dados e consultas.