from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . import serializers

# Create your views here.

class HelloApiView(APIView):
    """Testing API View."""

    # lets framework know to use this serializer for this class
    serializer_class = serializers.HelloSerializers

    def get(self, request, format=None):
        """Return a list of APIView features."""

        an_apiview = [
            'Uses HTTP methods as functions (get, post, patch, put, delete)',
            'It is similar to a traditional django view',
            'Gives you the most control over your logic',
            'It is mapped manually to URLs'
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})

    def post(self, request):
        """Create a hello message with our name."""

        # pass in the request data
        serializer = serializers.HelloSerializers(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handles updating an object."""

        return Response({'method': 'put'})

    def delete(self, request, pk=None):
        """Deletes an object."""
        return Response({'method': 'delete'})

    def patch(self, request, pk=None):
        """Patch request, only updates fields provided in the request."""
        return Response({'method': 'patch'})
