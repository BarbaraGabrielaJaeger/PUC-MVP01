#####################################################################################################################
# Barbara Gabriela Jaeger - Desenvolvido com base na aula 3 - meu app api
# Colocando comentarios para o entendimento dos comandos
# O código está configurando uma API RESTful usando Flask com suporte ao OpenAPI 3 para documentação automática.
# A aplicação foi configurada para aceitar requisições de origens diferentes (CORS), o que é útil para garantir que a API seja acessada por front-ends hospedados em domínios diferentes.
# O SQLAlchemy está sendo usado para interação com o banco de dados (gerenciamento de modelos como Produto e Comentario).
# Há também a configuração de tratamento de erros (ex: IntegrityError do SQLAlchemy) e a utilização de um logger para monitoramento.
# API gerencia produtos e comentários, com validação de dados e documentação da API automaticamente gerada com base no padrão OpenAPI.
######################################################################################################################

# iOpenAPI: Uma classe que permite a criação de APIs compatíveis com o padrão OpenAPI 3
# O OpenAPI é um padrão para descrever APIs RESTful, usado para documentação e interação com a API.
# Info: Usada para fornecer metadados sobre a API, como título, versão, etc.
# Tag: Usado para agrupar e categorizar endpoints na documentação da API
from flask_openapi3 import OpenAPI, Info, Tag

# redirect: Função do Flask que redireciona o usuário para outra URL. Pode ser útil para manipulação de rotas e fluxos de navegação.
from flask import redirect

#unquote: Função que decodifica uma string codificada em URL, ou seja, converte caracteres percentualmente codificados de volta para seu formato original.
from urllib.parse import unquote

# IntegrityError: Exceção do SQLAlchemy (um ORM para Python) que é levantada quando há um erro de integridade no banco de dados, como uma violação de chave primária ou estrangeira, ou a tentativa de inserir dados inválidos.
from sqlalchemy.exc import IntegrityError

# Session: Provavelmente é uma instância do SQLAlchemy session usada para interagir com o banco de dados (realizar queries, inserir, atualizar ou deletar registros).
# Produto e Comentario: Modelos definidos em outro lugar no código (provavelmente em model.py). Esses são modelos do banco de dados (entidades que representam tabelas no banco) e, possivelmente, mapeiam para a estrutura de dados de produtos e comentários na sua aplicação.
from model import Session, Produto, Comentario

# logger: Importação de um objeto de log personalizado, que é provavelmente utilizado para registrar eventos e mensagens dentro da aplicação. Pode ser configurado para gravar logs em arquivos, enviar para um sistema de monitoramento, etc.
from logger import logger

# schemas: Isso indica que todas as definições de esquemas (provavelmente usando Marshmallow ou similar) são importadas. Schemas são usados para validação e serialização de dados (transformar objetos em JSON e vice-versa).
from schemas import *

#CORS: Importa o CORS (Cross-Origin Resource Sharing) do Flask. CORS permite que a API seja acessada de diferentes origens (domínios), o que é útil quando sua aplicação front-end está em um domínio diferente do back-end.
from flask_cors import CORS

# Info: Cria um objeto Info com metadados sobre a API, como o título e a versão
info = Info(title="Minha API", version="1.0.0")

# OpenAPI: Cria uma instância do aplicativo com suporte a OpenAPI 3, passando os metadados definidos anteriormente (info) e configurando o título e a versão da API.
app = OpenAPI(__name__, info=info)
# CORS(app): Habilita o suporte a CORS no Flask, permitindo que seu back-end Flask aceite requisições de origens diferentes, o que é necessário para que o front-end (que pode estar em um domínio diferente) consiga fazer requisições para sua API.
CORS(app)

# definindo tags - as tags são usadas para organizar e categorizar os endpoints da API de maneira mais estruturada, especialmente para fins de documentação.
# As tags são úteis quando se utiliza um padrão como OpenAPI 3 (anteriormente conhecido como Swagger) para gerar documentação automática da API.
# Agrupar e categorizar seus endpoints de forma lógica - melhora a legibilidade e organização da documentação.
# Onde temos : 
    # name= O nome da tag   
    # description=  Descrição que explica a finalidade da tag, no caso, relacionada à documentação da API, possivelmente abordando diferentes formas de visualizar a documentação (Swagger, Redoc ou RapiDoc).
