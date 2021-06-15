import requests
from celery.decorators import task
import os

@task(
    name='Generate billing',
    bind=True,
    retry_backoff=True,
    max_retries=None,
    autoretry_for=(Exception,)
)
def generate_billing(self, **kwargs):
    """
    """
    url_service = os.environ.get('CHARGE_API')
    headers = {'content-type': 'application/json'}
    response = requests.post(url_service, json=kwargs, headers=headers, timeout=None)
    if response.status_code != 201:
        raise Exception(f'POST {url_service} returned unexpected response code: {response.status_code}')
    return response.json()
