-----

# 🚀 Projeto: Balanceamento de Carga com NGINX e Docker Compose

Este projeto demonstra a configuração de um sistema de **Load Balancing (Balanceamento de Carga)** usando **NGINX** para distribuir requisições entre múltiplas instâncias de uma aplicação web simples (Backend em Flask), tudo orquestrado via **Docker Compose**.

## ⚙️ Arquitetura do Projeto

A arquitetura utiliza o princípio de Round Robin para distribuir o tráfego de entrada.

  * **Backend (4x):** Quatro instâncias da aplicação em Flask que retornam o nome do container que a atendeu.
  * **Load Balancer (NGINX):** Roda na porta 80 e encaminha as requisições para as instâncias de backend na porta 5000.
  * **Cliente (`client.py`):** Um script Python executado fora dos containers que faz múltiplas requisições ao NGINX para demonstrar a distribuição de carga.

-----

## 💻 Pré-requisitos e Instalação de Dependências

Para rodar este projeto, você precisará dos seguintes softwares instalados e configurados na sua máquina:

### 1\. Docker Desktop (Obrigatório)

O **Docker Desktop** é necessário, pois ele instala o **Docker Engine** (para gerenciar containers) e o **Docker Compose** (para orquestrar múltiplos containers de uma vez).

#### Como Baixar e Instalar o Docker Desktop

1.  **Acesse o Site Oficial:** Visite a página de *Downloads* do Docker.
      * **Link de Download:** [Download Docker Desktop](https://www.docker.com/get-started/)
2.  **Selecione o Sistema Operacional:** Escolha o instalador adequado para sua plataforma (Windows, macOS, ou Linux).

##### 🔹 Para Windows e macOS

  * **Download:** Baixe o arquivo executável (`.exe` para Windows) ou o arquivo de imagem de disco (`.dmg` para macOS).
  * **Instalação:**
      * **Windows:** Execute o instalador e siga as instruções. É crucial que o **Hyper-V** (ou **WSL 2** no Windows 10/11 Home/Pro) esteja ativado e que a virtualização esteja habilitada na BIOS do seu computador.
      * **macOS:** Arraste o ícone do Docker para a pasta **Aplicativos** e clique duas vezes para iniciar.
  * **Primeira Execução:** Aceite o contrato de serviço e aguarde o Docker iniciar completamente. O ícone do Docker na barra de tarefas/menu deve ficar estável.

##### 🔹 Para Linux (Ubuntu/Debian)

  * Geralmente, o Docker Desktop é instalado via pacote `.deb` (no Ubuntu/Debian). Baixe o arquivo e instale via terminal:
    ```bash
    # Exemplo para pacote .deb (substitua pelo nome do arquivo baixado)
    sudo apt-get install ./docker-desktop-<versao>-<arquitetura>.deb
    ```
  * **Verificação:** Abra o terminal e verifique a instalação:
    ```bash
    docker version
    docker-compose version
    ```

### 2\. Python 3 (Local)

Você precisará do Python instalado localmente para executar o script cliente (`client.py`).

### 3\. Biblioteca `requests` do Python (Local)

O script cliente depende da biblioteca `requests` para fazer as requisições HTTP. Instale-a no seu ambiente Python local (fora do Docker):

```bash
pip install requests
```

-----

## 🛠️ Estrutura de Arquivos

Certifique-se de que a sua estrutura de diretórios esteja organizada da seguinte forma:

```
analise_desempenho/
├── app.py              # Aplicação backend em Flask
├── client.py           # Script cliente para testar o LB
├── docker-compose.yml  # Configuração para subir todos os containers
├── Dockerfile          # Instruções para construir a imagem do backend
├── nginx.conf          # Configuração do NGINX Load Balancer
└── requirements.txt    # Dependência do backend (Flask)
```

-----

## ▶️ Como Executar o Projeto

Siga os passos abaixo para construir, iniciar e testar o ambiente de balanceamento de carga.

### Passo 1: Navegar até o Diretório

Abra o seu terminal (ou Prompt de Comando/PowerShell) e navegue até a pasta raiz do projeto (`analise_desempenho`):

```bash
cd /caminho/para/analise_desempenho
```

### Passo 2: Construir e Iniciar o Ambiente Docker

Este comando irá construir a imagem do backend, criar uma rede interna e iniciar todos os cinco containers (4 apps + 1 NGINX) em segundo plano.

```bash
docker-compose up -d --build
```

### Passo 3: Executar o Script Cliente

Com o NGINX rodando e o balanceamento configurado (exposto na porta `80` do seu computador), execute o script cliente Python para enviar 20 requisições e observar a distribuição de carga.

```bash
python client.py
```

#### Saída Esperada:

A saída mostrará as requisições sendo distribuídas sequencialmente (Round Robin) entre os containers `app1`, `app2`, `app3` e `app4`, comprovando o balanceamento:

```
Fazendo 20 requisições para http://localhost/...

Requisição 1: Hello from app1
Requisição 2: Hello from app2
Requisição 3: Hello from app3
Requisição 4: Hello from app4
Requisição 5: Hello from app1
...
```

-----

## 🛑 Limpeza (Remoção dos Containers)

Para derrubar os containers e remover a rede criada pelo Docker Compose, execute:

```bash
docker-compose down
```

-----

Este vídeo do YouTube pode te ajudar a acompanhar o processo de instalação do Docker no Windows 10, caso precise de um guia visual: [Como Instalar o Docker no Windows 10? Passo a passo. 2023](https://www.youtube.com/watch?v=kh1gkqCrNx4).
