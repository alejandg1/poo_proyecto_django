# Generated by Django 4.2.6 on 2023-11-08 05:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notas', '0008_alter_userprofile_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='calification',
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
                ('re', models.IntegerField(default=0, verbose_name='re')),
                ('final', models.IntegerField(default=0, verbose_name='final')),
            ],
        ),
        migrations.CreateModel(
            name='enrollment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='notas',
            name='student',
        ),
        migrations.RemoveField(
            model_name='notas',
            name='subject',
        ),
        migrations.RemoveField(
            model_name='teacher_subject',
            name='subject',
        ),
        migrations.RemoveField(
            model_name='teacher_subject',
            name='teacher',
        ),
        migrations.RemoveField(
            model_name='paralell',
            name='student',
        ),
        migrations.RemoveField(
            model_name='paralell',
            name='subject',
        ),
        migrations.RemoveField(
            model_name='paralell',
            name='teacher',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='teacher',
        ),
        migrations.AddField(
            model_name='carrer',
            name='Subjects',
            field=models.ManyToManyField(default=None, to='notas.subject'),
        ),
        migrations.AddField(
            model_name='student',
            name='carrera',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='notas.carrer'),
        ),
        migrations.AddField(
            model_name='student',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='notas_studentPhoto'),
        ),
        migrations.AddField(
            model_name='subject',
            name='semestre',
            field=models.IntegerField(default=1, verbose_name='semestre'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='notas_teacherPhoto'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='notas_userPhoto'),
        ),
        migrations.DeleteModel(
            name='matricula',
        ),
        migrations.DeleteModel(
            name='Notas',
        ),
        migrations.DeleteModel(
            name='teacher_subject',
        ),
        migrations.AddField(
            model_name='enrollment',
            name='paralell',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='notas.paralell'),
        ),
        migrations.AddField(
            model_name='enrollment',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notas.student'),
        ),
        migrations.AddField(
            model_name='enrollment',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notas.subject'),
        ),
        migrations.AddField(
            model_name='enrollment',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='notas.teacher'),
        ),
        migrations.AddField(
            model_name='calification',
            name='enroll',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='notas.enrollment'),
        ),
    ]