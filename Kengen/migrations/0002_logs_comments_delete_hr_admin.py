# Generated by Django 4.2.1 on 2023-06-16 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Kengen', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='logs',
            name='comments',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.DeleteModel(
            name='HR_Admin',
        ),
    ]
