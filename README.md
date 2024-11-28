# movie-api
Projeto de Api de Filmes, servindo como biblioteca.

Está sendo utilizado o Framework Django, escrito em python.


# Dependências

- Python: 3.12.2
- Django: 5.1.1
- djangorestframework
- djangorestframework-simplejwt



1. Instalar dependências:

    pip install -r requirements.txt

2. Gere um ``.env`` local

    python contrib/env_gen.py



# Como usar aplicação
Para utilizar, você pode consumir a API via codigo com resposta JSON, o Postman ou qualquer aplicativo para essa finalidade.

As permissões de usuários para API consumir, pode ser criado no Django-admin grupos e definir as permissões, em seguida vincular o usuário ao grupo para herdar todas as permissões criada. É possivel também realizar a configuração de permissões diretamente no cadastro do usuário (observe os conflitos de permissões do grupo que estiver vinculado)

Foi mantido todas configurações padrão do Django


# Utilizando a padronização de .env para database
Caso queira utilizar o .env para definir as variaveis de ambiente e deixar o projeto profissional e universal para qualquer ambiente de hospedagem

1. Adicione no começo do arquivo settings.py:
```
# para funcionar arquivo secret key e database
from decouple import config, Csv
from dj_database_url import parse as dburl
```

2. Localize e atualize a secretkey e database para o codigo abaixo:
```
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# Database
default_dburl = 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')

DATABASES = {
    'default': config('DATABASE_URL', default=default_dburl, cast=dburl),
}
```

Realizando esses ajustes na settings.py vai ser usado obrigatoriamente as variaveis criada no .env


