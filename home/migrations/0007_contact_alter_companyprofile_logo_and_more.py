# Generated by Django 4.0.6 on 2022-08-02 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_phone_best_selling_phone_latest'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=50)),
                ('message', models.TextField()),
                ('sent', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contact',
                'db_table': 'contact',
                'managed': True,
            },
        ),
        migrations.AlterField(
            model_name='companyprofile',
            name='logo',
            field=models.ImageField(upload_to='logo'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='best_selling',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='phone',
            name='latest',
            field=models.BooleanField(),
        ),
    ]
