# Generated by Django 5.1.1 on 2024-09-14 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uniforms', '0003_alter_uniforms_codigo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrada',
            name='num_nota',
            field=models.CharField(max_length=10),
        ),
    ]
