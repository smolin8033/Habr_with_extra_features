# Generated by Django 3.2 on 2022-07-09 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_customuser_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='personal_info',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]