# Generated by Django 4.1 on 2022-08-20 23:28

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('construction', '0011_rename_userfavourites_userfavourite'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userfavourite',
            old_name='favourite',
            new_name='house_plan',
        ),
        migrations.AlterUniqueTogether(
            name='userfavourite',
            unique_together={('user', 'house_plan')},
        ),
    ]