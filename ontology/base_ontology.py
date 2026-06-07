import os
from owlready2 import *
from datetime import datetime

# Definindo o caminho para salvar a ontologia
ONTO_FILE = os.path.join(os.path.dirname(__file__), "taim_ontology.owl")

# Criando a Ontologia
onto = get_ontology("http://www.exemplo.org/taim#")

with onto:
    # =======================================================
    # 1. DEFINIÇÃO DAS CLASSES (Mínimo de 15)
    # =======================================================

    # SUPERCLASSES
    class Animal(Thing): pass
    class Habitat(Thing): pass
    class Infraestrutura(Thing): pass
    class Evento(Thing): pass
    class FatorAmbiental(Thing): pass

    # SUBCLASSES DE ANIMAL
    class Mamifero(Animal): pass
    class Ave(Animal): pass
    class Reptil(Animal): pass
    class Capivara(Mamifero): pass

    # SUBCLASSES DE HABITAT
    class CorpoDagua(Habitat): pass
    class Banhado(Habitat): pass
    class VegetacaoMista(Habitat): pass

    # SUBCLASSES DE INFRAESTRUTURA
    class Rodovia(Infraestrutura): pass
    class TrechoRodovia(Infraestrutura): pass

    # SUBCLASSES DE EVENTO
    class EventoAtropelamento(Evento): pass
    class EventoAvistamento(Evento): pass

    # SUBCLASSES DE FATOR AMBIENTAL
    class CondicaoClimatica(FatorAmbiental): pass
    class ClimaChuvoso(CondicaoClimatica): pass
    class ClimaEnsolarado(CondicaoClimatica): pass

    # =======================================================
    # 2. PROPRIEDADES DE OBJETO (Mínimo de 10)
    # =======================================================

    # Relações do Evento
    class envolveAnimal(ObjectProperty):
        domain    = [Evento]
        range     = [Animal]

    class ocorreEm(ObjectProperty):
        domain    = [Evento]
        range     = [TrechoRodovia]
        # Esta é uma RELAÇÃO ESPACIAL do evento

    class ocorreSob(ObjectProperty):
        domain    = [Evento]
        range     = [FatorAmbiental]
        # Relaciona ao clima e ambiente geral

    # Relações da Infraestrutura
    class proximoA(ObjectProperty):
        domain    = [TrechoRodovia]
        range     = [Habitat]
        # Esta é uma RELAÇÃO ESPACIAL

    class pertenceARodovia(ObjectProperty):
        domain    = [TrechoRodovia]
        range     = [Rodovia]

    # Relações do Animal
    class viveEm(ObjectProperty):
        domain    = [Animal]
        range     = [Habitat]

    class atravessa(ObjectProperty):
        domain    = [Animal]
        range     = [TrechoRodovia]

    class predadorDe(ObjectProperty):
        domain    = [Animal]
        range     = [Animal]

    class presaDe(ObjectProperty):
        domain    = [Animal]
        range     = [Animal]
        inverse_property = predadorDe

    class temCaracteristica(ObjectProperty):
        domain    = [Animal]
        range     = [Thing]

    # =======================================================
    # 3. PROPRIEDADES DE DADOS (Mínimo de 10)
    # =======================================================

    class nomeComum(DataProperty):
        domain = [Animal]
        range  = [str]

    class nomeCientifico(DataProperty):
        domain = [Animal]
        range  = [str]

    class kmRodovia(DataProperty):
        domain = [TrechoRodovia]
        range  = [float]

    class limiteVelocidade(DataProperty):
        domain = [TrechoRodovia]
        range  = [int]

    class dataHoraEvento(DataProperty):
        domain = [Evento]
        range  = [datetime]
        # RELAÇÃO TEMPORAL

    class temperaturaCelsius(DataProperty):
        domain = [CondicaoClimatica]
        range  = [float]

    class nivelAguaMetro(DataProperty):
        domain = [Banhado, CorpoDagua]
        range  = [float]

    class riscoCalculado(DataProperty):
        domain = [TrechoRodovia, Evento]
        range  = [float]

    class severidade(DataProperty):
        domain = [EventoAtropelamento]
        range  = [str]

    class latitude(DataProperty):
        domain = [TrechoRodovia, Evento, Habitat]
        range  = [float]
        # RELAÇÃO ESPACIAL (Coordenadas)

    class longitude(DataProperty):
        domain = [TrechoRodovia, Evento, Habitat]
        range  = [float]
        # RELAÇÃO ESPACIAL (Coordenadas)

    # =======================================================
    # 4. RESTRIÇÕES (EXEMPLOS)
    # =======================================================
    # Podemos definir restrições lógicas, como "Todo atropelamento envolve exatamente UM trecho e pelo menos UM animal"
    EventoAtropelamento.is_a.append(ocorreEm.exactly(1, TrechoRodovia))
    EventoAtropelamento.is_a.append(envolveAnimal.min(1, Animal))

print("Ontologia construida em memoria.")

# Salvando a ontologia em formato OWL (padrão RDF/XML aceito pelo Protégé)
onto.save(file=ONTO_FILE, format="rdfxml")
print(f"Ontologia salva com sucesso em: {ONTO_FILE}")
