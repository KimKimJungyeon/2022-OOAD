from django.shortcuts import render
from django.db.models import Q
from rest_framework.viewsets import ModelViewSet
from grouplist.models import Groups

# Create your views here.
def schedulelist(request,group_id):
    group = Groups.objects.get(Q(id =group_id))
    return render(request, 'index.html', {'group': group})

