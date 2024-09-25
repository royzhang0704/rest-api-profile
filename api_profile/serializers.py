from rest_framework import serializers #導入rest_framework內建的序列化器
from . import models 

class HelloSerializer(serializers.Serializer):
    """Serializers a name field for testing our APIView"""
    name=serializers.CharField(max_length=10)

class UserProfileSerializer(serializers.ModelSerializer): #有指定model的serializer
    """Serializer a user profile """
    class Meta:
        model=models.UserProfile
        fields=('id','email','name','password') #序列化要處理的字段
        extra_kwargs = {'password': #字段額外要處理的行為
            {'write_only':True,#數據只有被創建或是更新得時候使用 返回數據時不會顯示密碼
        'style':{'input_type':'password'}# 讓輸入密碼時顯示為＊在前端
                }
            }
    def create(self,validated_data): #處建新用戶
        """Create and return  a new user"""
        user=models.UserProfile.objects.create_user(
        email=validated_data['email'],
        name=validated_data['name'],
        password=validated_data['password']
        )

        return user

class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """Serializer profile feed items"""
    class Meta:
        model=models.ProfileFeedItem
        fields=('id','user_profile','status_text','created_on')
        extra_kwargs = {'user_profile':{'read_only':True}}
