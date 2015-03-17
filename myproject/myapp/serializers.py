from django.contrib.auth.models import User, Group
from myapp.models import gmailContacts 
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class MyappSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = gmailContacts
        fields = ('user', 'contacts')
