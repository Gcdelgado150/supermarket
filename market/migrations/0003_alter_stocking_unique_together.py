# Generated by Django 5.1 on 2024-08-26 16:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0002_alter_category_options_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='stocking',
            unique_together={('product', 'supermarket')},
        ),
    ]
