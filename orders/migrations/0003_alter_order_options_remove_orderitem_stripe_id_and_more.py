# Generated by Django 4.1.9 on 2023-07-03 20:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("orders", "0002_orderitem_stripe_id"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="order",
            options={"ordering": ["-created"]},
        ),
        migrations.RemoveField(
            model_name="orderitem",
            name="stripe_id",
        ),
        migrations.AddField(
            model_name="order",
            name="stripe_id",
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
