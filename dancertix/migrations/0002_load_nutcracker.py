# Generated by Django 2.2.6 on 2019-10-24 01:32
from datetime import datetime, date
from django.db import migrations
from django.utils import timezone


def unload_performances(apps, schema_editor):
	Performance = apps.get_model('dancertix', 'Performance')
	low_date = timezone.make_aware(
		datetime.combine(
			date(year=2019, month=1, day=1),
			datetime.min
		)
	)
	high_date = timezone.make_aware(
		datetime.combine(
			date(year=2019, month=12, day=31),
			datetime.max
		)
	)
	Performance.objects.filter(
		title='The Nutcracker',
		start_date__gte=low_date,
		start_date__lte=high_date
	).all().delete()


def load_performances(apps, schema_editor):
	Venue = apps.get_model('dancertix', 'Venue')
	Performance = apps.get_model('dancertix', 'Performance')

	day_hourmin = [
		(7, 1400),
		(7, 1930),
		(8, 1400),
		(14, 1400),
		(14, 1930),
		(15, 1400),
	]
	performance_start_times = [
		timezone.make_aware(
			datetime(year=2019, month=12, day=day, hour=hourmin//100, minute=hourmin%100)
		)
		for day, hourmin in day_hourmin
	]
	venue, is_new = Venue.objects.get_or_create(
		name='F. Scott Fitzgerald Theatre',
    	location='630 Edmunston Dr., Rockville, MD 20851'
    )
	for start_time in performance_start_times:
		Performance.objects.create(
			title='The Nutcracker',
    		start_time=start_time,
    		duration=150,
    		venue=venue
		)


class Migration(migrations.Migration):

    dependencies = [
        ('dancertix', '0001_initial'),
    ]

    operations = [
    	migrations.RunPython(load_performances, unload_performances)
    ]
