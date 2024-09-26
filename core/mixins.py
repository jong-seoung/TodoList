from typing import Optional, Type

from django.db.models import QuerySet
from rest_framework.serializers import Serializer


class ActionBasedViewSetMixin:
    queryset_map = {}
    serializer_class_map = {}

    def get_queryset(self) -> QuerySet:
        qs: Optional[QuerySet] = self.queryset_map.get(self.action, None)
        if qs is not None:
            self.queryset = qs
        return super().get_queryset()

    def get_serializer_class(self) -> Type[Serializer]:
        cls: Optional[Type[Serializer]] = self.serializer_class_map.get(self.action, None)
        if cls is not None:
            self.serializer_class = cls
        return super().get_serializer_class()