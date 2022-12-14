import json

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from rest_framework.generics import CreateAPIView

from ads.models import Category
from ads.serializers import CategorySerializer


class CategoryListView(ListView):
    model = Category

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        categories = self.object_list.all()
        response = []
        for cat in categories:
            response.append({'id': cat.pk, 'name': cat.name, "slug": cat.slug})

        return JsonResponse(response, safe=False)


class CategoryCreateView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# @method_decorator(csrf_exempt, name="dispatch")
# class CategoryCreateView(CreateView):
#     model = Category
#     fields = ['name']
#
#     def post(self, request, *args, **kwargs):
#         super().post(request, *args, **kwargs)
#         data = json.loads(request.body)
#         cat = Category.objects.create(name=data['name'])
#         return JsonResponse({'id': cat.pk,
#                              'name': cat.name,
#                              'slug': cat.slug
#                              }, safe=False)


class CategoryDetailView(DetailView):
    model = Category

    def get(self, *args, **kwargs):
        cat = self.get_object()

        return JsonResponse({'id': cat.pk,
                             'name': cat.name
                             }, safe=False)


@method_decorator(csrf_exempt, name="dispatch")
class CategoryUpdateView(UpdateView):
    model = Category
    fields = ['name']

    def patch(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)

        data = json.loads(request.body)

        if 'name' in data:
            self.object.name = data['name']

        self.object.save()

        return JsonResponse({'id': self.object.pk,
                             'name': self.object.name
                             })


@method_decorator(csrf_exempt, name="dispatch")
class CategoryDeleteView(DeleteView):
    model = Category
    success_url = "/"

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)
        return JsonResponse({'status': 'ok'}, status=204)
