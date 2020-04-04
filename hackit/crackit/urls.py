from django.urls import path
from . import views


urlpatterns = [

   path('image',views.take_images,name="images"),
   path('detect',views.Detect,name="detection"),

]
