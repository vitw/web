from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
	path('',views.blog,name = 'blog'),
	path('<int:article_id>/',views.detail,name = 'detail'),
	path('<int:article_id>/leave_comment',views.leave_comment,name = 'leave_comment'),
	path('register',views.register, name = 'register'),
	path('logout', views.logout_request,name = 'logout_request'),
	path('login',views.login_request,name = 'login_request'),
]
