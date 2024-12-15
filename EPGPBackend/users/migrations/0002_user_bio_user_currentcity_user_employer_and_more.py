# Generated by Django 5.1.4 on 2024-12-15 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='bio',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='currentCity',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='employer',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='facebook',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='github',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='homeState',
            field=models.CharField(blank=True, choices=[('AP', 'Andhra Pradesh'), ('AR', 'Arunachal Pradesh'), ('AS', 'Assam'), ('BR', 'Bihar'), ('CG', 'Chhattisgarh'), ('DL', 'Delhi'), ('GA', 'Goa'), ('GJ', 'Gujarat'), ('HR', 'Haryana'), ('HP', 'Himachal Pradesh'), ('JK', 'Jammu and Kashmir'), ('JH', 'Jharkhand'), ('KA', 'Karnataka'), ('KL', 'Kerala'), ('MP', 'Madhya Pradesh'), ('MH', 'Maharashtra'), ('MN', 'Manipur'), ('ML', 'Meghalaya'), ('MZ', 'Mizoram'), ('NL', 'Nagaland'), ('OD', 'Odisha'), ('PB', 'Punjab'), ('RJ', 'Rajasthan'), ('SK', 'Sikkim'), ('TN', 'Tamil Nadu'), ('TG', 'Telangana'), ('TR', 'Tripura'), ('UP', 'Uttar Pradesh'), ('UK', 'Uttarakhand'), ('WB', 'West Bengal'), ('AN', 'Andaman and Nicobar Islands'), ('CH', 'Chandigarh'), ('DN', 'Dadra and Nagar Haveli'), ('DD', 'Daman and Diu'), ('LD', 'Lakshadweep'), ('PY', 'Puducherry')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='homeTown',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='instagram',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='jobTitle',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='linkedIn',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='personalEmail',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='studyCenterCity',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='studyCenterName',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='studyCenterState',
            field=models.CharField(choices=[('BR', 'Bihar'), ('CG', 'Chhattisgarh'), ('CH', 'Chandigarh'), ('DL', 'Delhi'), ('GA', 'Goa'), ('GJ', 'Gujarat'), ('HR', 'Haryana'), ('JH', 'Jharkhand'), ('KA', 'Karnataka'), ('KL', 'Kerala'), ('MH', 'Maharashtra'), ('MP', 'Madhya Pradesh'), ('OD', 'Odisha'), ('PB', 'Punjab'), ('RJ', 'Rajasthan'), ('TG', 'Telangana'), ('TN', 'Tamil Nadu'), ('UK', 'Uttarakhand'), ('UP', 'Uttar Pradesh'), ('WB', 'West Bengal')], default='KL', max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='twitter',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='user',
            name='website',
            field=models.URLField(null=True),
        ),
    ]
