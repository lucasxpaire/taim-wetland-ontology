import os

ARQUIVO_SPARQL = os.path.join(os.path.dirname(__file__), "..", "docs", "relatorio_sparql.md")
ARQUIVO_TEX = os.path.join(os.path.dirname(__file__), "..", "docs", "relatorio.tex")

def converter_sparql_para_latex() -> str:
    if not os.path.exists(ARQUIVO_SPARQL):
        return "Arquivo SPARQL não encontrado."
        
    latex_str = ""
    with open(ARQUIVO_SPARQL, "r", encoding="utf-8") as f:
        linhas = f.readlines()
        
    dentro_codigo = False
    
    for linha in linhas:
        if linha.startswith("## Categoria:"):
            categoria = linha.replace("## Categoria:", "").strip()
            latex_str += f"\\subsection*{{Categoria: {categoria}}}\n\n"
        elif linha.startswith("### Consulta"):
            consulta = linha.replace("###", "").strip()
            latex_str += f"\\subsubsection*{{{consulta}}}\n\n"
        elif linha.startswith("**Descrição:**"):
            desc = linha.replace("**Descrição:**", "").strip()
            latex_str += f"\\textbf{{Descrição:}} {desc}\n\n"
        elif linha.startswith("**Código SPARQL:**"):
            latex_str += "\\textbf{Código SPARQL:}\n"
        elif linha.startswith("**Resultados Obtidos:**"):
            latex_str += "\\textbf{Resultados Obtidos:}\n"
        elif linha.startswith("```"):
            if dentro_codigo:
                latex_str += "\\end{lstlisting}\n\n"
                dentro_codigo = False
            else:
                latex_str += "\\begin{lstlisting}\n"
                dentro_codigo = True
        elif linha.startswith("---"):
            latex_str += "\\vspace{1cm}\n"
        else:
            if dentro_codigo:
                latex_str += linha
            
    return latex_str

