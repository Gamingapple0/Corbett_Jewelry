# Generated by Django 3.1.7 on 2021-03-17 06:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20210315_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(),
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='images/')),
                ('key', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='home.product')),
            ],
        ),
    ]
