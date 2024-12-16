# BARBARA GABRIELA JAEGER
# Sprint: Desenvolvimento Full Stack Básico (40530010058_20240_04)
#  O código define um esquema para um comentário usando o Pydantic, 
# uma biblioteca de validação de dados para Python. A classe ComentarioSchema herda 
# de BaseModel do Pydantic, o que permite que ela seja usada para validar e 
# estruturar os dados de um comentário from pydantic import BaseModel
# Portanto, a classe ComentarioSchema define os campos esperados para um comentário, com valores padrão para produto_id e texto. Quando um novo comentário for criado, esses dados
# podem ser validados para garantir que correspondam ao tipo e formato esperado.


class ComentarioSchema(BaseModel):
    """ Define como um novo comentário a ser inserido deve ser representado"""
    produto_id: int = 1
    texto: str = "Só comprar se o preço realmente estiver bom!"
