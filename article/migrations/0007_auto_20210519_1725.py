# Generated by Django 3.2.2 on 2021-05-19 09:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article_category', '0001_initial'),
        ('article', '0006_auto_20210518_2049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='articles', to='article_category.category'),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
