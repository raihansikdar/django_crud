from django.urls import path
from .views import *


urlpatterns = [
    path('test/',test,name= 'test'),
    path('api/person/',person_details,name= 'person_details'),
    path('person/<int:pk>/',person_details_update,name= 'person_details_update'),
]