# Generated by Django 4.2.6 on 2023-11-09 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notas', '0005_alter_student_photo_alter_teacher_photo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='photo',
            field=models.ImageField(blank=True, default='../media/default_photo.png', null=True, upload_to='../media/studentPhoto/'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='photo',
            field=models.ImageField(blank=True, default='../media/default_photo.png', null=True, upload_to='..teacherPhoto/'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='photo',
            field=models.ImageField(blank=True, default='../media/default_photo.png', null=True, upload_to='../media/userPhoto/'),
        ),
    ]
