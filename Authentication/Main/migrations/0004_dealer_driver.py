# Generated by Django 3.2.5 on 2022-02-13 10:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('Main', '0003_usr'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dealer',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('mobile', models.CharField(max_length=20)),
                ('material_type', models.CharField(max_length=250)),
                ('material_weight', models.FloatField()),
                ('quantity', models.IntegerField()),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('age', models.IntegerField()),
                ('truck_no', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=20)),
                ('capacity', models.FloatField()),
                ('transporter_name', models.CharField(default='Self', max_length=100)),
                ('experience', models.IntegerField()),
                ('routes', models.TextField(default='0')),
            ],
        ),
    ]