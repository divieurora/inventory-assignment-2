# Generated by Django 4.2.5 on 2023-09-09 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='category',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
