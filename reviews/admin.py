from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from .models import Review


class WordFilter(admin.SimpleListFilter):
    title = "Filter by words!"
    parameter_name = "potato"

    def lookups(self, request, model_admin) -> list[tuple[Any, str]]:
        return [
            ("good", "Good"),
            ("great", "Great"),
            ("awesome", "Awesome"),
        ]

    def queryset(self, request: Any, reviews) -> QuerySet[Any] | None:
        word = self.value()
        if word:
            return reviews.filter(payload__contains=word)
        else:
            return reviews


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("__str__", "payload")
    list_filter = ("rating",)
    list_filter = (
        WordFilter,
        "rating",
        "user__is_host",
        "room__category",
        "room__pet_friendly",
    )
