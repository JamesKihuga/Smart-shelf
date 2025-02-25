# Generated by Django 4.2 on 2024-12-08 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smartshelfapp', '0006_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientShelf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('username', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]
