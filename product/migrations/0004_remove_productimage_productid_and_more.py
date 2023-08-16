# Generated by Django 4.1 on 2023-08-16 14:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_remove_productimage_isfeatured_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productimage',
            name='productId',
        ),
        migrations.AddField(
            model_name='productimage',
            name='ProductInventoryId',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='product.productinventory'),
            preserve_default=False,
        ),
    ]
