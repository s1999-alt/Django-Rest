from django.urls import path,include
from myapp import views
from myapp.views import PersonViewSet
from rest_framework.routers import DefaultRouter

#router for ViewSets
router = DefaultRouter()
router.register(r'person',PersonViewSet,basename='person')
urlpatterns = router.urls




urlpatterns = [
    path('',include(router.urls)),
    path('index/',views.index,name='index'),
    path('person/',views.Persondetail,name='person'),
    path('personapi/',views.PersonView.as_view(),name='personapi'),
    path('register/',views.RegisterApi.as_view(),name='register')
]
