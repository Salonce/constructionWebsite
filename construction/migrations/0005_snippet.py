# Generated by Django 4.1 on 2022-08-15 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('construction', '0004_remove_houseplan_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Snippet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('body', models.TextField()),
            ],
        ),
    ]
