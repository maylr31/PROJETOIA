import requests

BASE_URL = "https://viacep.com.br/ws/"

def obter_endereco(cep: str) -> dict:
    """
    Faz uma requisição à API do ViaCEP para obter informações de endereço
    com base no CEP fornecido.
    
    Args:
        cep (str): O CEP para o qual deseja buscar o endereço.
    
    Returns:
        dict: Um dicionário contendo as informações do endereço, ou um
        dicionário vazio se a requisição falhar.
    """
    try:
        resposta = requests.get(f"{BASE_URL}{cep}/json", timeout=30)
        resposta.raise_for_status()
        return resposta.json()
    except requests.RequestException as e:
        print(f"Erro ao obter o endereço: {e}")
        return {}

# Entrada dinâmica
if __name__ == "__main__":
    cep = input("Digite o CEP: ").strip()
    endereco = obter_endereco(cep)
    print(endereco)
