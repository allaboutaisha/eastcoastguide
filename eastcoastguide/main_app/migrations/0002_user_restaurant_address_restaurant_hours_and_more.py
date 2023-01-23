<<<<<<< HEAD
# Generated by Django 4.1.3 on 2023-01-23 16:26
=======
# Generated by Django 4.1.5 on 2023-01-23 16:26
>>>>>>> main

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_id', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('avatar', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='restaurant',
            name='address',
            field=models.CharField(default='default', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='restaurant',
            name='hours',
            field=models.CharField(default='default', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='restaurant',
            name='image',
            field=models.CharField(default='default', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='restaurant',
            name='location',
            field=models.CharField(default='default', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='restaurant',
            name='price_range',
            field=models.CharField(default='default', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='restaurant',
            name='type',
            field=models.CharField(default='default', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='restaurant',
            name='website',
            field=models.CharField(default='default', max_length=100),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=100)),
                ('comment', models.CharField(max_length=100)),
                ('rating', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.user')),
            ],
        ),
        migrations.AddField(
            model_name='restaurant',
            name='comment',
            field=models.ManyToManyField(to='main_app.comment'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.user'),
        ),
    ]
