# Generated by Django 3.2 on 2022-04-29 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0005_alter_usercontact_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('telephone', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.EmailField(max_length=50)),
                ('title', models.CharField(default=None, max_length=100)),
                ('message', models.TextField()),
                ('replied', models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], default=False)),
                ('created', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
