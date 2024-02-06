# Generated by Django 5.0.1 on 2024-02-05 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0005_alter_attendance_unique_together'),
        ('employee', '0002_remove_employee_id_alter_employee_employee_code'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='attendance',
            unique_together=set(),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='punch_time',
            field=models.DateTimeField(),
        ),
        migrations.AlterUniqueTogether(
            name='attendance',
            unique_together={('employee_code', 'date', 'punch_time')},
        ),
    ]
