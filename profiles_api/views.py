from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status 
from rest_framework import filters
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication 
from rest_framework.authtoken.views import  ObtainAuthToken
from rest_framework.settings import  api_settings
from rest_framework.permissions import  IsAuthenticated
from profiles_api import serializers
from profiles_api import models
from profiles_api import permission


class HelloApiView(APIView):

    """Teste API VIEW"""

    serializers_class = serializers.HelloSerializer

    def get(self, request, fromat=None):

        """Retourne une liste de APIVIEW """

        an_apiview=[

            'Users HTTP methods as function (get, post, patch , put, delete)',
            'Est similaire au vue traditionnel de Django',
            'Donnes le plus de controle ',
            'Est mappé manuellement au URLs',
            
        ]
        
        return Response({'message':'Hello!', 'an_apiview':an_apiview})


    def post(self, request):

        """Crée un message avec un nom """

        serializers = self.serializers_class(data=request.data)

        if  serializers.is_valid():

            name = serializers.validated_data.get('name')

            message = f'Hello {name}'
            return Response({'message': message})
        else :
            return Response(serializers.errors, 
            status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk=None):
        """Teste PUT"""

        return Response({'method':'PUT'})

    def patch(self, request, pk=None):
        """Teste patch"""

        return Response({'message':'PATCH'})
    def delete(self, request, pk=None):

        return Response({'message':'Delete'})   
    

class HelloViewSet(viewsets.ViewSet):

    """Teste API ViewSet"""

    serializers_class = serializers.serializers

    def lsit(self, request):
        """renvoi un Hello message"""

        a_viewset = [
            'Utilise les actions (list, creat, retrieve, update, partial_update)',
            'Automatically maps to URLs using Touters', 
            'Bla bla bla'
        ]

        return Response({'message':'Hello!', 'a_viewset':a_viewset})


    def create(self,request):
        """ Create """

        serializers = self.serializers_class(data=request.data)

        if serializers.is_valid():

            name = serializers.validated_data.get('name')
            message = f'Hello {name}'

            return Response({'message':message})
        else:
            return Response(serializers.errors, 
            status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk=None):
        """Récuperer un objet via l'ID"""

        return Response({'http_method': 'GET'})
    
    def update(self, request):
        """Update un objet"""
        return Response({'message': 'PUT'})
    
    def partial_update(self, request):
        """ Update partiel"""
        return Response({'http_method':'PATCH'})
    def destroy(self, request):
        """Delete un objet"""

        return Response({'htt_method':'Delete'})

class UserProfileViewSet(viewsets.ModelViewSet):
    """Teste   """

    serializers_class = serializers.ProfileUserSerialzer
    queryset= models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes= (permission.UpdateOwnProfile,)
    filter_backend = (filters.SearchFilter,)
    search_filter = ('name', 'email')

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return serializers.ProfileUserSerialzer
        return serializers.ProfileUserSerialzer 

class UserLoginApiView(ObtainAuthToken):
    """ Crée un Token """

    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """" ~~~~~~ """
    authentication_classes = (TokenAuthentication,)
    seriale_class = serializers.ProfileFeedSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes =(
        permission.UpdateOwnStatus,
        IsAuthenticated
    )
 
    def perform_create(self, serializer):
        """ gggggggggg """

        serializer.save(user_profile=self.request.user)
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return serializers.ProfileFeedSerializer
        return serializers.ProfileFeedSerializer 


