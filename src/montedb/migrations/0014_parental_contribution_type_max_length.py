# Generated by Django 2.2.10 on 2020-03-16 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('montedb', '0013_add_unique_together_parentalcontribution'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parentalcontribution',
            name='type',
            field=models.CharField(choices=[('school_fee', 'School fee'), ('after_school_fee', 'After school fee'), ('kindergarten_le_30h_fee', 'Kindergarten (up to 30 hours)'), ('kindergarten_gt_30h_fee', 'Kindergarten (more than 30 hours)'), ('nursery_le_30h_fee', 'Nursery (up to 30 hours)'), ('nursery_gt_30h_fee', 'Nursery (more than 30 hours)')], max_length=25, verbose_name='Contribution type'),
        ),
    ]