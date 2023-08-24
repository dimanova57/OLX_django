from django.contrib.auth.decorators import user_passes_test
from django.db.models import Q
from django.shortcuts import get_object_or_404

from shop_main.forms import ProductForm
from shop_main.models import Product


def get_filters_for_query(request):
    query = request.GET.get('query')
    category = request.GET.get('category')
    question_filter = {}

    if query:
        question_filter = (Q(description__icontains=query) | Q(title__icontains=query))

    if category:
        question_filter['category'] = category

    return question_filter


def product_by_query(request):
    from shop_main.models import Product

    question_filters = get_filters_for_query(request)
    if not question_filters:
        print('123')
        questions = Product.objects.all()[:10]
    elif type(question_filters) == Q:
        questions = Product.objects.filter(question_filters)
    else:
        questions = Product.objects.filter(**question_filters)

    return questions


# def get_object_by_name(name: str, record_id: int):
#     """This function is helping you find true object"""
#
#     mapping = {
#         'question': Question,
#         'answer': Answer,
#         'post': UserPost,
#     }
#     model = mapping.get(name)
#
#     return get_object_or_404(model, pk=record_id)

#
# def get_form_by_name(name: str):
#     """This function is helping you find true form"""
#
#     mapping = {
#         'question': QuestionForm,
#         'answer': AnswerForm,
#         'post': PostForm,
#     }
#
#     return mapping.get(name)
