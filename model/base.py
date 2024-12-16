# BARBARA GABRIELA JAEGER
# Sprint: Desenvolvimento Full Stack Básico (40530010058_20240_04)
# classe  genérica para gerar e acessar as outras classes

from sqlalchemy.ext.declarative import declarative_base

# cria uma classe Base para o instanciamento de novos objetos/tabelas
Base = declarative_base()
