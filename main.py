from pyscript import display, document

def calculate_total(e):
    document.getElementById('output').innerHTML = ''

    qty_item1 = int(document.getElementById('qty_item1').value)
    qty_item2 = int(document.getElementById('qty_item2').value)
    qty_item3 = int(document.getElementById('qty_item3').value)
    qty_item4 = int(document.getElementById('qty_item4').value)

    # Prices for each item
    price_item1 = 249.99  # Triple Patty Burger
    price_item2 = 299.99  # Seafood Pasta
    price_item3 = 399.99  # Grilled Salmon
    price_item4 = 199.99  # Red Velvet Lava Cake

    # Calculate total for each item
    total_item1 = qty_item1 * price_item1
    total_item2 = qty_item2 * price_item2
    total_item3 = qty_item3 * price_item3
    total_item4 = qty_item4 * price_item4

    overall_total = total_item1 + total_item2 + total_item3 + total_item4

    # Display the overall total
    display(f'PHP {overall_total:.2f}', target='output')

def refresh_order(e):
    document.getElementById('qty_item1').value = 0
    document.getElementById('qty_item2').value = 0
    document.getElementById('qty_item3').value = 0
    document.getElementById('qty_item4').value = 0
    document.getElementById('output').innerHTML = ''

document.getElementById('calculate_btn').onclick = calculate_total

document.getElementById('refresh_btn').onclick = refresh_order