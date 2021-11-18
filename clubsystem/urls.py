from django.urls import path	

from . import views

urlpatterns = [

	path('', views.index, name='index'),
	path('photo/<str:pk>', views.viewPhoto, name='photo'),
	path('record/', views.recordnow, name='record'),
	path('add/', views.addPhoto, name='add'),
	
]