# Generated by Django 4.2.5 on 2024-03-02 12:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('srm', '0027_alter_advertisment_start_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisment',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 2, 12, 40, 20, 595700, tzinfo=datetime.timezone.utc)),
        ),
    ]