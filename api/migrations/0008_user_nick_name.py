# Generated by Django 4.2.5 on 2023-10-04 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_project_is_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='nick_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
