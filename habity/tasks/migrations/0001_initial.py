# Generated by Django 5.0 on 2024-07-17 17:46

import uuid

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="TaskCategory",
            fields=[
                (
                    "guid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("active", models.BooleanField(default=True)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("created_by", models.UUIDField()),
                ("updated", models.DateTimeField(auto_now=True)),
                ("updated_by", models.UUIDField()),
                ("name", models.CharField(max_length=50)),
                ("description", models.CharField(max_length=200)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Task",
            fields=[
                (
                    "guid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("active", models.BooleanField(default=True)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("created_by", models.UUIDField()),
                ("updated", models.DateTimeField(auto_now=True)),
                ("updated_by", models.UUIDField()),
                ("name", models.CharField(max_length=250)),
                ("description", models.TextField(blank=True, null=True)),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("Single", "Single"),
                            ("Recurring", "Recurring"),
                            ("Habit", "Habit"),
                        ],
                        max_length=50,
                    ),
                ),
                (
                    "priority",
                    models.CharField(
                        choices=[
                            ("High", "High"),
                            ("Medium", "Medium"),
                            ("Low", "Low"),
                        ],
                        max_length=50,
                    ),
                ),
                ("start_date", models.DateField()),
                ("end_date", models.DateField()),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tasks",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="tasks",
                        to="tasks.taskcategory",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
