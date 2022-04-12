# Generated by Django 3.1 on 2022-04-12 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fl_name', models.CharField(max_length=100)),
                ('rooms', models.CharField(max_length=3)),
                ('phone', models.CharField(max_length=10)),
                ('internal_address', models.CharField(max_length=8)),
                ('section', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=10)),
                ('internal_address', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sections', models.CharField(max_length=100)),
            ],
        ),
    ]