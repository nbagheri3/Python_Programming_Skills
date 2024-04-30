# ----------------------------------------------------------------------
# Name:      store
# Purpose:   implement a online store
# Author(s): Nahal Bagheri and Dasom Lee
# ----------------------------------------------------------------------
"""
This program represents and manipulates items sold by a fictional online
    store.

Product is created with its description and price.
Products have their own id which is generated automatically.
Products also have attribute stock which indicates the number of items
    in stock.
Product class has lowest_price and average_rating properties.
Products have categories 'GN' for general product object, 'VG' for video
game object, 'BK' for book object, and 'BL' for bundle object.
Bundle products have a 20% discount on the normal price.
"""
import string

class Product:

    """
    Represents a Product.
    Arguments:
    description (string): description of a product.
    list_price (int): price of a product.
    Attribute:
    category (string): indicates the type of a product.
    next_serial_number (int): denotes the next available serial number
    in the category.
    """

    category = 'GN'
    next_serial_number = 1

    def __init__(self, description, list_price):
        self.description = description
        self.list_price = list_price
        self.id = self.generate_product_id()
        self.stock = 0
        self.sales = []
        self.reviews = []

    def restock(self, quantity):
        """
        Add quantity to its stock.
        :param quantity (int): the number of items you want to add to
            stock.
        :return: None
        """
        self.stock += quantity

    def review(self, stars, text):
        """
        Add/save reviews in tuple into reviews list.
        :param stars (int): the number of stars the review receives.
        :param text (string): the text review received.
        :return: None
        """
        self.reviews.append((text, stars))

    def sell(self, quantity, sale_price):
        """
        Add/save the sold item's price into sales list to track.
        :param quantity (int): the number of items sold.
        :param sale_price (float): price of item sold in US dollars.
        :return: None
        """
        if quantity > self.stock:
            quantity = self.stock
        self.sales.extend([sale_price] * quantity)
        self.stock -= quantity

    @classmethod
    def generate_product_id(cls):
        """
        Generate product id for products.
        :return id (string): independent id generated.
        """
        id = f"{cls.category}{cls.next_serial_number:06}"
        cls.next_serial_number += 1
        return id

    def __str__(self):
        return f"{self.description}\nProduct ID: {self.id}\nList " \
               f"price: ${self.list_price:.2f}\nAvailable in stock: " \
               f"{self.stock}"

    def __add__(self, other):
        return Bundle(self,other)

    @property
    def lowest_price(self):
        """
        Find the lowest price of a product.
        :return: minimum value of sales if there is anything in
            sales list.
        """
        if self.sales:
            return min(self.sales)

    @property
    def average_rating(self):
        """
        Find the average rating.
        :return: the sum  of reviews if there is anything in
            sum list.
        """
        if self.reviews:
            return sum([review[1] for review in self.reviews]) / len(
                self.reviews)

class VideoGame(Product):

    """
    Represents a video game product.
    Arguments:
    description (string): description of a product.
    list_price (int): price of a product.
    Attribute:
    category (string): indicates the type of a product.
    next_serial_number (int): denotes the next available serial number
    in the category.
    """

    category = 'VG'
    next_serial_number = 1

    def __init__(self, description, list_price):
        super().__init__(description, list_price)

class Book(Product):

    """
    Represents a book Product.
    Arguments:
    description (string): description of a product.
    list_price (int): price of a product.
    author (string): the author of a book product.
    pages (int): the page number of a book product.
    Attribute:
    category (string): indicates the type of a product.
    next_serial_number (int): denotes the next available serial number
    in the category.
    """

    category = 'BK'
    next_serial_number = 1

    def __init__(self, description, author, pages, list_price):
        super().__init__(description, list_price)
        self.author = author
        self.pages = pages

    def __lt__(self, other):
        return self.pages < other.pages

    def __le__(self, other):
        return self.pages <= other.pages

    def __eq__(self, other):
        return self.pages == other.pages

