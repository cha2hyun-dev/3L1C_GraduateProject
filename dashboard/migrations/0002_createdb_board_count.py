# Generated by Django 3.0.5 on 2020-04-01 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='createdb',
            name='board_count',
            field=models.CharField(blank=True, choices=[('1', '1'), ('2', '2')], max_length=3, null=True),
        ),
    ]
