# Generated by Django 4.1.7 on 2023-03-12 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Feedback", "0005_feedbackdata_semester"),
    ]

    operations = [
        migrations.AddField(
            model_name="feedbackdata",
            name="average",
            field=models.FloatField(default=None),
        ),
        migrations.AddField(
            model_name="feedbackdata",
            name="total",
            field=models.PositiveIntegerField(default=None),
        ),
        migrations.AlterField(
            model_name="feedbackdata",
            name="doubt",
            field=models.PositiveSmallIntegerField(
                choices=[
                    (1, "Unsatisfactory"),
                    (2, "Satisfactory"),
                    (3, "Good"),
                    (4, "Very Good"),
                    (5, "Outstanding"),
                ],
                default=None,
                verbose_name="The teacher takes in effort to clear your doubts",
            ),
        ),
        migrations.AlterField(
            model_name="feedbackdata",
            name="interactive",
            field=models.PositiveSmallIntegerField(
                choices=[
                    (1, "Unsatisfactory"),
                    (2, "Satisfactory"),
                    (3, "Good"),
                    (4, "Very Good"),
                    (5, "Outstanding"),
                ],
                default=None,
                verbose_name="The teacher makes the class interactive",
            ),
        ),
        migrations.AlterField(
            model_name="feedbackdata",
            name="portion",
            field=models.PositiveSmallIntegerField(
                choices=[
                    (1, "Unsatisfactory"),
                    (2, "Satisfactory"),
                    (3, "Good"),
                    (4, "Very Good"),
                    (5, "Outstanding"),
                ],
                default=None,
                verbose_name="The teacher completes portions at the appropriate time",
            ),
        ),
        migrations.AlterField(
            model_name="feedbackdata",
            name="punctuality",
            field=models.PositiveSmallIntegerField(
                choices=[
                    (1, "Unsatisfactory"),
                    (2, "Satisfactory"),
                    (3, "Good"),
                    (4, "Very Good"),
                    (5, "Outstanding"),
                ],
                default=None,
                verbose_name="The teacher is punctual in coming to class",
            ),
        ),
    ]