# Generated by Django 4.2.2 on 2023-06-08 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_app', '0002_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]
