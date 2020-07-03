# CommonGround_Test
BackEnd Engineer Test

Enpoints:
POST api/products/bulk_insert
GET api/products

Test with curl:

Case 1: 
All products correct

curl -d '{"products": [{"id": "first_id","name": "nombre id","value": 50,"discount_value": 10,"stock": 1},{"id": "second_id","name": "nombre id dos","value": 60,"discount_value": 20,"stock": 0}]}' -H "Content-Type:application/json" -X POST http://new-django-env.eba-23xez4hn.us-west-2.elasticbeanstalk.com/api/products/bulk_insert

Response
{"status": "OK"}

Case 2:
All products with validations errors

curl -d '{"products": [{"id": "third_id","name": "no","value": -50,"discount_value": 50,"stock": -1},{"id": "sku_34","name": "nombre id dos","value": 60,"discount_value": 80,"stock": 0}]}' -H "Content-Type:application/json" -X POST http://new-django-env.eba-23xez4hn.us-west-2.elasticbeanstalk.com/api/products/bulk_insert

Response

{"status": "Error", "products_report": [{"product_id": ["third_id"], "errors": ["Invalid product name", "Invalid stock value", "Invalid value", "Invalid discount value"]}, {"product_id": ["sku_34"], "errors": ["Invalid discount value"]}], "number_of_products_unable_to_parse": 0}

Case 3:
Request with products unable to parse:

curl -d '{"products": [{"id": "third_id","nam": "no","value": -50,"discount_value": 50,"stock": -1},{"id": "sku_34","name": "nombre id dos","value": 60,"discount_value": 40,"stock": 0}]}' -H "Content-Type:application/json" -X POST http://new-django-env.eba-23xez4hn.us-west-2.elasticbeanstalk.com/api/products/bulk_insert

Response:
{"status": "Error", "products_report": [], "number_of_products_unable_to_parse": 1}
