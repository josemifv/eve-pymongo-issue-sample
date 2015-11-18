# -*- coding: utf-8 -*-

from eve import Eve
from eve.auth import BasicAuth


class DBAuth(BasicAuth):
    def check_auth(self, username, password, allowed_roles, resource, method):
        # use Eve's own db driver; no additional connections/resources are used
        accounts = app.data.driver.db['accounts']
        account = accounts.find_one({'username': username})
        return True


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

DATASETS_DOMAIN = {
    'accounts': accounts,
    # 'datasets': datasets,
    'protected_datasets': protected_datasets
}

my_settings = {
    'MONGO_HOST': 'ds047514.mongolab.com',
    'MONGO_USERNAME': 'demo',
    'MONGO_PASSWORD': 'demo',
    'MONGO_PORT': 47514,
    'MONGO_DBNAME': 'datasets-demo',
    'DEBUG': True,
    'DOMAIN': DATASETS_DOMAIN
}

app = Eve()
# app = Eve(settings=my_settings)

if __name__ == '__main__':
    app.run()