def gerar_latex():
    sparql_latex = converter_sparql_para_latex()
    
    conteudo_latex = f"""\\documentclass[12pt,a4paper]{{article}}
\\usepackage[utf8]{{inputenc}}
\\usepackage[T1]{{fontenc}}
\\usepackage[portuguese]{{babel}}
\\usepackage{{graphicx}}
\\usepackage{{geometry}}
\\usepackage{{listings}}
\\usepackage{{float}}
\\geometry{{a4paper, margin=2cm}}

\\title{{Relatório: Ontologia do Banhado do Taim}}
\\author{{Miguel Brondani \\and Lucas Pairé}}
\\date{{\\today}}

\\begin{{document}}

\\maketitle

\\section{{Abordagem da Solução}}
Este relatório descreve o desenvolvimento de uma ontologia em OWL para representar o ecossistema do Banhado do Taim e os eventos de atropelamento de fauna na rodovia BR-471. A estrutura organiza as espécies animais, trechos da rodovia, habitats e condições climáticas. 

Para o povoamento, um script Python coletou dados sobre a fauna da região diretamente da Wikipédia, garantindo o uso de espécies reais. Outro script automatizou a geração e inserção de indivíduos (instâncias) de acidentes e trechos rodoviários, aplicando restrições de cardinalidade do modelo.

\\section{{Modelagem da Ontologia}}
A ontologia foi organizada em cinco superclasses principais: Animal, Habitat, Rodovia, CondicaoAmbiental e Evento. A classe Animal contém classes para grupos taxonômicos (Mamifero, Ave, Reptil, Anfibio), que por sua vez possuem subclasses específicas para cada espécie validada (como Capivara e Jacaré-de-papo-amarelo). O modelo define dez propriedades de objeto (ex: envolveAnimal, ocorreEm) e treze propriedades de dados (ex: kmRodovia, fluxoVeiculosHora).

Também foram aplicadas restrições de cardinalidade nas classes principais:
\\begin{{itemize}}
    \\item \\textbf{{EventoAtropelamento}}: deve envolver exatamente 1 Animal, ocorrer em exatamente 1 TrechoRodovia, ocorrer sob exatamente 1 CondicaoClimatica, ter exatamente 1 severidadeAcidente e 1 dataHora.
    \\item \\textbf{{TrechoRodovia}}: deve pertencer a exatamente 1 Rodovia e ter exatamente 1 kmRodovia.
\\end{{itemize}}

\\vspace{{8cm}}
A Figura 1 apresenta a hierarquia principal das classes no Protégé.

\\begin{{figure}}[H]
\\centering
\\includegraphics[width=0.4\\textwidth]{{images/classes.jpeg}}
\\caption{{Hierarquia de classes no Protégé}}
\\end{{figure}}

As propriedades de objeto definem a relação entre os conceitos. A Figura 2 ilustra a interface de criação.

\\begin{{figure}}[H]
\\centering
\\includegraphics[width=0.8\\textwidth]{{images/propriedadesObjeto.jpeg}}
\\caption{{Propriedades de Objeto}}
\\end{{figure}}

\\vspace{{1cm}}
As propriedades de dados guardam métricas como coordenadas de GPS e temperatura. A Figura 3 mostra o mapeamento.

\\begin{{figure}}[H]
\\centering
\\includegraphics[width=0.4\\textwidth]{{images/propriedadesDados.jpeg}}
\\caption{{Propriedades de Dados}}
\\end{{figure}}

\\subsection*{{Decisões de Modelagem e Alternativas Consideradas}}

\\textbf{{Justificativa das Decisões de Modelagem:}}
Os fatores de risco foram modelados diretamente como atributos (tráfego como fluxo de veículos no trecho, e visibilidade como propriedade do clima), o que simplifica o esquema de classes. A estação do ano (estacaoAno) foi incluída no evento para possibilitar buscas por período sazonal de forma direta.

\\textbf{{Alternativas Consideradas e Descartadas:}}
\\begin{{enumerate}}
    \\item \\textbf{{Espécies como atributos vs. Subclasses:}} Cogitou-se modelar espécies apenas como atributos de texto (ex: indivíduos da classe Mamifero com um campo nomeComum = "Capivara"). Isso foi descartado porque impedia consultas baseadas na classe específica (ex: buscar instâncias de Capivara). Definir cada espécie como uma subclasse resolveu o problema e tornou a hierarquia taxonômica correta.
    
    \\item \\textbf{{Severidade como Classe vs. Propriedade de Dados:}} Considerou-se criar uma classe própria para a severidade do acidente. A ideia foi descartada para evitar complexidade desnecessária no grafo, optando-se por um campo simples de texto no evento (ex: "Fatal", "Fuga").
\\end{{enumerate}}

\\section{{Povoamento Automatizado}}
O povoamento da ontologia gerou 137 indivíduos através de um script Python. O script cruzou as espécies coletadas da Wikipédia com trechos da rodovia BR-471 (KMs 10 a 29) e gerou 60 acidentes fictícios sob diferentes condições:

\\begin{{itemize}}
    \\item \\textbf{{Tráfego}}: preenchido através da propriedade \\textit{{fluxoVeiculosHora}} nos trechos rodoviários.
    \\item \\textbf{{Visibilidade}}: definida no clima. Dias ensolarados simulam visibilidade alta (1000m a 5000m), enquanto chuva ou neblina reduzem a visibilidade (20m a 300m).
    \\item \\textbf{{Estação do Ano}}: gerada automaticamente a partir do mês do evento (ex: Janeiro associado a "Verão", Julho a "Inverno").
\\end{{itemize}}

A Figura 4 comprova a geração e injeção automática dos eventos de atropelamento na classe final.

\\begin{{figure}}[H]
\\centering
\\includegraphics[width=0.8\\textwidth]{{images/individuos.jpeg}}
\\caption{{Lista de indivíduos da classe EventoAtropelamento}}
\\end{{figure}}

\\subsection*{{Limitações e Inconsistências de Dados}}
A modelagem possui algumas limitações e pontos de atenção:
\\begin{{itemize}}
    \\item \\textbf{{Extração de espécies}}: A busca por termos na Wikipédia é baseada em palavras-chave exatas, o que pode falhar caso o texto do artigo mude ou utilize termos alternativos.
    \\item \\textbf{{Dados simulados}}: Como não há acesso fácil a uma base de dados governamental pública e atualizada de acidentes no Taim, as instâncias de atropelamento e medições climáticas foram geradas artificialmente com valores plausíveis.
    \\item \\textbf{{Raciocínio OWL}}: A biblioteca RDFLib usada em Python não executa raciocínio OWL em tempo de execução de consultas SPARQL. Para contornar isso nas buscas por superclasses (como Mamifero ou Ave), foi necessário usar caminhos de propriedades transitivas (\\textit{{rdf:type/rdfs:subClassOf*}}) nas consultas.
\\end{{itemize}}

\\vspace{{8cm}}
\\section{{Grafo da Ontologia}}
A visualização no OntoGraf apresenta a rede de conexões entre os indivíduos mapeados (animais, trechos rodoviários, climas e eventos de atropelamento), demonstrando o relacionamento entre as instâncias da ontologia.

\\begin{{figure}}[H]
\\centering
\\includegraphics[width=0.8\\textwidth]{{images/ontologia.jpeg}}
\\caption{{Grafo de conexões (OntoGraf)}}
\\end{{figure}}

\\section{{Protocolo de Uso de LLM}}
Os modelos de linguagem foram utilizados como assistentes no desenvolvimento do código Python e na validação das consultas SPARQL e da sintaxe OWL. O processo seguiu três regras:
\\begin{{enumerate}}
    \\item Uso do modelo para estruturar e validar as consultas SPARQL complexas.
    \\item Apoio na escrita do código de injeção e povoamento da ontologia base.
    \\item Revisão das definições da ontologia para evitar erros de sintaxe.
\\end{{enumerate}}
Nenhuma informação ecológica ou de fauna foi gerada por alucinação; todas as espécies foram estritamente validadas a partir do texto obtido da Wikipédia.

\\section{{Consultas SPARQL}}
As trinta consultas exigidas foram automatizadas via script Python usando a biblioteca RDFLib. O código carregou o banco de conhecimento e extraiu os relatórios abaixo. As respostas comprovam a viabilidade das perguntas lógicas.

{sparql_latex}

\\end{{document}}
"""

    with open(ARQUIVO_TEX, "w", encoding="utf-8") as f:
        f.write(conteudo_latex)

if __name__ == "__main__":
    gerar_latex()
    print(f"Relatório LaTeX gerado em: {ARQUIVO_TEX}")
