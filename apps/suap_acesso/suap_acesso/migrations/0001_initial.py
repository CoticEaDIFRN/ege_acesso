# Generated by Django 2.1.2 on 2018-10-30 22:27

import django.contrib.auth.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=150, primary_key=True, serialize=False, verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, null=True, verbose_name='givenName')),
                ('last_name', models.CharField(blank=True, max_length=150, null=True, verbose_name='sn')),
                ('social_name', models.CharField(blank=True, max_length=150, null=True, verbose_name='social_name')),
                ('department', models.CharField(blank=True, max_length=150, null=True, verbose_name='department')),
                ('campus', models.CharField(blank=True, max_length=150, null=True, verbose_name='extensionAttribute1')),
                ('ativo', models.CharField(blank=True, max_length=150, null=True, verbose_name='extensionAttribute10')),
                ('is_active', models.BooleanField(default=True, verbose_name='Está ativo?')),
                ('is_staff', models.BooleanField(default=False, verbose_name='staff status')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='superuser status')),
                ('carrer', models.CharField(blank=True, max_length=150, null=True, verbose_name='extensionAttribute2')),
                ('job', models.CharField(blank=True, max_length=150, null=True, verbose_name='extensionAttribute3')),
                ('cpf', models.CharField(blank=True, max_length=150, null=True, verbose_name='extensionAttribute6')),
                ('academic_email', models.CharField(blank=True, max_length=150, null=True, verbose_name='extensionAttribute4')),
                ('enterprise_email', models.CharField(blank=True, max_length=150, null=True, verbose_name='mail')),
                ('email', models.CharField(blank=True, max_length=150, null=True, verbose_name='personal mail')),
                ('title', models.CharField(blank=True, max_length=150, null=True, verbose_name='title')),
                ('photo_blob', models.TextField(blank=True, null=True, verbose_name='thumbnailPhoto')),
                ('created_at', models.CharField(blank=True, max_length=150, null=True, verbose_name='whenCreated')),
                ('changed_at', models.CharField(blank=True, max_length=150, null=True, verbose_name='whenChanged')),
                ('password_set_at', models.CharField(blank=True, max_length=150, null=True, verbose_name='pwdLastSet')),
                ('last_access', models.DateTimeField(blank=True, null=True, verbose_name='last access')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Usuário',
                'verbose_name_plural': 'Usuários',
                'ordering': ['first_name'],
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
