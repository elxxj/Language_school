# Generated by Django 4.2.2 on 2023-06-08 13:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school_app', '0003_level'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseEdition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(null=True)),
                ('start_date', models.DateField(null=True)),
                ('end_date', models.DateField(null=True)),
                ('max_students', models.PositiveIntegerField(null=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_app.course')),
                ('level', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='school_app.level')),
            ],
        ),
    ]
