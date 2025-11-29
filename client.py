import requests
import time

NGINX_URL = "http://localhost"
NUM_REQUESTS = 20

print(f"Fazendo {NUM_REQUESTS} requisições para {NGINX_URL}...\n")

for i in range(1, NUM_REQUESTS + 1):
    try:
        response = requests.get(NGINX_URL)
        if response.status_code == 200:
            print(f"Requisição {i}: {response.text.strip()[0:17]}")
        else:
            print(f"Requisição {i}: Erro - {response.status_code}")
    except requests.exceptions.ConnectionError as e:
        print(f"Requisição {i}: Erro de conexão - {e}")
    time.sleep(0.5)