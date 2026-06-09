import requests
from bs4 import BeautifulSoup

URL_TAIM = "https://pt.wikipedia.org/wiki/Banhado_do_Taim"

ESPECIES_ALVO = {
    "Mamifero": ["Capivara", "Tuco-tuco", "Ratão-do-banhado", "Graxaim"],
    "Ave": ["Cisne-de-pescoço-preto", "Flamingo", "Colhereiro", "Maçarico", "Tachã", "Garça-moura"],
    "Reptil": ["Jacaré-de-papo-amarelo", "Tartaruga", "Cobra"],
    "Anfibio": ["Sapo", "Rã"]
}

def obter_html_wikipedia(url: str) -> str:
    # NLP extraction necessita tratar possiveis falhas de rede
    headers = {'User-Agent': 'TrabalhoAcademicoBot/1.0 (lucas@example.com)'}
    resposta = requests.get(url, headers=headers, timeout=10)
    resposta.raise_for_status()
    return resposta.text

def extrair_texto_puro(html: str) -> str:
    sopa = BeautifulSoup(html, "html.parser")
    return sopa.get_text().lower()

def buscar_especies_no_texto(texto_base: str, dicionario_alvo: dict) -> dict:
    especies_encontradas = {}
    
    for classe_animal, nomes_comuns in dicionario_alvo.items():
        animais_validados = []
        for animal in nomes_comuns:
            if animal.lower() in texto_base:
                animais_validados.append(animal)
        
        if animais_validados:
            especies_encontradas[classe_animal] = animais_validados
            
    return especies_encontradas

def obter_animais_confirmados() -> dict:
    html = obter_html_wikipedia(URL_TAIM)
    texto = extrair_texto_puro(html)
    return buscar_especies_no_texto(texto, ESPECIES_ALVO)

if __name__ == "__main__":
    animais = obter_animais_confirmados()
    print("Espécies validadas pela Wikipedia do Taim:")
    print(animais)
