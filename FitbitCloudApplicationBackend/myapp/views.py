from django.shortcuts import render
from django.http import JsonResponse
from .fitbit_auth import get_access_token
import requests



def get_access(request):
    # Your code to get the access token...
    print('Session:', request.session.items())  
    # Your access token
    access_token = request.session.get('access_token')
    if access_token is None:
        access_token = get_access_token(request)
    print("token: ", access_token)
    
    # Return the access token in the response
    return JsonResponse({'access_token': access_token})


def activity_log(request, activity_type=None, date=None):
    print("request: ", request)
    auth_header = request.META.get('HTTP_AUTHORIZATION')
    # print("auth_header: ", auth_header)
    if auth_header is not None:
        access_token = auth_header.split(' ')[1]  # The access token is after the 'Bearer ' part of the header
    else:
        access_token = None     
    # The headers for the API request
    headers = {
        'Authorization': f'Bearer {access_token}',
    }
    if request.path == '/api/activity/log/':
        api_url = 'https://api.fitbit.com/1/user/-/activities/list.json?afterDate=2019-01-01&sort=asc&offset=0&limit=100'
    else:
        return JsonResponse({'error': 'Invalid path'}, status=400)
    activity = requests.get(api_url, headers=headers)
    # print("activity: ", activity.json())
    return JsonResponse(activity.json())

def activities_frequent(request, activity_type=None, date=None):
        
    auth_header = request.META.get('HTTP_AUTHORIZATION')

    if auth_header is not None:
        access_token = auth_header.split(' ')[1]  # The access token is after the 'Bearer ' part of the header
    else:
        access_token = None
        
    # The headers for the API request
    headers = {
        'Authorization': f'Bearer {access_token}',
    }
    if request.path == '/api/activity/frequent_activities/':
        api_url = 'https://api.fitbit.com/1/user/-/activities/frequent.json'
    else:
        return JsonResponse({'error': 'Invalid path'}, status=400)
    
    activity = requests.get(api_url, headers=headers)
    if activity.status_code == 200:
        # print("activity_frequent: ", activity.text)
        activity_data = activity.json()
        return JsonResponse(activity_data[0])
    else:
        return JsonResponse({'error': 'API call failed', 'details': activity.text}, status=400)

def activities_recent(request, activity_type=None, date=None): 
    print("request: ", request)        
    auth_header = request.META.get('HTTP_AUTHORIZATION')

    if auth_header is not None:
        access_token = auth_header.split(' ')[1]  # The access token is after the 'Bearer ' part of the header
    else:
        access_token = None
        
    # The headers for the API request
    headers = {
        'Authorization': f'Bearer {access_token}',
    }
    if request.path == '/api/activity/recent_activity/':
        api_url = 'https://api.fitbit.com/1/user/-/activities/recent.json'
    else:
        return JsonResponse({'error': 'Invalid path'}, status=400)
    
    activity = requests.get(api_url, headers=headers)
    if activity.status_code == 200:
        # print("activity_recent: ", activity.text)
        activity_data = activity.json()
        return JsonResponse(activity_data[0])
    else:
        return JsonResponse({'error': 'API call failed', 'details': activity.text}, status=400)

def activities_time(request, date=None):
    print("request: ", request)  
    auth_header = request.META.get('HTTP_AUTHORIZATION')

    if auth_header is not None:
        access_token = auth_header.split(' ')[1]  # The access token is after the 'Bearer ' part of the header
    else:
        access_token = None
        
    # The headers for the API request
    headers = {
        'Authorization': f'Bearer {access_token}',
    }
    if date is not None:
        api_url = f'https://api.fitbit.com/1/user/-/activities/steps/date/{date}/1d.json'
    else:
        return JsonResponse({'error': 'Invalid path'}, status=400)
    
    activity = requests.get(api_url, headers=headers)
    print("activity_time: ", activity.json())
    return JsonResponse(activity.json())

