# Generated by Django 4.1 on 2023-01-21 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Automobile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('result', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='DerekOne',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('result', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='HezbeOne',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('result', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Moter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('result', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='TaxiOne',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('result', models.CharField(max_length=300)),
            ],
        ),
    ]
