# Generated by Django 3.0.8 on 2020-07-12 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0002_myshop'),
    ]

    operations = [
        migrations.AddField(
            model_name='myshop',
            name='shop_owner_pic',
            field=models.ImageField(default='N/A', upload_to='seller'),
        ),
        migrations.AlterField(
            model_name='seller',
            name='phone_no',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
