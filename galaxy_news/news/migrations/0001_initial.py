# Generated by Django 4.0.1 on 2022-02-01 02:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='title')),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='title')),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='title')),
                ('description', models.CharField(max_length=299, verbose_name='description')),
                ('image', models.ImageField(blank=True, upload_to='image/%Y/%m/%d', verbose_name='image')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='author')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.categories', verbose_name='category')),
                ('tags', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.tags', verbose_name='tags')),
            ],
        ),
    ]
