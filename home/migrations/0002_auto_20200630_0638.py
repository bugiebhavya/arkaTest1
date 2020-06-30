# Generated by Django 3.0.7 on 2020-06-30 06:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=200)),
                ('country', models.CharField(default='India', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_name', models.CharField(max_length=200)),
                ('product_id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('price', models.IntegerField()),
                ('color', models.CharField(max_length=30)),
                ('created_date', models.DateTimeField(verbose_name='date created')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Company')),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='user',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]