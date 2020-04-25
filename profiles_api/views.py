from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status 
from profiles_api import serializers



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



