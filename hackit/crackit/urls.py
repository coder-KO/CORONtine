from django.urls import path
from . import views


urlpatterns = [

   path('',views.Index,name="index_page"),
<<<<<<< HEAD
   path('image',views.take_images,name="take_images"),
=======
   path('image',views.take_images,name="images"),
   path('detect',views.Detect,name="detection"),
>>>>>>> cadcd62876fbf2edca9d724c79c21df4be2cea2e

]
