# Generated by Django 5.0.1 on 2024-01-30 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='sample',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone_no', models.IntegerField(default='')),
                ('alternative_phoneno', models.IntegerField(default='')),
                ('address', models.CharField(default='', max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('litre', models.IntegerField(default='')),
            ],
        ),
    ]
