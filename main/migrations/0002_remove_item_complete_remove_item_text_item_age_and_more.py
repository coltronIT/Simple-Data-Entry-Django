# Generated by Django 4.0.3 on 2022-03-01 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='complete',
        ),
        migrations.RemoveField(
            model_name='item',
            name='text',
        ),
        migrations.AddField(
            model_name='item',
            name='age',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='item',
            name='hometown',
            field=models.CharField(default='unlisted', max_length=200),
        ),
        migrations.AddField(
            model_name='item',
            name='name',
            field=models.CharField(default='unlisted', max_length=200),
        ),
        migrations.AddField(
            model_name='item',
            name='title',
            field=models.CharField(default='unlisted', max_length=200),
        ),
    ]