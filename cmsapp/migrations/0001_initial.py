# Generated by Django 4.1.6 on 2023-03-07 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CourseModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Course_Name', models.CharField(max_length=100)),
                ('Course_Fees', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TeacherModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=100)),
                ('Last_Name', models.CharField(max_length=100)),
                ('User_Name', models.CharField(max_length=100)),
                ('Address', models.CharField(max_length=200)),
                ('Email', models.CharField(max_length=100)),
                ('Age', models.IntegerField()),
                ('image', models.ImageField(null=True, upload_to='image/')),
                ('Course_Name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cmsapp.coursemodel')),
            ],
        ),
        migrations.CreateModel(
            name='StudentModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Student_Name', models.CharField(max_length=100)),
                ('Phone_Number', models.IntegerField()),
                ('Gender', models.CharField(max_length=100)),
                ('Address', models.CharField(max_length=200)),
                ('Join_Date', models.DateField(auto_now=True)),
                ('Course_Name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cmsapp.coursemodel')),
            ],
        ),
    ]
