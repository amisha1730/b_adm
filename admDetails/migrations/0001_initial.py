# Generated by Django 4.1.6 on 2023-02-11 12:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('specializations', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AdmDetail',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('contact', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('additionalInfo', models.CharField(max_length=255)),
                ('inTime', models.TimeField()),
                ('outTime', models.TimeField()),
                ('adm', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('specialization', models.ManyToManyField(to='specializations.specialization')),
            ],
        ),
    ]
