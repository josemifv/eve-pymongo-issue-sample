import unittest
from main import app


class MainTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_get_protected_datasets_without_authentication_must_return_401(self):
        rv = self.app.get('/protected_datasets', content_type='application/json')
        assert '401' in rv.status

    def test_get_protected_datasets_with_authentication_must_return_200(self):
        headers = [('Accept', 'application/json'), ('Authorization', 'Basic ZGVtbzpkZW1v')]
        rv = self.app.get('/protected_datasets', headers=headers)
        assert '200' in rv.status


if __name__ == '__main__':
    unittest.main()
