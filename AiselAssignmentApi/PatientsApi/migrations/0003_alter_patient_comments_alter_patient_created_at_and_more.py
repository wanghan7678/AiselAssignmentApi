# Generated by Django 5.2 on 2025-04-08 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PatientsApi', '0002_alter_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='comments',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='created_at',
            field=models.DateTimeField(auto_created=True, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='deleted_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='deleted_by',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
