# Generated by Django 3.1.3 on 2020-11-23 09:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppliedStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.company')),
            ],
            options={
                'db_table': 'appliedstatus',
            },
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.company')),
            ],
            options={
                'db_table': 'likes',
            },
        ),
        migrations.CreateModel(
            name='Recommendation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contens', models.CharField(max_length=1000, null=True)),
            ],
            options={
                'db_table': 'recommenders',
            },
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('date', models.DateField(auto_now=True, null=True)),
            ],
            options={
                'db_table': 'resumes',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('email', models.EmailField(max_length=200, unique=True)),
                ('password', models.CharField(max_length=1000)),
                ('phone', models.CharField(max_length=45)),
                ('apllied_status', models.ManyToManyField(related_name='applied_status', through='user.AppliedStatus', to='company.Company')),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='User_tag_filter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.tag')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
            options={
                'db_table': 'user_tag_filters',
            },
        ),
        migrations.CreateModel(
            name='User_district_filter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.district')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
            options={
                'db_table': 'user_district_filters',
            },
        ),
        migrations.CreateModel(
            name='User_carrer_filter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carrer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.carrer')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
            options={
                'db_table': 'user_carrer_filters',
            },
        ),
        migrations.AddField(
            model_name='user',
            name='carrer_filter',
            field=models.ManyToManyField(related_name='user_careers_filters', through='user.User_carrer_filter', to='company.Carrer'),
        ),
        migrations.AddField(
            model_name='user',
            name='district_filter',
            field=models.ManyToManyField(related_name='user_districts_filters', through='user.User_district_filter', to='company.District'),
        ),
        migrations.AddField(
            model_name='user',
            name='likes',
            field=models.ManyToManyField(related_name='likes', through='user.Like', to='company.Company'),
        ),
        migrations.AddField(
            model_name='user',
            name='recomender',
            field=models.ManyToManyField(related_name='recomenders', through='user.Recommendation', to='user.User'),
        ),
        migrations.AddField(
            model_name='user',
            name='tag_filter',
            field=models.ManyToManyField(related_name='user_tags_filters', through='user.User_tag_filter', to='company.Tag'),
        ),
        migrations.CreateModel(
            name='Resume_detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intro', models.CharField(max_length=100)),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.resume')),
            ],
            options={
                'db_table': 'resume_details',
            },
        ),
        migrations.AddField(
            model_name='resume',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user'),
        ),
        migrations.AddField(
            model_name='recommendation',
            name='from_commender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recomender_from_comender', to='user.user'),
        ),
        migrations.AddField(
            model_name='recommendation',
            name='to_comender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recomender_to_comender', to='user.user'),
        ),
        migrations.CreateModel(
            name='Past_carrer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=45)),
                ('company', models.CharField(max_length=45)),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.resume_detail')),
            ],
            options={
                'db_table': 'past_carrers',
            },
        ),
        migrations.AddField(
            model_name='like',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user'),
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=45)),
                ('school_name', models.CharField(max_length=45)),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.resume_detail')),
            ],
            options={
                'db_table': 'grades',
            },
        ),
        migrations.CreateModel(
            name='Award',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=45)),
                ('name', models.CharField(max_length=45)),
                ('detail', models.CharField(max_length=200)),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.resume_detail')),
            ],
            options={
                'db_table': 'awards',
            },
        ),
        migrations.AddField(
            model_name='appliedstatus',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user'),
        ),
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('achievement', models.CharField(max_length=45)),
                ('year', models.CharField(max_length=45)),
                ('detail', models.CharField(max_length=200)),
                ('past_carrer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.past_carrer')),
            ],
            options={
                'db_table': 'achievements',
            },
        ),
    ]
