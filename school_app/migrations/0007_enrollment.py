# Generated by Django 4.2.2 on 2023-06-08 13:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school_app', '0006_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_enrolled', models.DateTimeField(auto_now_add=True)),
                ('course_edition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_app.courseedition')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_app.student')),
            ],
        ),
    ]