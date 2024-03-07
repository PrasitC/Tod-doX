# from django.contrib import admin
# from django.urls import path,include
# from . import views
# urlpatterns = [
#  path('', views.tasklist, name= "task-list"),
#  path('task-detail/<str:pk>/', views.taskdetail, name="task-Detail"),
#  path('task-update/<str:pk>/', views.taskupdate, name="task-update"),
#  path('task-add/', views.taskcreate , name="task-add" ),
#  path('task-delete/<str:pk>/', views.taskdelete , name="task-delete"),
# ]




from django.contrib import admin
from django.urls import path, include, re_path
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('todo', views.ToDoViewSets, basename='todo')

urlpatterns = [
    # home page route
    re_path(r'^$',views.index, name='home'),

    # route todo query api
    path('api/', include(router.urls)),

    # user registration api route
    path('register/', views.RegisterUserView.as_view()),

    # user login api route
    path('login/', views.LoginUserView.as_view()),

    # user logout api route
    path('logout/', views.logOutUser),

]