from django.contrib import admin
from .models import *

admin.site.register(Experiment)
admin.site.register(Sequence)
admin.site.register(Session)
admin.site.register(Event)
