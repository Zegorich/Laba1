# Generated by Django 5.0.3 on 2024-05-18 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_alter_order2_account_money_alter_order2_spent_money_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='registration_code',
            field=models.IntegerField(blank=True, null=True, verbose_name='Код учёта'),
        ),
        migrations.AddField(
            model_name='user',
            name='registration_code_flag',
            field=models.BooleanField(blank=True, default=0, null=True, verbose_name='без имени'),
        ),
        migrations.AlterField(
            model_name='user',
            name='debt',
            field=models.FloatField(blank=True, null=True, verbose_name='Долг клиента'),
        ),
    ]
