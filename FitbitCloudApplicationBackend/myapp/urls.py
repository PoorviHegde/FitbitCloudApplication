from django.urls import path
from . import views

urlpatterns = [
    path('api/activity/log/', views.activity, name='activity_log'),
    # path('api/activity/lap_location', views.activity, name='activity_lap_location'),
    path('api/activity/type/<str:activity_type>/', views.activity, name='activity_by_type'),
    path('api/activity/date/<str:date>/', views.activity, name='activity_summary_by_date'),
    path('api/activity/frequent_activities/', views.activity, name='activity_frequent_activities'),
    path('api/activity/recent_activity/', views.activity, name='activity_recent_activity'),

    path('api/body/goal/', views.body, name='body_goal'),
    path('api/body/fat/', views.body, name='body_fat'),
    path('api/body/weight/', views.body, name='body_weight'),

    path('api/breathing/date_range/<str:start_date>/<str:end_date>/',  views.breathing, name='breathing_by_date_range'),

    path('api/cardio_fitness_score/date_range/<str:start_date>/<str:end_date>/date_range/', views.cardio, name='cardio_fitness_score_by_date_range'),

    path('api/devices/alarms/<str:device_id>/', views.devices, name='devices_alarms_list'),
    path('api/devices/devices/', views.devices, name='devices_devices_list'),

    path('api/ecg/', views.ecg, name='ecg'),

    path('api/friends/', views.friends  , name='friends'),

    path('api/heartrate/by_date_range/', views.heartrate, name='heartrate_by_date_range'),
    path('api/heartrate/variability_by_date/', views.heartrate, name='heartrate_variability_by_date'),
    path('api/heartrate/variability_by_interval/', views.heartrate, name='heartrate_variability_by_interval'),

    path('api/nutrition/food_log/<str:date>', views.nutrition, name='nutrition_food_log'),
    path('api/nutrition/recent_food/', views.nutrition, name='nutrition_recent_food'),
    path('api/nutrition/water_log/', views.nutrition, name='nutrition_water_log'),

    path('api/oxygen/summary_by_interval/<str:start_date>/<str:end_date>/', views.oxygen, name='oxygen_summary_by_interval'),

    path('api/sleep/log_by_interval/<str:start_date>/<str:end_date>/', views.sleep, name='sleep_log_by_date_range'),
    path('api/sleep/log_list/', views.sleep, name='sleep_log_list'),

    path('api/temperature/core_by_interval/<str:start_date>/<str:end_date>/', views.temperature, name='temperature_core_by_interval'),
    path('api/temperature/skin_by_interval/<str:start_date>/<str:end_date>/', views.temperature, name='temperature_skin_by_range'),
]