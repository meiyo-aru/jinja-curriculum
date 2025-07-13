import time
import httpx
from api import *

async def get_data_external_api(url_api):
    try:
        start = time.time()
        async with httpx.AsyncClient() as client:
            response = await client.get(url_api, timeout = 5)
            response.raise_for_status()

        end = time.time()
        print("tempo external_api = " + str(end - start))
        dados = response.json()
        return dados
    
    # handle exceptions
    except httpx.TimeoutException:
        print("Erro: A requisição para a API externa excedeu o tempo limite.")
        return Response(
            content="<p>O serviço externo demorou muito para responder.</p>",
            media_type="text/html",
            status_code=status.HTTP_504_GATEWAY_TIMEOUT # Gateway Timeout
        )
    except httpx.RequestError as e:
        # handle network error, connection, DNS, etc.
        print(f"Erro de requisição para a API externa: {e}")
        return Response(
            content=f"<p>Não foi possível obter dados do serviço externo: {e}</p>",
            media_type="text/html",
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
    except httpx.HTTPStatusError as e:
        print(f"Erro de status HTTP da API externa: {e.response.status_code} - {e.response.text}")
        return Response(
            content=f"<p>Erro na resposta do serviço externo: {e.response.status_code}</p>",
            media_type="text/html",
            status_code=e.response.status_code # return error status of external api
        )
    except ValueError: # Error decoding JSON (response is not valid JSON)
        print("Erro: A resposta da API externa não é um JSON válido.")
        return Response(
            content="<p>A resposta do serviço externo não pôde ser processada.</p>",
            media_type="text/html",
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
    except Exception as e: # Catch any other unexpected exception
        print(f"Ocorreu um erro inesperado: {e}")
        return Response(
            content="<p>Ocorreu um erro inesperado ao buscar dados.</p>",
            media_type="text/html",
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
