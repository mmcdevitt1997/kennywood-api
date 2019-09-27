# Generated by Django 2.2.5 on 2019-09-27 20:19

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.expressions


class Migration(migrations.Migration):

    dependencies = [
        ('kennywoodapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'ordering': (django.db.models.expressions.OrderBy(django.db.models.expressions.F('user.date_joined'), nulls_last=True),)},
        ),
        migrations.AlterField(
            model_name='attraction',
            name='area',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='attractions', to='kennywoodapi.ParkArea'),
        ),
    ]
