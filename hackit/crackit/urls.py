from django.urls import path
from . import views


urlpatterns = [

   path('',views.Index,name='index_page'),
   path('image',views.take_images,name="images"),
   path('detect',views.Detect,name="detection"),
   path('chest_scan',views.chest_scan,name='chest_scan'),
   # path('random',views.random,name='random'),

]
