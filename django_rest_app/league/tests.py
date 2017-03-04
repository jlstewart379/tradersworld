import json
from django.test import TestCase
from django.test import LiveServerTestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient



class LeagueTests(LiveServerTestCase):

    def setUp(self):
        self.client = APIClient()

    def test_it_can_create_a_league(self):
        user_id = self._create_user(1)
        data = {'name': 'firstLeague', 'password': 'bonus', 'commissioner': user_id}
        response = self.client.post('/league/create/', data)
        self.assertEqual(201, response.status_code)

    def test_it_can_get_a_league(self):
        user_id = self._create_user(2)
        res = self._create_league(user_id)
        league_info = res.content.decode('utf-8')
        league_id = json.loads(league_info)['id']
        response = self.client.get('/league/{}/'.format(league_id))
        expected = '{"id":%s,"name":"firstLeague","commissioner":%s,"participants":' \
                   '[{"name":"test_user_2","weekWins":0,"weekLosses":0,"overallWins":0,"overallLosses":0}]}'\
            % (league_id, user_id)
        self.assertEqual(response.content.decode('utf-8'), expected)

    def test_participants_can_join_league(self):
        user_ids = self._create_users([1, 2, 3])
        commish_id = user_ids[0]
        league_data = self._create_league(commish_id)
        league_id = json.loads(league_data.content.decode('utf-8'))['id']
        data = {'participant': user_ids[1]}
        response = self.client.put('/league/add_user/{}/'.format(league_id), data)
        expected = '{"id":%s,"name":"firstLeague","commissioner":%s}' % (league_id, commish_id)
        self.assertEqual(response.content.decode('utf-8'), expected)



    def _create_league(self, commish_id):
        data = {'name': 'firstLeague', 'password': 'bonus', 'commissioner': commish_id}
        return self.client.post('/league/create/', data)


    def _create_users(self, users):
        ids = []
        for user in users:
            ids.append(self._create_user(user))
        return ids
        
    def _create_user(self, idx):
        username = "test_user_{}".format(idx)
        password = "test_password_{}".format(idx)
        email = "test_users_{}@email.com".format(idx)
        response = self.client.post('/registration/users/new/', {'username': username, 'password': password, 'email': email}, format='json')
        return json.loads(response.content.decode('utf-8'))['id']

