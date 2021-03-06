# Generated by Django 3.1.2 on 2020-11-03 14:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cafe',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cafe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cafe.cafe')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cafe.customer')),
            ],
        ),
    ]
