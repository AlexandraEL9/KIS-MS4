# Generated by Django 3.2.25 on 2024-11-02 18:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20241023_1459'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='has_sizes',
            new_name='has_dietary_options',
        ),
    ]