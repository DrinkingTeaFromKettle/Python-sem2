from collections import namedtuple, defaultdict


def groupProducts(products):
    group_products = defaultdict(list)

    for product in products:
        group_products[product.name].append(product)
    print("Pogrupowane produkty: ")
    for name, product in group_products.items():
        print(name, "->", product)

    return group_products

if __name__ == '__main__':
    print("Lista produktów: \n")

    productTuple = namedtuple("Product", ["name", "price", "weight"])
    parmigiano = productTuple("parmigiano reggiano", 30.99, 0.2)
    cheddar = productTuple("cheddar", 12.99, 0.3)
    lazur_blue = productTuple("blue cheese", 8.99, 0.1)
    danish_blue = productTuple("blue cheese", 15.00, 0.15)
    print(parmigiano)
    print(cheddar)
    print(danish_blue)
    print(lazur_blue)
    products = [parmigiano, cheddar, danish_blue, lazur_blue]
    groupProducts(products)
