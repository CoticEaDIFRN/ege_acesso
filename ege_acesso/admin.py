"""
The MIT License (MIT)

Copyright 2015 Umbrella Tech.
Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
from django.contrib.admin import register, ModelAdmin, TabularInline
from django.utils.translation import gettext_lazy as _
from .models import User, Application


class ApplicationInline(TabularInline):
    model = Application


@register(User)
class UserAdmin(ModelAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'cpf', 'civil_name', 'social_name', 'status', 'active')}),
        (_('Relationship'), {'fields': ('campus', 'department', 'title', 'carrer', 'job')}),
        (_('E-Mails'), {'fields': ('email', 'enterprise_email', 'academic_email', 'scholar_email')}),
        (_('Dates'), {'fields': ('first_access', 'last_access', 'deleted')}),
        (_('Active Directory Dates'), {'fields': ('created_at', 'changed_at', 'password_set_at', 'last_access_at')}),
        # (_('Foto'), {'fields': ('photo_blob', )}),
        # (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups')}),
    )
    readonly_fields = []
    for fs in fieldsets:
        readonly_fields += fs[1]['fields']
    list_display = ('username', 'printing_name', 'cpf', 'status')
    list_filter = ('is_staff', 'is_superuser', 'is_active') + fieldsets[1][1]['fields']
    # + ('groups',)
    search_fields = ('username', 'civil_name', 'social_name', 'email') + fieldsets[2][1]['fields']
    ordering = ('username',)
    # filter_horizontal = ('groups', 'user_permissions',)
    inlines = [ApplicationInline]
