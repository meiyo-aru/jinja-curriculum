import requests
from api import *

async def get_data_external_api(url_api):
    try:
        response_api = requests.get(url_api, timeout=5) # add timeout
        response_api.raise_for_status() # throw exception for status HTTP 4xx/5xx

        dados = response_api.json()
        return dados

    except requests.exceptions.Timeout:
        print("Erro: A requisição para a API externa excedeu o tempo limite.")
        return Response(
            content="<p>O serviço externo demorou muito para responder.</p>",
            media_type="text/html",
            status_code=status.HTTP_504_GATEWAY_TIMEOUT # Gateway Timeout
        )
    except requests.exceptions.RequestException as e:
        # catch connection errors, HTTP (4xx/5xx) or  others requisition problems
        print(f"Erro de requisição para a API externa: {e}")
        return Response(
            content=f"<p>Não foi possível obter dados do serviço externo: {e}</p>",
            media_type="text/html",
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
    except ValueError: # Error decoding JSON (response is not valid JSON)
        print("Erro: A resposta da API externa não é um JSON válido.")
        return Response(
            content="<p>A resposta do serviço externo não pôde ser processada.</p>",
            media_type="text/html",
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
    except Exception as e:
        # Catch any other unexpected exception
        print(f"Ocorreu um erro inesperado: {e}")
        return Response(
            content="<p>Ocorreu um erro inesperado ao buscar dados.</p>",
            media_type="text/html",
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
