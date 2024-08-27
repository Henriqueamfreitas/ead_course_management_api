# Generated by Django 5.1 on 2024-08-27 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('courses', '0001_initial'),
        ('students_courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='my_courses',
            field=models.ManyToManyField(related_name='students', through='students_courses.StudentCourse', to='courses.course'),
        ),
        migrations.AddField(
            model_name='account',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
    ]
