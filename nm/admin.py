from django.contrib import admin
from nm.models import *


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question']
    date_hierarchy = 'pub_date'

admin.site.register(Poll, PollAdmin)


class ChoiceAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Poll',               {'fields': ['poll']}),
        ('Vote information', {'fields': ['choice_text', 'votes']}),
    ]


admin.site.register(Choice, ChoiceAdmin)