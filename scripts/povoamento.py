import os
import random
from datetime import datetime, timedelta
from owlready2 import get_ontology

from extracao_wikipedia import obter_animais_confirmados

CAMINHO_BASE = os.path.join(os.path.dirname(__file__), "..", "ontology", "ontologia_taim.owl")
CAMINHO_POPULADO = os.path.join(os.path.dirname(__file__), "..", "ontology", "taim_ontology_populated.owl")

def carregar_ontologia_base():
    return get_ontology(f"file://{CAMINHO_BASE}").load()

def instanciar_habitats(onto):
    habitats_criados = []
    nomes_banhados = ["Banhado_da_Mangueira", "Banhado_do_Nicola", "Banhado_Central"]
    
    for i, nome in enumerate(nomes_banhados):
        banhado = onto.Banhado(nome)
        banhado.nivelAguaMetro = [random.uniform(0.5, 2.5)]
        habitats_criados.append(banhado)
        
    return habitats_criados

def instanciar_infraestrutura(onto, habitats):
    trechos_criados = []
    
    for km in range(10, 30):
        trecho = onto.TrechoRodovia(f"BR471_KM_{km}")
        trecho.kmRodovia = [float(km)]
        trecho.latitude = [random.uniform(-32.0, -33.0)]
        trecho.longitude = [random.uniform(-52.0, -53.0)]
        
        # Relaciona o trecho a um habitat proximo
        habitat_vizinho = random.choice(habitats)
        trecho.proximoA.append(habitat_vizinho)
        
        trechos_criados.append(trecho)
        
    return trechos_criados

def instanciar_animais_reais(onto, animais_validados, habitats):
    animais_criados = []
    
    # Mapeamento do nome da classe em string para a Classe Owlready2
    mapa_classes = {
        "Mamifero": onto.Mamifero,
        "Ave": onto.Ave,
        "Reptil": onto.Reptil,
        "Anfibio": onto.Anfibio
    }
    
    for classe_texto, especies in animais_validados.items():
        ClasseOntologia = mapa_classes.get(classe_texto, onto.Animal)
        
        for especie in especies:
            # Cria 5 individuos de cada especie
            for i in range(1, 6):
                animal = ClasseOntologia(f"{especie.replace(' ', '_')}_{i}")
                animal.nomeComum = [especie.capitalize()]
                
                # Relaciona animal ao habitat
                habitat_base = random.choice(habitats)
                animal.viveEm.append(habitat_base)
                
                animais_criados.append(animal)
                
    return animais_criados

def instanciar_condicoes_climaticas(onto):
    condicoes = []
    tipos = ["Chuva_Forte", "Neblina_Densa", "Ensolarado", "Nublado"]
    
    for i, tipo in enumerate(tipos):
        clima = onto.CondicaoClimatica(f"Clima_{tipo}_{i}")
        clima.temperaturaCelsius = [random.uniform(5.0, 35.0)]
        condicoes.append(clima)
        
    return condicoes

def gerar_data_aleatoria():
    inicio = datetime(2025, 1, 1)
    dias_aleatorios = random.randint(0, 365)
    horas_aleatorias = random.randint(0, 23)
    return inicio + timedelta(days=dias_aleatorios, hours=horas_aleatorias)

def instanciar_eventos_atropelamento(onto, animais, trechos, condicoes):
    eventos_criados = []
    
    # Criaremos 60 eventos para bater a meta de 100 individuos totais com folga
    for i in range(1, 61):
        evento = onto.EventoAtropelamento(f"Acidente_Taim_00{i}")
        
        animal_vitima = random.choice(animais)
        trecho_local = random.choice(trechos)
        clima_momento = random.choice(condicoes)
        
        # Propriedades de Objeto
        evento.envolveAnimal.append(animal_vitima)
        evento.ocorreEm.append(trecho_local)
        evento.ocorreSob.append(clima_momento)
        
        # O animal atravessa a rodovia
        animal_vitima.atravessa.append(trecho_local)
        
        # Propriedades de Dados
        evento.dataHora = [gerar_data_aleatoria()]
        evento.severidadeAcidente = [random.choice(["Fatal", "Ferimento_Leve", "Fuga"])]
        
        eventos_criados.append(evento)
        
    return eventos_criados

def popular_ontologia():
    print("Iniciando extração de dados reais da Wikipedia...")
    especies_reais = obter_animais_confirmados()
    
    print("Carregando Ontologia Base...")
    onto = carregar_ontologia_base()
    
    print("Gerando Indivíduos...")
    habitats = instanciar_habitats(onto)
    trechos = instanciar_infraestrutura(onto, habitats)
    animais = instanciar_animais_reais(onto, especies_reais, habitats)
    condicoes = instanciar_condicoes_climaticas(onto)
    
    eventos = instanciar_eventos_atropelamento(onto, animais, trechos, condicoes)
    
    total = len(habitats) + len(trechos) + len(animais) + len(condicoes) + len(eventos)
    
    print(f"Salvando {total} indivíduos...")
    onto.save(file=CAMINHO_POPULADO, format="rdfxml")
    print(f"Sucesso! Ontologia populada salva em: {CAMINHO_POPULADO}")

if __name__ == "__main__":
    popular_ontologia()
