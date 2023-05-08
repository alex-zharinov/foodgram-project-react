from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from recipes.models import Recipe
from rest_framework import status
from rest_framework.response import Response
from users.models import Subscribe

User = get_user_model()


class MixinMethodPostDelete():
    def add_to(self, model_create, model_obj, serializer, pk, request):
        user = request.user
        obj = get_object_or_404(model_obj, id=pk)
        if model_obj == Recipe:
            if model_create.objects.filter(user=user, recipe__id=pk).exists():
                return Response(status=status.HTTP_400_BAD_REQUEST)
            model_create.objects.create(user=user, recipe=obj)
            serializer = serializer(obj)
        if model_obj == User:
            serializer = serializer(obj,
                                    data=request.data,
                                    context={"request": request})
            serializer.is_valid(raise_exception=True)
            Subscribe.objects.create(user=user, author=obj)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete_from(self, model_delete, model_obj, user, pk):
        if model_obj == Recipe:
            obj = model_delete.objects.filter(user=user, recipe__id=pk)
        if model_obj == User:
            author = get_object_or_404(model_obj, id=pk)
            obj = get_object_or_404(model_delete, user=user, author=author)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def post_delete_obj(
            self, model_target, model_obj, serializer, request, pk
    ):
        if request.method == 'POST':
            return self.add_to(
                model_target, model_obj, serializer, pk, request
            )
        return self.delete_from(model_target, model_obj, request.user, pk)
