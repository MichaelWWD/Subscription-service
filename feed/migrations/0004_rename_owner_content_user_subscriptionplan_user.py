# Generated by Django 4.2 on 2023-04-06 12:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('feed', '0003_alter_subscription_service'),
    ]

    operations = [
        migrations.RenameField(
            model_name='content',
            old_name='owner',
            new_name='user',
        ),
        migrations.AddField(
            model_name='subscriptionplan',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
