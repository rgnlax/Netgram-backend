import django_filters
from api.models import *
from rest_framework import filters


class NewsFilter(filters.FilterSet):
    before_id = django_filters.NumberFilter(name="id", lookup_type='lt')

    class Meta:
        model = News
        fields = ['id']

class EventsFilter(filters.FilterSet):
    before_id = django_filters.NumberFilter(name="id", lookup_type='lt')

    class Meta:
        model = Event
        fields = ['id']

class TimetableFilter(filters.FilterSet):
    group_id = django_filters.NumberFilter(name="group")

    class Meta:
        model = Timetable
        fields = ['group_id']
