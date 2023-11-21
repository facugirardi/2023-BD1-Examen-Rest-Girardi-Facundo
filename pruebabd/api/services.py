from .models import *


class CustomerService():
    def get_all(self):
        return Customer.objects.all()
    
    def fitrarComienzaCon(self, letra):
        return Customer.objects.filter(contact_name__startswith = letra)
    
    def fitrarTerminaCon(self, letra):
        return Customer.objects.filter(contact_name__endswith = letra)

    def create_object(self, data):
        return Customer.objects.create(**data)

    def delete_object(self, id):
        return Customer.objects.filter(id=id).remove()

    def contains(self, data):
        return Customer.objects.filter(contact_name__contains=data)
    
    def mayor_que(self, field_name, value):
        filter_args = {f"{field_name}__gt": value}
        return Customer.objects.filter(**filter_args)

    def mayor_igual(self, field_name, value):
        filter_args = {f"{field_name}__gte": value}
        return Customer.objects.filter(**filter_args)

    def menor_que(self, field_name, value):
        filter_args = {f"{field_name}__lt": value}
        return Customer.objects.filter(**filter_args)

    def menor_igual(self, field_name, value):
        filter_args = {f"{field_name}__lte": value}
        return Customer.objects.filter(**filter_args)

    def first(self):
        return Customer.objects.all().first()

    def last(self):
        return Customer.objects.all().last()


    # Customer.objects.filter(id=10).update(phone_number='987654321')
    # Customer.objects.create(first_name='Joel', country='Canada')
    # Customer.objects.filter(fk__first_name__contains='Joel')
    # Customer.objects.values('phone_number').all()
    # Customer.objects.filter(date_field__year=year)
    # Customer.objects.filter(date_field__month=month)
    # Customer.objects.filter(date_field__day=day)
    # Customer.objects.filter(Q(country='Canada') | Q(country='Netherlands'))
    # Customer.objects.all()[:5]
    # Customer.objects.all().order_by('country') --> ascendente
    # Customer.objects.all().order_by('-country') --> descendente

    # date_value = datetime.strptime(gt, '%Y-%m-%d').date()
    # Customer.objects.filter(date_field__gt=date_value)

