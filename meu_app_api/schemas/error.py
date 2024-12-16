# BARBARA GABRIELA JAEGER
# Sprint: Desenvolvimento Full Stack Básico (40530010058_20240_04)
# O código define um esquema para representar uma mensagem de erro usando Pydantic.
# Portanto, a classe ErrorSchema é usada para estruturar e representar mensagens de erro, com um valor padrão para o campo mesage. Isso pode ser útil para uniformizar c
# omo os erros são retornados ou exibidos em uma aplicação.


from pydantic import BaseModel
class ErrorSchema(BaseModel):
    """ Define como uma mensagem de eero será representada
    """
    mesage: str = "Erro de Esquema"
