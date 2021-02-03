from django.test import TestCase
from .models import Customer, Product, Order, OrderId
from datetime import date


class CustomerTest(TestCase):
    def setup_Customer(self):
        self.customer = Customer.objects.create(user="Bhanu", name="bhanu", email="bhanu@email.com")
        return self.customer.name

    def test_Customer(self):
        c = self.customer
        self.assertTrue(isinstance(c, self.customer))
        self.assertEqual(str(c), 'bhanu')


class ProductTest(TestCase):
    def setup_Product(self):
        self.product = Product.objects.create(name="mobile", price=15000, digitral=False)
        return self.product.name

    def test_Product(self):
        p = self.product
        self.assertTrue(isinstance(p, self.product))
        self.assertEqual(str(p), "mobile")


class OrderTest(TestCase):
    def setup_Order(self):
        self.c = Customer.object.get(pk=id)
        self.order = Order.objects.create(customer=self.c, date_ordered=date.today(), transaction_id=123456)
        return self.id()

    def test_Order(self):
        o = self.order
        self.assertEqual(isinstance(o, self.order))
        self.assertTrue(self.id(), o.id)


