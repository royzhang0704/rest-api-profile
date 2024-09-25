from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin,BaseUserManager
from django.conf import settings

class UserProfileManager(BaseUserManager): #自定義一個用戶管理器 處理如何創建一個超級用戶及普通用戶
    """Manager for user profiles"""
    def create_user(self,email,name,password=None):#normal user
        if not email: #沒輸入email直接給你一個報錯
            raise ValueError("User must have an email address")
        email=self.normalize_email(email) #把email 正規化 例如大寫字母轉小寫  normalize_email 為Baseusermanager 得內建工具
        user=self.model(email=email,name=name) #會把我們當前管理的model調出來引用 並把輸入的email,name設為model的值

        user.set_password(password) #把輸入的password 加密保存 
        user.save(using=self._db) #把用戶保存到資料庫裡面

        return user

    def create_superuser(self,email,name,password):#建立用戶的方法建立在普用戶上 之後在透過is_staff and is_superuser 標記此用戶 
        """Create and save a new superuser with given details"""
        user=self.create_user(email,name,password)
        user.is_superuser=True
        user.is_staff=True
        user.save(using=self._db) #修改了兩個參數 要在重新保存update

        return user

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for user in the system"""
    email=models.EmailField(max_length=255,unique=True)
    name=models.CharField(max_length=255)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)

    objects=UserProfileManager() ## 告訴 Django 這個模型應該使用自定義的 UserProfileManager

    USERNAME_FIELD = 'email' #指定用 email 作為用戶的唯一識別字段（而不是 Django 默認的 username）。
    REQUIRED_FIELDS=['name'] # 除了 `USERNAME_FIELD`（即 `email`）之外，創建用戶時必須提供的字段。這裡強制要求用戶在創建時提供 `name`。

    def get_full_name(self):
        """Retrieve full name of user"""
        return self.name
    def get_short_name(self):
        """Retrieve short name of user"""
        return self.name

    def __str__(self):
        """Return  string representation of our user"""
        return self.email

class ProfileFeedItem(models.Model):
    """Profile status update"""
    user_profile=models.ForeignKey(
    settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE #若關聯的user被刪除 那麼資料庫裡面他的分布內容也要一起被刪除
    )
    status_text=models.CharField(max_length=255)
    created_on=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.status_text
