# Generated by Django 4.2.7 on 2023-12-14 16:00

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("conversation", "0003_alter_conversation_modified_at"),
    ]

    operations = [
        migrations.RenameField(
            model_name="conversationmessage",
            old_name="coversation",
            new_name="conversation",
        ),
    ]
