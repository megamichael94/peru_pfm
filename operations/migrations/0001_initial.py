# Generated by Django 5.1 on 2024-12-21 04:59

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Enterprise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512, verbose_name='name')),
                ('id_number', models.CharField(blank=True, max_length=15, verbose_name='id number')),
            ],
            options={
                'verbose_name': 'Enterprise',
                'verbose_name_plural': 'Enterprises',
            },
        ),
        migrations.CreateModel(
            name='LineOfBusiness',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512, verbose_name='name')),
                ('code', models.IntegerField(unique=True, verbose_name='code')),
            ],
            options={
                'verbose_name': 'Line of business',
                'verbose_name_plural': 'Line of businesses',
            },
        ),
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, upload_to='', verbose_name='file')),
                ('image', models.ImageField(blank=True, upload_to='', verbose_name='image')),
                ('creation_datetime', models.DateTimeField(auto_now_add=True, verbose_name='creation date ')),
                ('issue_date', models.DateField(default=django.utils.timezone.now, verbose_name='date issued')),
                ('total', models.FloatField(verbose_name='total')),
                ('taxes_percentage', models.IntegerField(default=10, verbose_name='taxes percentage')),
                ('taxes', models.FloatField(blank=True, null=True, verbose_name='taxes amount')),
                ('total_without_taxes', models.FloatField(blank=True, null=True, verbose_name='total without taxes')),
                ('is_it_tax_deductible', models.BooleanField(default=True, verbose_name='is tax deductible')),
                ('issuer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='operations.enterprise', verbose_name='issuer')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='enterprise',
            name='line_of_business',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='operations.lineofbusiness', verbose_name='line of business'),
        ),
        migrations.CreateModel(
            name='Outcome',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, upload_to='', verbose_name='file')),
                ('image', models.ImageField(blank=True, upload_to='', verbose_name='image')),
                ('creation_datetime', models.DateTimeField(auto_now_add=True, verbose_name='creation date ')),
                ('issue_date', models.DateField(default=django.utils.timezone.now, verbose_name='date issued')),
                ('total', models.FloatField(verbose_name='total')),
                ('taxes_percentage', models.IntegerField(default=10, verbose_name='taxes percentage')),
                ('taxes', models.FloatField(blank=True, null=True, verbose_name='taxes amount')),
                ('total_without_taxes', models.FloatField(blank=True, null=True, verbose_name='total without taxes')),
                ('is_it_tax_deductible', models.BooleanField(default=True, verbose_name='is tax deductible')),
                ('issuer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='operations.enterprise', verbose_name='issuer')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
