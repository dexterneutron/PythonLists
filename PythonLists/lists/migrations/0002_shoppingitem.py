# Generated by Django 3.2.6 on 2021-08-09 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShoppingItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('quantity', models.CharField(max_length=30)),
            ],
        ),
    ]