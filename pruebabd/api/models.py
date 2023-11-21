from django.db import models


class Category(models.Model):
    category_name = models.CharField(("Category Name:"), max_length=15)
    description = models.TextField(("Description:"))
    picture = models.BinaryField(("Picture:"))

    def __str__(self):
        return f"Category Name: {self.category_name}"


class Supplier(models.Model):
    company_name = models.CharField(("Company Name:"), max_length=40)
    contact_name = models.CharField(("Contact Name:"), max_length=30, null=True, blank=True)
    contact_title = models.CharField(("Nombre Estacion:"), max_length=30, null=True, blank=True) 
    address = models.CharField(("Nombre Estacion:"), max_length=60, null=True, blank=True)
    city = models.CharField(("Nombre Estacion:"), max_length=15, null=True, blank=True)
    region = models.CharField(("Nombre Estacion:"), max_length=15, null=True, blank=True)
    postal_code = models.CharField(("Nombre Estacion:"), max_length=10, null=True, blank=True)
    country = models.CharField(("Nombre Estacion:"), max_length=15, null=True, blank=True)
    phone = models.CharField(("Nombre Estacion:"), max_length=24, null=True, blank=True)
    fax = models.CharField(("Nombre Estacion:"), max_length=24, null=True, blank=True)
    homepage = models.TextField(("Nombre Estacion:"), null=True, blank=True)

    def __str__(self):
        return f"Supplier {self.id}"


class Product(models.Model):
    product_name = models.CharField(("Product Name:"), max_length=40)
    quantity_per_unit = models.CharField(("Quantity Per Unit:"), max_length=20, null=True, blank=True)
    unit_price = models.DecimalField(("Unit Price:"), max_digits=10, decimal_places=4, default=0)
    units_in_stock = models.SmallIntegerField(("Units In Stock:"), default=0)
    units_on_order = models.SmallIntegerField(("Units On Order:"), default=0)
    reorder_level = models.SmallIntegerField(("Reorder Level:"), default=0)
    discontinued = models.BooleanField(("Discontinued:"), default=False)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.product_name}"


class Customer(models.Model):
    company_name = models.CharField(("Company Name:"), max_length=40)
    contact_name = models.CharField(("Contact Name:"), max_length=30, null=True, blank=True)
    contact_title = models.CharField(("Contact Title:"), max_length=30, null=True, blank=True)
    address = models.CharField(("Address:"), max_length=60, null=True, blank=True)
    city = models.CharField(("City:"), max_length=15, null=True, blank=True)
    region = models.CharField(("Region:"), max_length=15, null=True, blank=True)
    postal_code = models.CharField(("Postal Code:"), max_length=10, null=True, blank=True)
    country = models.CharField(("Country:"), max_length=15, null=True, blank=True)
    phone = models.CharField(("Phone:"), max_length=24, null=True, blank=True)
    fax = models.CharField(("Fax:"), max_length=24, null=True, blank=True)

    def __str__(self):
        return f'{self.CustomerID} - {self.CompanyName}'


class Employee(models.Model):
    last_name = models.CharField(("Last Name:"), max_length=20)
    first_name = models.CharField(("First Name:"), max_length=10)
    title = models.CharField(("Title:"), max_length=30, null=True, blank=True)
    title_of_courtesy = models.CharField(("Title of Courtesy:"), max_length=25, null=True, blank=True)
    birth_date = models.DateTimeField(null=True, blank=True)
    hire_date = models.DateTimeField(null=True, blank=True)
    address = models.CharField(max_length=60, null=True, blank=True)
    city = models.CharField(max_length=15, null=True, blank=True)
    region = models.CharField(max_length=15, null=True, blank=True)
    postal_code = models.CharField(max_length=10, null=True, blank=True)
    country = models.CharField(max_length=15, null=True, blank=True)
    home_phone = models.CharField(max_length=24, null=True, blank=True)
    extension = models.CharField(max_length=4, null=True, blank=True)
    photo = models.BinaryField(null=True, blank=True)
    notes = models.TextField()
    reports_to = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    photo_path = models.CharField(max_length=255, null=True, blank=True)
    salary = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f'{self.EmployeeID} - {self.last_name}, {self.first_name}'


class Shipper(models.Model):
    company_name = models.CharField(max_length=40)
    phone = models.CharField(max_length=24, null=True, blank=True)

    def __str__(self):
        return f'{self.shipper_id} - {self.company_name}'


class Order(models.Model): 
    order_date = models.DateTimeField(null=True, blank=True)
    required_date = models.DateTimeField(null=True, blank=True)
    shipped_date = models.DateTimeField(null=True, blank=True)
    freight = models.DecimalField(max_digits=10, decimal_places=4, default=0)
    ship_name = models.CharField(max_length=40, null=True, blank=True)
    ship_address = models.CharField(max_length=60, null=True, blank=True)
    ship_city = models.CharField(max_length=15, null=True, blank=True)
    ship_region = models.CharField(max_length=15, null=True, blank=True)
    ship_postal_code = models.CharField(max_length=10, null=True, blank=True)
    ship_country = models.CharField(max_length=15, null=True, blank=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True, blank=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)
    ship_via = models.ForeignKey(Shipper, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.order_id} - {self.order_date}'


class OrderDetails(models.Model):
    unit_price = models.DecimalField(max_digits=10, decimal_places=4, default=0, null=False)
    quantity = models.SmallIntegerField(default=1, null=False)
    discount = models.FloatField(default=0, null=False)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.order_id} - {self.product_id}'




# Clase Region y Territorios


# class Region(models.Model):
#     region_description = models.CharField(max_length=50)

#     def __str__(self):
#         return f'{self.region_id} - {self.region_description}'


# class Territory(models.Model):
#     territory_description = models.CharField(max_length=50)
#     region_id = models.ForeignKey(Region, on_delete=models.CASCADE, null=True, blank=True)

#     def __str__(self):
#         return f'{self.territory_id} - {self.territory_description}'

