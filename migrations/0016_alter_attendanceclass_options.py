# Generated by Django 4.1.2 on 2022-10-14 03:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0015_attendancerange'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='attendanceclass',
            options={'verbose_name': 'Attendance', 'verbose_name_plural': 'Attendance'},
        ),
    ]
