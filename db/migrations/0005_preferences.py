# Generated by Django 2.1.7 on 2019-03-05 18:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0004_course_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='Preferences',
            fields=[
                ('faculty', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='db.Faculty')),
            ],
        ),
    ]
