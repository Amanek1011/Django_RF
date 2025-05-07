from django.contrib import admin

from apps.tester.models import *


admin.site.register(Test)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(UserTest)

