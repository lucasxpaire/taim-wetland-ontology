import os
from rdflib import Graph
from definicao_consultas import obter_todas_as_consultas

CAMINHO_ONTOLOGIA = os.path.join(os.path.dirname(__file__), "..", "ontology", "ontologia_populada.owl")
CAMINHO_RELATORIO = os.path.join(os.path.dirname(__file__), "..", "docs", "relatorio_sparql.md")

def carregar_grafo_rdf() -> Graph:
    print("Carregando ontologia para o motor SPARQL...")
    g = Graph()
    g.parse(CAMINHO_ONTOLOGIA, format="xml")
    return g

def formatar_resultado_sparql(resultado) -> str:
    linhas = []
    vars = resultado.vars
    if not vars:
        return "Nenhum resultado retornado ou consulta de agregação nula."
        
    for row in resultado:
        valores = []
        for var in vars:
            val = row[var]
            if val is not None:
                texto_limpo = str(val).replace("http://www.exemplo.org/taim#", "")
                valores.append(f"{var}: {texto_limpo}")
        linhas.append(" | ".join(valores))
        
    if not linhas:
        return "Zero resultados encontrados."
        
    if len(linhas) > 10:
        texto = "\n".join(linhas[:10])
        texto += f"\n... (e mais {len(linhas) - 10} resultados ocultados por brevidade)"
        return texto
    return "\n".join(linhas)

def gerar_relatorio_markdown(consultas: list, grafo: Graph):
    print("Iniciando execução das consultas...")
    
    with open(CAMINHO_RELATORIO, "w", encoding="utf-8") as f:
        f.write("# Relatório Final: Consultas SPARQL (Etapa 5)\n\n")
        f.write("Este documento apresenta as 30 consultas SPARQL em OWL sobre a ontologia populada.\n\n")
        
        categoria_atual = ""
        for i, consulta in enumerate(consultas, 1):
            if consulta["categoria"] != categoria_atual:
                categoria_atual = consulta["categoria"]
                f.write(f"## Categoria: {categoria_atual}\n\n")
                
            f.write(f"### Consulta {i}\n")
            f.write(f"**Descrição:** {consulta['descricao']}\n\n")
            f.write("**Código SPARQL:**\n```sparql\n")
            f.write(consulta["codigo"].strip() + "\n```\n\n")
            
            f.write("**Resultados Obtidos:**\n```text\n")
            try:
                res = grafo.query(consulta["codigo"])
                texto_resultado = formatar_resultado_sparql(res)
                f.write(texto_resultado + "\n")
            except Exception as e:
                f.write(f"Erro: {str(e)}\n")
            f.write("```\n\n---\n\n")

if __name__ == "__main__":
    grafo_ontologia = carregar_grafo_rdf()
    lista_consultas = obter_todas_as_consultas()
    
    gerar_relatorio_markdown(lista_consultas, grafo_ontologia)
    print(f"Sucesso! Relatório gerado em: {CAMINHO_RELATORIO}")
