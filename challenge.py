def linear_search_product(product_list, target_product):
    indices = []
    for i, product in enumerate(product_list):
        if product == target_product:
            indices.append(i)
    return indices

# Example usage:
products = ["Apple", "Banana", "Orange", "Banana", "Pear", "Banana"]
target = "Banana"
result = linear_search_product(products, target)
print(result)  # Output: [1, 3, 5]