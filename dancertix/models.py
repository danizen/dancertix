from datetime import datetime

from django.db import models
from django.contrib.auth import get_user_model
from natural_keys import NaturalKeyModel


User = get_user_model()


class Dancer(NaturalKeyModel):
    display_name = models.CharField(max_length=120, unique=True, db_index=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    guardian = models.ManyToManyField(User)

    class Meta:
        db_table = 'dancers'

    def __str__(self):
        return self.display_name

    def __repr__(self):
        return '<Dancer: %s (%r)>' % (self.display_name, self.pk)


class Venue(NaturalKeyModel):
    name = models.CharField(max_length=50, unique=True, db_index=True)
    location = models.TextField()

    class Meta:
        db_table = 'venues'

    def __str__(self):
        return self.name

    def __repr__(self):
        return '<Venue: %s (%r)>' % (self.name, self.pk)


class Performance(NaturalKeyModel):
    title = models.CharField(max_length=50)
    start_time = models.DateTimeField()
    duration = models.IntegerField()
    venue = models.ForeignKey(Venue, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'performances'
        unique_together = [('title', 'start_time')]

    @property
    def when(self):
        return datetime.strftime(self.start_time, "%b-%d at %I:%M %p")

    def __str__(self):
        return '%s on %s' % (self.title, self.when)

    def __repr__(self):
        return '<Performance: %s on %s (%r)>' % (self.title, self.when, self.pk)


class Reservation(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    dancer = models.ForeignKey(Dancer, on_delete=models.CASCADE)
    performance = models.ForeignKey(Performance, on_delete=models.CASCADE)
    note = models.TextField()
    will_call = models.NullBooleanField()
    purchased = models.BooleanField(default=False)
    num_tickets = models.IntegerField()

    class Meta:
        db_table = 'reservations'

    def __repr__(self):
        return '<Reservation: %s, %d (%r)>' % (self.owner.name, self.num_tickets, self.pk)
