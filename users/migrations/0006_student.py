# Generated by Django 4.2.2 on 2023-07-11 16:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_classroom_campus_classes'),
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('student_id', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL, verbose_name='student_id')),
                ('gpa', models.FloatField()),
                ('credits', models.FloatField()),
                ('major', models.CharField(max_length=50)),
                ('courses_taken', models.ManyToManyField(to='users.classes')),
            ],
        ),
    ]