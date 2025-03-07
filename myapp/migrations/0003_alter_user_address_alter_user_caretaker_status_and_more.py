# Generated by Django 4.2.6 on 2023-10-18 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_children'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='caretaker_status',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='dob',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='id_proof',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='ph_number',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='place',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='resume',
            field=models.FileField(default=0, upload_to=''),
        ),
        migrations.AlterField(
            model_name='user',
            name='salary',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='usertype',
            field=models.IntegerField(default=0),
        ),
    ]
