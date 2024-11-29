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
        # Chama a API com o CEP fornecido
        resposta = requests.get(f"{BASE_URL}{cep}/json", timeout=30)
        resposta.raise_for_status()  # Levanta exceção se o status não for 200
        return resposta.json()
    except requests.RequestException as e:
        print(f"Erro ao obter o endereço: {e}")
        return {}

# Exemplo de uso
print(obter_endereco("14804062"))
