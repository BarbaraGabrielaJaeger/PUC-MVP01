# BARBARA GABRIELA JAEGER
# Sprint: Desenvolvimento Full Stack Básico (40530010058_20240_04)

# O código prepara a base para criar e manipular dados relacionados a produtos e 
# comentários, usando Pydantic para validação, e também utiliza tipos opcionais e listas,
# que são frequentemente úteis para definir campos que podem conter múltiplos valores 
# ou ser ausentes.
from pydantic import BaseModel
from typing import Optional, List
from model.produto import Produto
from schemas import ComentarioSchema

# O código define um esquema para representar um produto utilizando o Pydantic.
# A classe ProdutoSchema define os dados essenciais para um produto, 
# com campos para nome, quantidade (opcional) e valor. Esses dados são estruturados e validados automaticamente 
# usando o Pydantic, com valores padrão fornecidos para cada campo
class ProdutoSchema(BaseModel):
    """ Define como um novo produto a ser inserido deve ser representado"""
    nome: str = "Cebola roxa"
    quantidade: Optional[int] = 12
    valor: float = 12.50

# A classe ProdutoBuscaSchema estrutura a busca de um produto, 
# esperando um nome como critério de pesquisa. O campo nome tem um valor 
# padrão que pode ser utilizado para indicar ao usuário que ele deve informar um produto.
class ProdutoBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no nome do produto.
    """
    nome: str = "Informe o produto"

#A classe ListagemProdutosSchema define a estrutura para retornar 
# uma lista de produtos, onde cada produto é validado conforme o esquema ProdutoSchema.
# A lista de produtos é armazenada no atributo produtos
class ListagemProdutosSchema(BaseModel):
    """ Define como uma listagem de produtos será retornada.
    """
    produtos:List[ProdutoSchema]

# A função apresenta_produtos pega uma lista de produtos e a converte 
# para um formato específico, incluindo apenas os campos nome, quantidade e valor de cada produto, 
# retornando essa lista como parte de um dicionário.
def apresenta_produtos(produtos: List[Produto]):
    """ Retorna uma representação do produto seguindo o schema definido em
        ProdutoViewSchema.
    """
    result = []
    for produto in produtos:
        result.append({
            "nome": produto.nome,
            "quantidade": produto.quantidade,
            "valor": produto.valor,
        })

    return {"produtos": result}

# A classe ProdutoViewSchema define a estrutura para retornar os dados
# de um produto, incluindo informações sobre o produto e seus comentários.
# Ela combina dados como id, nome, quantidade, valor, total_comentarios e uma lista de comentários (comentarios).
class ProdutoViewSchema(BaseModel):
    """ Define como um produto será retornado: produto + comentários.
    """
    id: int = 1
    nome: str = "Banana Prata"
    quantidade: Optional[int] = 12
    valor: float = 12.50
    total_cometarios: int = 1
    comentarios:List[ComentarioSchema]

# A classe ProdutoDelSchema define como será a resposta após a remoção de um produto, 
# incluindo uma mensagem de sucesso e o nome do produto excluído.
class ProdutoDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mesage: str = "Efetuado com sucesso."
    nome: str =  "Produto excluido."
# A função apresenta_produto cria e retorna um dicionário com os dados do produto, incluindo seu ID, nome, quantidade, valor, 
# total de comentários e uma lista de textos dos comentários associados.
def apresenta_produto(produto: Produto):
    """ Retorna uma representação do produto seguindo o schema definido em
        ProdutoViewSchema.
    """
    return {
        "id": produto.id,
        "nome": produto.nome,
        "quantidade": produto.quantidade,
        "valor": produto.valor,
        "total_cometarios": len(produto.comentarios),
        "comentarios": [{"texto": c.texto} for c in produto.comentarios]
    }
