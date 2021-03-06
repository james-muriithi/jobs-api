# Generated by Django 4.0.3 on 2022-03-22 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_job_company_alter_job_full_text_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='link',
            field=models.CharField(default=11, max_length=150, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='job',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='title',
            field=models.CharField(max_length=150),
        ),
    ]
