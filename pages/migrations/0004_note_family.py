# Generated by Django 3.2 on 2021-04-15 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_note_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='family',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
