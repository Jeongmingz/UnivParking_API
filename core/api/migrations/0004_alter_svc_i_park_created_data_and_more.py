# Generated by Django 4.2.6 on 2023-10-20 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_svc_i_park_created_data_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='svc_i_park',
            name='created_data',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='svc_i_park',
            name='updated_data',
            field=models.DateTimeField(auto_now=True),
        ),
    ]