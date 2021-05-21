# Generated by Django 3.2.2 on 2021-05-19 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('describe', models.TextField()),
                ('content', models.ImageField(upload_to='photo/%Y%m%d')),
            ],
        ),
    ]