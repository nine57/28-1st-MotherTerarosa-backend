import json
from json.decoder import JSONDecodeError

from django.http.response import JsonResponse
from django.views         import View

from orders.models         import Order_Product
from users.models          import User
from products.models       import Product
from utils.login_decorator import login_decorator

class OrderView(View):
    @login_decorator
    def post(self, request):
        try:
            data = json.loads(request.body)

            product_id = data['product_id']
            quantity   = data['quantity']

            users        = request.user
            points       = int(users.point)
            products     = Product.objects.get(id=product_id)
            total_price  = int(products.price) * int(quantity)
            remain_point = points - total_price

            if remain_point < 0:
                print('잔액 부족')
                return JsonResponse({"message" : "NOT_ENOUGH_POINT"}, status=400)

            Order_Product.objects.create(
                product_id  = product_id,
                quantity    = quantity,
                total_price = total_price
            )

            updated_user       = User.objects.get(id = users.id)
            updated_user.point = remain_point
            updated_user.save()

            user_data = {
                "user_name"  : users.name,
                "user_point" : remain_point
            }

            return JsonResponse({"result" : user_data}, status=200)

        except KeyError:
            return JsonResponse({"message" : "KEY_ERROR"}, status=400)
        except JSONDecodeError:
            return JsonResponse({"message" : "JSONDecodeError"}, status=400)
        except Product.DoesNotExist:
            return JsonResponse({"message" : "INVALID_PRODUCT"}, status=400)