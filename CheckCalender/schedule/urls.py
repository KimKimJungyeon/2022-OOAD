from django.urls import path
from schedule.views import ScheduleView

urlpatterns= [
    path('<int:group_id>/', ScheduleView.as_view({'get': 'group_redirect', 'put':'schedule_list'}), name='group'),
    path('<int:group_id>/scheduleList/', ScheduleView.as_view({'get': 'schedule_list'}), name= 'schedule_list'),
    path('<int:group_id>/info/', ScheduleView.as_view({'get': 'group_info','post': 'update_group_info'}), name= 'group_info'),
    path('<int:group_id>/schedule/', ScheduleView.as_view({'get': 'group_schedule'}), name='group_schedule'),
    path('<int:group_id>/scheduleList/update/', ScheduleView.as_view({'get': 'redirect_schedule_update', 'post': 'schedule_update'}), name='group_schedule_update'),
]