# Minha API - BARBARA GABRIELA JAEGER 13/12/2024

Este pequeno projeto faz parte do material diático da Disciplina **Desenvolvimento Full Stack Básico - Sprint 01 - base aula 03** 

Professores: Marisa e Angelo

Aluna: Barbara Gabriela Jaeger
## Sprint: Desenvolvimento Full Stack Básico (40530010058_20240_04)

## REQUISITOS: 
    ## FIXAR AS TECNOLOGIAS COM O QUE FOI DADO EM AULA
    ## CRIAR UM API
    ## INSERIR DADOS, RECUPERAR DADOS E CONSULTAR DADOS
    ## BACK END  EM PYTHON
    ## FRONT END EM HTML
    ## INTERFACES - FRONT END + CONTRATO DE COMUNICAÇÃO (END POINT) +
    ## EXEMPLO CADASTRAR USUARIO COM O QUE APARECE NA TELA  E DOS MÉTODOS
    ## BACK END E FRONT END PRECISA ESTAR ADEQUADA
    ## API E SWAGGER E DOCUMENTAR IGUAL A AULA 3 
    ## DOCUMENTAÇÃO DE VENDA ATÉ PARA O API
    ## MODEL INTERMEDIARIO QUE VAI MAPEAR OS OBJETOS PARA O BANCO DE DADOS

Códigos das disciplinas da especialização online **Pós-Graduação em Desenvolvimento Full Stack**, do Departamento de Informática da PUC-Rio.

Coordenação: **Prof. Marcos Kalinowski** (*kalinowski@inf.puc-rio.br*)
Professores: Marisa e Angelo

Aluna: Barbara Gabriela Jaeger
## Sprint: Desenvolvimento Full Stack Básico (40530010058_20240_04)


# LINUX https://learn.microsoft.com/en-us/windows/wsl/install
---
## Como executar 
Será necessário ter todas as libs python listadas no `requirements.txt` instaladas.
Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo.

> É fortemente indicado o uso de ambientes virtuais do tipo [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

```
(env)$ pip install -r requirements.txt
```

Este comando instala as dependências/bibliotecas, descritas no arquivo `requirements.txt`.

Para executar a API  basta executar:

```
(env)$ flask run --host 0.0.0.0 --port 5000
```

Em modo de desenvolvimento é recomendado executar utilizando o parâmetro reload, que reiniciará o servidor
automaticamente após uma mudança no código fonte. 
```
(env)$ flask run --host 0.0.0.0 --port 5000 --reload
para parar Press CTRL+c
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 nome_do_seu_arquivo:app
```

Abra o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador para verificar o status da API em execução.
--
 Running on http://172.29.155.70:5000/ (Press CTRL+C to quit)
---
## Registro dos meus comandos basicos
1) Preferir o terminal do linux , comando: wsl
   Vantagem: Criar o ambiente terminal, e não na maquina local
   https://learn.microsoft.com/en-us/windows/wsl/install

2) Instalar python
sudo apt update
sudo apt install python3

-- ver a versão
python3 --version
bash ->   3.11.9
 wsl ->   3.12.3

2)Criar no python e ativar o ambiente virtual
python -m venv nome-do-ambiente
python -m venv venv_api
python3.12 -m venv venv_api

##comandos individuais
    python3 -m venv venv_api
    source venv_api/bin/active
    upgrade no python
    python -m ensurepip --upgrade

3) Ative o ambiente
Windows: nome-do-ambiente\Scripts\activate
Linux/macOS:source nome-do-ambiente/bin/activate
source venv_api/bin/activate

aparece na frente do prompt:
(venv_api) root@DESKTOP-9IJ8T5U:/mnt/c/Users/User/Downloads/MVP-BARBARAJAEGER/MVP-BARBARAJAEGER/meu_app_api# 
apt install python3.12-venv


4) verificar a instalação
pip show Flask-Cors
pip install Flask-Cors
----------
pip install -U flask-cors
---------
pip install flask-openapi3==2.1.0
pip install flask-openapi3==2.1.0
pip install flask_openapi3-2.1.0-py3-none-any
5) garantir a instalação dos requirements.txt
pip3 install -r requirements.txt

---- no meu caso precisei alterar
 
Dica do professor dando erro na instalação apagar as versoes do requiremnt
Flask==2.1.3
Flask-Cors==3.0.10
flask-openapi3==2.1.0
Flask-SQLAlchemy==2.5.1
nose2==0.12.0
pydantic==1.10.2
SQLAlchemy==1.4.41
SQLAlchemy-Utils==0.38.3
typing_extensions==4.3.0
werkzeug==2.0.3


