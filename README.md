# Pratica_TDD_1
 Desafio de Qualidade e Teste de Software em Django

## Biblioteca

A biblioteca é um projeto de cadastro das informações de um livro utilizando o framework Django com intuito de aprendizagem.

### Instalando o Python:
Comece instalando o Python em sua máquina. Você pode fazer o download da versão mais recente do Python no site oficial no site "Download Python" e siga as instruções de instalação fornecidas.

### Instalando o Gerenciador de Pacotes PIP:
O próximo passo é garantir que você tenha o PIP (Python Package Installer) instalado para gerenciar pacotes Python. Para fazer isso, siga as instruções em "Instalando o PIP" no site oficial.

### Como rodar o projeto?

cd Pratica_TDD_1/
virtualenv venv
cd venv
cd scripts
activate.bat
cd ..
cd ..
pip install -r requirements.txt
cd biblioteca/
python manage.py migrate
python manage.py test
coverage run --source='.' manage.py test 
coverage html
python manage.py runserver
