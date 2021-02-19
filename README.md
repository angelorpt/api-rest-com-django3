# API REST com Django3

## Anotações do Curso

### Ambiente de Desenvolvimento

**Preparando o Ambiente**

```bash
$ python -m venv ./venv
```

**Ativando o ambiente no Windows**
```bash
$ venv\Scripts\activate
```

**Instalando o Django no ambiente ativado**
```bash
$ pip install django
```

**Criando projeto utilizando Django Admin**
```bash
$ django-admin startproject setup .
```
**No arquivo "settings.py" alterar:**
* LANGUAGE_CODE = 'pt-br'
* TIME_ZONE = 'America/Sao_Paulo'

**Rodando o serviço**
```bash
$ python manage.py runserver
```

### Requisição GET

**Criando um app**
```bash
$ python manage.py startapp escola
```
