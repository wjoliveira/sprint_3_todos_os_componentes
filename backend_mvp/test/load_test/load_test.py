from locust import HttpUser, between, task


class LoadTest(HttpUser):
    """
    Configurando um teste de carga com o Locust
    """
    wait_time = between(1, 3)

    @task
    def add_produto(self):
        """
        Fazendo a inserção de Rotas aleatórias
        """

        # criando a Rota
        rota_backbone = {
            "nome": "ROTA RIO DE JANEIRO - SÃO PAULO",
            "descricao": "Enlace de fibra ótica interligando as cidades do Rio e de São Paulo, seguindo o traçado da Via Dutra",
            "uf_ponta_a": "RJ",
            "cidade_ponta_a": "RIO DE JANEIRO",
            "uf_ponta_b": "SP",
            "cidade_ponta_b": "SÃO PAULO"
        }
        # configurando a requisição
        headers = {'Content-Type': 'multipart/form-data'}
        response = self.client.post('Rota de Backbone', data=rota_backbone, headers=headers)

        # verificando a resposta
        data_response = response.json()
        if response.status_code == 200:
            print("Rota Backbone %s salvo na base" % rota_backbone["nome"])
        elif response.status_code == 409:
            print(data_response["message"] + rota_backbone["nome"])
        else:
            print("Falha na rota de adição de uma Rota de Backbone")


    @task
    def listagem(self):
        """ Fazendo uma listagem dos itens salvos.
        """
        # configurando a requisição
        response = self.client.get("rotas_backbone")

        # verificando a resposta
        data = response.json()
        if response.status_code == 200:
            print("Total de itens salvos: %d" % len(data["rotas_backbone"]))
        else:
            print("Falha na rota /rotas_backbone")

    @task
    def get_rota_backbone(self):
        """ Fazendo uma busca pela rota de backbone de id 1.
        """
        # configurando a requisição
        response = self.client.get("rota_backbone?id=1")

        # verificando a resposta
        data = response.json()
        if response.status_code == 200:
            print("Rota visitado: %s" % data["nome"])
        else:
            print("Falha na rota /rota_backbone?id=1")

    @task
    def busca_rota_backbone(self):
        """ Fazendo uma busca por Rotas de Backbone que tem o termo "SÃO PAULO".
        """
        # configurando a requisição
        response = self.client.get("busca_rota_backbone?termo=SÃO PAULO")

        data = response.json()
        if response.status_code == 200:
            print("Total de Rotas de Backbone: %d" % len(data["Rotas de Backbone"]))
        else:
            print("Falha na rota /busca_rota_backbone")