# Generated by Django 2.2.4 on 2019-08-17 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('officers', '0003_auto_20190817_1802'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Agents',
            new_name='Agent',
        ),
        migrations.RenameModel(
            old_name='Customers',
            new_name='Customer',
        ),
        migrations.RenameModel(
            old_name='Loans',
            new_name='Loan',
        ),
        migrations.RenameModel(
            old_name='Officers',
            new_name='Officer',
        ),
    ]
