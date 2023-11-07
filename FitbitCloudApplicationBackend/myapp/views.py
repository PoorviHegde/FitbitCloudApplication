from django.shortcuts import render
from django.http import JsonResponse
from .fitbit_auth import get_access_token
import requests

def activity(request, activity_type=None, date=None):
    # Your access token
    access_token = request.session.get('access_token')

    # The headers for the API request
    headers = {
        'Authorization': f'Bearer {access_token}',
    }
    # Replace this with your actual data

    if request.path == '/api/activity/log/':
        api_url = 'https://api.fitbit.com/1/user/-/activities/list.json'
    elif request.path == 'api/activity/frequent_activities/':
        api_url = 'https://api.fitbit.com/1/user/-/activities/frequent.json'
    elif request.path == 'api/activity/recent_activity/':
        api_url = 'https://api.fitbit.com/1/user/-/activities/recent.json'
    elif activity_type is not None:
        api_url = f'https://api.fitbit.com/1/user/-/activities/{activity_type}.json'
    elif date is not None:
        api_url = f'https://api.fitbit.com/1/user/-/activities/date/{date}.json'
    else:
        return JsonResponse({'error': 'Invalid path'}, status=400)


    activity = requests.get(api_url, headers=headers)
    return JsonResponse(activity.json())


# Create your views here.

def body(request):
    # Your access token
    access_token = request.session.get('access_token')

    # The headers for the API request
    headers = {
        'Authorization': f'Bearer {access_token}',
    }

    # Determine the API endpoint based on the path
    if request.path == '/api/body/goal/':
        api_url = 'https://api.fitbit.com/1/user/-/body/log/weight/goal.json'
    elif request.path == '/api/body/fat/':
        api_url = 'https://api.fitbit.com/1/user/-/body/log/fat.json'
    elif request.path == '/api/body/weight/':
        api_url = 'https://api.fitbit.com/1/user/-/body/log/weight.json'
    else:
        return JsonResponse({'error': 'Invalid path'}, status=400)

    # Replace this with your actual data
    body = requests.get(api_url, headers=headers)
    return JsonResponse(body.json())


def breathing(request, start_date=None, end_date=None):
    # Your access token
    access_token = request.session.get('access_token')

    # The headers for the API request
    headers = {
        'Authorization': f'Bearer {access_token}',
    }

    if start_date and end_date:
        api_url = f'https://api.fitbit.com/1/user/-/breathing/date_range/{start_date}/{end_date}.json'
    else:
        return JsonResponse({'error': 'Both start_date and end_date are required'}, status=400)
   
    # Replace this with your actual data
    breathing = requests.get(api_url, headers=headers)
    return JsonResponse(breathing.json())


def cardio(request,start_date=None, end_date=None):
    # Your access token
    access_token = request.session.get('access_token')

    # The headers for the API request
    headers = {
        'Authorization': f'Bearer {access_token}',
    }

    # Check if both start_date and end_date are provided
    if start_date and end_date:
        api_url = f'https://api.fitbit.com/1/user/-/cardio/date_range/{start_date}/{end_date}.json'
    else:
        return JsonResponse({'error': 'Both start_date and end_date are required'}, status=400)
    
    # Replace this with your actual data
    cardio = requests.get(api_url, headers=headers)
    return JsonResponse(cardio.json())


def devices(request, device_id=None):
    # Your access token
    access_token = request.session.get('access_token')

    # The headers for the API request
    headers = {
        'Authorization': f'Bearer {access_token}',
    }

    if request.path == '/api/devices/':
        api_url = 'https://api.fitbit.com/1/user/-/devices.json'
    elif device_id is not None:
        api_url = 'https://api.fitbit.com/1/user/-/devices/tracker/{device_id}/alarms.json'
    else:
        return JsonResponse({'error': 'Invalid path'}, status=400)

    # Replace this with your actual data
    devices = requests.get(api_url, headers=headers)
    return JsonResponse(devices.json())


def ecg(request):
    # Your access token
    access_token = request.session.get('access_token')

    # The headers for the API request
    headers = {
        'Authorization': f'Bearer {access_token}',
    }

    if request.path == '/api/ecg/':
        api_url = 'https://api.fitbit.com/1/user/-/ecg/list.json'
    else:
        return JsonResponse({'error': 'Invalid path'}, status=400)

    
    # Replace this with your actual data
    ecg = requests.get(api_url, headers=headers)
    return JsonResponse(ecg.json())


def friends(request):
    # Your access token
    access_token = request.session.get('access_token')

    # The headers for the API request
    headers = {
        'Authorization': f'Bearer {access_token}',
    }

    if request.path == '/api/friends/':
        api_url = 'https://api.fitbit.com/1.1/user/-/friends.json'
    else:
        return JsonResponse({'error': 'Invalid path'}, status=400)

    # Replace this with your actual data
    friends = requests.get(api_url, headers=headers)
    return JsonResponse(friends.json())


