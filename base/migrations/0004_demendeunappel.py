# Generated by Django 4.1 on 2022-11-02 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_service_status_alter_client_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='DemendeUnAppel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('service', models.CharField(max_length=200)),
            ],
        ),
    ]
