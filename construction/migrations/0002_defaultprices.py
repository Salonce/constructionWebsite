# Generated by Django 4.1 on 2022-08-08 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('construction', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DefaultPrices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.FloatField(max_length=255)),
            ],
        ),
    ]
