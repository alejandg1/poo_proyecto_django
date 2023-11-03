# Generated by Django 4.2.6 on 2023-11-03 21:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notas', '0006_faculty_alter_userprofile_photo_carrer'),
    ]

    operations = [
        migrations.CreateModel(
            name='matricula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Notas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('n1', models.IntegerField(default=0, verbose_name='n1')),
                ('n2', models.IntegerField(default=0, verbose_name='n2')),
                ('n3', models.IntegerField(default=0, verbose_name='n3')),
                ('n4', models.IntegerField(default=0, verbose_name='n4')),
                ('ex1', models.IntegerField(default=0, verbose_name='ex1')),
                ('ex2', models.IntegerField(default=0, verbose_name='ex2')),
                ('p1', models.IntegerField(default=0, verbose_name='p1')),
                ('p2', models.IntegerField(default=0, verbose_name='p2')),
                ('final', models.IntegerField(default=0, verbose_name='final')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notas.student')),
            ],
        ),
        migrations.CreateModel(
            name='paralell',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='name')),
                ('code', models.CharField(max_length=20, verbose_name='code')),
                ('is_active', models.BooleanField(default=True, verbose_name='is_active')),
                ('student', models.ManyToManyField(through='notas.matricula', to='notas.student')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='name')),
                ('code', models.CharField(max_length=20, verbose_name='code')),
                ('is_active', models.BooleanField(default=True, verbose_name='is_active')),
            ],
        ),
        migrations.CreateModel(
            name='teacher_subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notas.subject')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notas.teacher')),
            ],
        ),
        migrations.DeleteModel(
            name='Carrera',
        ),
        migrations.DeleteModel(
            name='Facultad',
        ),
        migrations.AddField(
            model_name='subject',
            name='teacher',
            field=models.ManyToManyField(through='notas.teacher_subject', to='notas.teacher'),
        ),
        migrations.AddField(
            model_name='paralell',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notas.subject'),
        ),
        migrations.AddField(
            model_name='paralell',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notas.teacher'),
        ),
        migrations.AddField(
            model_name='notas',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notas.subject'),
        ),
        migrations.AddField(
            model_name='matricula',
            name='paralell',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notas.paralell'),
        ),
        migrations.AddField(
            model_name='matricula',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notas.student'),
        ),
        migrations.AddField(
            model_name='matricula',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notas.subject'),
        ),
    ]
