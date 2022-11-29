# Generated by Django 4.1.2 on 2022-11-29 05:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_profile_image'),
        ('store', '0009_rename_brand_product_description_alter_order_updated_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='description',
        ),
        migrations.RemoveField(
            model_name='order',
            name='product',
        ),
        migrations.RemoveField(
            model_name='order',
            name='status',
        ),
        migrations.AddField(
            model_name='order',
            name='completed',
            field=models.BooleanField(default=False, verbose_name=('Completed',)),
        ),
        migrations.AddField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='accounts.customer'),
        ),
        migrations.AddField(
            model_name='order',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name=('Active',)),
        ),
        migrations.AddField(
            model_name='order',
            name='is_archived',
            field=models.BooleanField(default=False, help_text=('Means the oder has been cancelled.',), verbose_name=('Archived',)),
        ),
        migrations.AddField(
            model_name='order',
            name='transaction_id',
            field=models.CharField(default=False, max_length=250),
        ),
        migrations.AlterField(
            model_name='order',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name=('Created',)),
        ),
        migrations.AlterField(
            model_name='order',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name=('Updated',)),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name=('Created',)),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name=('Updated',)),
        ),
        migrations.AlterField(
            model_name='orderpayment',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name=('Created',)),
        ),
        migrations.AlterField(
            model_name='orderpayment',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name=('Updated',)),
        ),
        migrations.AlterField(
            model_name='product',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name=('Updated',)),
        ),
    ]