def activities_summary(request,date=None):
        
    auth_header = request.META.get('HTTP_AUTHORIZATION')

    if auth_header is not None:
        access_token = auth_header.split(' ')[1]  # The access token is after the 'Bearer ' part of the header
    else:
        access_token = None
        
    # The headers for the API request
    headers = {
        'Authorization': f'Bearer {access_token}',
    }
    if date is not None:
        api_url = f'https://api.fitbit.com/1/user/-/activities/date/{date}.json'
    else:
        return JsonResponse({'error': 'Invalid path'}, status=400)
    
    activity = requests.get(api_url, headers=headers)
    # print("activit_summary: ", activity.json())
    return JsonResponse(activity.json())

# Create your views here.

def body_goal(request):
    print("request: ", request)
    auth_header = request.META.get('HTTP_AUTHORIZATION')
    # print("auth_header: ", auth_header)

    if auth_header is not None:
        access_token = auth_header.split(' ')[1]  # The access token is after the 'Bearer ' part of the header
    else:
        access_token = None
        
    # The headers for the API request
    headers = {
        'Authorization': f'Bearer {access_token}',
    }
    # Determine the API endpoint based on the path
    if request.path == '/api/body/goal/':
        api_url = 'https://api.fitbit.com/1/user/-/body/log/weight/goal.json'
    else:
        return JsonResponse({'error': 'Invalid path'}, status=400)

    # Replace this with your actual data
    body = requests.get(api_url, headers=headers)
    # print("body: ", body.json())
    return JsonResponse(body.json())

def body_weight(request,date=None):
    print("request: ", request)
    auth_header = request.META.get('HTTP_AUTHORIZATION')
    # print("auth_header: ", auth_header)

    if auth_header is not None:
        access_token = auth_header.split(' ')[1]  # The access token is after the 'Bearer ' part of the header
    else:
        access_token = None
        
    # The headers for the API request
    headers = {
        'Authorization': f'Bearer {access_token}',
    }

    # Determine the API endpoint based on the path
    if date is not None:
        api_url = f'https://api.fitbit.com/1/user/-/body/log/weight/date/{date}.json'
    else:
        return JsonResponse({'error': 'Invalid path'}, status=400)

    # Replace this with your actual data
    body = requests.get(api_url, headers=headers)
    # print("body: ", body.json())
    return JsonResponse(body.json())

def body_fat(request,date=None):
    print("request: ", request)
    auth_header = request.META.get('HTTP_AUTHORIZATION')
    # print("auth_header: ", auth_header)

    if auth_header is not None:
        access_token = auth_header.split(' ')[1]  # The access token is after the 'Bearer ' part of the header
    else:
        access_token = None
        
    # The headers for the API request
    headers = {
        'Authorization': f'Bearer {access_token}',
    }

    # Determine the API endpoint based on the path
    if date is not None:
        api_url = f'https://api.fitbit.com/1/user/-/body/log/fat/date/{date}.json'
    else:
        return JsonResponse({'error': 'Invalid path'}, status=400)

    # Replace this with your actual data
    body = requests.get(api_url, headers=headers)
    # print("body: ", body.json());
    return JsonResponse(body.json())


def breathing(request, start_date=None, end_date=None):
    print("request: ", request)
    auth_header = request.META.get('HTTP_AUTHORIZATION')
    # print("auth_header: ", auth_header)

    if auth_header is not None:
        access_token = auth_header.split(' ')[1]  # The access token is after the 'Bearer ' part of the header
    else:
        access_token = None

    # The headers for the API request
    headers = {
        'Authorization': f'Bearer {access_token}',
    }

    if start_date and end_date:
        api_url = f'https://api.fitbit.com/1/user/-/br/date/{start_date}/{end_date}.json'
    else:
        return JsonResponse({'error': 'Both start_date and end_date are required'}, status=400)
   
    # Replace this with your actual data
    breathing = requests.get(api_url, headers=headers)
    # print("breathing: ", breathing.json())
    return JsonResponse(breathing.json())


