# Generated by Django 4.1.7 on 2023-02-26 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_send_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Main_office',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='')),
                ('title', models.CharField(max_length=255)),
                ('information', models.CharField(max_length=255)),
            ],
        ),
    ]