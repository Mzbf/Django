from rest_framework import serializers 


class HelloSerializer(serializers.Serializer):

    """ Serializers """


    name = serializers.CharField(max_length=10)

