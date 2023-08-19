# Generated by Django 4.2.4 on 2023-08-19 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=13)),
                ('generated_code', models.CharField(max_length=6)),
                ('invitation_code', models.CharField(blank=True, max_length=6)),
                ('login_code', models.CharField(max_length=4)),
                ('friends_number', models.ManyToManyField(blank=True, to='user.phone')),
            ],
        ),
    ]
