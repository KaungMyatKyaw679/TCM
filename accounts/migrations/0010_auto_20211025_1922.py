# Generated by Django 3.2.8 on 2021-10-25 12:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_feed'),
    ]

    operations = [
        migrations.CreateModel(
            name='Writer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='feed',
            old_name='Content',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='feed',
            old_name='Photo',
            new_name='photo',
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookname', models.CharField(max_length=100, null=True)),
                ('bookno', models.CharField(max_length=100, null=True)),
                ('category', models.CharField(choices=[('thuta', 'သုတ'), ('yatha', 'ရသ')], max_length=50, null=True)),
                ('status', models.CharField(choices=[('ya', 'ရရှိနိုင်'), ('maya', 'မရရှိနိုင်သေးပါ')], max_length=100, null=True)),
                ('Writer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.writer')),
            ],
        ),
    ]
