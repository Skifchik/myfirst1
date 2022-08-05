from polls.models import Order as OrderModel
from django.forms import model_to_dict
from django.http import JsonResponse, HttpResponseBadRequest
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from json import loads


def orders_list(request):
    order_query = OrderModel.objects.all().values('id', 'user_id', 'order_info')
    total_size = order_query.count()
    orders = list(order_query)
    return JsonResponse({'orders': orders, 'total_size': total_size})


@method_decorator(csrf_exempt, name='dispatch')
class Order(View):
    def get(self, request):

        try:
            order_id = int(request.GET.get('order_id'))
            order = OrderModel.objects.get(id=order_id)
            return JsonResponse(model_to_dict(order))
        except(ValueError, OrderModel.DoesNotExist):
            return HttpResponseBadRequest()

    def post(self, reguest):
        status = 0
        post_body = loads(reguest.body)
        user_id = post_body.get('order_info')
        order_info = post_body.get('order_info')

        if user_id == 1:
            new_order = {'user_id': user_id, 'order_info': order_info}
            OrderModel.objects.create(**new_order)
            status = 1

        return JsonResponse({'status': status})
