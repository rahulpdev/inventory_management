'''
Create an application which manages an inventory of products.
Create a product class which has a price, id, and units on hand.
Then create an inventory class which keeps track of various products and can sum up the inventory value.
'''
from inspect import signature
import retail_stock_classes as retail


product1 = retail.Product('Joe Schmo','sku0001',25.99,234)
product2 = retail.Product('Jack Whack','sku0002',34.99,145)
product3 = retail.Product('Jane The','sku0003',13.99,3456)
product4 = retail.Product('Summit Patel','sku0004',114.99,24)
product5 = retail.Product('Stazy Joe','sku0005',28.99,267)
stock1 = retail.Stock('downtown',[product1,product2])
stock2 = retail.Stock('suburbs',[product3,product4,product5])
inventory1 = retail.Inventory('FurnitureRUs',[stock1,stock2])