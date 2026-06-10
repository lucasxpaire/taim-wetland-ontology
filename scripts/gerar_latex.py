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
    tipo_codigo = ""
    
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
                tipo_codigo = linha.replace("```", "").strip()
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
\\author{{Desenvolvimento Acadêmico}}
\\date{{\\today}}

\\begin{{document}}

\\maketitle

\\section{{Abordagem da Solução}}
Este relatório apresenta a modelagem de uma ontologia para o ecossistema do Banhado do Taim. O foco do projeto foi mapear eventos de atropelamentos de fauna na rodovia BR 471. A solução adotada foi criar um modelo limpo contendo exatamente quinze classes. A arquitetura garantiu responsabilidades claras para cada conceito ecológico.

A extração de dados utilizou um algoritmo em Python para validar as espécies animais direto da Wikipedia. Em seguida, outro algoritmo simulou e injetou as instâncias na ontologia final.

\\section{{Modelagem da Ontologia}}
A estrutura foi dividida em superclasses principais como Animal, Habitat, Rodovia, CondicaoAmbiental e Evento. O modelo contém dez propriedades de objeto que conectam esses conceitos. O modelo também possui dez propriedades de dados para atributos numéricos e textuais.

A Figura 1 apresenta a hierarquia principal das classes no Protégé.

\\begin{{figure}}[H]
\\centering
\\includegraphics[width=0.8\\textwidth]{{images/classes.jpeg}}
\\caption{{Hierarquia de classes no Protégé}}
\\end{{figure}}

As propriedades de objeto definem a relação entre os conceitos. A Figura 2 ilustra a interface de criação.

\\begin{{figure}}[H]
\\centering
\\includegraphics[width=0.8\\textwidth]{{images/propriedadesObjeto.jpeg}}
\\caption{{Propriedades de Objeto}}
\\end{{figure}}

As propriedades de dados guardam métricas como coordenadas de GPS e temperatura. A Figura 3 mostra o mapeamento.

\\begin{{figure}}[H]
\\centering
\\includegraphics[width=0.8\\textwidth]{{images/propriedadesDados.jpeg}}
\\caption{{Propriedades de Dados}}
\\end{{figure}}

\\section{{Povoamento Automatizado}}
O povoamento da ontologia gerou 137 indivíduos concretos. O cruzamento dos animais reais extraídos da Wikipedia com KMs da BR 471 simulou acidentes de trânsito em diferentes condições climáticas.

A Figura 4 comprova a geração e injeção automática dos eventos de atropelamento na classe final.

\\begin{{figure}}[H]
\\centering
\\includegraphics[width=0.8\\textwidth]{{images/individuos.jpeg}}
\\caption{{Lista de indivíduos da classe EventoAtropelamento}}
\\end{{figure}}

\\section{{Grafo da Ontologia}}
A visualização espacial comprova a estrutura de teia exigida no projeto. O OntoGraf gerou a visão completa das conexões entre os indivíduos de fauna e as ocorrências físicas.

\\begin{{figure}}[H]
\\centering
\\includegraphics[width=0.8\\textwidth]{{images/ontologia.jpeg}}
\\caption{{Grafo de conexões (OntoGraf)}}
\\end{{figure}}

\\section{{Protocolo de Emprego de LLMs}}
O uso de Grandes Modelos de Linguagem apoiou ativamente a construção arquitetural desta solução. O LLM serviu como assistente direto para planejamento do código Python e verificação da sintaxe OWL.

O protocolo seguiu três diretrizes estritas:
1. Validação de conhecimento extraído sobre as espécies reais do Taim.
2. Auxílio na escrita de consultas SPARQL complexas.
3. Geração de código automatizado e revisões estruturais para manter a base limpa e focada.

Nenhum dado fictício biológico foi inventado. O LLM operou restrito às regras de lógica de banco de dados e simulação numérica.

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
