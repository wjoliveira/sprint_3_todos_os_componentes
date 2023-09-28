from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import  Union

from models import Base


class RotaBackbone(Base):
    __tablename__ = 'tbl_rota_backbone'
    id = Column("pk_rota_backbone", Integer, primary_key=True)
    nome = Column(String(255))
    descricao = Column(String(4000))
    uf_ponta_a = Column(String(2))
    cidade_ponta_a = Column(String(100))
    uf_ponta_b = Column(String(2))
    cidade_ponta_b = Column(String(100))
    data_cadastro = Column(DateTime, default=datetime.now())

    def __init__(self, nome, descricao, uf_ponta_a, cidade_ponta_a, 
                 uf_ponta_b, cidade_ponta_b, data_cadastro: Union[DateTime, None] = None):
        """
        Cria uma nova Rota de Backbone

        Argumentos:
            nome: Nome da rota de backbone. Ex.: ROTA RIO DE JANEIRO - SÃO PAULO
            descricao: Descrição com detalhes e explicações sobre a Rota
            uf_ponta_a: UF da cidade que marca o início da Rota. Ex.: RJ
            cidade_ponta_a: Nome da cidade que marca o início da Rota. Ex.: RIO DE JANEIRO
            uf_ponta_b: UF da cidade que marca o final da Rota. Ex.: SP
            cidade_ponta_b: Nome da cidade que marca o final da Rota. Ex.: SÃO PAULO
            data_cadastro: Data em qua a Rota foi inserida na base de dados
        """
        self.nome = nome
        self.descricao = descricao
        self.uf_ponta_a = uf_ponta_a
        self.cidade_ponta_a = cidade_ponta_a
        self.uf_ponta_b = uf_ponta_b
        self.cidade_ponta_b = cidade_ponta_b

        if data_cadastro:
            self.data_cadastro = data_cadastro

    def to_dict(self):
        """
        Retorna um dicionário com a representação do objeto da Rota de Backbone
        """
        return {
            "id": self.id,
            "nome": self.nome,
            "descricao": self.descricao,
            "uf_ponta_a": self.uf_ponta_a,
            "cidade_ponta_a": self.cidade_ponta_a,
            "uf_ponta_b": self.uf_ponta_b,
            "cidade_ponta_b": self.cidade_ponta_b,
            "data_cadastro": self.data_cadastro
        }
    
    def __repr__(self):
        """
        Retorna uma representação da Rota de Backbone em forma de texto
        """
        return f"RotaBackbone(id={self.id}, nome='{self.nome}', descricao='{self.descricao}', uf_ponta_a='{self.uf_ponta_a}', cidade_ponta_a='{self.cidade_ponta_a}', uf_ponta_b='{self.uf_ponta_b}', cidade_ponta_b='{self.cidade_ponta_b}')"
    