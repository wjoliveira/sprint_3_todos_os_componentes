# sprint_3_todos_os_componentes

# PUC RIO - DESENVOLVEDOR FULL STACK - MVP SPRINT 3 - COMPONETES FRONTEND E BACKEND

Projeto para avaliação de aprendizado referente a curso de Pós Graduação da PUC RIO

## Como executar esse código

Os 3 componentes solicitados estão neste repositório. Para a utilização é necessário possuir o docker instalado em sua máquina, habilitado para utlizar docker compose.

Após sincronizar o repositório, para subir os containers, utilizar o comando 

```
docker compose up -d
```

Para acessar o frontend, abra o navegador e acesso o endereço http://127.0.0.1:8080

A API externa utilizada é a BrasilApi. Foram utilizadas duas chamadas, que estão no arquivi scripts.js, junto com o frontend

- https://brasilapi.com.br/api/ibge/uf/v1
- https://brasilapi.com.br/api/ibge/municipios/v1/{siglaUF}?providers=dados-abertos-br,gov,wikipedia

Para acessar o backennd, abra o navegador e acesso o endereço http://127.0.0.1:5000

Caso ocorra algum problema com o acesso ao backend, realizar a sequência de comnados abaixo:

Entrar no container do backend:
```
docker exec -it backend_mvp bash
```
Acessar o diretório de trabalho:
```
cd /home/python/app
```
Instalar as dependências do projeto:
```
pip install -r requirements.txt
```
rodar a aplicação do flask
```
flask run --host 0.0.0.0 --port 5000
```
