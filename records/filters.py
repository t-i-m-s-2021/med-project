import django_filters

from records.models import Record


class RecordFilter(django_filters.FilterSet):
    class Meta:
        model = Record
        fields = ['fullname', 'description', 'localisation', 'author', 'created_at', 'updated_at']