# Generated by Django 2.1.5 on 2019-01-14 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mailroom', '0002_auto_20190114_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otherdetail',
            name='phone',
            field=models.IntegerField(blank=True),
        ),
    ]
