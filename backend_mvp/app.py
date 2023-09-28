from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError

#from models import Session, RotaBackbone, TrechoRota
from models import Session, RotaBackbone
from logger import logger
from schemas import *
from flask_cors import CORS

info = Info(title="Backbone API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# definindo tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
rota_backbone_tag = Tag(name="RotaBackbone", description="Adição, visualização e remoção de Rotas de Backbone à base")
#trecho_rota_tag = Tag(name="TrechoRota", description="Adição de um trecho à uma rota cadastrado na base")


@app.get("/", tags=[home_tag])
def home():
    """ Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')


@app.post('/rota_backbone', tags=[rota_backbone_tag],
    responses={"200": RotaBackboneViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_rota_backbone(form: RotaBackboneSchema):
    """ Adiciona uma nova Rota de Backbone à base de dados
    Retorna uma representação das Rotas de Backbone e Trechos associados.
    """
    print(form)
    rota_backbone = RotaBackbone(
        nome=form.nome,
        descricao=form.descricao,
        uf_ponta_a=form.uf_ponta_a,
        cidade_ponta_a=form.cidade_ponta_a,
        uf_ponta_b=form.uf_ponta_b,
        cidade_ponta_b=form.cidade_ponta_b
    )
    logger.info(f"Adicionando Rota de Backbone de nome: '{rota_backbone.nome}'")
    try:
        # criando conexão com a base
        session = Session()
        # adiciona rota de backbone
        session.add(rota_backbone)
        # efetivando o chamado de adição de novo item na tabela
        session.commit()
        logger.info("Adicionando Rota de Backbone: %s" % rota_backbone)
        return apresenta_rota_backbone(rota_backbone), 200
    
    except IntegrityError as e:
        # como a duplicidade do nome é a provável razão do Integrity Error
        error_msg = "Rota de Backbone de mesmo nome e marca já salvo na base :/"
        logger.warning(f"Erro ao adicionar Rota de Backbone '{rota_backbone.nome}', {error_msg}")
        return {"message": error_msg}, 409
    
    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível salvar novo item :/"
        logger.warning(f"Erro ao adicionar Rota de Backbone '{rota_backbone.nome}', {error_msg}")
        return {"message": error_msg}, 400
    

@app.get('/rotas_backbone', tags=[rota_backbone_tag],
    responses={"200": ListagemRotasBackboneSchema, "404": ErrorSchema})
def get_rotas_backbone():
    """ Faz a busca por todos as Rotas de Backbone cadastradas
    Retorna uma representação da listagem de Rotas.
    """
    logger.info(f"Coletando Rotas de Backbone")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    rotas_backbone = session.query(RotaBackbone).all()

    if not rotas_backbone:
        # se não há Rotas de Backbone cadastradas
        return {"rotas_backbone": []}, 200
    else:
        logger.info(f"%d Rotas de Backbone encontradas" % len(rotas_backbone))
        # retorna a representação de produtos
        return apresenta_rotas_backbone(rotas_backbone), 200


@app.get('/rota_backbone', tags=[rota_backbone_tag],
    responses={"200": RotaBackboneViewSchema, "404": ErrorSchema})
def get_rota_backbone(query: RotaBackboneBuscaIDSchema):
    """ Faz a busca por uma Rota de Backbone a partir do id da rota
    Retorna uma representação das Rotas e Trechos associados.
    """
    rota_backbone_id = query.id
    logger.info(f"Coletando dados sobre a Rota de Backbone #{rota_backbone_id}")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    rota_backbone = session.query(RotaBackbone).filter(RotaBackbone.id == rota_backbone_id).first()

    if not rota_backbone:
        # se a Rota não foi encontrada
        error_msg = "Rota de Backbone não encontrada na base :/"
        logger.warning(f"Erro ao buscar Rota de Backbone '{rota_backbone_id}', {error_msg}")
        return {"message": error_msg}, 404
    else:
        logger.info("Rota de Backbone encontrada: %s" % rota_backbone)
        # retorna a representação da Rota de Backbone
        return apresenta_rota_backbone(rota_backbone), 200
    

@app.delete('/rota_backbone', tags=[rota_backbone_tag],
    responses={"200": RotaBackboneDelSchema, "404": ErrorSchema})
def del_rota_backbone(query: RotaBackboneBuscaIDSchema):
    """ Delete uma Rota de Backbone a partir do id informado
    Retona uma mensagem de confirmação da remoção
    """
    #produto_nome = unquote(unquote(query.nome))
    #logger.info(f"Deletendo dados sobre produto #{produto_nome}")
    ## criando conexão com a base
    #session = Session()
    ## fazendo a remoção
    #count = session.query(Produto).filter(Produto.nome == produto_nome).delete()
    #session.commit()
    rota_backbone_id = query.id
    logger.info(f"Deletendo dados sobre a Rota de Backbone #{rota_backbone_id}")
    # criando conexão com a base
    session = Session()
    # fazendo a remoção
    count = session.query(RotaBackbone).filter(RotaBackbone.id == rota_backbone_id).delete()
    session.commit()

    if count:
        # retorna a representação da mensagem de confirmação
        logger.info(f"Deletendo Rota de Backbone #{rota_backbone_id}")
        return {"message": "Rota de Backbone removida", "id": rota_backbone_id}
    else:
        # se a Rota de Backbone não foi encontrado
        error_msg = "Rota de Backbone não encontrada na base :/"
        logger.warning(f"Erro ao deletar Rota de Backbone #'{rota_backbone_id}', {error_msg}")
        return {"message": error_msg}, 404
    

@app.get('/busca_rota_backbone', tags=[rota_backbone_tag],
    responses={"200": ListagemRotasBackboneSchema, "404": ErrorSchema})
def busca_rota_backbone(query: RotaBackboneBuscaPorNomeSchema):
    """Faz a busca por Rotas de Backbone em que o termo é passado.
    Retorna uma representação dos produtos e comentários associados.
    """
    termo = unquote(query.termo)
    logger.info(f"Fazendo a busca por nome com o termo: {termo}")
    # criando conexão com a base
    session = Session()
    # fazemos a pesquisa
    rotas_backbone = session.query(RotaBackbone).filter(RotaBackbone.nome.ilike(f"%{termo}%")).all()

    if not rotas_backbone:
        # se não há Rotas de BAckbone cadastradas
        return {"rotas_backbone": []}, 200
    else:
        logger.info(f"%d Rotas de Backbone encontradas" % len(rotas_backbone))
        # retorna a representação de Rotas de Backbone
        return apresenta_rotas_backbone(rotas_backbone), 200
    

@app.put('/rota_backbone', tags=[rota_backbone_tag],
         responses={"200": RotaBackboneViewSchema, "404": ErrorSchema})
def update_rota_backbone(form: RotaBackboneViewSchema):
    """
    Atualiza as informações de uma Rota de Backbone
    """
    rota_backbone_id = form.id

    logger.debug(f"Atualizando Rota de Backbone de ID: '{form.id}'")
    try:
        session = Session()
        atualiza_rota = session.query(RotaBackbone).filter(RotaBackbone.id == rota_backbone_id).first()

        if not atualiza_rota:
            error_msg = "Rota não encontrada no banco de dados :/"
            return {"Message": error_msg}, 404
        else:

            if form.nome:
                atualiza_rota.nome = form.nome

            if form.descricao:
                atualiza_rota.descricao = form.descricao

            if form.uf_ponta_a:
                atualiza_rota.uf_ponta_a = form.uf_ponta_a

            if form.uf_ponta_b:
                atualiza_rota.uf_ponta_b = form.uf_ponta_b

            if form.cidade_ponta_a:
                atualiza_rota.cidade_ponta_a

            if form.cidade_ponta_b:
                atualiza_rota.cidade_ponta_b

            session.add(atualiza_rota)

            session.commit()
            logger.debug(f"Atualizando a Rota de BAckbone ID: '{form.id}'")
            return apresenta_rota_backbone(atualiza_rota), 200

    except IntegrityError as e:
        error_msg = f"Erro ao atualizar a Rota de Backbone ID '{form.id}', código de erro: '{e}'"
        logger.warning(error_msg)
        return {"Message": error_msg}, 409
    
    except Exception as e:
        error_msg = f"Erro ao atualizar a Rota de Backbone ID '{form.id}', código de erro: '{e}'"
        logger.warning(error_msg)
        return {"Message": error_msg}, 409
    
    