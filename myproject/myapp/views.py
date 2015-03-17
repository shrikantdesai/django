from django.shortcuts import render_to_response
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from myapp.serializers import UserSerializer, GroupSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from myapp.models import gmailContacts
from myapp.serializers import MyappSerializer
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return render_to_response('index.html')



class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

@csrf_exempt
@api_view(['GET', 'POST'])
def contacts_list(request):
    """
    List all snippets, or create a new snippet.
    """
    if request.method == 'GET':
        gmailcontacts = gmailContacts.objects.all()
        serializer = MyappSerializer(gmailcontacts, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MyappSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