def cardio(request,start_date=None, end_date=None):
    print("request: ", request)
    auth_header = request.META.get('HTTP_AUTHORIZATION')
    # print("auth_header: ", auth_header)

    if auth_header is not None:
        access_token = auth_header.split(' ')[1]  # The access token is after the 'Bearer ' part of the header
    else:
        access_token = None

    # The headers for the API request
    headers = {
        'Authorization': f'Bearer {access_token}',
    }

    # Check if both start_date and end_date are provided
    if start_date and end_date:
        api_url = f'https://api.fitbit.com/1/user/-/cardioscore/date/{start_date}/{end_date}.json'
    else:
        return JsonResponse({'error': 'Both start_date and end_date are required'}, status=400)
    
    # Replace this with your actual data
    cardio = requests.get(api_url, headers=headers)
    # print("cardio: ", cardio.json())
    return JsonResponse(cardio.json())


def alarms(request, device_id=None):
    print("request: ", request)
    auth_header = request.META.get('HTTP_AUTHORIZATION')
    # print("auth_header: ", auth_header)

    if auth_header is not None:
        access_token = auth_header.split(' ')[1]  # The access token is after the 'Bearer ' part of the header
    else:
        access_token = None

    # The headers for the API request
    headers = {
        'Authorization': f'Bearer {access_token}',
    }

    if device_id is not None:
        api_url = 'https://api.fitbit.com/1/user/-/devices/tracker/{device_id}/alarms.json'
    else:
        return JsonResponse({'error': 'Invalid path'}, status=400)

    # Replace this with your actual data
    devices = requests.get(api_url, headers=headers)
    # print("alarms: ", alarms)
    return JsonResponse(devices.json(),safe=False)

def devices(request):
    print("request: ", request)
    auth_header = request.META.get('HTTP_AUTHORIZATION')
    # print("auth_header: ", auth_header)

    if auth_header is not None:
        access_token = auth_header.split(' ')[1]  # The access token is after the 'Bearer ' part of the header
    else:
        access_token = None

    # The headers for the API request
    headers = {
        'Authorization': f'Bearer {access_token}',
    }

    if request.path == '/api/devices/list/':
        api_url = 'https://api.fitbit.com/1/user/-/devices.json'
    else:
        return JsonResponse({'error': 'Invalid path'}, status=400)

    # Replace this with your actual data
    devices = requests.get(api_url, headers=headers)
    # print("devices: ", devices.json())
    return JsonResponse(devices.json(),safe=False)


def ecg(request):
    print("request: ", request)
    auth_header = request.META.get('HTTP_AUTHORIZATION')
    # print("auth_header: ", auth_header)

    if auth_header is not None:
        access_token = auth_header.split(' ')[1]  # The access token is after the 'Bearer ' part of the header
    else:
        access_token = None

    headers = {
        'Authorization': f'Bearer {access_token}',
    }


    if request.path == '/api/ecg/':
        api_url = 'https://api.fitbit.com/1/user/-/ecg/list.json?afterDate=2023-10-01&sort=asc&limit=1&offset=0'
    else:
        return JsonResponse({'error': 'Invalid path'}, status=400)

    
    # Replace this with your actual data
    ecg = requests.get(api_url, headers=headers)
    # print("ecg: ", ecg.json())
    return JsonResponse(ecg.json())

def heart_intraday(request,date=None):
    print("request: ", request)
    auth_header = request.META.get('HTTP_AUTHORIZATION')
    print("auth_header: ", auth_header)

    if auth_header is not None:
        access_token = auth_header.split(' ')[1]  # The access token is after the 'Bearer ' part of the header
    else:
        access_token = None

    headers = {
        'Authorization': f'Bearer {access_token}',
    }


    if date is not None:
        api_url = 'https://api.fitbit.com/1/user/-/activities/heart/date/{date}/1d.json'
    else:
        return JsonResponse({'error': 'Invalid path'}, status=400)

    
    # Replace this with your actual data
    heartrate = requests.get(api_url, headers=headers)
    print("heartrate: ", heartrate.json())
    return JsonResponse(heartrate.json())


def friends(request):
    print("request: ", request)
    auth_header = request.META.get('HTTP_AUTHORIZATION')
    # print("auth_header: ", auth_header)

    if auth_header is not None:
        access_token = auth_header.split(' ')[1]  # The access token is after the 'Bearer ' part of the header
    else:
        access_token = None

    headers = {
        'Authorization': f'Bearer {access_token}',
    }

    if request.path == '/api/friends/':
        api_url = 'https://api.fitbit.com/1.1/user/-/friends.json'
    else:
        return JsonResponse({'error': 'Invalid path'}, status=400)

    # Replace this with your actual data
    friends = requests.get(api_url, headers=headers)
    # print("friends: ", friends.json())
    return JsonResponse(friends.json())


