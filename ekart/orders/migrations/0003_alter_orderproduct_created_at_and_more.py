# Generated by Django 4.1.2 on 2023-01-24 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0002_remove_orderproduct_color_remove_orderproduct_size_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="orderproduct",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="orderproduct",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
