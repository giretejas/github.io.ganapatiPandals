# Generated by Django 4.0.4 on 2022-09-07 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_logins'),
    ]

    operations = [
        migrations.CreateModel(
            name='me',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=60)),
                ('subject', models.CharField(max_length=70)),
                ('message', models.CharField(max_length=30)),
            ],
        ),
    ]
