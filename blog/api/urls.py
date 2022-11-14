from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views
from django.contrib import admin
from django.urls import path
from core.views import front

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", front, name="front"),
]

urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('posts/', views.PostList.as_view()),
    path('posts/<int:pk>/', views.PostDetail.as_view()),
    path('categories/', views.CategoryList.as_view()),
    path('categories/<int:pk>/', views.CategoryDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
