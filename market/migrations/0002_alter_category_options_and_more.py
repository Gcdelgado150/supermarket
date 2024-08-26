# Generated by Django 5.1 on 2024-08-26 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Categoria', 'verbose_name_plural': 'Categorias'},
        ),
        migrations.AlterField(
            model_name='customer',
            name='subscription_type',
            field=models.CharField(blank=True, choices=[('D', 'Dummy'), ('R', 'Registered'), ('P', 'Pay'), ('S', 'Special')], max_length=1, null=True),
        ),
    ]
