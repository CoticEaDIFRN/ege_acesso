from rest_framework.serializers import ModelSerializer
from .models import User, SpecialNeed


class SpecialNeedSerializer(ModelSerializer):
    class Meta:
        model = SpecialNeed
        fields = '__all__'


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'cpf', 'is_active', 'presentation_name', 'civil_name', 'social_name', 'campus',
                  'campus_code', 'department', 'title', 'carrer', 'job', 'polo', 'polo_code', 'course', 'course_code',
                  'email', 'enterprise_email', 'academic_email', 'scholar_email', 'photo_url', 'biografy',
                  'is_biografy_public', 'photo_solicitation_at', 'photo_approved_at', 'photo_approved_by', 'font_size',
                  'theme_skin', 'legends', 'sign_language', 'screen_reader', 'special_needs', 'is_special_needs_public',
                  'pending_photo', 'valid_photo', 'printing_name', 'sigla')
