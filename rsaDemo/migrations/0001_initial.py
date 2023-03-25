# Generated by Django 3.2.9 on 2021-11-06 09:56

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='messageModel',
            fields=[
                ('messageId', models.BigAutoField(primary_key=True, serialize=False)),
                ('text', models.TextField(blank=True, null=True)),
                ('bits', models.IntegerField(choices=[(128, '128 bits'), (256, '256 bits'), (512, '512 bits'), (1024, '1024 bits'), (2048, '2048 bits')], default='128')),
                ('cipherText', models.TextField(blank=True, null=True)),
                ('sender', models.CharField(default='', max_length=200)),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('read', models.BooleanField(default=False)),
                ('ctlist', models.TextField(blank=True, null=True)),
                ('publicKey', models.TextField(blank=True, null=True)),
                ('phi', models.TextField(blank=True, null=True)),
                ('modulus', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='roomModel',
            fields=[
                ('roomId', models.BigAutoField(primary_key=True, serialize=False)),
                ('roomName', models.CharField(max_length=200, unique=True)),
                ('roomType', models.CharField(choices=[('private', 'private'), ('public', 'public')], default='private', max_length=50)),
                ('createdOn', models.DateTimeField(default=datetime.datetime.now)),
                ('password', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='userModel',
            fields=[
                ('uid', models.BigAutoField(primary_key=True, serialize=False)),
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='roomHasMessages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('messageId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rsaDemo.messagemodel')),
                ('roomId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rsaDemo.roommodel')),
            ],
        ),
        migrations.AddField(
            model_name='messagemodel',
            name='room',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='rsaDemo.roommodel'),
        ),
        migrations.CreateModel(
            name='createsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roomId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rsaDemo.roommodel')),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rsaDemo.usermodel')),
            ],
        ),
    ]
