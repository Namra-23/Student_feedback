# Generated by Django 4.1.4 on 2023-02-24 05:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Review', '0004_semester_subject_faculty'),
        ('Feedback', '0003_alter_feedbackdata_interactive'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedbackdata',
            name='teacher_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Review.faculty', verbose_name='Name of Teacher'),
        ),
    ]
