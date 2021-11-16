# Generated by Django 3.2.9 on 2021-11-16 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClinicalData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskCode', models.CharField(max_length=100, null=True, unique=True)),
                ('taskName', models.CharField(max_length=100, null=True)),
                ('department', models.CharField(max_length=100, null=True)),
                ('chiefInstitution', models.CharField(max_length=100, null=True)),
                ('studySubjectNumbers', models.IntegerField(null=True)),
                ('studyPeriod', models.IntegerField(null=True)),
                ('studyType', models.CharField(max_length=100, null=True)),
                ('studyPhase', models.CharField(max_length=100, null=True)),
                ('studyScope', models.CharField(max_length=100, null=True)),
                ('created_at', models.DateField(auto_now_add=True, null=True)),
                ('updated_at', models.DateField(null=True)),
            ],
        ),
    ]
