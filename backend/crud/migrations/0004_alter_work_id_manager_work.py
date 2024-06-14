# Generated by Django 5.0.4 on 2024-05-13 22:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0003_taskprogress'),
        ('paginaDeInicio', '0002_remove_user_photo_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='id_manager_work',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='obras_dirigidas', to='paginaDeInicio.user'),
        ),
    ]
