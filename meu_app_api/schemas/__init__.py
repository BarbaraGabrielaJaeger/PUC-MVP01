# BARBARA GABRIELA JAEGER
# Sprint: Desenvolvimento Full Stack Básico (40530010058_20240_04)
# Esses esquemas são usados para validar, formatar e estruturar dados que serão manipulados na aplicação, como produtos, comentários e erros.


from schemas.comentario import ComentarioSchema
from schemas.produto import ProdutoSchema, ProdutoBuscaSchema, ProdutoViewSchema, \
                            ListagemProdutosSchema, ProdutoDelSchema, apresenta_produtos, \
                            apresenta_produto, apresenta_produtos
from schemas.error import ErrorSchema
