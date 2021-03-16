import src.extract as extract

def test_split_product_size():
    test_list = [
        {'product_name': 'Smoothies - Berry Beautiful',
        'product_price': '2.0',
        'product_size': None},

        {'product_name': 'Large Latte',
        'product_price': '2.45',
        'product_size': None}
        ]

    expected = [
        {'product_name': 'Smoothies - Berry Beautiful',
        'product_price': '2.0',
        'product_size': None},

        {'product_name': 'Latte',
        'product_price': '2.45',
        'product_size': 'Large'}
        ]

    actual = extract.split_product_size(test_list)

    assert expected == actual