# Generated by Django 5.0 on 2024-10-19 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='cart',
        ),
        migrations.AddField(
            model_name='cart',
            name='products',
            field=models.ManyToManyField(to='cart.product'),
        ),
    ]
