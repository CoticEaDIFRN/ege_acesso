suap_ead_
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
        # (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups')}),
        (_('Photo'), {'fields': ('photo_url', 'valid_photo', 'pending_photo', 'photo_solicitation_at', 'photo_approved_at',
                                 'photo_approved_by')}),
        (_('Accessibility'), {'fields': ('theme_skin', 'font_size', 'legends', 'sign_language', 'screen_reader',
                                         'is_special_needs_public', 'special_needs')}),
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
