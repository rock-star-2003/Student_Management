# Generated by Django 4.2.15 on 2024-08-30 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_batch_department_alter_student_bach_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batch',
            name='date',
            field=models.IntegerField(blank=True, max_length=3, null=True),
        ),
    ]