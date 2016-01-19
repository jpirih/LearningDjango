from django.contrib import admin
from app.models import *

# Register your models here.
admin.site.register(Track)

class SpeakerAdmin(admin.ModelAdmin):
    list_display = ('name', 'bio',)
    fieldsets = (
            ('General information', {
                'fields': ('name', 'bio',)
            }),
            ('Social media', {
                'classes': ('collapse',),
                'fields': ('twitter', 'facebook'),
                'description': 'Add social media here'
            })
        )

admin.site.register(Speaker, SpeakerAdmin)

class SessionAdmin(admin.ModelAdmin):
    list_display = ('title', 'status',)
    search_fields = ['title', 'abstract']
    list_filter = ('track__title', 'speaker',)
    actions = ['make_approved', 'reject']

    def make_approved(self, request, queryset):
        rows_updated = queryset.update(status = 'a')
        if rows_updated == 1:
            message_bit = '1 session was'
        else:
            message_bit = '%s sesssions where' % rows_updated

        self.message_user(request, '%s approved.' % message_bit)
    make_approved.short_description = 'Mark sessions as approved'

    def reject(self, request, queryset):
        rows_rejected = queryset.update(status = 'r')
        if rows_rejected == 1:
            message_bit = '1 session was '
        else:
            message_bit = '%s sesssions were' % rows_rejected

        self.message_user(request, '%s rejected' % message_bit)
    reject.short_description = 'Reject session(s)'

admin.site.register(Session, SessionAdmin)
