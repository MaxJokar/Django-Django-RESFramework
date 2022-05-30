# Generated by Django 4.0.4 on 2022-05-28 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiTestApp', '0002_rename_personmodel_person'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('register_date', models.DateField(auto_now_add=True)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.AlterField(
            model_name='person',
            name='password',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
    ]
