# Generated by Django 3.0.3 on 2020-05-28 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20200527_0754'),
    ]

    operations = [
        migrations.AddField(
            model_name='column',
            name='home_display',
            field=models.BooleanField(default=False, verbose_name='首页显示'),
        ),
        migrations.AddField(
            model_name='column',
            name='nav_display',
            field=models.BooleanField(default=False, verbose_name='导航显示'),
        ),
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.CharField(max_length=256, unique=True, verbose_name='网址'),
        ),
    ]
