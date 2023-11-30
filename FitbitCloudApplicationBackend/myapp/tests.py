import json
from unittest.mock import patch
from django.test import TestCase, RequestFactory, override_settings
from django.conf import settings
from .views import get_access,activity_log,activities_type,activities_summary,activities_frequent,activities_recent,body_goal,body_fat,body_weight,breathing,cardio,alarms,devices,ecg,friends,heartrateVariability,heartrate,food,recent_food,water,oxygen,sleep,sleeplog,temperature_core,temperature_skin

@override_settings(MIDDLEWARE=[mw for mw in settings.MIDDLEWARE if mw != 'django.middleware.csrf.CsrfViewMiddleware'])
class GetAccessTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    @patch('myapp.views.get_access_token')
    def test_get_access(self,mock_get_access_token):
        # Mock the get_access_token function to return a fixed access token
        mock_get_access_token.return_value = 'mock_access_token'

        # Create a mock request
        request = self.factory.get('/get_access_token/')

        # Add a session to the request
        request.session = {}

        # Call the get_access function
        response = get_access(request)

        # Parse the response content as JSON
        response_content = json.loads(response.content)

        # Check if the response is what you expect
        self.assertEqual(response.status_code, 200)
        self.assertIn('access_token',response_content)

class Tests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_activity_log(self):
        # Create a mock request
        request = self.factory.get('/api/activity/log/')
        
        # Add an 'HTTP_AUTHORIZATION' header to the request
        request.META['HTTP_AUTHORIZATION'] = 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyM1JLTEsiLCJzdWIiOiJCUlBEOUwiLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJ3aHIgd251dCB3cHJvIHdzbGUgd2VjZyB3c29jIHdhY3Qgd294eSB3dGVtIHd3ZWkgd2NmIHdzZXQgd2xvYyB3cmVzIiwiZXhwIjoxNzAxMzEwNTgwLCJpYXQiOjE3MDEyODE3ODB9.0ri5a_qqjG0zGMyrEWYroTaR8168Kurj0NVbyIefr_8'

        # Call the activity_log function
        response = activity_log(request)

        # Parse the response content as JSON
        response_content = json.loads(response.content)

        # Check if the response is what you expect
        self.assertEqual(response.status_code, 200)
        # Add more assertions here based on what you expect in the response content

    def test_activities_summary(self):
        # Create a mock request
        request = self.factory.get('/api/activity/summary/2023-11-02/')

        # Add an 'HTTP_AUTHORIZATION' header to the request
        request.META['HTTP_AUTHORIZATION'] = f'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyM1JLTEsiLCJzdWIiOiJCUlBEOUwiLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJ3aHIgd251dCB3cHJvIHdzbGUgd2VjZyB3c29jIHdhY3Qgd294eSB3dGVtIHd3ZWkgd2NmIHdzZXQgd2xvYyB3cmVzIiwiZXhwIjoxNzAxMzEwNTgwLCJpYXQiOjE3MDEyODE3ODB9.0ri5a_qqjG0zGMyrEWYroTaR8168Kurj0NVbyIefr_8'

        # Call the activities_summary function
        response = activities_summary(request,'2023-11-02')

        # Check if the response is what you expect
        self.assertEqual(response.status_code, 200)
        # Add more assertions here based on what you expect in the response content

    def test_activities_frequent(self):
        # Create a mock request
        request = self.factory.get('/api/activity/frequent_activities/')

        # Add an 'HTTP_AUTHORIZATION' header to the request
        request.META['HTTP_AUTHORIZATION'] = 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyM1JLTEsiLCJzdWIiOiJCUlBEOUwiLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJ3aHIgd251dCB3cHJvIHdzbGUgd2VjZyB3c29jIHdhY3Qgd294eSB3dGVtIHd3ZWkgd2NmIHdzZXQgd2xvYyB3cmVzIiwiZXhwIjoxNzAxMzEwNTgwLCJpYXQiOjE3MDEyODE3ODB9.0ri5a_qqjG0zGMyrEWYroTaR8168Kurj0NVbyIefr_8'

        # Call the activities_frequent function
        response = activities_frequent(request)


        # Check if the response is what you expect
        self.assertEqual(response.status_code, 200)
        # Add more assertions here based on what you expect in the response content

    def test_activities_recent(self):
        # Create a mock request
        request = self.factory.get('/api/activity/recent_activity/')

        # Add an 'HTTP_AUTHORIZATION' header to the request
        request.META['HTTP_AUTHORIZATION'] = 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyM1JLTEsiLCJzdWIiOiJCUlBEOUwiLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJ3aHIgd251dCB3cHJvIHdzbGUgd2VjZyB3c29jIHdhY3Qgd294eSB3dGVtIHd3ZWkgd2NmIHdzZXQgd2xvYyB3cmVzIiwiZXhwIjoxNzAxMzEwNTgwLCJpYXQiOjE3MDEyODE3ODB9.0ri5a_qqjG0zGMyrEWYroTaR8168Kurj0NVbyIefr_8'

        # Call the activities_recent function
        response = activities_recent(request)

        # Check if the response is what you expect
        self.assertEqual(response.status_code, 200)
        # Add more assertions here based on what you expect in the response content
    
    def test_body_goal(self):
        # Create a mock request
        request = self.factory.get('/api/body/goal/')

        # Add an 'HTTP_AUTHORIZATION' header to the request
        request.META['HTTP_AUTHORIZATION'] = 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyM1JLTEsiLCJzdWIiOiJCUlBEOUwiLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJ3aHIgd251dCB3cHJvIHdzbGUgd2VjZyB3c29jIHdhY3Qgd294eSB3dGVtIHd3ZWkgd2NmIHdzZXQgd2xvYyB3cmVzIiwiZXhwIjoxNzAxMzEwNTgwLCJpYXQiOjE3MDEyODE3ODB9.0ri5a_qqjG0zGMyrEWYroTaR8168Kurj0NVbyIefr_8'

        # Call the body_goal function
        response = body_goal(request)

        # Parse the response content as JSON
        response_content = json.loads(response.content)

        # Check if the response is what you expect
        # self.assertEqual(response.status_code, 200)
        # Add more assertions here based on what you expect in the response content

    def test_body_fat(self):
        # Create a mock request
        request = self.factory.get('/api/body/fat/date/2020-09-01/')

        # Add an 'HTTP_AUTHORIZATION' header to the request
        request.META['HTTP_AUTHORIZATION'] = f'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyM1JLTEsiLCJzdWIiOiJCUlBEOUwiLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJ3aHIgd251dCB3cHJvIHdzbGUgd2VjZyB3c29jIHdhY3Qgd294eSB3dGVtIHd3ZWkgd2NmIHdzZXQgd2xvYyB3cmVzIiwiZXhwIjoxNzAxMzEwNTgwLCJpYXQiOjE3MDEyODE3ODB9.0ri5a_qqjG0zGMyrEWYroTaR8168Kurj0NVbyIefr_8'

        # Call the body_fat function
        response = body_fat(request,'2023-11-02')

        # Parse the response content as JSON
        response_content = json.loads(response.content)

        # Check if the response is what you expect
        # self.assertEqual(response.status_code, 200)
        # Add more assertions here based on what you expect in the response content

    def test_body_weight(self):
        # Create a mock request
        request = self.factory.get('/api/body/weight/date/2020-09-01/')

        # Add an 'HTTP_AUTHORIZATION' header to the request
        request.META['HTTP_AUTHORIZATION'] = f'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyM1JLTEsiLCJzdWIiOiJCUlBEOUwiLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJ3aHIgd251dCB3cHJvIHdzbGUgd2VjZyB3c29jIHdhY3Qgd294eSB3dGVtIHd3ZWkgd2NmIHdzZXQgd2xvYyB3cmVzIiwiZXhwIjoxNzAxMzEwNTgwLCJpYXQiOjE3MDEyODE3ODB9.0ri5a_qqjG0zGMyrEWYroTaR8168Kurj0NVbyIefr_8'

        # Call the body_weight function
        response = body_weight(request,'2023-11-02')

        # Parse the response content as JSON
        response_content = json.loads(response.content)

        # Check if the response is what you expect
        # self.assertEqual(response.status_code, 200)
        # Add more assertions here based on what you expect in the response content

    def test_breathing(self):
        # Create a mock request
        request = self.factory.get('/api/breathing/date_range/2020-09-01/2020-09-02/')

        # Add an 'HTTP_AUTHORIZATION' header to the request
        request.META['HTTP_AUTHORIZATION'] = 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyM1JLTEsiLCJzdWIiOiJCUlBEOUwiLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJ3aHIgd251dCB3cHJvIHdzbGUgd2VjZyB3c29jIHdhY3Qgd294eSB3dGVtIHd3ZWkgd2NmIHdzZXQgd2xvYyB3cmVzIiwiZXhwIjoxNzAxMzEwNTgwLCJpYXQiOjE3MDEyODE3ODB9.0ri5a_qqjG0zGMyrEWYroTaR8168Kurj0NVbyIefr_8'
        
        # Call the breathing function
        response = breathing(request,'2023-11-01','2023-11-02')
        
        # Parse the response content as JSON
        response_content = json.loads(response.content)
        
        # Check if the response is what you expect
        # self.assertEqual(response.status_code, 200)
        # Add more assertions here based on what you expect in the response content

    def test_cardio(self):
        # Create a mock request
        request = self.factory.get('/api/cardio_fitness_score/date_range/2023-11-01/2023-11-02/')

        # Add an 'HTTP_AUTHORIZATION' header to the request
        request.META['HTTP_AUTHORIZATION'] = 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyM1JLTEsiLCJzdWIiOiJCUlBEOUwiLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJ3aHIgd251dCB3cHJvIHdzbGUgd2VjZyB3c29jIHdhY3Qgd294eSB3dGVtIHd3ZWkgd2NmIHdzZXQgd2xvYyB3cmVzIiwiZXhwIjoxNzAxMzEwNTgwLCJpYXQiOjE3MDEyODE3ODB9.0ri5a_qqjG0zGMyrEWYroTaR8168Kurj0NVbyIefr_8'
        
        # Call the cardio function
        response = cardio(request,'2023-11-01','2023-11-02')
        
        # Parse the response content as JSON
        response_content = json.loads(response.content)
        
        # Check if the response is what you expect
        self.assertEqual(response.status_code, 200)
        # Add more assertions here based on what you expect in the response content

    def test_alarms(self):
        # Create a mock request
        request = self.factory.get('/api/devices/tracker/2470017778/')

        # Add an 'HTTP_AUTHORIZATION' header to the request
        request.META['HTTP_AUTHORIZATION'] = 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyM1JLTEsiLCJzdWIiOiJCUlBEOUwiLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJ3aHIgd251dCB3cHJvIHdzbGUgd2VjZyB3c29jIHdhY3Qgd294eSB3dGVtIHd3ZWkgd2NmIHdzZXQgd2xvYyB3cmVzIiwiZXhwIjoxNzAxMzEwNTgwLCJpYXQiOjE3MDEyODE3ODB9.0ri5a_qqjG0zGMyrEWYroTaR8168Kurj0NVbyIefr_8'
        
        # Call the alarms function
        response = alarms(request,'2470017778')
        
        
        # Check if the response is what you expect
        self.assertEqual(response.status_code, 200)
        # Add more assertions here based on what you expect in the response content

    def test_devices(self):
                # Create a mock request
        request = self.factory.get('/api/devices/list/')

        # Add an 'HTTP_AUTHORIZATION' header to the request
        request.META['HTTP_AUTHORIZATION'] = f'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyM1JLTEsiLCJzdWIiOiJCUlBEOUwiLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJ3aHIgd251dCB3cHJvIHdzbGUgd2VjZyB3c29jIHdhY3Qgd294eSB3dGVtIHd3ZWkgd2NmIHdzZXQgd2xvYyB3cmVzIiwiZXhwIjoxNzAxMzEwNTgwLCJpYXQiOjE3MDEyODE3ODB9.0ri5a_qqjG0zGMyrEWYroTaR8168Kurj0NVbyIefr_8'
        
        # Call the alarms function
        response = devices(request)
        
        
        # Check if the response is what you expect
        self.assertEqual(response.status_code, 200)
        # Add more assertions here based on what you expect in the response content

    def test_ecg(self):
        # Create a mock request
        request = self.factory.get('/api/ecg/')

        # Add an 'HTTP_AUTHORIZATION' header to the request
        request.META['HTTP_AUTHORIZATION'] = f'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyM1JLTEsiLCJzdWIiOiJCUlBEOUwiLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJ3aHIgd251dCB3cHJvIHdzbGUgd2VjZyB3c29jIHdhY3Qgd294eSB3dGVtIHd3ZWkgd2NmIHdzZXQgd2xvYyB3cmVzIiwiZXhwIjoxNzAxMzEwNTgwLCJpYXQiOjE3MDEyODE3ODB9.0ri5a_qqjG0zGMyrEWYroTaR8168Kurj0NVbyIefr_8'
        
        # Call the alarms function
        response = ecg(request)
        
        
        # Check if the response is what you expect
        self.assertEqual(response.status_code, 200)
        # Add more assertions here based on what you expect in the response content

    def test_friends(self):
        # Create a mock request
        request = self.factory.get('/api/friends/')

        # Add an 'HTTP_AUTHORIZATION' header to the request
        request.META['HTTP_AUTHORIZATION'] = f'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyM1JLTEsiLCJzdWIiOiJCUlBEOUwiLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJ3aHIgd251dCB3cHJvIHdzbGUgd2VjZyB3c29jIHdhY3Qgd294eSB3dGVtIHd3ZWkgd2NmIHdzZXQgd2xvYyB3cmVzIiwiZXhwIjoxNzAxMzEwNTgwLCJpYXQiOjE3MDEyODE3ODB9.0ri5a_qqjG0zGMyrEWYroTaR8168Kurj0NVbyIefr_8'
        
        # Call the alarms function
        response = friends(request)
        
        
        # Check if the response is what you expect
        self.assertEqual(response.status_code, 200)
        # Add more assertions here based on what you expect in the response content

    def test_heartrateVariability(self):
        # Create a mock request
        request = self.factory.get('/api/heartrate/variability/2023-11-01/')

        # Add an 'HTTP_AUTHORIZATION' header to the request
        request.META['HTTP_AUTHORIZATION'] = f'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyM1JLTEsiLCJzdWIiOiJCUlBEOUwiLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJ3aHIgd251dCB3cHJvIHdzbGUgd2VjZyB3c29jIHdhY3Qgd294eSB3dGVtIHd3ZWkgd2NmIHdzZXQgd2xvYyB3cmVzIiwiZXhwIjoxNzAxMzEwNTgwLCJpYXQiOjE3MDEyODE3ODB9.0ri5a_qqjG0zGMyrEWYroTaR8168Kurj0NVbyIefr_8'
        
        # Call the alarms function
        response = heartrateVariability(request,'2023-11-01')
        
        
        # Check if the response is what you expect
        self.assertEqual(response.status_code, 200)
        # Add more assertions here based on what you expect in the response content

    def test_heartrate(self):
        # Create a mock request
        request = self.factory.get('/api/heartrate/2023-11-01/2023-11-02/')

        # Add an 'HTTP_AUTHORIZATION' header to the request
        request.META['HTTP_AUTHORIZATION'] = f'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyM1JLTEsiLCJzdWIiOiJCUlBEOUwiLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJ3aHIgd251dCB3cHJvIHdzbGUgd2VjZyB3c29jIHdhY3Qgd294eSB3dGVtIHd3ZWkgd2NmIHdzZXQgd2xvYyB3cmVzIiwiZXhwIjoxNzAxMzEwNTgwLCJpYXQiOjE3MDEyODE3ODB9.0ri5a_qqjG0zGMyrEWYroTaR8168Kurj0NVbyIefr_8'
        
        # Call the alarms function
        response = heartrate(request,'2023-11-01','2023-11-02')
        
        
        # Check if the response is what you expect
        self.assertEqual(response.status_code, 200)
        # Add more assertions here based on what you expect in the response content


    def test_food(self):
        # Create a mock request
        request = self.factory.get('/api/nutrition/food_log/2023-11-01/')

        # Add an 'HTTP_AUTHORIZATION' header to the request
        request.META['HTTP_AUTHORIZATION'] = f'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIxMlJLTEsiLCJzdWIiOiJCUlBEOUwiLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiIiLCJleHAiOjE3MDEyNjAzOTAsImlhdCI6MTcwMTIzMTU5MH0.3s6I5k1dQZnY0gj3V0kVqW3n0qjE6gZJzYz0Bz0G3Y0'
        
        # Call the alarms function
        response = food(request,'2023-11-01')
        
        
        # Check if the response is what you expect
        self.assertEqual(response.status_code, 200)
        # Add more assertions here based on what you expect in the response content

    def test_recent_food(self):
        # Create a mock request
        request = self.factory.get('/api/nutrition/recent_food/')

        # Add an 'HTTP_AUTHORIZATION' header to the request
        request.META['HTTP_AUTHORIZATION'] = f'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIxMlJLTEsiLCJzdWIiOiJCUlBEOUwiLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiIiLCJleHAiOjE3MDEyNjAzOTAsImlhdCI6MTcwMTIzMTU5MH0.3s6I5k1dQZnY0gj3V0kVqW3n0qjE6gZJzYz0Bz0G3Y0'
        
        # Call the alarms function
        response = recent_food(request)
        
        
        # Check if the response is what you expect
        self.assertEqual(response.status_code, 200)
        # Add more assertions here based on what you expect in the response content

    
    def test_water(self):
        # Create a mock request
        request = self.factory.get('/api/nutrition/water_log/2023-11-01')

        # Add an 'HTTP_AUTHORIZATION' header to the request
        request.META['HTTP_AUTHORIZATION'] = f'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIxMlJLTEsiLCJzdWIiOiJCUlBEOUwiLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiIiLCJleHAiOjE3MDEyNjAzOTAsImlhdCI6MTcwMTIzMTU5MH0.3s6I5k1dQZnY0gj3V0kVqW3n0qjE6gZJzYz0Bz0G3Y0'
        
        # Call the alarms function
        response = water(request,'2023-11-01')
        
        
        # Check if the response is what you expect
        self.assertEqual(response.status_code, 200)
        # Add more assertions here based on what you expect in the response content

    def test_oxygen(self):
        # Create a mock request
        request = self.factory.get('/api/oxygen/2023-11-01')

        # Add an 'HTTP_AUTHORIZATION' header to the request
        request.META['HTTP_AUTHORIZATION'] = f'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIxMlJLTEsiLCJzdWIiOiJCUlBEOUwiLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiIiLCJleHAiOjE3MDEyNjAzOTAsImlhdCI6MTcwMTIzMTU5MH0.3s6I5k1dQZnY0gj3V0kVqW3n0qjE6gZJzYz0Bz0G3Y0'
        
        # Call the alarms function
        response = oxygen(request,'2023-11-01')
        
        
        # Check if the response is what you expect
        self.assertEqual(response.status_code, 200)
        # Add more assertions here based on what you expect in the response content

    def test_sleep(self):
        # Create a mock request
        request = self.factory.get('/api/sleep/2023-11-01/2023-11-02')

        # Add an 'HTTP_AUTHORIZATION' header to the request
        request.META['HTTP_AUTHORIZATION'] = f'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIxMlJLTEsiLCJzdWIiOiIxMlJLTEsiLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJleHAiOjE3MDEyNjAzOTAsImlhdCI6MTcwMTIzMTU5MH0.3s6I5k1dQZnY0gj3V0kVqW3n0qjE6gZJzYz0Bz0G3Y0'
        
        # Call the alarms function
        response = sleep(request,'2023-11-01','2023-11-02')
        
        
        # Check if the response is what you expect
        self.assertEqual(response.status_code, 200)
        # Add more assertions here based on what you expect in the response content

    def test_sleeplog(self):
        # Create a mock request
        request = self.factory.get('/api/sleeplog/2023-11-01')

        # Add an 'HTTP_AUTHORIZATION' header to the request
        request.META['HTTP_AUTHORIZATION'] = f'Bearer eyJhbGciOiJIUzI1NiJ9eyJhdWQiOiIxMlJLTEsiLCJzdWIiOiIxMlJLTEsiLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJleHAiOjE3MDEyNjAzOTAsImlhdCI6MTcwMTIzMTU5MH0.3s6I5k1dQZnY0gj3V0kVqW3n0qjE6gZJzYz0Bz0G3Y0'
        
        # Call the alarms function
        response = sleeplog(request,'2023-11-01')
        
        
        # Check if the response is what you expect
        self.assertEqual(response.status_code, 200)
        # Add more assertions here based on what you expect in the response content

    def test_temperature_core(self):
        # Create a mock request
        request = self.factory.get('/api/temperature/core/2023-11-01/2023-11-02')

        # Add an 'HTTP_AUTHORIZATION' header to the request
        request.META['HTTP_AUTHORIZATION'] = f'Bearer eyJhbGciOiJIUzI1NiJ9eyJhdWQiOiIxMlJLTEsiLCJzdWIiOiIxMlJLTEsiLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJleHAiOjE3MDEyNjAzOTAsImlhdCI6MTcwMTIzMTU5MH0.3s6I5k1dQZnY0gj3V0kVqW3n0qjE6gZJzYz0Bz0G3Y0'
        
        # Call the alarms function
        response = temperature_core(request,'2023-11-01','2023-11-02')
        
        
        # Check if the response is what you expect
        self.assertEqual(response.status_code, 200)
        # Add more assertions here based on what you expect in the response content

    def test_temperature_skin(self):
        # Create a mock request
        request = self.factory.get('/api/temperature/skin/2023-11-01/2023-11-02')

        # Add an 'HTTP_AUTHORIZATION' header to the request
        request.META['HTTP_AUTHORIZATION'] = f'Bearer eyJhbGciOiJIUzI1NiJ9eyJhdWQiOiIxMlJLTEsiLCJzdWIiOiIxMlJLTEsiLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJleHAiOjE3MDEyNjAzOTAsImlhdCI6MTcwMTIzMTU5MH0.3s6I5k1dQZnY0gj3V0kVqW3n0qjE6gZJzYz0Bz0G3Y0'
        
        # Call the alarms function
        response = temperature_skin(request,'2023-11-01','2023-11-02')
        
        
        # Check if the response is what you expect
        self.assertEqual(response.status_code, 200)
        # Add more assertions here based on what you expect in the response content

    
    
    

    

    


