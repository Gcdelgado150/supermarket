# Generated by Django 5.1 on 2024-08-26 18:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0003_alter_stocking_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='stocking',
            unique_together=set(),
        ),
    ]