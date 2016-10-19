import flask
import json
import server as server
import unittest

class FlaskServerTest(unittest.TestCase):

    def setUp(self):
    #Run app in testing mode to retrieve exceptions and stack traces
        server.app.testing = True
        self.app = server.app.test_client()

    def test_hello(self):
        response = self.app.get('/hello')
        self.assertEqual(response.status_code, 200)
        assert response.status_code == 200, "status_code was OK"
        assert response.data == "HELLO Children!, Hi Chef!"

    def test_hello_to_person(self):
        response = self.app.get('/hello/Jay')
        assert response.data == "Hello Jay"

    def test_pets(self):
        response = self.app.get('/pets')
        assert response.data == ""

if __name__ == '__main__':
    unittest.main()
