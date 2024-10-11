from rest_framework import serializers
from myapp.models import Person



class PersonSerializer(serializers.ModelSerializer):
  class Meta:
    model = Person
    fields = '__all__'
  
  def validate(self, attr):
    special_characters = "!@#$%^&*()-+?_=,<>/"

    if any(c in special_characters for c in attr['name']):
      raise serializers.ValidationError("Name Should not have special characters")
    
    if attr['age'] < 18 :
      raise serializers.ValidationError("Age Should be above 18")
    
    return attr