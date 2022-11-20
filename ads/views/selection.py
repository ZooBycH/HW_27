from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from ads.models import Selection
from ads.permissions import IsOwnerSelection
from ads.serializers import SelectionDetailSerializers, SelectionListSerializers, SelectionSerializers


class SelectionViewSet(ModelViewSet):
    queryset = Selection.objects.all()

    default_serializer = SelectionSerializers
    serializer_classes = {
        'list': SelectionListSerializers,
        'retrieve': SelectionDetailSerializers
    }

    default_permission = [AllowAny()]
    permission = {
        'create': [IsAuthenticated()],
        'update': [IsAuthenticated(), IsOwnerSelection()],
        'partial_update': [IsAuthenticated(), IsOwnerSelection()],
        'destroy': [IsAuthenticated(), IsOwnerSelection()],
    }

    def get_permissions(self):
        return self.permission.get(self.action, self.default_permission)

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer)
