############
Consulta API
############

API de consultas.

**********
Instruções
**********

Executar testes
===============

:: 

$ python manage.py test -v 2

Iniciar
========

:: 

$ python manage.py runserver 0.0.0.0:8000


Administração
===============

Para acessar a adminstração é necessário a criação de um usuário.

Criar super usuário
^^^^^^^^^^^^^^^^^^^

:: 

$ python manage.py createsuperuser


Acessar a Administração
^^^^^^^^^^^^^^^^^^^^^^^

http://localhost:8000/admin


Endpoints
=========

A api  disponibiliza dois endpoints:


/api/v1/appointments/
^^^^^^^^^^^^^^^^^^^^^

GET
"""

:: 

$ curl -X GET http://localhost:8000/api/v1/appointments/


POST
""""

:: 

$ curl -d '{"patient":"01fcc220-49ee-4b9c-8a9a-0d5ea9a4293f", "physician":"d4feda94-cf49-4580-abe9-21fb02a9d5db", "price": "200.00"}' -H "Content-Type: application/json" -X POST http://localhost:8000/api/v1/appointments/

Resultado

.. code-block:: JSON

  {
    "id": "ab2ec149-ba5d-4ccd-9945-16d3255dd3ae",
    "start_date": "2021-06-14T15:03:16.822947-03:00",
    "end_date": null,
    "price": "200.00",
    "patient": "01fcc220-49ee-4b9c-8a9a-0d5ea9a4293f",
    "physician": "d4feda94-cf49-4580-abe9-21fb02a9d5db"
  }


PUT
"""

::

$ curl -d '{"id":"ab2ec149-ba5d-4ccd-9945-16d3255dd3ae","start_date":"2021-06-14T15:03:16.822947-03:00","end_date":null,"price":"150.00","patient":"01fcc220-49ee-4b9c-8a9a-0d5ea9a4293f","physician":"d4feda94-cf49-4580-abe9-21fb02a9d5db"}' -H "Content-Type: application/json" -X PUT http://localhost:8000/api/v1/appointments/ab2ec149-ba5d-4ccd-9945-16d3255dd3ae/

Resultado

.. code-block:: JSON

  {
    "id": "ab2ec149-ba5d-4ccd-9945-16d3255dd3ae",
    "start_date": "2021-06-14T15:03:16.822947-03:00",
    "end_date": null,
    "price": "150.00",
    "patient": "01fcc220-49ee-4b9c-8a9a-0d5ea9a4293f",
    "physician": "d4feda94-cf49-4580-abe9-21fb02a9d5db"
  }

PATCH
"""""

::

$ curl -d '{"price":"300.00"}' -H "Content-Type: application/json" -X PATCH http://localhost:8000/api/v1/appointments/ab2ec149-ba5d-4ccd-9945-16d3255dd3ae/

Resultado

.. code-block:: JSON

  {
    "id": "ab2ec149-ba5d-4ccd-9945-16d3255dd3ae",
    "start_date": "2021-06-14T15:03:16.822947-03:00",
    "end_date": null,
    "price": "300.00",
    "patient": "01fcc220-49ee-4b9c-8a9a-0d5ea9a4293f",
    "physician": "d4feda94-cf49-4580-abe9-21fb02a9d5db"
  }

DELETE
""""""

::

$ curl -X DELETE http://localhost:8000/api/v1/appointments/ab2ec149-ba5d-4ccd-9945-16d3255dd3ae/


/api/v1/appointments/{id}/finish/
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

PUT
"""

:: 

$ curl -X PUT http://localhost:8000/api/v1/appointments/ab2ec149-ba5d-4ccd-9945-16d3255dd3ae/finish/


.. code-block:: JSON

  {
    "id": "ab2ec149-ba5d-4ccd-9945-16d3255dd3ae",
    "start_date": "2021-06-14T15:03:16.822947-03:00",
    "end_date": "2021-06-14T15:43:03.997454-03:00",
    "price": "200.00",
    "patient": "01fcc220-49ee-4b9c-8a9a-0d5ea9a4293f",
    "physician": "d4feda94-cf49-4580-abe9-21fb02a9d5db"
  }
