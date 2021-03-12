from django.urls import path
from .views import mycurd_list, mycurdDetails, mycurdCreate, curdUpdate, curdDelete


app_name='mycurd'

urlpatterns=[
    path('', mycurd_list),
    path('create/', mycurdCreate),
    path('<id>/', mycurdDetails),
    path('<id>/update/', curdUpdate),
    path('<id>/delete/', curdDelete),
]
