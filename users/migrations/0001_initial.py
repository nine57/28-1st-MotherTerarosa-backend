# Generated by Django 4.0 on 2022-01-05 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('username', models.CharField(max_length=30, unique=True)),
                ('password', models.CharField(max_length=300)),
                ('address', models.CharField(blank=True, max_length=500)),
                ('mobile_number', models.CharField(blank=True, max_length=50)),
                ('email', models.CharField(max_length=50, unique=True)),
                ('point', models.DecimalField(decimal_places=2, default=1000000, max_digits=9)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
