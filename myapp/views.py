from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Person
from .serializers import PersonSerializer


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
    datas = request.data
    serializer = PersonSerializer(data=datas)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.error_messages)
  
  elif request.method == 'PUT':
    data = request.data
    obj = Person.objects.get(id = data['id'] )
    serializer = PersonSerializer(obj,data=data, partial=False)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.error_messages)
  
  elif request.method == 'PATCH':
    data = request.data
    obj = Person.objects.get(id=data['id'])
    serializer = PersonSerializer(obj,data=data, partial=True)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.error_messages)
  
  else:
    data = request.data
    obj = Person.objects.get(id = data['id'])
    obj.delete()
    return Response('Person details deleted')