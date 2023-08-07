# Generated by Django 4.2.2 on 2023-08-07 11:00

from decimal import Decimal
import django.core.validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("vending", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("first_name", models.CharField(max_length=25)),
                ("last_name", models.CharField(max_length=25)),
                ("user_name", models.CharField(max_length=25)),
                (
                    "balance",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=4,
                        validators=[
                            django.core.validators.MinValueValidator(Decimal("0.00"))
                        ],
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "db_table": "user",
            },
        ),
    ]