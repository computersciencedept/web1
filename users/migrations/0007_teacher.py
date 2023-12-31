# Generated by Django 4.2.2 on 2023-07-11 19:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='teacher',
            fields=[
                ('teacher_id', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL, verbose_name='teacher_id')),
                ('title', models.CharField(max_length=50)),
                ('courses_teaching', models.ManyToManyField(to='users.classes')),
            ],
        ),
    ]
