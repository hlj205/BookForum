# Generated by Django 2.0.5 on 2018-09-08 05:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Discussion', '0011_auto_20180908_1247'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='receivers',
        ),
        migrations.AddField(
            model_name='notification',
            name='receiver',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='receive_notifies', to=settings.AUTH_USER_MODEL, verbose_name='接收者'),
            preserve_default=False,
        ),
    ]
