from django.db import models

class Groups(models.Model):
    #모임 구조 - 모임 이름, 모임 번호, 모임 비밀번호, 모임 기타 정보, 생성일자
    id = models.BigAutoField(
        primary_key= True
    )
    name = models.CharField(
        max_length=50,
    )
    passward = models.CharField(
        max_length=50,
    )
    memo = models.CharField(
        blank=True,
        max_length=300
    )
    creation_date = models.DateTimeField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = "group"

