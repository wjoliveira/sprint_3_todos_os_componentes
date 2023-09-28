from pydantic import BaseModel
from typing import Optional, List
from models.rota_backbone import RotaBackbone


class RotaBackboneSchema(BaseModel):
    """
    Define como uma nova Rota de Backbone deve ser representada
    """
    nome: str = "ROTA RIO DE JANEIRO - SÃO PAULO"
    descricao: str = "Enlace de fibra ótica interligando as cidades do Rio e de São Paulo, seguindo o traçado da Via Dutra"
    uf_ponta_a: str = "RJ"
    cidade_ponta_a: str = "RIO DE JANEIRO"
    uf_ponta_b: str = "SP"
    cidade_ponta_b: str = "SÃO PAULO"


class RotaBackboneViewSchema(BaseModel):
    """
    Define como uma Rota de Backbone deve ser visualizada
    """
    nome: str = "ROTA RIO DE JANEIRO - SÃO PAULO"
    descricao: str = "Enlace de fibra ótica interligando as cidades do Rio e de São Paulo, seguindo o traçado da Via Dutra"
    uf_ponta_a: str = "RJ"
    cidade_ponta_a: str = "RIO DE JANEIRO"
    uf_ponta_b: str = "SP"
    cidade_ponta_b: str = "SÃO PAULO"


class RotaBackboneBuscaPorNomeSchema(BaseModel):
    """
    Define como deve ser a estrutura que representa a busca, que será realizada com base no nome da Rota.
    """
    termo: str = "SÃO PAULO"


class RotaBackboneBuscaIDSchema(BaseModel):
    """ 
    Define como deve ser a estrutura que representa a busca, que será feita apenas com base no ID da Rota.
    """
    id: int = 1


class ListagemRotasBackboneSchema(BaseModel):
    """
    Define como uma listagem de Rotas será retornada.
    """
    rotas_backbone:List[RotaBackboneViewSchema]


def apresenta_rotas_backbone(rotas_backbone: List[RotaBackbone]):
    """ 
    Retorna uma representação da Rota seguindo o schema definido em ListagemRotasBackboneSchema.
    """
    result = []
    for rota_backbone in rotas_backbone:
        result.append({
            "id": rota_backbone.id,
            "nome": rota_backbone.nome,
            "descricao": rota_backbone.descricao,
            "uf_ponta_a": rota_backbone.uf_ponta_a,
            "cidade_ponta_a": rota_backbone.cidade_ponta_a,
            "uf_ponta_b": rota_backbone.uf_ponta_b,
            "cidade_ponta_b": rota_backbone.cidade_ponta_b
        })

    return {"rotas_backbone": result}
    

class RotaBackboneViewSchema(BaseModel):
    """
    Define como uma Rota será retornada.
    """
    id: int = 1
    nome: str = "ROTA RIO DE JANEIRO - SÃO PAULO"
    descricao: str = "Enlace de fibra ótica interligando as cidades do Rio e de São Paulo, seguindo o traçado da Via Dutra"
    uf_ponta_a: str = "RJ"
    cidade_ponta_a: str = "RIO DE JANEIRO"
    uf_ponta_b: str = "SP"
    cidade_ponta_b: str = "SÃO PAULO"


class RotaBackboneDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição de remoção.
    """
    message: str
    id: int


def apresenta_rota_backbone(rota_backbone: RotaBackbone):
    """ 
    Retorna uma representação da Rota seguindo o schema definido em ListagemRotaBackboneSchema.
    """
    return {
        "id": rota_backbone.id,
        "nome": rota_backbone.nome,
        "descricao": rota_backbone.descricao,
        "uf_ponta_a": rota_backbone.uf_ponta_a,
        "cidade_ponta_a": rota_backbone.cidade_ponta_a,
        "uf_ponta_b": rota_backbone.uf_ponta_b,
        "cidade_ponta_b": rota_backbone.cidade_ponta_b
    }