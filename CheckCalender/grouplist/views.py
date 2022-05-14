from django.shortcuts import render
from django.db.models import Q
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from grouplist.models import Groups
from grouplist.serializer import GroupSerializer

class GroupListView(ModelViewSet):
    queryset = Groups.objects.all()
    serializer_class = GroupSerializer

    def list(self,request):
        queryset = Groups.objects.all()
        serializer = self.get_serializer(queryset,many=True)
        return Response(serializer.data,status=200)

    def update(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request):
        group_id = self.request.GET.get('id')
        group_password = self.request.GET.get('password')

        queryset = Groups.objects.filter(Q(id=group_id)&Q(password=group_password))
        if queryset:
            queryset.delete() 
            data = {
                'delete' : '모임이 정상 삭제 되었습니다.'
            }
        return Response(data, status=status.HTTP_204_NO_CONTENT)

