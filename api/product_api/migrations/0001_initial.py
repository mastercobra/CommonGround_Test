# Generated by Django 3.0.8 on 2020-07-02 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.CharField(max_length=250, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250)),
                ('value', models.FloatField()),
                ('discount_value', models.FloatField(null=True)),
                ('stock', models.IntegerField()),
            ],
        ),
    ]
