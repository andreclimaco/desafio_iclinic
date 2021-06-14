#############
Cobranças API
#############

API de cobranças.

**********
Instruções
**********

Iniciar
========

:: 

$ python manage.py runserver 0.0.0.0:9000


Administração
===============

Para acessar a adminstração é necessário a criação de um usuário.

Criar super usuário
^^^^^^^^^^^^^^^^^^^

:: 

$ python manage.py createsuperuser


Acessar a Administração
^^^^^^^^^^^^^^^^^^^^^^^

http://localhost:9000/admin


Endpoints
=========

A api disponibiliza um endpoint:


/api/v1/charges/
^^^^^^^^^^^^^^^^

GET
"""

:: 

$ curl -X GET http://localhost:9000/api/v1/charges/


POST
""""

:: 

$ curl -d '{"appointment":"e8933a87-be8e-4b5e-b1bf-60c8cc965218", "value":"250.00"}' -H "Content-Type: application/json" -X POST http://localhost:9000/api/v1/charges/

Resultado

.. code-block:: JSON

  {
    "id": "66880762-2771-4503-8602-d56d87500948",
    "value": "250.00",
    "appointment": "e8933a87-be8e-4b5e-b1bf-60c8cc965218"
  }


PUT
"""

::

$ curl -d '{"id":"66880762-2771-4503-8602-d56d87500948","value":"350.00","appointment":"e8933a87-be8e-4b5e-b1bf-60c8cc965218"}' -H "Content-Type: application/json" -X PUT http://localhost:9000/api/v1/charges/66880762-2771-4503-8602-d56d87500948/

Resultado

.. code-block:: JSON

  {
    "id": "66880762-2771-4503-8602-d56d87500948",
    "value": "350.00",
    "appointment": "e8933a87-be8e-4b5e-b1bf-60c8cc965218"
  }

PATCH
"""""

::

$ curl -d '{"value":"400.00"}' -H "Content-Type: application/json" -X PATCH http://localhost:9000/api/v1/charges/66880762-2771-4503-8602-d56d87500948/

Resultado

.. code-block:: JSON

  {
    "id": "66880762-2771-4503-8602-d56d87500948",
    "value": "400.00",
    "appointment": "e8933a87-be8e-4b5e-b1bf-60c8cc965218"
  }

DELETE
""""""

::

$ curl -X DELETE http://localhost:9000/api/v1/charges/66880762-2771-4503-8602-d56d87500948/
