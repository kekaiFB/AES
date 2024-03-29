# Generated by Django 4.2.2 on 2023-06-21 08:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Element',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Элемент')),
            ],
            options={
                'verbose_name': 'Элемент вкладки',
                'verbose_name_plural': '2 Элементы вкладок',
                'ordering': ['tab', 'title'],
            },
        ),
        migrations.CreateModel(
            name='Tab',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, unique=True, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Вкладка',
                'verbose_name_plural': '1 Вкладки',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Files',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('element', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elements.element', verbose_name='Элемент')),
            ],
            options={
                'verbose_name': 'Файлы вкладки',
                'verbose_name_plural': '2.1 Файлы вкладок',
                'ordering': ['element'],
            },
        ),
        migrations.AddField(
            model_name='element',
            name='tab',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elements.tab', verbose_name='Вкладка'),
        ),
    ]
