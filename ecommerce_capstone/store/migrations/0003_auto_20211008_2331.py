# Generated by Django 3.2.8 on 2021-10-09 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_cart'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='Product',
            new_name='product_id',
        ),
        migrations.RenameField(
            model_name='cart',
            old_name='User',
            new_name='user_id',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='Product',
            new_name='product_id',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='User',
            new_name='user_id',
        ),
        migrations.RenameField(
            model_name='payment',
            old_name='User',
            new_name='user_id',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='Product',
            new_name='product_id',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='User',
            new_name='user_id',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='user',
            new_name='user_id',
        ),
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='upload/'),
        ),
        migrations.AlterField(
            model_name='order',
            name='price',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(),
        ),
    ]
