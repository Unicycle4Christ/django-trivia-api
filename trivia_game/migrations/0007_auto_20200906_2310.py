# Generated by Django 3.0.1 on 2020-09-07 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trivia_game', '0006_auto_20200906_2155'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='gender',
            field=models.CharField(choices=[('M', 'MALE'), ('F', 'FEMALE'), ('*', 'N/A')], default='*', max_length=10),
        ),
        migrations.AddField(
            model_name='questioncategory',
            name='gender',
            field=models.CharField(choices=[('M', 'MALE'), ('F', 'FEMALE'), ('*', 'N/A')], default='*', max_length=10),
        ),
    ]
