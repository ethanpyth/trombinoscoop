# Generated by Django 4.0.3 on 2022-04-04 10:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Trombinoscoop', '0008_alter_publication_nb_like_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='author_fk',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='Trombinoscoop.person'),
        ),
    ]