class Bundle(Product):

    """
    Represents the bundle of products with more than 2 products.
    Arguments:
    products (object): at least 2 product objects or more.
    Attribute:
    category (string): indicates the type of a product.
    next_serial_number (int): denotes the next available serial number
        in the category.
    bundle_discount (int): to calculate the 20% discount.
    """

    category = 'BL'
    next_serial_number = 1
    bundle_discount = 20

    def __init__(self, product1, product2, *rest):
        self.products = [product1, product2] + list(rest)
        description = " & ".join(p.description for p in self.products)
        list_price = sum(p.list_price for p in self.products) * (
                    1 - self.bundle_discount * 0.01)
        super().__init__(description, list_price)

# for test
def main():
    # Step 1 test
    sunglasses = Product('Vans Hip Cat Sunglasses', 14)
    print(Product.category)

    print(Product.next_serial_number)

    print(sunglasses.id)

    print(sunglasses.description)

    print(sunglasses.list_price)

    print(sunglasses.stock)

    print(sunglasses.reviews)

    print(sunglasses.sales)

    headphones = Product('Apple Airpods Pro', 199)
    sunglasses.restock(20)
    headphones.restock(5)
    print(sunglasses)

    print(headphones)

    sunglasses.sell(3, 14)
    sunglasses.sell(1, 10)
    print(sunglasses.sales)

    headphones.sell(8, 170)  # There are only 5 available
    print(headphones.sales)

    print(sunglasses)

    print(headphones)

    sunglasses.restock(10)
    print(sunglasses)

    headphones.restock(20)
    print(headphones)

    sunglasses.review(5, 'Great sunglasses! Love them.')
    sunglasses.review(3, 'Glasses look good but they scratch easily')
    headphones.review(4, 'Good but expensive')
    print(sunglasses.reviews)

    print(headphones.reviews)

    print(Product.category)

    print(Product.next_serial_number)

    print('-'*100)
    # Step 2 test
    print(sunglasses.lowest_price)

    print(sunglasses.average_rating)

    backpack = Product('Nike Explore', 60)
    print(backpack.average_rating)

    print(backpack.lowest_price)

    print('-' * 100)
    # Step 3 test
    mario = VideoGame('Mario Tennis Aces', 50)
    mario.restock(10)
    mario.sell(3, 40)
    mario.sell(4, 35)
    print(mario)

    print(mario.lowest_price)

    mario.review(5, 'Fun Game!')
    mario.review(3, 'Too easy')
    mario.review(1, 'Boring')

    print(mario.average_rating)

    lego = VideoGame('LEGO The Incredibles', 30)
    print(lego)

    lego.restock(5)
    lego.sell(10, 20)
    print(lego)

    print(lego.lowest_price)

    print(VideoGame.category)

    print(VideoGame.next_serial_number)

    print('-' * 100)
    # Step 4 test
    book1 = Book('The Quick Python Book', 'Naomi Ceder', 472, 39.99)

    print(book1.author)

    print(book1.pages)

    book1.restock(10)
    book1.sell(3, 30)
    book1.sell(1, 32)
    book1.review(5, 'Excellent how to guide')
    print(book1)

    print(book1.average_rating)

    print(book1.lowest_price)

    book2 = Book('Learning Python', 'Mark Lutz', 1648, 74.99)
    book1.restock(20)
    book1.sell(2, 50)
    print(book2)

    print(book1 > book2)

    print(book1 < book2)

    print(Book.category)

    print(Book.next_serial_number)
    print('-' * 100)
    #Step 5 test

    bundle1 = Bundle(sunglasses, backpack, mario)
    print(bundle1)

    bundle1.restock(3)
    bundle1.sell(1, 90)
    print(bundle1)

    bundle1.sell(2, 95)
    print(bundle1)

    bundle1.restock(3)
    bundle1.sell(1, 90)
    print(bundle1)

    bundle1.sell(3, 95)
    print(bundle1)

    print(bundle1.lowest_price)

    bundle2 = Bundle(book1, book2)
    bundle2.restock(2)
    print(bundle2)

    print(Bundle.category)

    print(Bundle.next_serial_number)

    print(Bundle.bundle_discount)

    print('-' * 100)
    # Step 6 test
    back_to_school_bundle = backpack + book1
    print(back_to_school_bundle)

    best_bundle = sunglasses + headphones + book1 + mario
    print(best_bundle)

if __name__ == '__main__':
    main()