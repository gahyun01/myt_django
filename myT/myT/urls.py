from django.urls import path
from . import views
from myT.views import logout_view
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),  # 기본 경로로 views.index 뷰를 처리
]

# 로그인 및 로그아웃 URL
urlpatterns += [
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', logout_view, name='logout'),
]

# post
urlpatterns += [
    path('planner/', views.Planner, name='planner'),
]
