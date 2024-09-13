from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    def get(self,request,format=None):
        """Retutrn a list of APIView features"""
        an_apiview=[
            'Uses HTTP methods as funtion(get,post,put,patch,delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over you application logic',
            'Is mapped manually to URLs'
        ]
        return Response({'message':'hello!','an_apiview':an_apiview})