# Generated by Django 4.2.4 on 2024-01-28 03:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_alter_product_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='slue',
            new_name='slug',
        ),
    ]
