# Generated by Django 5.2.1 on 2025-05-16 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_webinfo_webliner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coverletter',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='cv',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]
