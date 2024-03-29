# Generated by Django 4.2.2 on 2023-06-21 08:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('elements', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='files',
            name='photo',
        ),
        migrations.AddField(
            model_name='files',
            name='files',
            field=models.FileField(blank=True, null=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.CreateModel(
            name='Images',
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
    ]
