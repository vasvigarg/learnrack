# Generated by Django 4.1.5 on 2023-01-07 06:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0003_course_tag"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="course",
            name="tag",
        ),
    ]
