# Generated by Django 4.1 on 2022-08-15 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('construction', '0002_alter_houseplan_additions_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='houseplan',
            name='title',
            field=models.CharField(default='empty', max_length=255),
        ),
    ]