# Generated by Django 5.1.6 on 2025-03-03 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("videos", "0004_video_state"),
    ]

    operations = [
        migrations.AddField(
            model_name="video",
            name="publish_timestamp",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
