# Generated by Django 4.1.7 on 2023-03-28 19:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('garagem', '0007_alter_cor_options_veiculo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='veiculo',
            name='categoria',
        ),
        migrations.RemoveField(
            model_name='veiculo',
            name='cor',
        ),
        migrations.RemoveField(
            model_name='veiculo',
            name='marca',
        ),
    ]
