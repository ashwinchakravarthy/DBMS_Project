# Generated by Django 3.1.2 on 2020-12-01 05:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fest_app', '0004_auto_20201122_0723'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='event_price',
            new_name='event_prize',
        ),
        migrations.AlterField(
            model_name='event',
            name='event_date_time',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_description',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='jury',
            name='event',
            field=models.ForeignKey(default=5, on_delete=django.db.models.deletion.SET_DEFAULT, to='fest_app.event'),
        ),
        migrations.AlterField(
            model_name='result',
            name='res_event',
            field=models.ForeignKey(default=5, on_delete=django.db.models.deletion.SET_DEFAULT, to='fest_app.event'),
        ),
        migrations.AlterField(
            model_name='result',
            name='runner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='event_runner', to='fest_app.student'),
        ),
        migrations.AlterField(
            model_name='student',
            name='stud_part_events',
            field=models.ForeignKey(default=5, on_delete=django.db.models.deletion.CASCADE, to='fest_app.event'),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='vol_event',
            field=models.ForeignKey(default=5, on_delete=django.db.models.deletion.SET_DEFAULT, to='fest_app.event'),
        ),
    ]
