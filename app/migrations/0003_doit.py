# Generated by Django 5.0.1 on 2024-02-07 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_tryit'),
    ]

    operations = [
        migrations.CreateModel(
            name='doit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('message', models.TextField()),
            ],
        ),
    ]
