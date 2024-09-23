from rest_framework.views import APIView #用來創建APIview結構 可以自定義各種request狀態 做複雜的邏輯操做
from rest_framework.response import Response #用來返回request 狀態 
from rest_framework import status,filters,viewsets #status用來創建狀態 返回給開發者是哪種錯誤,viewset 用來創建viewset 的格式可以快速使用crud操作,filters提供過濾功能與搜尋功能
from rest_framework.authentication import TokenAuthentication #處理基於 token 的身份驗證。
from api_profile import serializers,models,permissions #導入我得app 裡面的這三個文件 分別序列化資料把資料轉成json格式 或從json 格式轉為model結構 ,以及自定義權限
from rest_framework.authtoken.views import ObtainAuthToken #提供一個用來獲取 token 的 API 端點。
from rest_framework.settings import api_settings #用來訪問和修改 DRF 的全局配置。
from rest_framework.permissions import IsAuthenticatedOrReadOnly #限制未登錄用戶只能進行讀取操作


class HelloApiView(APIView):                        #APIView
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



class HelloViewset(viewsets.ViewSet):               #ViewSet
    """Test API ViewSet"""
    serializer_class=serializers.HelloSerializer

    def list(self,request):#列印出所有object get method 
        """Return hello message"""
        a_viewset=[
        "Uses action (list,create,retrieve,update,partial_update,destory)",
        "Automatically map to URLs using Routers",
        "Provides more funtionality with less code"
        ]
        return Response({'message':'hello ViewSets','a_viewset':a_viewset})

    def create(self,request):#post method 
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

    def retrieve(self,request,pk=None):#查看單一object 為get method 
        """Handel getting an object by its id"""
        return Response({'http_method':'GET'})

    def update(self,request,pk=None): #完全更新一個object put method 
        """Handle updatring an object"""
        return Response({'http_method':'PUT'})

    def partial_update(self,request,pk=None):# 部分更新 對應到 patch method
        """Handel updating part of an object"""
        return Response({'http_method':'PATCH'})

    def destroy(self,request,pk=None):# 對應http delete method
        
        """Handel removing an objec t"""
        return Response({'http_method':'DELETE'})

class UserProfileViewSet(viewsets.ModelViewSet):    #ModelViewSet
    """Handel creating  and updating profile"""
    serializer_class=serializers.UserProfileSerializer
    queryset=models.UserProfile.objects.all()
    authentication_classes=(TokenAuthentication,)
    permission_classes=(permissions.UpdateOwnProfile,)
    filter_backends=(filters.SearchFilter,)
    search_fields=('name','email')

class UserProfileFeedViewSet(viewsets.ModelViewSet): ##ModelViewSet
    """Handles creating,reading and updating profile feed items"""
    authentication_classes=(TokenAuthentication,)
    serializer_class=serializers.ProfileFeedItemSerializer
    queryset=models.ProfileFeedItem.objects.all()
    permissions_classes=(
    permissions.UpdateOwnStatus, #自定義的權限控制
    IsAuthenticatedOrReadOnly #此為內建的權限控制
    )
    def perform_create(self,serializer):
        """Sets the user profile to the logged in user"""
        serializer.save(user_profile=self.request.user)

class UserLoginAPIView(ObtainAuthToken):#使登入時會產生一個Token 之後會用這個Token驗證身分
    """Handel creating user authentication tokens"""
    renderer_classes=api_settings.DEFAULT_RENDERER_CLASSES  #把Token轉換成Json格式讓Server讀取




