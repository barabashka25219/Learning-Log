# Generated by Django 4.1 on 2023-11-29 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0003_topic_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='image',
            field=models.ImageField(null=True, upload_to='images/%Y%m%d'),
        ),
    ]
