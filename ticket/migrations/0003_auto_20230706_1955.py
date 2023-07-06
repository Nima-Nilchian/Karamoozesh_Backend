# Generated by Django 3.2 on 2023-07-06 16:25

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_user_is_consultant'),
        ('consultation', '0001_initial'),
        ('ticket', '0002_remove_ticket_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='qa',
            name='ticket_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='QA', to='ticket.ticket'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ticket',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, null=True, validators=[django.core.validators.RegexValidator(message='the phone number is wrong!', regex='^(09|\\+989)\\d{9}$')]),
        ),
        migrations.AlterField(
            model_name='qa',
            name='consultant_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='QA', to='consultation.consultant'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='qa',
            name='user_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='QA', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
