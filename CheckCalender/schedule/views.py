from django.shortcuts import render
from django.db.models import Q
from grouplist.models import Groups

def schedulelist(request,group_id):
    group = Groups.objects.get(Q(id =group_id))
    return render(request, 'index.html', {'group': group})

