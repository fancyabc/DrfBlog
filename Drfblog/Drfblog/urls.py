"""Drfblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from article.views import article, category, tag, avatar, user_info
from comment.views import CommentViewSet


router = DefaultRouter()
router.register(r'article', viewset=article.ArticleViewSet)
router.register(r'category', viewset=category.CategoryViewSet)
router.register(r'tag', viewset=tag.TagViewSet)
router.register(r'avatar', viewset=avatar.AvatarViewSet)
router.register(r'comment', viewset=CommentViewSet)
router.register(r'user', viewset=user_info.UserViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),  # 可视化接口

    path('api/', include(router.urls)),    # drf 默认路由器自动注册

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
