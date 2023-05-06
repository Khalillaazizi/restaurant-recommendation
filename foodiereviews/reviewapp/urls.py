from django.urls import path

from . import views

app_name = 'reviewapp'
urlpatterns = [
    
    path('', views.inde, name= 'inde'),
    path('index/', views.index, name= 'index'),
    
    path('addnew/',views.addnew, name='addnew'),
    
    path('signup', views.handleSignup, name='handleSignup'),
    
    
    
    path('home/', views.home, name='home'),
    
    
    path('resto/<int:restaurant_id>/', views.details, name='details'),
    
    path('delete/<int:id>', views.destroy, name='destroyer'),
    
    path('resto/<int:restaurant_id>/add/', views.add, name='add'),

   
    path('resto/<int:restaurant_id>/reviewed/', views.reviewed, name='reviewed'),

   
    path('api/comment/add/', views.CommentAdd.as_view(), name="comment"),
    

    path('api/reply/add/', views.ReplyAdd.as_view(), name="reply"),


    path('api/like/add/', views.LikeAdd.as_view(), name="like"),

    path('api/restaurants/list/', views.GetRestaurantsByCategory.as_view(), name="restaurants_by_category"),
    
]