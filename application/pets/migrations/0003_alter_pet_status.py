# Generated by Django 4.1.4 on 2022-12-21 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0002_alter_pet_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='status',
            field=models.CharField(choices=[('available', 'available'), ('pending', 'pending'), ('sold', 'sold')], default='available', max_length=20),
        ),
    ]