# O nome da tag, que será exibido na documentação da API.
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
# O nome da tag, que será usada para agrupar endpoints relacionados à gerenciamento de produtos.
produto_tag = Tag(name="Produto", description="Adição, visualização e remoção de produtos à base")
# O nome da tag, que será usada para agrupar endpoints relacionados à adicionar comentários a um produto
comentario_tag = Tag(name="Comentario", description="Adição de um comentário à um produtos cadastrado na base")

# O código que você forneceu define um endpoint da sua aplicação Flask que é acessado via o método GET na raiz (/) da API
# decorador do Flask, utilizado para associar uma função a um endpoint da aplicação. O método HTTP especificado é o GET, o que significa que a função será chamada quando uma requisição GET for feita para o caminho especificado.
# '/' indica que este endpoint é o caminho raiz da aplicação, ou seja, quando alguém acessar o endereço http://<seu_dominio>/, este endpoint será executado
# tag Documentação  
@app.get('/', tags=[home_tag])
# Esta é a função que será executada quando o endpoint / for acessado. 
# Ela é responsável por realizar a ação associada a esse endpoint (no caso, redirecionar para outra URL).
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')
# Redirect: A função redirect do Flask é usada para redirecionar o usuário para uma nova URL.

# tag Produtos = gestão de produtos
# @app.post é um decorador do Flask que mapeia a função abaixo para o método HTTP POST.
# "200": ProdutoViewSchema: Se a requisição for bem-sucedida, o servidor retornará um código 200 OK e um produto criado. 
# "409": ErrorSchema: O código 409 (Conflict) será retornado se houver um conflito na criação do produto. Já existe ou campo único violado, define como a resposta de erro sera estruturada.
# "400": ErrorSchema: O código 400 (Bad Request) será retornado se a requisição for malformada, ou seja, se os dados fornecidos não forem válidos, or exemplo, campos obrigatórios ausentes ou dados no formato errado.
# comando logger ajuda a debugar e aparece no terminal
@app.post('/produto', tags=[produto_tag],
          responses={"200": ProdutoViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_produto(form: ProdutoSchema):
    """Adiciona um novo Produto no cadastro 

    Retorna uma representação dos produtos e seus atributos associados.
    """
    produto = Produto(
        nome=form.nome,
        fornecedor=form.fornecedor,
        categoria=form.categoria,
        quantidade=form.quantidade,
        valor=form.valor)
    logger.debug(f"Incluir produto de nome: '{produto.nome}'")
    try:
        # criando conexão com a base
        session = Session()
        # adicionando produto
        session.add(produto)
        # efetivando o camando de adição de novo item na tabela
         # salva com commit
        session.commit()
        logger.debug(f"Incluído com sucesso o produto de nome: '{produto.nome}'")
        return apresenta_produto(produto), 200

    except IntegrityError as e:
        # como a duplicidade do nome é a provável razão do IntegrityError
        error_msg = "Produto de mesmo nome já exste no cadastro:/"
        logger.warning(f"Erro ao incluir o produto '{produto.nome}', {error_msg}")
        return {"mesage": error_msg}, 409

    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível salvar novo produto :/"
        logger.warning(f"Erro ao tentar incluir o produto '{produto.nome}', {error_msg}")
        return {"mesage": error_msg}, 400
# get_produtos(): É a função que será chamada quando uma requisição GET for feita para /produtos
# assinatura dos metodos , forma de chamar e /produtos e a tag que pertence olhando o swagger
@app.get('/produtos', tags=[produto_tag],
         responses={"200": ListagemProdutosSchema, "404": ErrorSchema})
# define uma função que determina o comportamento do método
def get_produtos():
    """Faz a busca por todos os Produto cadastrados

    Retorna uma representação da listagem de produtos.
    """
    logger.debug(f"Pesquisando produtos ")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    produtos = session.query(Produto).all()

    if not produtos:
        # se não há produtos cadastrados
        return {"produtos": []}, 200
    else:
        logger.debug(f"%d produtos econtrados" % len(produtos))
        # retorna a representação de produto
        print(produtos)
        return apresenta_produtos(produtos), 200
   
    #### novo
    @app.get('/produtos', tags=[produto_tag],
         responses={"200": ListagemProdutosSchema, "404": ErrorSchema})
# define uma função que determina o comportamento do método
def get_produtos():
    """Faz a busca por fornecedor e seus produtos existentes no cadastrado

    Retorna uma representação dos produtos cadastreados para o mesmo fornecedor informado.
    """
    logger.debug(f"Coletando produtos ")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    produtos = session.query(Produto).filter(Produto.fabricante == produto_fabricante).first()
  
      if not produtos:
        # se não há produtos cadastrados
        return {"produtos": []}, 200
    else:
        logger.debug(f"%d produtos econtrados" % len(produtos))
        # retorna a representação de produto
        print(produtos)
        return apresenta_produtos(produtos), 200
    ####

@app.get('/produto', tags=[produto_tag],
         responses={"200": ProdutoViewSchema, "404": ErrorSchema})
def get_produto(query: ProdutoBuscaSchema):
    """Faz a busca por um Produto a partir do id do produto

    Retorna o produto com seus atributos associados.
    """
    produto_nome = query.nome
    logger.debug(f"Buscando dados sobre produto #{produto_nome}")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    produto = session.query(Produto).filter(Produto.nome == produto_nome).first()

    if not produto:
        # se o produto não foi encontrado
        error_msg = "Produto com o nome não encontrado na base :/"
        logger.warning(f"Erro ao buscar produto '{produto_nome}', {error_msg}")
        return {"mesage": error_msg}, 404
    else:
        logger.debug(f"Produto econtrado: '{produto.nome}'")
        # retorna a representação de produto
        return apresenta_produto(produto), 200


@app.delete('/produto', tags=[produto_tag],
            responses={"200": ProdutoDelSchema, "404": ErrorSchema})
def del_produto(query: ProdutoBuscaSchema):
    """Exclui um Produto a partir do nome de produto informado

    Retorna uma mensagem de confirmação de exclusão.
    """
    produto_nome = unquote(unquote(query.nome))
    print(produto_nome)
    logger.debug(f"Excluíndo dados sobre produto #{produto_nome}")
    # criando conexão com a base
    session = Session()
    # fazendo a remoção
    count = session.query(Produto).filter(Produto.nome == produto_nome).delete()
     # salva com commit
    session.commit()

    if count:
        # retorna a representação da mensagem de confirmação
        logger.debug(f"Excluíndo o produto #{produto_nome}")
        return {"mesage": "Produto excluído com sucesso", "id": produto_nome}
    else:
        # se o produto não foi encontrado
        error_msg = "Produto não encontrado no cadastro :/"
        logger.warning(f"Erro ao excluir o produto #'{produto_nome}', {error_msg}")
        return {"mesage": error_msg}, 404


@app.post('/cometario', tags=[comentario_tag],
          responses={"200": ProdutoViewSchema, "404": ErrorSchema})
def add_comentario(form: ComentarioSchema):
    """Inclui um novo comentário à um produtos cadastrado na base identificado pelo id

    Retorna uma representação dos produtos e atributos associados.
    """
    produto_id  = form.produto_id
    logger.debug(f"Adicionando comentários ao produto #{produto_id}")
    # criando conexão com a base
    session = Session()
    # fazendo a busca pelo produto
    produto = session.query(Produto).filter(Produto.id == produto_id).first()

    if not produto:
        # se produto não encontrado
        error_msg = "Produto não encontrado na base :/"
        logger.warning(f"Erro ao adicionar comentário ao produto '{produto_id}', {error_msg}")
        return {"mesage": error_msg}, 404

    # criando o comentário
    texto = form.texto
    comentario = Comentario(texto)

    # adicionando o comentário ao produto
    produto.adiciona_comentario(comentario)
    # salva com commit
    session.commit()

    logger.debug(f"Adicionado comentário ao produto #{produto_id}")

    # retorna a representação de produto
    return apresenta_produto(produto), 200
