# Generated by Django 3.2.7 on 2021-09-14 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0002_rename_is_mvp_realtor_hire_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='realtor',
            name='is_mvp',
            field=models.BooleanField(default=False),
        ),
    ]
