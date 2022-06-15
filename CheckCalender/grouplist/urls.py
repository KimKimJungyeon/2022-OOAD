
from django.urls import path
from grouplist.views import GroupListView,detail,password


urlpatterns= [
    path('home/', GroupListView.as_view({'get': 'list'}), name= "index"),
    path('write/', GroupListView.as_view({'get': 'write'}), name = "write"),
    path('update/', GroupListView.as_view({'post': 'update'}), name = 'update'),
    path('password/<int:group_id>/', detail, name= "detail"),
    path('passwordcheck/<int:group_id>/', password, name= "password"),
]