from django.shortcuts import render
from django.db.models import Q
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.urls import reverse
from rest_framework.viewsets import ModelViewSet
from grouplist.models import Groups
from grouplist.serializer import GroupSerializer

def detail(request, group_id):
    group = Groups.objects.get(id=group_id)
    return render(request, 'password.html', {'group_name': group.name, 'group_id': group.id, 'errors' : None})

def password(request, group_id):
    group = Groups.objects.get(Q(id=group_id))
    if request.GET['password']== group.passward:
        return HttpResponseRedirect(reverse('group', args=[group_id]))
    else:
        return HttpResponseRedirect(reverse('detail', args=[group_id]))


class GroupListView(ModelViewSet):
    queryset = Groups.objects.all()
    serializer_class = GroupSerializer

    def list(self,request):
        queryset = Groups.objects.all().order_by('-id')
        paginator = Paginator(queryset, 5)
        page = int(request.GET.get('page', 1))
        group_list = paginator.get_page(page)

        return render(request, "home.html", {'title':'모임 일정잡기', 'group_list':group_list}) 

    def write(self,request):
        return render(request, "write.html")

    def update(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return HttpResponseRedirect(reverse('index'))

    def delete(self, request):
        group_id = self.request.GET.get('id')
        group_password = self.request.GET.get('passward')

        queryset = Groups.objects.filter(Q(id=group_id)&Q(password=group_password))
        if queryset:
            queryset.delete() 
        return HttpResponseRedirect(reverse('index'))

