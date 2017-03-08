import json
from django.test import LiveServerTestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient

class UserTests(LiveServerTestCase):

    def setUp(self):
        self.client = APIClient()

    def test_it_can_get_create_user(self):
        self._create_user(1)
        user = User.objects.get(username='test_user_1')
        self.assertIsNotNone(user)

    def test_it_can_get_a_user(self):
        user_id = self._create_user(2)
        user = User.objects.get(username='test_user_2')
        response = self.client.get('/registration/users/{}/'.format(user.id))
        content = response.content.decode('utf-8')
        expected = '{"id":%s,"username":"test_user_2","email":"test_users_2@email.com"}' % user_id
        self.assertEqual(content, expected)

    def test_it_can_obtain_auth_token(self):
        self._create_user(3)
        user = User.objects.get(username='test_user_3')
        response = self.client.post('/registration/auth_token/', {'username': user.username, 'password': 'test_password_3'})
        self.assertTrue('"token":"' in response.content.decode('utf-8'))

    def test_it_can_get_a_profile(self):
        self._create_user(3)
        user = User.objects.get(username='test_user_3')
        response = self.client.get('')

    def test_it_can_get_an_authenticated_user(self):
        user_id = self._create_user(4)
        response = self.client.post('/registration/auth_token/', {'username':'test_user_4', 'password': 'test_password_4'})
        token = json.loads(response.content.decode('utf-8'))["token"]

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)

        response = self.client.get('/registration/users/current/')
        expected = '{"id":%s,"username":"test_user_4","email":"test_users_4@email.com"}' % user_id
        self.assertEqual(response.content.decode('utf-8'), expected)

    def _create_user(self, idx):
        username = "test_user_{}".format(idx)
        password = "test_password_{}".format(idx)
        email = "test_users_{}@email.com".format(idx)
        response = self.client.post('/registration/users/new/', {'username': username, 'password': password, 'email': email}, format='json')
        return json.loads(response.content.decode('utf-8'))['id']
