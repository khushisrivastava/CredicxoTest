# Generated by Django 3.0.8 on 2020-07-01 13:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('bank_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='BranchDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch', models.CharField(max_length=255)),
                ('ifsc', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('district', models.CharField(max_length=255)),
                ('bank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bank_details', to='bank.Bank')),
            ],
        ),
    ]
