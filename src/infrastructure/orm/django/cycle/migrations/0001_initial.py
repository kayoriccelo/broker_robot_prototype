# Generated by Django 2.2.12 on 2024-01-03 12:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CycleModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('sequence', models.IntegerField()),
                ('martingale', models.BooleanField(default=False)),
                ('martingale_multipler', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('martingale_reverse', models.BooleanField(default=False)),
                ('soros', models.BooleanField(default=False)),
                ('soros_percentage_profit', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('status', models.IntegerField(choices=[(1, 'Active'), (2, 'Inactive')], default=1)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cycles', to='account.AccountModel')),
            ],
            options={
                'verbose_name': 'Cycle',
                'verbose_name_plural': 'Cycle',
                'db_table': 'cycle',
            },
        ),
    ]
