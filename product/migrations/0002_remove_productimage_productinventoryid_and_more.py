# Generated by Django 4.1 on 2023-08-16 15:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productimage',
            name='ProductInventoryId',
        ),
        migrations.AddField(
            model_name='productimage',
            name='ProductId',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='product.product'),
            preserve_default=False,
        ),
    ]
