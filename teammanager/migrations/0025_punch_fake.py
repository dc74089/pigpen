# Generated by Django 2.2.3 on 2019-08-07 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teammanager', '0024_auto_20190806_1630'),
    ]

    operations = [
        migrations.AddField(
            model_name='punch',
            name='fake',
            field=models.BooleanField(default=False),
        ),
    ]
