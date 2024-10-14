from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Person
from .serializers import PersonSerializer, RegisterSerializer, LoginSerializer
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination

from rest_framework.views import APIView
from rest_framework import viewsets



# This is the views using api_view decorator
@api_view(['GET','POST'])
def index(request):
  if request.method == 'GET':
    person_details = {
      'name': 'siyad',
      'age': 24,
      'job': 'full stack developer'
    } 
    return Response(person_details)
  
  elif request.method == 'POST':
    return Response("This is a post")
  

@api_view(['GET','POST','PUT','PATCH','DELETE'])
def Persondetail(request):
  if request.method == 'GET':
    personobj = Person.objects.all()
    serializer = PersonSerializer(personobj, many=True)
    return Response(serializer.data)
  
  elif request.method == 'POST':
    data = request.data
    serializer = PersonSerializer(data=data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors)
  
  elif request.method == 'PUT':
    data = request.data
    obj = Person.objects.get(id = data['id'] )
    serializer = PersonSerializer(obj,data=data, partial=False)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors)
  
  elif request.method == 'PATCH':
    data = request.data
    obj = Person.objects.get(id=data['id'])
    serializer = PersonSerializer(obj,data=data, partial=True)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors)
  
  else:
    data = request.data
    obj = Person.objects.get(id = data['id'])
    obj.delete()
    return Response('Person details deleted')
  





#This is the class-based view using APIView
class PersonView(APIView):
  permission_classes = [IsAuthenticated]
  authentication_classes = [TokenAuthentication]

  def get(self, request):
    person = Person.objects.all()
    serializer = PersonSerializer(person, many=True)
    return Response(serializer.data)
  
  def post(self, request):
    return Response("This is post APIVIEW")
  

#Pagination View
class CustomPagination(PageNumberPagination):
  page_size = 2
  page_size_query_param = 'page'

#This is the class-based view using model Viewsets
class PersonViewSet(viewsets.ModelViewSet):
  permission_classes = [AllowAny]
  serializer_class = PersonSerializer
  queryset = Person.objects.all()
  pagination_class = CustomPagination


  def list(self, request):
    search = request.GET.get('search')
    queryset = self.queryset

    if search:
      queryset = queryset.filter(name__startswith= search)

    paginated_queryset = self.paginate_queryset(queryset)
    
    serializer = PersonSerializer(paginated_queryset, many=True)
    return self.get_paginated_response(serializer.data)
  

# User Registration View

class RegisterView(APIView):
  def post(self, request):
    _data = request.data
    serializer = RegisterSerializer(data = _data)

    if not serializer.is_valid():
      return Response(serializer.errors)
    serializer.save()

    return Response("user created")
  


class LoginView(APIView):
  permission_classes = [AllowAny]
  def post(self, request):
    _data = request.data
    serializer = LoginSerializer(data=_data)

    if not serializer.is_valid():
      return Response(serializer.errors)
    
    print("-------------------------",serializer.data)
    user = authenticate(username = serializer.data['username'], password = serializer.data['password'])

    if not user:
      return Response("Invalid", status=status.HTTP_404_NOT_FOUND)
    
    token, created = Token.objects.get_or_create(user=user)

    if created:
      print("New Token Created",token)
    else:
      print("Existing Token is",token)

    return Response({'message':"Login successfully", 'token': str(token)})

    

