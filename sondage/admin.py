from django.contrib import admin
from .models import Section, Question, Option, Response, ResponseOption

admin.site.register(Section)
admin.site.register(Question)
admin.site.register(Option)
admin.site.register(Response)
admin.site.register(ResponseOption)