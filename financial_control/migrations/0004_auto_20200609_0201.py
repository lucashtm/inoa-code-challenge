# Generated by Django 3.0.7 on 2020-06-09 02:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('financial_control', '0003_expense_value'),
    ]

    operations = [
        migrations.RenameField(
            model_name='expense',
            old_name='category_id',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='expense',
            old_name='user_id',
            new_name='user',
        ),
    ]
