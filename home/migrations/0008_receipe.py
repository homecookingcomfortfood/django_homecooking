# Generated by Django 3.0.7 on 2021-09-10 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_smoothie_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='receipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('desc', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
    ]
