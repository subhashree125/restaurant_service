# Generated by Django 4.2.13 on 2024-07-08 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_orderhistory_delete_userprofile"),
    ]

    operations = [
        migrations.AlterField(
            model_name="orderhistory", name="quantities", field=models.TextField(),
        ),
    ]
