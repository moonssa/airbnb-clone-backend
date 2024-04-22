# Generated by Django 5.0.4 on 2024-04-22 06:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
        ('experience', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='categories.category'),
        ),
        migrations.AlterField(
            model_name='perk',
            name='details',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='perk',
            name='explanation',
            field=models.TextField(blank=True, null=True),
        ),
    ]