def heartrate(request, start_date=None, end_date=None):
    print("request: ", request)
    auth_header = request.META.get('HTTP_AUTHORIZATION')
    # print("auth_header: ", auth_header)

    if auth_header is not None:
        access_token = auth_header.split(' ')[1]  # The access token is after the 'Bearer ' part of the header
    else:
        access_token = None

    headers = {
        'Authorization': f'Bearer {access_token}',
    }


    # Determine the API endpoint based on the path
    
    if start_date and end_date:
            api_url = f'https://api.fitbit.com/1/user/-/activities/heart/date/{start_date}/{end_date}.json'
    else:
        return JsonResponse({'error': 'Both start_date and end_date are required'}, status=400)


    heartrate = requests.get(api_url, headers=headers)
    # print("heartrate: ", heartrate.json())
    return JsonResponse(heartrate.json())

def heartrateVariability(request, date=None):
    print("request: ", request)
    auth_header = request.META.get('HTTP_AUTHORIZATION')
    # print("auth_header: ", auth_header)

    if auth_header is not None:
        access_token = auth_header.split(' ')[1]  # The access token is after the 'Bearer ' part of the header
    else:
        access_token = None

    headers = {
        'Authorization': f'Bearer {access_token}',
    }

    # Determine the API endpoint based on the path

    if date is not None:
            api_url = f'https://api.fitbit.com/1/user/-/hrv/date/{date}/all.json'
    else:
        return JsonResponse({'error': 'Invalid path'}, status=400)

    heartrate = requests.get(api_url, headers=headers)
    # print("heartrate: ", heartrate.json())
    return JsonResponse(heartrate.json())



def food(request, date=None):
    print("request: ", request)
    auth_header = request.META.get('HTTP_AUTHORIZATION')
    # print("auth_header: ", auth_header)

    if auth_header is not None:
        access_token = auth_header.split(' ')[1]  # The access token is after the 'Bearer ' part of the header
    else:
        access_token = None

    headers = {
        'Authorization': f'Bearer {access_token}',
    }

    if date:
            api_url = 'https://api.fitbit.com/1/user/-/foods/log/date/{date}.json'
    else:
        return JsonResponse({'error': 'Invalid path'}, status=400) 

    # Replace this with your actual data
    nutrition = requests.get(api_url, headers=headers)
    # print("nutrition: ", nutrition.json())
    return JsonResponse(nutrition.json())

def water(request, date=None):
    print("request: ", request)
    auth_header = request.META.get('HTTP_AUTHORIZATION')
    # print("auth_header: ", auth_header)

    if auth_header is not None:
        access_token = auth_header.split(' ')[1]  # The access token is after the 'Bearer ' part of the header
    else:
        access_token = None

    headers = {
        'Authorization': f'Bearer {access_token}',
    }


    if date:
            api_url = f'https://api.fitbit.com/1/user/-/foods/log/water/date/{date}.json'
    else:
        return JsonResponse({'error': 'Invalid path'}, status=400) 


    # Replace this with your actual data
    nutrition = requests.get(api_url, headers=headers)
    # print("nutrition: ", nutrition.json())
    return JsonResponse(nutrition.json())

def recent_food(request):
    print("request: ", request)
    auth_header = request.META.get('HTTP_AUTHORIZATION')
    # print("auth_header: ", auth_header)

    if auth_header is not None:
        access_token = auth_header.split(' ')[1]  # The access token is after the 'Bearer ' part of the header
    else:
        access_token = None

    headers = {
        'Authorization': f'Bearer {access_token}',
    }

    if request.path == '/api/nutrition/recent_food/':
        api_url = 'https://api.fitbit.com/1/user/-/foods/log/recent.json'
    else:
        return JsonResponse({'error': 'Invalid path'}, status=400) 


    # Replace this with your actual data
    nutrition = requests.get(api_url, headers=headers)
    # print("nutrition: ", nutrition.json())
    return JsonResponse(nutrition.json(),safe=False)


