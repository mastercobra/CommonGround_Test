from .serializers import ProductSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.exceptions import ParseError
from django.http import JsonResponse
from .models import Product
import json


class ProductApi(APIView):

    def post(self, request):
        try:
            serializer = ProductSerializer(data=request.data['products'], many=True)
        except ParseError as e:
            return JsonResponse({"Status": "Error", "Message": "Request body is not a json"},
                                status=status.HTTP_400_BAD_REQUEST)
        except KeyError as e:
            return JsonResponse({"Status": "Error", "Message": "Expecting key value: 'products'"},
                                status=status.HTTP_400_BAD_REQUEST)
        if serializer.is_valid(raise_exception=False):
            serializer.save()
            return JsonResponse({'status': 'OK'}, status=status.HTTP_201_CREATED)
        else:
            errors = serializer.errors
            validate_errors = []
            parse_errors = 0
            for error in errors:
                if len(error) != 0 and 'product_id' in error:
                    validate_errors.append(json.loads(json.dumps(error)))
                if len(error) != 0 and 'product_id' not in error:
                    parse_errors += 1
            error_response = {
                'status': 'Error',
                'products_report': validate_errors,
                'number_of_products_unable_to_parse': parse_errors
            }
            return JsonResponse(error_response, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


class GetProductApi(APIView):
    def get(self, request):
        products = Product.objects.all()
        data = [json.loads(str(product)) for product in products]
        return JsonResponse({'products': data}, status=status.HTTP_200_OK)