# Generated by Django 4.1.9 on 2023-07-01 03:52

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("shop", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="product",
            options={
                "ordering": ["name"],
                "verbose_name": "товар",
                "verbose_name_plural": "товары",
            },
        ),
    ]
