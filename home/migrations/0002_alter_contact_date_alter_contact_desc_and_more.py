# Generated by Django 4.0.1 on 2022-01-12 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='desc',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.CharField(max_length=122, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=122, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(max_length=12, null=True),
        ),
    ]
