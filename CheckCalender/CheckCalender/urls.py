from django.contrib import admin
from django.urls import path, include
from schedule.views import ScheduleView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('grouplist.urls')),
    path('group/', include('schedule.urls')),
]
