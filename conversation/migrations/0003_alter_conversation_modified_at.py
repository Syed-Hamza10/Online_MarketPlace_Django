# Generated by Django 4.2.7 on 2023-12-10 18:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("conversation", "0002_alter_conversation_modified_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="conversation",
            name="modified_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
