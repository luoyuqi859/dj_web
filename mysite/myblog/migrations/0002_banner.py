# Generated by Django 3.0.2 on 2020-01-20 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]