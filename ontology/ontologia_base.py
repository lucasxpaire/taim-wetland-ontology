import os
from datetime import datetime
from owlready2 import get_ontology, Thing, ObjectProperty, DataProperty

ARQUIVO_ONTO = os.path.join(os.path.dirname(__file__), "ontologia_base.owl")

onto = get_ontology("http://www.exemplo.org/taim#")

with onto:
    # --- CLASSES E SUBCLASSES ---
    class Animal(Thing): pass
    class Mamifero(Animal): pass
    class Ave(Animal): pass
    class Reptil(Animal): pass
    class Anfibio(Animal): pass

    class Habitat(Thing): pass
    class Banhado(Habitat): pass
    class CorpoDagua(Habitat): pass
    class Vegetacao(Habitat): pass

    class Rodovia(Thing): pass
    class TrechoRodovia(Rodovia): pass

    class CondicaoAmbiental(Thing): pass
    class CondicaoClimatica(CondicaoAmbiental): pass

    class Evento(Thing): pass
    class EventoAtropelamento(Evento): pass

    # --- PROPRIEDADES DE OBJETO (Relações) ---
    class envolveAnimal(ObjectProperty):
        domain = [EventoAtropelamento]
        range = [Animal]

    class ocorreEm(ObjectProperty):
        domain = [EventoAtropelamento]
        range = [TrechoRodovia]

    class ocorreSob(ObjectProperty):
        domain = [EventoAtropelamento]
        range = [CondicaoClimatica]

    class proximoA(ObjectProperty):
        domain = [TrechoRodovia]
        range = [Habitat]

    class viveEm(ObjectProperty):
        domain = [Animal]
        range = [Habitat]

    class atravessa(ObjectProperty):
        domain = [Animal]
        range = [Rodovia]

    class pertenceARodovia(ObjectProperty):
        domain = [TrechoRodovia]
        range = [Rodovia]

    class presaDe(ObjectProperty):
        domain = [Animal]
        range = [Animal]

    class predadorDe(ObjectProperty):
        domain = [Animal]
        range = [Animal]
        inverse_property = presaDe

    class ocorreuAntesDe(ObjectProperty):
        domain = [EventoAtropelamento]
        range = [EventoAtropelamento]

    # --- PROPRIEDADES DE DADOS (Atributos) ---
    class dataHora(DataProperty):
        domain = [EventoAtropelamento]
        range = [datetime]

    class kmRodovia(DataProperty):
        domain = [TrechoRodovia]
        range = [float]

    class nomeCientifico(DataProperty):
        domain = [Animal]
        range = [str]

    class nomeComum(DataProperty):
        domain = [Animal]
        range = [str]

    class velocidadeVia(DataProperty):
        domain = [Rodovia]
        range = [int]

    class temperaturaCelsius(DataProperty):
        domain = [CondicaoClimatica]
        range = [float]

    class nivelAguaMetro(DataProperty):
        domain = [Habitat]
        range = [float]

    class severidadeAcidente(DataProperty):
        domain = [EventoAtropelamento]
        range = [str]

    class latitude(DataProperty):
        domain = [TrechoRodovia]
        range = [float]

    class longitude(DataProperty):
        domain = [TrechoRodovia]
        range = [float]

onto.save(file=ARQUIVO_ONTO, format="rdfxml")
