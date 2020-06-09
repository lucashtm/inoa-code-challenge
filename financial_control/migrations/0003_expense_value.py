# Generated by Django 3.0.7 on 2020-06-09 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financial_control', '0002_auto_20200609_0043'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='value',
            field=models.DecimalField(decimal_places=10, default=0, max_digits=20),
            preserve_default=False,
        ),
    ]
