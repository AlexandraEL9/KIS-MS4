# Generated by Django 3.2.25 on 2024-11-02 19:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20241102_1926'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='has_dietary_options',
            new_name='has_sizes',
        ),
        migrations.RemoveField(
            model_name='product',
            name='dietary_options',
        ),
        migrations.DeleteModel(
            name='DietaryOption',
        ),
    ]
