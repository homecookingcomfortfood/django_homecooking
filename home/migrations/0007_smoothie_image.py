# Generated by Django 3.0.7 on 2021-09-06 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20210906_1845'),
    ]

    operations = [
        migrations.AddField(
            model_name='smoothie',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]