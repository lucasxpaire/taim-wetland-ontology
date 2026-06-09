import os
from owlready2 import *
from datetime import datetime

# Definindo o caminho para salvar a ontologia
ONTO_FILE = os.path.join(os.path.dirname(__file__), "taim_ontology.owl")

# Criando a Ontologia
onto = get_ontology("http://www.exemplo.org/taim#")

with onto:
    # =======================================================
    # 1. DEFINIÇÃO DAS CLASSES (Exatamente 15 Classes Essenciais)
    # =======================================================

    # --- ANIMAIS ---
    class Animal(Thing): pass
    class Mamifero(Animal): pass
    class Ave(Animal): pass
    class Reptil(Animal): pass
    class Anfibio(Animal): pass

    # --- HABITATS ---
    class Habitat(Thing): pass
    class Banhado(Habitat): pass
    class CorpoDagua(Habitat): pass
    class Vegetacao(Habitat): pass

    # --- INFRAESTRUTURA (RODOVIA) ---
    class Rodovia(Thing): pass
    class TrechoRodovia(Rodovia): pass

    # --- CONDIÇÕES AMBIENTAIS ---
    class CondicaoAmbiental(Thing): pass
    class CondicaoClimatica(CondicaoAmbiental): pass

    # --- EVENTOS ---
    class Evento(Thing): pass
    class EventoAtropelamento(Evento): pass


    # =======================================================
    # 2. PROPRIEDADES DE OBJETO (Mínimo de 10)
    # =======================================================

    class envolveAnimal(ObjectProperty):
        domain    = [EventoAtropelamento]
        range     = [Animal]

    class ocorreEm(ObjectProperty):
        domain    = [EventoAtropelamento]
        range     = [TrechoRodovia]
        # [Relação Espacial]

    class ocorreSob(ObjectProperty):
        domain    = [EventoAtropelamento]
        range     = [CondicaoClimatica]

    class proximoA(ObjectProperty):
        domain    = [TrechoRodovia]
        range     = [Habitat]
        # [Relação Espacial]

    class viveEm(ObjectProperty):
        domain    = [Animal]
        range     = [Habitat]

    class atravessa(ObjectProperty):
        domain    = [Animal]
        range     = [Rodovia]

    class pertenceARodovia(ObjectProperty):
        domain    = [TrechoRodovia]
        range     = [Rodovia]

    class presaDe(ObjectProperty):
        domain    = [Animal]
        range     = [Animal]

    class predadorDe(ObjectProperty):
        domain    = [Animal]
        range     = [Animal]
        inverse_property = presaDe

    class ocorreuAntesDe(ObjectProperty):
        domain    = [EventoAtropelamento]
        range     = [EventoAtropelamento]
        # [Relação Temporal]


    # =======================================================
    # 3. PROPRIEDADES DE DADOS (Mínimo de 10)
    # =======================================================

    class dataHora(DataProperty):
        domain = [EventoAtropelamento]
        range  = [datetime]

    class kmRodovia(DataProperty):
        domain = [TrechoRodovia]
        range  = [float]

    class nomeCientifico(DataProperty):
        domain = [Animal]
        range  = [str]

    class nomeComum(DataProperty):
        domain = [Animal]
        range  = [str]

    class velocidadeVia(DataProperty):
        domain = [Rodovia]
        range  = [int]

    class temperaturaCelsius(DataProperty):
        domain = [CondicaoClimatica]
        range  = [float]

    class nivelAguaMetro(DataProperty):
        domain = [Habitat]
        range  = [float]

    class severidadeAcidente(DataProperty):
        domain = [EventoAtropelamento]
        range  = [str]

    class latitude(DataProperty):
        domain = [TrechoRodovia]
        range  = [float]

    class longitude(DataProperty):
        domain = [TrechoRodovia]
        range  = [float]


print("Ontologia básica (sem opcionais) construída em memória.")

# Salvando a ontologia em formato OWL (padrão RDF/XML aceito pelo Protégé)
onto.save(file=ONTO_FILE, format="rdfxml")
print(f"Ontologia salva com sucesso em: {ONTO_FILE}")