def oxygen(request, date=None):
    print("request: ", request)
    auth_header = request.META.get('HTTP_AUTHORIZATION')
    # print("auth_header: ", auth_header)

    if auth_header is not None:
        access_token = auth_header.split(' ')[1]  # The access token is after the 'Bearer ' part of the header
    else:
        access_token = None

    headers = {
        'Authorization': f'Bearer {access_token}',
    }

    # Replace this with your actual data

    if date is not None:
            api_url = f'https://api.fitbit.com/1/user/-/spo2/date/{date}.json'
    else:
        return JsonResponse({'error': 'Invalid path'}, status=400)

    oxygen = requests.get(api_url, headers=headers)
    print("oxygen: ", oxygen.json())
    return JsonResponse(oxygen.json())

def sleep(request, start_date:None, end_date:None):
    print("request: ", request)
    auth_header = request.META.get('HTTP_AUTHORIZATION')
    # print("auth_header: ", auth_header)

    if auth_header is not None:
        access_token = auth_header.split(' ')[1]  # The access token is after the 'Bearer ' part of the header
    else:
        access_token = None

    headers = {
        'Authorization': f'Bearer {access_token}',
    }

    if start_date and end_date:
            api_url = f'https://api.fitbit.com/1.2/user/-/sleep/date/{start_date}/{end_date}.json'
    else:
        return JsonResponse({'error': 'Invalid path'}, status=400)

    # Replace this with your actual data
    sleep = requests.get(api_url, headers=headers)
    # print("sleep: ", sleep.json())
    return JsonResponse(sleep.json())


def sleeplog(request, date:None):
    print("request: ", request)
    auth_header = request.META.get('HTTP_AUTHORIZATION')
    # print("auth_header: ", auth_header)

    if auth_header is not None:
        access_token = auth_header.split(' ')[1]  # The access token is after the 'Bearer ' part of the header
    else:
        access_token = None

    headers = {
        'Authorization': f'Bearer {access_token}',
    }

    if date:
            api_url = f'https://api.fitbit.com/1.2/user/-/sleep/date/{date}.json'
    else:
        return JsonResponse({'error': 'Invalid path'}, status=400)

    # Replace this with your actual data
    sleep = requests.get(api_url, headers=headers)
    # print("sleep: ", sleep.json())
    return JsonResponse(sleep.json())

def temperature_core(request, start_date:None, end_date:None):
    print("request: ", request)
    auth_header = request.META.get('HTTP_AUTHORIZATION')
    # print("auth_header: ", auth_header)

    if auth_header is not None:
        access_token = auth_header.split(' ')[1]  # The access token is after the 'Bearer ' part of the header
    else:
        access_token = None

    headers = {
        'Authorization': f'Bearer {access_token}',
    }

    if start_date and end_date:
        api_url = f'https://api.fitbit.com/1/user/-/temp/core/date/{start_date}/{end_date}.json'
    else:
        return JsonResponse({'error': 'Invalid path'}, status=400)
    
    temperature = requests.get(api_url, headers=headers)
    # print("temperature: ", temperature.json())
    return JsonResponse(temperature.json())
    

def temperature_skin(request, start_date:None, end_date:None):
    print("request: ", request)
    auth_header = request.META.get('HTTP_AUTHORIZATION')
    # print("auth_header: ", auth_header)

    if auth_header is not None:
        access_token = auth_header.split(' ')[1]  # The access token is after the 'Bearer ' part of the header
    else:
        access_token = None

    headers = {
        'Authorization': f'Bearer {access_token}',
    }

    if start_date and end_date:
            api_url = f'https://api.fitbit.com/1/user/-/temp/skin/date/{start_date}/{end_date}.json'
    else:
        return JsonResponse({'error': 'Invalid path'}, status=400)
    

    # Replace this with your actual data
    temperature = requests.get(api_url, headers=headers)
    # print("temperature: ", temperature.json())
    return JsonResponse(temperature.json())

