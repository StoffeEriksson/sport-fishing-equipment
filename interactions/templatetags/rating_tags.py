from django import template

register = template.Library()

@register.filter
def average_rating(ratings_queryset):
    if not ratings_queryset.exists():
        return 0
    total = sum(rating.score for rating in ratings_queryset)
    return round(total / ratings_queryset.count(), 1)

@register.filter
def to_int(value):
    try:
        return int(value)
    except (ValueError, TypeError):
        return 0
