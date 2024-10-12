from rest_framework import serializers
from myapp.models import Person,Team



class TeamSerializer(serializers.ModelSerializer):
  class Meta:
    model = Team
    fields = ['team_name']


class PersonSerializer(serializers.ModelSerializer):
  team = TeamSerializer()
  team_info = serializers.SerializerMethodField()
  class Meta:
    model = Person
    fields = '__all__'
  
  def get_team_info(self, obj):
    return "extra field"
  
  def validate(self, attr):
    special_characters = "!@#$%^&*()-+?_=,<>/"

    if any(c in special_characters for c in attr['name']):
      raise serializers.ValidationError("Name Should not have special characters")
    
    if attr['age'] < 18 :
      raise serializers.ValidationError("Age Should be above 18")
    
    return attr