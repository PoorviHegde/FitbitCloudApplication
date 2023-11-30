from django.urls import path
from . import views

urlpatterns = [
    path('get_access_token/', views.get_access, name='get_access_token'),

    path('api/activity/log/', views.activity_log, name='activity_log'),
    # path('api/activity/lap_location', views.activity, name='activity_lap_location'),
    # path('api/activity/type/<str:activity_type>/', views.activities_type, name='activity_by_type'),
    path('api/activity/summary/<str:date>/', views.activities_summary, name='activity_summary_by_date'),
    path('api/activity/frequent_activities/', views.activities_frequent, name='activity_frequent'),
    path('api/activity/recent_activity/', views.activities_recent, name='activity_recent_activity'),

    path('api/body/goal/', views.body_goal, name='body_goal'),
    path('api/body/fat/date/<str:date>/', views.body_fat, name='body_fat'),
    path('api/body/weight/date/<str:date>/', views.body_weight, name='body_weight'),

    path('api/breathing/date_range/<str:start_date>/<str:end_date>/',  views.breathing, name='breathing_by_date_range'),

    path('api/cardio_fitness_score/date_range/<str:start_date>/<str:end_date>/', views.cardio, name='cardio_fitness_score_by_date_range'),

   
    path('api/devices/list/', views.devices, name='devices_devices_list'),
    path('api/devices/tracker/2470017778/', views.alarms, name='devices_alarms_list'),

    path('api/ecg/', views.ecg, name='ecg'),

    path('api/friends/', views.friends  , name='friends'),

    path('api/heartrate/variability/<str:date>/', views.heartrateVariability, name='heartrate_variability_by_date'),
    path('api/heartrate/<str:start_date>/<str:end_date>/', views.heartrate, name='heartrate_by_date_range'),

    path('api/nutrition/food_log/<str:date>/', views.food, name='nutrition_food_log'),
    path('api/nutrition/recent_food/', views.recent_food, name='nutrition_recent_food'),
    path('api/nutrition/water_log/<str:date>/', views.water, name='nutrition_water_log'),

    path('api/oxygen/<str:date>/', views.oxygen, name='oxygen_summary_by_interval'),

    path('api/sleep/<str:start_date>/<str:end_date>/', views.sleep, name='sleep_log_by_date_range'),
    path('api/sleeplog/<str:date>/', views.sleeplog, name='sleep_log'),

    path('api/temperature/core/<str:start_date>/<str:end_date>/', views.temperature_core, name='temperature_core_by_interval'),
    path('api/temperature/skin/<str:start_date>/<str:end_date>/', views.temperature_skin, name='temperature_skin_by_range'),
]