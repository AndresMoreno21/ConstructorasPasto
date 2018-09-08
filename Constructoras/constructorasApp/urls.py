from django.contrib import admin
from django.urls import path
from constructorasApp import views


urlpatterns = [
	
    path('',views.constructoras_base,name='constructoras-lista'),
    path('edificios/<int:id>/',views.edificos_detail,name='edificios-lista'),
    path('apartamentos/<int:pk>/',views.apartamentos_detail,name='apartamentos-lista'),
    path('fotos/<int:pk>/',views.carrete_detail,name='fotos-lista'),

]