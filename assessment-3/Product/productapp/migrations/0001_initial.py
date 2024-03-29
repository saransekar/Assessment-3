# Generated by Django 2.2.2 on 2019-06-26 06:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=20)),
                ('contact_name', models.CharField(max_length=20)),
                ('client_code', models.CharField(max_length=15, unique=True)),
                ('mobile_number', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'client',
            },
        ),
        migrations.CreateModel(
            name='Router',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wireless_router_ip', models.CharField(max_length=30)),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='productapp.Client')),
            ],
            options={
                'db_table': 'router',
            },
        ),
        migrations.CreateModel(
            name='ProductImplementation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('installation_date', models.DateField(blank=True, null=True)),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='productapp.Client')),
            ],
            options={
                'db_table': 'product_implementation',
            },
        ),
        migrations.CreateModel(
            name='Hub',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hub_ip', models.CharField(max_length=30)),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='productapp.Client')),
            ],
            options={
                'db_table': 'hub',
            },
        ),
    ]
