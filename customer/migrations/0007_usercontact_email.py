# Generated by Django 3.2 on 2022-04-29 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0006_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercontact',
            name='email',
            field=models.EmailField(default='info@elmania.com', max_length=50),
            preserve_default=False,
        ),
    ]