def heartrate(request, start_date=None, end_date=None):
    # Your access token
    access_token = request.session.get('access_token')

    # The headers for the API request
    headers = {
        'Authorization': f'Bearer {access_token}',
    }

    # Determine the API endpoint based on the path
    if request.path == '/api/heartrate/by_date_range/':
        if start_date and end_date:
            api_url = f'https://api.fitbit.com/1/user/-/activities/heart/date/{start_date}/{end_date}.json'
        else:
            return JsonResponse({'error': 'Both start_date and end_date are required'}, status=400)
    elif request.path == '/api/heartrate/variability_by_date/':
        if start_date:
            api_url = f'https://api.fitbit.com/1/user/-/hrv/{start_date}.json'
        else:
            return JsonResponse({'error': 'start_date is required'}, status=400)
    elif request.path == '/api/heartrate/variability_by_interval/':
        if start_date and end_date:
            api_url = f'https://api.fitbit.com/1/user/-/hrv/date/{start_date}/{end_date}/all.json'
        else:
            return JsonResponse({'error': 'Both start_date and end_date are required'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid path'}, status=400)

    heartrate = requests.get(api_url, headers=headers)
    return JsonResponse(heartrate.json())


def nutrition(request, date=None):
    # Your access token
    access_token = request.session.get('access_token')

    # The headers for the API request
    headers = {
        'Authorization': f'Bearer {access_token}',
    }

    if request.path == '/api/nutrition/summary/':
        if date:
            api_url = 'https://api.fitbit.com/1/user/-/foods/log/date/{date}.json'
        else:
            return JsonResponse({'error': 'date is required'}, status=400)
    elif request.path == '/api/nutrition/recent_food/':
        api_url = 'https://api.fitbit.com/1/user/-/foods/log/recent.json'
    elif request.path == '/api/nutrition/water_log/':
        if date:
            api_url = f'https://api.fitbit.com/1/user/-/foods/log/water/date/{date}.json'
        else:
            return JsonResponse({'error': 'date is required'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid path'}, status=400)
    


    # Replace this with your actual data
    nutrition = requests.get(api_url, headers=headers)
    return JsonResponse(nutrition.json())


def oxygen(request, start_date=None, end_date=None):
    # Your access token
    access_token = request.session.get('access_token')

    # The headers for the API request
    headers = {
        'Authorization': f'Bearer {access_token}',
    }
    # Replace this with your actual data

    if request.path == '/api/oxygen/summary_by_interval/':
        if start_date and end_date:
            api_url = f'https://api.fitbit.com/1/user/-/spo2/date/{start_date}/{end_date}.json'
        else:
            return JsonResponse({'error': 'Both start_date and end_date are required'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid path'}, status=400)

    oxygen = requests.get(api_url, headers=headers)
    return JsonResponse(oxygen.json())

def sleep(request, start_date:None, end_date:None):
    # Your access token
    access_token = request.session.get('access_token')

    # The headers for the API request
    headers = {
        'Authorization': f'Bearer {access_token}',
    }

    if request.path == '/api/sleep/log_by_interval/':
        if start_date and end_date:
            api_url = f'https://api.fitbit.com/1.2/user/-/sleep/date/{start_date}/{end_date}.json'
        else:
            return JsonResponse({'error': 'Both start_date and end_date are required'}, status=400)
    elif request.path == '/api/sleep/log_list/':
        api_url = f'https://api.fitbit.com/1.2/user/-/sleep/list.json'
    else:
        return JsonResponse({'error': 'Invalid path'}, status=400)

    # Replace this with your actual data
    sleep = requests.get(api_url, headers=headers)
    return JsonResponse(sleep.json())

def temperature(request, start_date:None, end_date:None):
    # Your access token
    access_token = request.session.get('access_token')

    # The headers for the API request
    headers = {
        'Authorization': f'Bearer {access_token}',
    }

    if request.path == '/api/temperature/core_by_interval/':
        if start_date and end_date:
            api_url = f'https://api.fitbit.com/1/user/-/temp/core/date/{start_date}/{end_date}.json'
        else:
            return JsonResponse({'error': 'Both start_date and end_date are required'}, status=400)
    elif request.path == '/api/temperature/skin_by_interval/':
        if start_date and end_date:
            api_url = f'https://api.fitbit.com/1/user/-/temp/skin/date/{start_date}/{end_date}.json'
        else:
            return JsonResponse({'error': 'Both start_date and end_date are required'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid path'}, status=400)
    

    # Replace this with your actual data
    temperature = requests.get(api_url, headers=headers)
    return JsonResponse(temperature.json())

