# Generated by Django 4.2 on 2023-04-21 17:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='purchase',
            options={'ordering': ['-date']},
        ),
    ]
