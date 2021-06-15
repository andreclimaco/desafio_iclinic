###########################
iClinic Teste SRE Arquiteto
###########################
 

Problema
########

`Acesse aqui a descrição do problema. <link https://gist.github.com/rbouchabki/1c1e9826cbb6282c7ffd77703183f8f3>`__


Solução
#######

Ferramentas utilizadas:

- `Django REST framework`__
- `PostgreSQL <link https://www.postgresql.org/docs/>`__
- `RabbitMQ <link https://www.rabbitmq.com/documentation.html>`__
- `Celery <link https://docs.celeryproject.org/en/stable/>`__
- `Flower <link https://flower.readthedocs.io/en/latest/>`__
- `Redis <link https://redis.io/documentation>`__
- `Docker <link https://docs.docker.com/>`__
- `Docker Compose <link https://docs.docker.com/compose/>`__

__ https://www.django-rest-framework.org


.. image:: docs/desafio_iclinic.png
  :alt: Proposta de solução

=================
**Inicializando**
=================

Pré-requisitos
--------------
- `Git <link https://git-scm.com/book/en/v2/Getting-Started-Installing-Git>`__
- `Docker compose <link https://docs.docker.com/compose/install/>`__

Clone repositório
-----------------

::

$ git clone git@github.com:andreclimaco/desafio_iclinic.git


Acesse o diretório
------------------

::

$ cd desafio_iclinic/


Execute o Docker Compose
------------------------

::

$ docker-compose build
$ docker-compose up -d

==========
**Testes**
==========

API de consultas
----------------

::

$ docker-compose run --rm appointment-api python manage.py test -v 2

API de cobranças
----------------

::

$ docker-compose run --rm charge-api python manage.py test -v 2


=======================================
**Acessando a Administração do Django**
=======================================

.. image:: docs/screenshot/django-admin-login.png
  :alt: Login Django Admin

Pré-requisitos
--------------

Crie um super usuário
^^^^^^^^^^^^^^^^^^^^^

::

$ docker-compose run --rm appointment-api python manage.py createsuperuser

ou

::

$ docker-compose run --rm charge-api python manage.py createsuperuser

Acesse
^^^^^^
- http://localhost:9000/admin/

.. image:: docs/screenshot/django-admin.png
  :alt: Django Admin