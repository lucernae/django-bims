# Generated by Django 2.0.4 on 2018-04-24 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bims', '0003_auto_20180417_1146'),
    ]

    operations = [
        migrations.AddField(
            model_name='biologicalcollectionrecord',
            name='validated',
            field=models.BooleanField(default=False),
        ),
    ]