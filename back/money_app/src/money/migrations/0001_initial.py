import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.RunSQL(
            sql="""
                CREATE SCHEMA IF NOT EXISTS content;
            """,
            reverse_sql='',
        ),
        migrations.RunSQL(
            sql="""
                ALTER ROLE money SET search_path TO content,public;
            """,
            reverse_sql='',
        ),
    ]
