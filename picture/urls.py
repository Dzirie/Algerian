from django.urls import path
from . import views

app_name='picture'


urlpatterns=[
path('',views.pictures,name='pictures'),
path('add/',views.add_picture,name='add'),
path('details/<int:image_id>/',views.details,name='details'),
path('<int:pk>/edit/',views.edit_picture,name='edit'),
path('<int:pk>/delete/',views.delete,name='delete'),
path('your_pictures/',views.your_pictures,name='your_pictures'),
path('search/',views.search_picture,name='search'),
]

