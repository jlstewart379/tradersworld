import json
from django.test import TestCase
from django.test import LiveServerTestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient



class LeagueTests(LiveServerTestCase):

    def setUp(self):
        self.client = APIClient()

    def test_it_can_create_a_league(self):
        self._create_user(1)
        data = {'name': 'firstLeague', 'password': 'bonus', 'commissioner': 1}
        response = self.client.post('/league/create/', data)
        self.assertEqual(201, response.status_code)

    def test_it_can_get_a_league(self):
        self._create_user(2)
        res = self._create_league(2) 
        league_info = res.content.decode('utf-8')
        league_id = json.loads(league_info)['id']
        response = self.client.get('/league/{}/'.format(league_id))
        self.assertEqual(response.content, b'{"id":2,"name":"firstLeague","commissioner":2,"participants":[{"name":"test_user_2","weekWins":0,"weekLosses":0,"overallWins":0,"overallLosses":0}]}') 

    def test_participants_can_join_league(self):
        self._create_users([1, 2, 3])
        commish_id = User.objects.all()[0].pk
        league_data = self._create_league(commish_id)
        league_id = json.loads(league_data.content.decode('utf-8'))['id']
        data = {'participant':3}
        response = self.client.put('/league/add_user/{}/'.format(league_id), data)
        self.assertEqual(response.content, b'{"id":3,"name":"firstLeague","commissioner":3}')



    def _create_league(self, commish_id):
        data = {'name': 'firstLeague', 'password': 'bonus', 'commissioner': commish_id}
        return self.client.post('/league/create/', data)


    def _create_users(self, users):
        for user in users:
            self._create_user(user)
        
    def _create_user(self, idx):
        username = "test_user_{}".format(idx)
        password = "test_password_{}".format(idx)
        email = "test_users_{}@email.com".format(idx)
        return self.client.post('/registration/users/new/', {'username': username, 'password': password, 'email': email}, format='json')

