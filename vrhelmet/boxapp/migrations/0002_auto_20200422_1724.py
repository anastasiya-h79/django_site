# Generated by Django 3.0.4 on 2020-04-22 17:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prodapp', '0003_auto_20200421_1712'),
        ('boxapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.PositiveIntegerField()),
                ('sum', models.PositiveIntegerField()),
                ('deliveryprice', models.PositiveIntegerField()),
                ('totalpurchase', models.PositiveIntegerField()),
                ('delivery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boxapp.Delivery')),
                ('methodpay', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boxapp.Methodpay')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prodapp.Helmets')),
            ],
        ),
        migrations.AddField(
            model_name='userinfo',
            name='comment',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Комментарий к заказу'),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='delivery',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='boxapp.Delivery', verbose_name='Способ доставки'),
        ),
        migrations.DeleteModel(
            name='Box',
        ),
        migrations.AddField(
            model_name='order',
            name='userinfo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boxapp.Userinfo'),
        ),
    ]
