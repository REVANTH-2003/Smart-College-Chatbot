# Generated by Django 3.2.18 on 2023-02-21 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0005_semester1internal1_semester1internal2_semester1model1_semester2internal1_semester2internal2_semester'),
    ]

    operations = [
        migrations.CreateModel(
            name='CseStudyMaterial',
            fields=[
                ('semester', models.IntegerField(primary_key=True, serialize=False)),
                ('link', models.CharField(max_length=100)),
            ],
        ),
    ]