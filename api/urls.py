from django.urls import path
from myapp import views


urlpatterns = [
    path('index/',views.index,name='index'),
    path('person/',views.Persondetail,name='person')
]
