# Generated by Django 4.2.4 on 2023-10-02 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('robots', '0003_rename_is_availabe_robot_is_available'),
    ]

    operations = [
        migrations.AlterField(
            model_name='robot',
            name='is_available',
            field=models.BooleanField(default=True),
        ),
    ]
