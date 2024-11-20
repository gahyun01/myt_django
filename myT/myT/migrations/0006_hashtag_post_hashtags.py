# Generated by Django 5.1.3 on 2024-11-20 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myT', '0005_postimage_number_alter_postimage_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hashtag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='hashtags',
            field=models.ManyToManyField(blank=True, related_name='posts', to='myT.hashtag'),
        ),
    ]
