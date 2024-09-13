from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from api_profile import serializers
class HelloApiView(APIView):

    serializer_class=serializers.HelloSerializer
    def get(self,request,format=None):
        """Retutrn a list of APIView features"""
        an_apiview=[
            'Uses HTTP methods as funtion(get,post,put,patch,delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over you application logic',
            'Is mapped manually to URLs'
        ]
        return Response({'message':'hello!','an_apiview':an_apiview})
    

    def post(self,request):
        """Create a hello message with our name"""
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f"hello {name}"
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
        
    def put(self,request,pk=None):
        """Handle updating an object"""
        return Response({'method':'PUT'})
    
    def patch(self,request,pk=None):
        """Handle  a partial update of an object"""
        return Response({'method':'PATCH'})
    def delete(self,request,pk=None):
        """Delete an object"""
        return Response({'method':'DELETE'})