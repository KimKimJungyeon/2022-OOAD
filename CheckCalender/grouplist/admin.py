from django.contrib import admin
from grouplist.models import Groups
from schedule.models import Schedule

admin.site.register(Groups)
admin.site.register(Schedule)
