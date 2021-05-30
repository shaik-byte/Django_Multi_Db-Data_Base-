from django.contrib import admin
from django.urls import include, path
from .views import app1_details

# from app1.views import main1
# from app2.views import main2
from .views import app1_details
urlpatterns = [
	path('shaik/', views.app1_details,),
   
]
