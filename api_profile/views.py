from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from api_profile import serializers,models,permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
class HelloApiView(APIView):
    """Test APIView"""
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



class HelloViewset(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class=serializers.HelloSerializer

    def list(self,request):
        """Return hello message"""
        a_viewset=[
        "Uses action (list,create,retrieve,update,partial_update)",
        "Automatically map to URLs using Routers",
        "Provides more funtionality with less code"
        ]
        return Response({'message':'hello ViewSets','a_viewset':a_viewset})

    def create(self,request):
        """Create new message"""
        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f"hello {name}!~"
            return Response({'message':message})
        else:
            return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self,request,pk=None):
        """Handel getting an object by its id"""
        return Response({'http_method':'GET'})

    def update(self,request,pk=None):
        """Handle updatring an object"""
        return Response({'http_method':'PUT'})

    def partial_update(self,request,pk=None):
        """Handel updating part of an object"""
        return Response({'http_method':'PATCH'})

    def destroy(self,request,pk=None):
        """Handel removing an object"""
        return Response({'http_method':'DELETE'})

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handel creating  and updating profile"""
    serializer_class=serializers.UserProfileSerializer
    queryset=models.UserProfile.objects.all()
    authentication_classes=(TokenAuthentication,)
    permission_classes=(permissions.UpdateOwnProfile,)
    filter_backends=(filters.SearchFilter,)
    search_fields=('name','email')


class UserLoginAPIView(ObtainAuthToken):
    """Handel creating user authentication tokens"""
    renderer_classes=api_settings.DEFAULT_RENDERER_CLASSES
