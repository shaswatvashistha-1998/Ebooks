# Generated by Django 3.0.3 on 2020-05-10 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='profileinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200)),
                ('Description', models.CharField(max_length=200)),
                ('Author', models.CharField(max_length=200)),
                ('published_date', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, upload_to='profile_image')),
            ],
        ),
    ]