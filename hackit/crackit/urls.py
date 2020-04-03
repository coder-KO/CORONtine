from django.urls import path
from . import views


urlpatterns = [

   path('',views.Index,name="index_page"),
   path('image',views.take_images,name="take_images"),

]
