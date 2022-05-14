from django.db import models

class Group(models.Model):
    #모임 구조 - 모임 이름, 모임 번호, 모임 비밀번호, 모임 기타 정보, 생성일자
    id = models.BigAutoField(
        primary_key= True
    )
    name = models.CharField()
    passward = models.CharField()
    memo = models.CharField(
        null=True
    )
    creation_date = models.DateTimeField()

    class Meta:
        db_table = "group"

