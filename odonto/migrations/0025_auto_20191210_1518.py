# Generated by Django 2.0.13 on 2019-12-10 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('odonto', '0024_auto_20191206_1449'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orthodonticassessment',
            name='assess_and_appliance_fitted',
        ),
        migrations.RemoveField(
            model_name='orthodonticassessment',
            name='assess_and_refuse_treatment',
        ),
        migrations.RemoveField(
            model_name='orthodonticassessment',
            name='assessment_and_review',
        ),
        migrations.AddField(
            model_name='orthodonticassessment',
            name='assessment',
            field=models.CharField(choices=[('Assess & review', 'Assess & review'), ('Assess & refuse treatment', 'Assess & refuse treatment'), ('Assess & appliance fitted', 'Assess & appliance fitted')], default='', max_length=256, verbose_name='Assessment Type'),
        ),
    ]
