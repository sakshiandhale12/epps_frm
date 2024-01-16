# queries.py
from .models import PiAddress
from django.db.models import Max


def get_api(data):
    filters = {key: value for key, value in data.items() if key in ["id", "addtype", "address", "city"]}
    
    if not any(filters.values()):
        queryset = PiAddress.objects.all()
    else:
        queryset = PiAddress.objects.filter(**filters)

    result = list(queryset.values())
    return result

def post_api(data):
    try:
        new_highest_id = PiAddress.objects.aggregate(Max('id'))['id__max'] or 0

        new_address = PiAddress.objects.create(
            id=new_highest_id + 1,
            addtype=data['addtype'],
            address=data['address'],
            city=data['city']
        )
    except Exception as e:
        print("Error:", e)
        return "error"

    return "ok"

def put_api(data):
    try:
        pi_address = PiAddress.objects.get(id=data['id'])
        pi_address.addtype = data['addtype']
        pi_address.address = data['address']
        pi_address.city = data['city']
        pi_address.save()
    except Exception as e:
        print("Error:", e)
        return "error"

    return "ok"
