# Generated by Django 4.1 on 2022-08-20 22:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('construction', '0009_delete_inventory'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserFavourites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('favourite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favourite', to='construction.houseplan')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Seller',
        ),
    ]
