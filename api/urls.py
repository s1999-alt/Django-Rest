from django.urls import path
from myapp import views


urlpatterns = [
    path('index/',views.index,name='index'),
    path('person/',views.Persondetail,name='person'),
    path('personapi/',views.PersonView.as_view(),name='personapi')
]
