# Generated by Django 3.2.2 on 2021-05-10 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('developer', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='template_post',
            name='image',
        ),
        migrations.AddField(
            model_name='template_post',
            name='image1',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='profile_pics'),
        ),
        migrations.AddField(
            model_name='template_post',
            name='image2',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='profile_pics'),
        ),
        migrations.AddField(
            model_name='template_post',
            name='image3',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='profile_pics'),
        ),
        migrations.AddField(
            model_name='template_post',
            name='image4',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='profile_pics'),
        ),
        migrations.AddField(
            model_name='template_post',
            name='image5',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='profile_pics'),
        ),
    ]
