# Generated by Django 5.1.6 on 2025-03-05 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('processor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='webhook_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
