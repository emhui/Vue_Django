# Generated by Django 3.0.3 on 2020-05-28 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_auto_20200528_0848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='column',
            name='slug',
            field=models.CharField(db_index=True, max_length=256, verbose_name='栏目网址'),
        ),
    ]
