# Generated by Django 5.1.6 on 2025-03-03 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("videos", "0006_video_timestamp_video_updated"),
    ]

    operations = [
        migrations.AlterField(
            model_name="video",
            name="video_id",
            field=models.CharField(max_length=220, unique=True),
        ),
    ]
