def get_prices():
    products = []
    store_prices = {}


    #ask for the number of products
    num_products = int(input("enter the number of products you want to compare :"))


    #ask for the store names
    num_stores = int(input("enter the number of stores you want to compare (2 or 3):  "))
    store_names = []

    for t in range(num_stores):
        store_name = input(f"enter the name of store {t + 1}:")
        store_names.append(store_name)


    #get the product names and their prices in each store
    for product_index in range(num_products):
        product_name =input(f"\nEnter product name {product_index + 1}:")
        products.append(product_name)
        product_prices = {}
        for store in store_names:
            price = float(input(f"enter the price of {product_name} at {store}:$"))
            product_prices[store] = price
        store_prices [product_name] = product_prices

    return store_prices, store_names, products

def print_comparison(store_prices, store_names, products):
    print("\nprice comprasion summary:\n")
    print(f"{'product':<20}", end=" ")

    #print the store names as headers
    for store in store_names:
        print(f"{store:<15}", end =" ")
    print()
    #print each product's prices
    for product in products:
        print(f"{product:<20}", end=" ")
        for store in store_names:
            print(f"${store_prices[product][store]:<15.2f}",end= " ")
        print()
def main():
    print("welcome to the price comparison program!")
    store_prices, store_names, products = get_prices()
    print_comparison(store_prices, store_names, products)
if __name__ == "__main__":
    main()


    



        