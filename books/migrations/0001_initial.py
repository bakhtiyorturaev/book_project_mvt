# Generated by Django 5.0.1 on 2024-04-03 11:25

import books.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('pageCount', models.IntegerField(default=0)),
                ('shortDescription', models.CharField(max_length=256, null=True)),
                ('book_file', models.FileField(blank=True, null=True, upload_to=books.models.upload_to)),
                ('image', models.ImageField(default='book_image/book_image.jpg', upload_to='media')),
                ('create_at', models.DateField(auto_now=True)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('authors', models.ManyToManyField(to='books.author')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='books.book')),
            ],
            options={
                'db_table': 'review_table',
            },
        ),
    ]
