# Generated by Django 2.1 on 2018-08-16 08:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('status', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_id', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('course_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('dep_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('dep_name', models.CharField(max_length=20)),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('exam_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Marks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Exam')),
            ],
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('parent_id', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('parent_pass', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_id', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('student_pass', models.CharField(max_length=15)),
                ('student_name', models.CharField(max_length=20)),
                ('student_id_DOB', models.DateField()),
                ('student_enr_year', models.CharField(max_length=4)),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('sub_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('sub_name', models.CharField(max_length=20)),
                ('sub_credit', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('teacher_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('teacher_name', models.CharField(max_length=20)),
                ('teacher_salary', models.CharField(max_length=20)),
                ('sub_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Subject')),
            ],
        ),
        migrations.AddField(
            model_name='parent',
            name='student_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Student'),
        ),
        migrations.AddField(
            model_name='marks',
            name='student_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Student'),
        ),
        migrations.AddField(
            model_name='marks',
            name='sub_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Subject'),
        ),
        migrations.AddField(
            model_name='course',
            name='sub_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Subject'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='student_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Student'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='teacher_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Teacher'),
        ),
    ]
