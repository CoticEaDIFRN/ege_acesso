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
                  'pending_photo', 'valid_photo')
