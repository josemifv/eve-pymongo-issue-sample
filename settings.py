import os
from main import DBAuth

# MongoDB configuration
MONGO_HOST = 'ds047514.mongolab.com'
MONGO_USERNAME = 'demo'
MONGO_PASSWORD = 'demo'
MONGO_PORT = '47514'
MONGO_DBNAME = 'datasets-demo'

# Enable for debugging
DEBUG = True

# Account schema (for authorization)
accounts_schema = {
    'username': {
        'type': 'string',
        'required': True,
        'unique': True
    },
    'password': {
        'type': 'string',
        'required': True,
    },
    'roles': {
        'type': 'list',
        'allowed': ['admin', 'user'],
        'required': True
    }
}

# Datasets schema (a simple media file)
datasets_schema = {
    'file': {
        'type': 'media'
    }
}

# RESOURCES
accounts = {
    'schema': accounts_schema,
    'internal_resource': True
}

datasets = {
    'item_title': 'dataset',
    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,
    'schema': datasets_schema
}

protected_datasets = {
    'authentication': DBAuth(),
    'item_title': 'protected_dataset',
    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,
    'schema': datasets_schema
}

DOMAIN = {
    'accounts': accounts,
    'datasets': datasets,
    'protected_datasets': protected_datasets
}
