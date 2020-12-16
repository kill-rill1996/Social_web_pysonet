from rest_framework import mixins, viewsets, generics


class MixedPermission:
    """Миксин для action"""

    def get_permissions(self):
        try:
            return [permission for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
                return [permission() for permission in self.permission_classes]


class MixedPermissionViewSet(MixedPermission, viewsets.ViewSet):
    """Объединение нашего permission с вьюсетом"""
    pass


class MixedPermissionGenericViewSet(MixedPermission, viewsets.generics):
    """Объединение нашего permission с viewsets.generic"""
    pass


class CreateUpdateDestroyDS(mixins.CreateModelMixin,
                            mixins.UpdateModelMixin,
                            mixins.DestroyModelMixin,
                            MixedPermission,
                            viewsets.GenericViewSet):
    """Объединение нашего permission с viewset.generic и с миксинами"""
    pass


class CreateRetrieveUpdateDestroyDS(mixins.CreateModelMixin,
                                    mixins.RetrieveModelMixin,
                                    mixins.UpdateModelMixin,
                                    mixins.DestroyModelMixin,
                                    MixedPermission,
                                    viewsets.GenericViewSet):
    """Объединение нашего permission с viewset.generic и с миксинами(retrieve)"""
    pass


