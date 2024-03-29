# Generated by Django 3.0.7 on 2020-08-16 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='email')),
                ('username', models.CharField(max_length=30, unique=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last login')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(blank=True, max_length=100)),
                ('user_type', models.CharField(blank=True, choices=[('IT', 'IT'), ('HOD', 'HOD'), ('HR', 'HR'), ('OPERATIONS', 'OPERATIONS'), ('ACCOUNT', 'ACCOUNT'), ('AUDIT', 'AUDIT'), ('ENC', 'ENC'), ('IMPACT SUPPORT', 'IMPACT SUPPORT')], max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
