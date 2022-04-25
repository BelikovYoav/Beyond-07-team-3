# Generated by Django 4.0.3 on 2022-04-24 07:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_add_possible_meeting_test_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='PossibleParticipant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('participant_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                 to='events.eventparticipant')),
                ('possible_meeting_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                 to='events.optionalmeetingdates')),
            ],
        ),
    ]
