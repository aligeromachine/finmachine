from django.http import JsonResponse, HttpRequest
# from api.back.v1.main import task_response

def content_respo(request: HttpRequest, *args, **kwargs):

    ls: list = [
        {
            "id": 1,
            "name": 'Wireless Mouse',
            "category": 'Electronics',
            "price": 29.99,
            "inStock": 'Yes',
            "rating": 4.5,
        },
        {
            "id": 2,
            "name": 'Bluetooth Keyboard',
            "category": 'Electronics',
            "price": 49.99,
            "inStock": 'Yes',
            "rating": 4.0,
        },
        {
            "id": 3,
            "name": 'HD Monitor',
            "category": 'Electronics',
            "price": 199.99,
            "inStock": 'No',
            "rating": 4.8,
        },
        {
            "id": 4,
            "name": 'Office Chair',
            "category": 'Furniture',
            "price": 150.0,
            "inStock": 'Yes',
            "rating": 4.3,
        },
        {
            "id": 5,
            "name": 'Desk Lamp',
            "category": 'Furniture',
            "price": 25.99,
            "inStock": 'No',
            "rating": 4.7,
        },
    ]

    return JsonResponse(ls, safe=False)
