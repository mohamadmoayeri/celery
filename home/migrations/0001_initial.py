# Generated by Django 3.1.6 on 2021-02-15 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='factorial_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_id', models.CharField(max_length=50)),
                ('n', models.IntegerField()),
                ('result', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]