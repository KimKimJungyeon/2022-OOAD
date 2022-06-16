from rest_framework import serializers
from grouplist.models import Groups

class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Groups
        fields= ("id", "name", "passward", "memo", "creation_date")
