def shopping_cart_list_creation(ingredients):
    shopping_list = '\n'.join([
        f'{ingredient["ingredient__name"]} - {ingredient["amount"]} '
        f'{ingredient["ingredient__measurement_unit"]}'
        for ingredient in ingredients
    ])
    filename = 'shopping_list.txt'
    return filename, shopping_list
