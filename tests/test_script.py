import unittest
import json
from main import app

class TestFlaskApi(unittest.TestCase):
    def setUp(self):
        # creates a test client
        self.app = app.test_client()
        # propagate the exceptions to the test client
        self.app.testing = True

    def test_random_recipe_route(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/recipe/random')

        # assert the status code of the response
        self.assertEqual(result.status_code, 200)

        # assert that the content returned by the route is JSON
        self.assertEqual(result.content_type, 'application/json')

        # if necessary, you can add more checks to validate the content of the response
        # data = json.loads(result.get_data(as_text=True))
        # self.assertIn('key', data)  # replace 'key' with actual key you expect in the response

if __name__ == '__main__':
    unittest.main()
