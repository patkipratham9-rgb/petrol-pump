def calculate_fuel_cost(litres, price_per_litre):
    return litres * price_per_litre


if __name__ == "__main__":
    fuel_type = input("Fuel type (Petrol / Diesel): ")
    litres = float(input("Quantity in litres: "))
    price_per_litre = float(input("Price per litre (₹): "))

    total_cost = calculate_fuel_cost(litres, price_per_litre)

    print("\n--- Fuel Bill Summary ---")
    print("Fuel Type:", fuel_type)
    print("Quantity (Litres):", litres)
    print("Price per Litre: ₹", price_per_litre)
    print("Total Fuel Cost: ₹", total_cost)