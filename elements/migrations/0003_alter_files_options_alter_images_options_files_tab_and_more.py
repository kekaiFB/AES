# Generated by Django 4.2.2 on 2023-06-21 08:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('elements', '0002_remove_files_photo_files_files_images'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='files',
            options={'ordering': ['element'], 'verbose_name': 'Файлы элемента', 'verbose_name_plural': '2.1 Файлы элементов'},
        ),
        migrations.AlterModelOptions(
            name='images',
            options={'ordering': ['element'], 'verbose_name': 'Изображения элемента', 'verbose_name_plural': '2.2 Изображения элементов'},
        ),
        migrations.AddField(
            model_name='files',
            name='tab',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='elements.tab', verbose_name='Вкладка'),
        ),
        migrations.AddField(
            model_name='images',
            name='tab',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='elements.tab', verbose_name='Вкладка'),
        ),
        migrations.AlterField(
            model_name='images',
            name='photo',
            field=models.ImageField(upload_to='files/%Y/%m/%d/'),
        ),
    ]