# Generated by Django 3.2.2 on 2021-05-12 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('developer', '0002_auto_20210511_0457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='template_post',
            name='file',
            field=models.FileField(upload_to='media'),
        ),
    ]
