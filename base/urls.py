from django.urls import path
from . import views



urlpatterns = [
   path('index/', views.index, name="index"),
   path('create/', views.create, name="create"),
   path('login/', views.login_user, name="login"),
   path('logout/', views.logout_user, name="logout"),
   path('blogs/', views.blog, name="blogs"),
   path('blogs/<str:pk>', views.single, name="single"),
   path('profile/<str:pk>', views.profile, name="profile"),
   path('create-blog/', views.create_blog, name='create-blog'),
   path('delete-blog/<str:pk>', views.delete_blog, name='delete'),
   path('update-blog/<str:pk>', views.delete_blog, name='update'),
]
