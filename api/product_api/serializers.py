from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    id = serializers.CharField(max_length=250)

    class Meta:
        model = Product
        fields = '__all__'

    def create(self, validate_data):
        instance = Product()
        validate_data = validate_data['product']
        instance.id = validate_data.get('id')
        instance.name = validate_data.get('name')
        instance.value = validate_data.get('value')
        instance.discount_value = validate_data.get('discount_value')
        instance.stock = validate_data.get('stock')
        instance.save()
        return instance

    def validation_name(self, data):
        len_name = len(data)
        if len_name < 3 or len_name > 55:
            return {'status': 'error', 'message': 'Invalid product name'}
        else:
            return {'status': 'success'}

    def validation_value(self, data):
        if data <= 0 or data >= 99999.9:
            return {'status': 'error', 'message': 'Invalid value'}
        else:
            return {'status': 'success'}

    def validation_stock(self, data):
        if data <= -1:
            return {'status': 'error', 'message': 'Invalid stock value'}
        else:
            return {'status': 'success'}

    def validation_discount_value(self, data_value, data_discount_value):
        if data_discount_value >= data_value:
            return {'status': 'error', 'message': 'Invalid discount value'}
        else:
            return {'status': 'success'}

    def validation_id(self, data):
        if len(Product.objects.filter(id=data)) != 0:
            return {'status': 'error', 'message': 'Invalid id'}
        else:
            return{'status': 'sucesss'}

    def validate(self, data):
        errors = []
        validations = []
        validations.append(self.validation_id(data['id']))
        validations.append(self.validation_name(data['name']))
        validations.append(self.validation_stock(data['stock']))
        validations.append(self.validation_value(data['value']))
        validations.append(
            self.validation_discount_value(data['value'], data['discount_value']))

        for value in validations:
            if value['status'] == 'error':
                errors.append(value['message'])

        if len(errors) == 0:
            return {'status': 'Ok', 'product': data}
        else:
            raise serializers.ValidationError({'product_id': data['id'],
                                               'errors': errors})



