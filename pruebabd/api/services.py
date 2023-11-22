from .models import *

class CategoryService():
    def get_all():
        return Category.objects.all()
    
    def fitrarComienzaCon(letra):
        return Category.objects.filter(category_name__startswith = letra)
    
    def fitrarTerminaCon(letra):
        return Category.objects.filter(category_name__endswith = letra)

    def create_object(data):
        return Category.objects.create(**data)

    def delete_object(id):
        return Category.objects.filter(id=id).remove()

    def contains(data):
        return Category.objects.filter(category_name__contains=data)
    
    def mayor_que(field_name, value):
        filter_args = {f"{field_name}__gt": value}
        return Category.objects.filter(**filter_args)

    def mayor_igual(field_name, value):
        filter_args = {f"{field_name}__gte": value}
        return Category.objects.filter(**filter_args)

    def menor_que(field_name, value):
        filter_args = {f"{field_name}__lt": value}
        return Category.objects.filter(**filter_args)

    def menor_igual(field_name, value):
        filter_args = {f"{field_name}__lte": value}
        return Category.objects.filter(**filter_args)

    def first():
        return Category.objects.all().first()

    def last():
        return Category.objects.all().last()
    



class CustomerService():
    def get_all():
        return Customer.objects.all()
    
    def fitrarComienzaCon(letra):
        return Customer.objects.filter(contact_name__startswith = letra)
    
    def fitrarTerminaCon(letra):
        return Customer.objects.filter(contact_name__endswith = letra)

    def create_object(data):
        return Customer.objects.create(**data)

    def delete_object(id):
        return Customer.objects.filter(id=id).remove()

    def contains(data):
        return Customer.objects.filter(contact_name__contains=data)
    
    def mayor_que(field_name, value):
        filter_args = {f"{field_name}__gt": value}
        return Customer.objects.filter(**filter_args)

    def mayor_igual(field_name, value):
        filter_args = {f"{field_name}__gte": value}
        return Customer.objects.filter(**filter_args)

    def menor_que(field_name, value):
        filter_args = {f"{field_name}__lt": value}
        return Customer.objects.filter(**filter_args)

    def menor_igual(field_name, value):
        filter_args = {f"{field_name}__lte": value}
        return Customer.objects.filter(**filter_args)

    def first():
        return Customer.objects.all().first()

    def last():
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




class ProductService():
    def get_all():
        return Product.objects.all()
    
    def fitrarComienzaCon(letra):
        return Product.objects.filter(product_name__startswith = letra)
    
    def fitrarTerminaCon(letra):
        return Product.objects.filter(product_name__endswith = letra)

    def create_object(data):
        return Product.objects.create(**data)

    def delete_object(id):
        return Product.objects.filter(id=id).remove()

    def contains(data):
        return Product.objects.filter(product_name__contains=data)
    
    def mayor_que(field_name, value):
        filter_args = {f"{field_name}__gt": value}
        return Product.objects.filter(**filter_args)

    def mayor_igual(field_name, value):
        filter_args = {f"{field_name}__gte": value}
        return Product.objects.filter(**filter_args)

    def menor_que(field_name, value):
        filter_args = {f"{field_name}__lt": value}
        return Product.objects.filter(**filter_args)

    def menor_igual(field_name, value):
        filter_args = {f"{field_name}__lte": value}
        return Product.objects.filter(**filter_args)

    def first():
        return Product.objects.all().first()

    def last():
        return Product.objects.all().last()
    



class SupplierService():
    def get_all():
        return Supplier.objects.all()
    
    def fitrarComienzaCon(letra):
        return Supplier.objects.filter(contact_name__startswith = letra)
    
    def fitrarTerminaCon(letra):
        return Supplier.objects.filter(contact_name__endswith = letra)

    def create_object(data):
        return Supplier.objects.create(**data)

    def delete_object(id):
        return Supplier.objects.filter(id=id).remove()

    def contains(data):
        return Supplier.objects.filter(contact_name__contains=data)
    
    def mayor_que(field_name, value):
        filter_args = {f"{field_name}__gt": value}
        return Supplier.objects.filter(**filter_args)

    def mayor_igual(field_name, value):
        filter_args = {f"{field_name}__gte": value}
        return Supplier.objects.filter(**filter_args)

    def menor_que(field_name, value):
        filter_args = {f"{field_name}__lt": value}
        return Supplier.objects.filter(**filter_args)

    def menor_igual(field_name, value):
        filter_args = {f"{field_name}__lte": value}
        return Supplier.objects.filter(**filter_args)

    def first():
        return Supplier.objects.all().first()

    def last():
        return Supplier.objects.all().last()