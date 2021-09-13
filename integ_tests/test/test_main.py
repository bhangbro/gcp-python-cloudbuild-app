import http.client
import json
import os
import ssl
import unittest

endpoint = os.environ.get("API_ENDPOINT", "python-flask-service-shnjd7oeia-ue.a.run.app")

context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)

class MainIntegrationTests(unittest.TestCase):

    def test_hello_world(self):
        connection = http.client.HTTPSConnection(endpoint, context=context)
        headers = {'Content-type': 'application/json'}
        connection.request('GET', '/', headers=headers)

        response = connection.getresponse()
        print(response.status)
        print(response.reason)
        r = response.read().decode()
        print(r)
        connection.close()
        self.assertEqual('Hello World!', r)

if __name__ == '__main__':
    unittest.main()