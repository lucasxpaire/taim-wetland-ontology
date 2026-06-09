PREFIXOS = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX taim: <http://www.exemplo.org/taim#>
"""

def obter_todas_as_consultas():
    consultas = []
    
    # --- 1. CONSULTAS SIMPLES (POR CLASSE) ---
    consultas.extend([
        {
            "categoria": "Simples",
            "descricao": "Listar todas as Capivaras registradas na ontologia.",
            "codigo": PREFIXOS + "SELECT ?capivara WHERE { ?capivara rdf:type taim:Capivara . }"
        },
        {
            "categoria": "Simples",
            "descricao": "Listar todos os Jacarés-de-papo-amarelo registrados.",
            "codigo": PREFIXOS + "SELECT ?jacare WHERE { ?jacare rdf:type taim:Jacaré-de-papo-amarelo . }"
        },
        {
            "categoria": "Simples",
            "descricao": "Listar todos os trechos de rodovia mapeados.",
            "codigo": PREFIXOS + "SELECT ?trecho WHERE { ?trecho rdf:type taim:TrechoRodovia . }"
        },
        {
            "categoria": "Simples",
            "descricao": "Listar todos os Eventos de Atropelamento.",
            "codigo": PREFIXOS + "SELECT ?evento WHERE { ?evento rdf:type taim:EventoAtropelamento . }"
        },
        {
            "categoria": "Simples",
            "descricao": "Listar todas as Condições Climáticas registradas.",
            "codigo": PREFIXOS + "SELECT ?clima WHERE { ?clima rdf:type taim:CondicaoClimatica . }"
        },
        {
            "categoria": "Simples",
            "descricao": "Listar todos os habitats do tipo Banhado.",
            "codigo": PREFIXOS + "SELECT ?banhado WHERE { ?banhado rdf:type taim:Banhado . }"
        }
    ])

    # --- 2. CONSULTAS COM MÚLTIPLAS RELAÇÕES ---
    consultas.extend([
        {
            "categoria": "Múltiplas Relações",
            "descricao": "Buscar eventos associados a um animal específico e o trecho onde ocorreu.",
            "codigo": PREFIXOS + "SELECT ?evento ?animal ?trecho WHERE { ?evento rdf:type taim:EventoAtropelamento . ?evento taim:envolveAnimal ?animal . ?evento taim:ocorreEm ?trecho . }"
        },
        {
            "categoria": "Múltiplas Relações",
            "descricao": "Descobrir em quais habitats os animais acidentados costumam viver.",
            "codigo": PREFIXOS + "SELECT DISTINCT ?animal ?habitat WHERE { ?evento rdf:type taim:EventoAtropelamento . ?evento taim:envolveAnimal ?animal . ?animal taim:viveEm ?habitat . }"
        },
        {
            "categoria": "Múltiplas Relações",
            "descricao": "Listar trechos de rodovia, seus acidentes e as condições climáticas exatas no momento.",
            "codigo": PREFIXOS + "SELECT ?trecho ?evento ?clima WHERE { ?evento taim:ocorreEm ?trecho . ?evento taim:ocorreSob ?clima . }"
        },
        {
            "categoria": "Múltiplas Relações",
            "descricao": "Buscar trechos de rodovia que registraram acidentes e também estão próximos a um banhado.",
            "codigo": PREFIXOS + "SELECT ?trecho ?evento ?banhado WHERE { ?evento taim:ocorreEm ?trecho . ?trecho taim:proximoA ?banhado . ?banhado rdf:type taim:Banhado . }"
        },
        {
            "categoria": "Múltiplas Relações",
            "descricao": "Listar animais que atravessaram a rodovia e se envolveram em um acidente.",
            "codigo": PREFIXOS + "SELECT ?animal ?evento WHERE { ?animal taim:atravessa ?trecho . ?evento taim:envolveAnimal ?animal . }"
        },
        {
            "categoria": "Múltiplas Relações",
            "descricao": "Listar animais mamíferos, o evento associado e o trecho onde ocorreu.",
            "codigo": PREFIXOS + "SELECT ?mamifero ?evento ?trecho WHERE { ?mamifero rdf:type taim:Mamifero . ?evento taim:envolveAnimal ?mamifero . ?evento taim:ocorreEm ?trecho . }"
        }
    ])

    # --- 3. CONSULTAS COM FILTROS (Temperatura, KM) ---
    consultas.extend([
        {
            "categoria": "Filtros",
            "descricao": "Listar eventos ocorridos em clima frio (Temperatura Celsius < 15°C).",
            "codigo": PREFIXOS + "SELECT ?evento ?temp WHERE { ?evento taim:ocorreSob ?clima . ?clima taim:temperaturaCelsius ?temp . FILTER(?temp < 15) }"
        },
        {
            "categoria": "Filtros",
            "descricao": "Listar acidentes de severidade 'Fatal'.",
            "codigo": PREFIXOS + "SELECT ?evento WHERE { ?evento taim:severidadeAcidente ?severidade . FILTER(str(?severidade) = 'Fatal') }"
        },
        {
            "categoria": "Filtros",
            "descricao": "Listar trechos de rodovia antes do KM 20.",
            "codigo": PREFIXOS + "SELECT ?trecho ?km WHERE { ?trecho taim:kmRodovia ?km . FILTER(?km < 20) }"
        },
        {
            "categoria": "Filtros",
            "descricao": "Listar habitats com nível de água perigosamente alto (Nível > 2 metros).",
            "codigo": PREFIXOS + "SELECT ?habitat ?nivel WHERE { ?habitat taim:nivelAguaMetro ?nivel . FILTER(?nivel > 2) }"
        },
        {
            "categoria": "Filtros",
            "descricao": "Listar eventos envolvendo apenas Capivaras (filtragem por string no nome comum).",
            "codigo": PREFIXOS + "SELECT ?evento ?nome WHERE { ?evento taim:envolveAnimal ?animal . ?animal taim:nomeComum ?nome . FILTER(str(?nome) = 'Capivara') }"
        },
        {
            "categoria": "Filtros",
            "descricao": "Listar eventos de atropelamento ocorridos em altas temperaturas (> 30°C).",
            "codigo": PREFIXOS + "SELECT ?evento ?temp WHERE { ?evento taim:ocorreSob ?clima . ?clima taim:temperaturaCelsius ?temp . FILTER(?temp > 30) }"
        }
    ])

    # --- 4. CONSULTAS COM AGREGAÇÃO ---
    consultas.extend([
        {
            "categoria": "Agregação",
            "descricao": "Contar o número total de eventos de atropelamento.",
            "codigo": PREFIXOS + "SELECT (COUNT(?evento) AS ?totalAcidentes) WHERE { ?evento rdf:type taim:EventoAtropelamento . }"
        },
        {
            "categoria": "Agregação",
            "descricao": "Contar o número de animais vitimados agrupados por habitat em que vivem.",
            "codigo": PREFIXOS + "SELECT ?habitat (COUNT(?animal) AS ?totalAnimais) WHERE { ?animal taim:viveEm ?habitat . ?evento taim:envolveAnimal ?animal . } GROUP BY ?habitat"
        },
        {
            "categoria": "Agregação",
            "descricao": "Contar o número de acidentes agrupados por Trecho de Rodovia.",
            "codigo": PREFIXOS + "SELECT ?trecho (COUNT(?evento) AS ?totalAcidentes) WHERE { ?evento taim:ocorreEm ?trecho . } GROUP BY ?trecho"
        },
        {
            "categoria": "Agregação",
            "descricao": "Descobrir a temperatura máxima registrada nos eventos.",
            "codigo": PREFIXOS + "SELECT (MAX(?temp) AS ?maxTemp) WHERE { ?evento taim:ocorreSob ?clima . ?clima taim:temperaturaCelsius ?temp . }"
        },
        {
            "categoria": "Agregação",
            "descricao": "Descobrir o KM médio onde os acidentes ocorrem.",
            "codigo": PREFIXOS + "SELECT (AVG(?km) AS ?kmMedio) WHERE { ?evento taim:ocorreEm ?trecho . ?trecho taim:kmRodovia ?km . }"
        },
        {
            "categoria": "Agregação",
            "descricao": "Contar o número de acidentes que foram fatais.",
            "codigo": PREFIXOS + "SELECT (COUNT(?evento) AS ?fatais) WHERE { ?evento taim:severidadeAcidente ?sev . FILTER(str(?sev) = 'Fatal') }"
        }
    ])

    # --- 5. CONSULTAS REPRESENTANDO CENÁRIO RELEVANTE ---
    consultas.extend([
        {
            "categoria": "Cenário",
            "descricao": "Cenário de Risco Crítico: Quais rodovias acumularam chuva forte (Temperatura < 20°C) e tiveram acidentes fatais?",
            "codigo": PREFIXOS + "SELECT ?trecho ?temp ?sev WHERE { ?evento taim:ocorreEm ?trecho . ?evento taim:ocorreSob ?clima . ?clima taim:temperaturaCelsius ?temp . ?evento taim:severidadeAcidente ?sev . FILTER(?temp < 20 && str(?sev) = 'Fatal') }"
        },
        {
            "categoria": "Cenário",
            "descricao": "Cenário de Deslocamento Animal: Quais animais aquáticos (Aves) sofreram acidentes em KMs próximos ao Banhado da Mangueira?",
            "codigo": PREFIXOS + "SELECT ?ave ?trecho WHERE { ?ave rdf:type taim:Ave . ?evento taim:envolveAnimal ?ave . ?evento taim:ocorreEm ?trecho . ?trecho taim:proximoA ?habitat . FILTER(REGEX(str(?habitat), 'Mangueira', 'i')) }"
        },
        {
            "categoria": "Cenário",
            "descricao": "Cenário de Prevenção: Obter a lista de trechos com acidentes de grandes mamíferos (Capivara) para possível instalação de placas.",
            "codigo": PREFIXOS + "SELECT DISTINCT ?trecho WHERE { ?evento taim:ocorreEm ?trecho . ?evento taim:envolveAnimal ?animal . ?animal rdf:type taim:Capivara . }"
        },
        {
            "categoria": "Cenário",
            "descricao": "Cenário Hidrológico: Animais atropelados perto de habitats com nível de água muito alto (risco de inundação forçando fuga).",
            "codigo": PREFIXOS + "SELECT ?animal ?nivel WHERE { ?evento taim:envolveAnimal ?animal . ?animal taim:viveEm ?habitat . ?habitat taim:nivelAguaMetro ?nivel . FILTER(?nivel >= 2.0) }"
        },
        {
            "categoria": "Cenário",
            "descricao": "Cenário de Rota Segura: Encontrar trechos da BR-471 (KM > 25) que não possuem banhados próximos com níveis altos de água.",
            "codigo": PREFIXOS + "SELECT ?trecho ?km WHERE { ?trecho taim:kmRodovia ?km . ?trecho taim:proximoA ?habitat . ?habitat taim:nivelAguaMetro ?nivel . FILTER(?km > 25 && ?nivel < 1.0) }"
        },
        {
            "categoria": "Cenário",
            "descricao": "Cenário Investigativo: Resumo completo de um evento (Qual o animal envolvido, em qual km da rodovia e sob qual clima).",
            "codigo": PREFIXOS + "SELECT ?evento ?animal ?km ?temp WHERE { ?evento taim:envolveAnimal ?animal . ?evento taim:ocorreEm ?trecho . ?trecho taim:kmRodovia ?km . ?evento taim:ocorreSob ?clima . ?clima taim:temperaturaCelsius ?temp . } LIMIT 5"
        }
    ])

    return consultas
