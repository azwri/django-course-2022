# Generated by Django 4.0.6 on 2022-08-05 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_alter_flower_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flower',
            name='slug',
            field=models.SlugField(blank=True, default=''),
        ),
    ]
