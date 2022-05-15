from django.contrib import admin
from django.urls import path
from grouplist.views import GroupListView,detail,password
from schedule.views import schedulelist

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', GroupListView.as_view({'get': 'list'}), name= "index"),
    path('write/', GroupListView.as_view({'get': 'write'}), name = "write"),
    path('update/', GroupListView.as_view({'post': 'update'}), name = 'update'),
    path('password/<int:group_id>/', detail, name= "detail"),
    path('passwordcheck/<int:group_id>/', password, name= "password"),
    path('group/<int:group_id>/', schedulelist, name='group'),
]
