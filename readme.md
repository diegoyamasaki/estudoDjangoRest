## Aplicação de estudo de Django Rest Framework

# Instalação no heroku

- Projeto tem que estar num repositorio
- pip install python-decouple
- criar arquivo .env
- adicionar variavel SECRET_KEY
- adicionar variavel DEBUG
- instalar pip install dj-database-url

criar app no heroku
heroku apps:create pontos-turisticos-diego

url: https://pontos-turisticos-diego.herokuapp.com/
git  https://git.heroku.com/pontos-turisticos-diego.git

adiciona no setting a url no allowed hosts

instalar plugin
heroku plugins:install heroku-config

subir as configs para o app
heroku config:push --app pontos-turisticos-diego