
prices = {
    "pomarańcze": 0.99,
    "jogurt": 0.59,
    "mleko": 1.29,
    "jajka": 2.49 }
print("pomarańcze 0.99",
    "jogurt 0.59,"
    "mleko 1.29,"
    "jajka 2.49")


shopping_cart = []

while True:
    item = input("Wpisz nazwę produktu (lub wpisz 'koniec', aby zakończyć): ")
    
    if item == "koniec":
        break
    
    if item not in prices:
        print("Nie mamy tego produktu w sklepie.")
        continue
    
    price = prices[item]
    print(f"Dodaję {item} do koszyka za {price:.2f} zł")
    shopping_cart.append(price)

total_price = sum(shopping_cart)

print(f"Całkowita cena zakupów to: {total_price:.2f} zł")
