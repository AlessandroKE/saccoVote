# Generated by Django 5.0.1 on 2024-04-01 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_alter_election_end_date_alter_election_start_date'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='usersacco',
            constraint=models.UniqueConstraint(fields=('user', 'sacco'), name='unique_sacco_member'),
        ),
    ]
