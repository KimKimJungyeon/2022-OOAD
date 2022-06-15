from django.shortcuts import render
from django.db.models import Q
from grouplist.models import Groups
from rest_framework import viewsets,status
from rest_framework.response import Response
from schedule.models import Schedule
from schedule.serializer import ScheduleSerializer
from django.core.paginator import Paginator
from django.urls import reverse
from django.http import HttpResponseRedirect
from grouplist.serializer import GroupSerializer

class ScheduleView(viewsets.ViewSet):

    def update_group_info(self,request,group_id):
        group = Groups.objects.get(Q(id = group_id))
        group_data = {
            "name" : request.data["name"],
            "memo" : request.data["memo"],
            "passward" : request.data["passward"],
        }
        serializer = GroupSerializer(group, data=group_data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        
        return HttpResponseRedirect(reverse('group_info', args=[group_id]))

    def redirect_schedule_update(self,request,group_id):
        group = Groups.objects.get(id=group_id)
        return render(request, 'schedule_write.html', {'group': group})

    def schedule_list(self, request,group_id):
        group = Groups.objects.get(Q(id=group_id))
        schedule = Schedule.objects.filter(Q(group=group_id)).order_by("id")

        paginator = Paginator(schedule, 10)
        page = int(request.GET.get('page', 1))
        queryset = paginator.get_page(page)
        print(queryset)
        serializer = ScheduleSerializer(queryset, many=True)

        return render(request, 'schedule_list.html', {'group': group, 'schedule_list':serializer.data})

    def schedule_update(self, request,group_id):
        schedule_data = {
            "group" : group_id,
            "date" : request.data["date"],
            "memo" : request.data["memo"],
        }
        serializer = ScheduleSerializer(data=schedule_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return HttpResponseRedirect(reverse('schedule_list', args=[group_id]))
    
    def group_info(self, request,group_id):
        queryset = Groups.objects.get(Q(id=group_id))
        serializer= GroupSerializer(queryset)
        print(serializer.data)
        return render(request, 'schedule_info.html', serializer.data)

    def group_redirect(self, request,group_id):
        queryset = Groups.objects.get(Q(id =group_id))
        response = {
            "group":{
                "id" : queryset.id,
                "name" : queryset.name,
                "memo" : queryset.memo,
            }
        }
        return render(request, 'schedule.html', response)

    def group_schedule(self, request,group_id):
        queryset = Groups.objects.get(Q(id =group_id))
        _schedule = Schedule.objects.filter(Q(group=group_id))
        rsp = {
            "group":{
                "id" : queryset.id,
                "name" : queryset.name,
                "memo" : queryset.memo,
            },
            "schedule":{}
        }
        if not _schedule:
            rsp["schedule"]["boolean"]= False
        else :
            schedule_list = []
            for item in _schedule:
                temp ={
                    "year": item.date.year,
                    "month" : item.date.month,
                    "day" : item.date.day,
                }
                schedule_list.append(temp)
            rsp["schedule"]["boolean"]= True
            rsp["schedule"]["results"] = schedule_list
        return Response(rsp,status=status.HTTP_200_OK)
