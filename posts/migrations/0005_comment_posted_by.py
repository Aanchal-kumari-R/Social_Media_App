# Generated by Django 5.1.4 on 2024-12-31 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_alter_comment_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='posted_by',
            field=models.CharField(default='aanchalsingh', max_length=100),
            preserve_default=False,
        ),
    ]
