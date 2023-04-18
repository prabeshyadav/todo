from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('updatetask/<str:pk>/',views.update_task,name='update')
    
]
