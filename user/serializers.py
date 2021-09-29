from rest_framework import serializers
from .models import users, projects, lists, cards

class userserializer(serializers.ModelSerializer):
    class Meta:
        model = users
        fields = ('Username', 'Usertype')
    
class projectserializer(serializers.ModelSerializer):
    class Meta:
        model = projects
        fields = ('Title', 'Description', 'Status', 'Duedate', 'Member')

class listserializer(serializers.ModelSerializer):
    class Meta:
        model = lists
        fields = ('Name', 'Under_Project')

class cardserializer(serializers.ModelSerializer):
    class Meta:
        model = cards
        fields = ('Name', 'Description', 'Status', 'Duedate', 'Under_Project', 'Under_List')

