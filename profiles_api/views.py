from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers

class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer
    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your application logic',
            'Is mapped mannualy to URLs',
        ]

        return Response({'message': 'Hello','an_apiview': an_apiview})

    def post(self, request):
        """Create a hello message with your name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors,  # By defualt the Response() return a http:200 ok request. Since this is error, we need to change it to http:400 bad request
                            status = status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):  #Used to update an object. PK is used to identify the row/object we need to update. Kinda like databases
        """Handle updating an object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):  #Used to update only certian specified fields not the entire object
        """Handle a partial update on an object"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Delete and object"""
        return Response({'method': 'DELETE'})
