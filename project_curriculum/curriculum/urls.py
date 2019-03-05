from django.urls import path
from django.contrib.auth import views as auth_views
from .views import curriculum_list
from .views import home,my_logout
from .views import curriculum_update,curriculum_delete,user_login
from .views import register,curriculum_new

urlpatterns = [
    path('',home,name='home'),
    path('register/', register,name='curriculum_register'),
    path('new/', curriculum_new,name='curriculum_new'),
    # path('user_login/$',user_login,name='user_login'),
    path('logout/',my_logout,name='logout'),
    path('list/',curriculum_list,name='curriculum_list'),
    path('update/<int:id>/',curriculum_update,name='curriculum_update'),
    path('delete/<int:id>/',curriculum_delete,name='curriculum_delete'),
]