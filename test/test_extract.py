import src.extract as extract

def test_clear_orders():
    test_list = [
        {'order': ',Frappes - Coffee,2.75,,\
            Speciality Tea - Darjeeling,1.3,,\
            Smoothies - Berry Beautiful,2.0,\
            Large,Latte,2.45'}
        ]
    expected = [
        {'order': 'Frappes - Coffee,2.75,\
            Speciality Tea - Darjeeling,1.3,\
            Smoothies - Berry Beautiful,2.0,\
            Large-Latte,2.45'}
        ]

    actual = extract.clear_orders(test_list)

    assert expected == actual


def test_create_orders_dictionary():
    test_list = [
        {'order': 'Frappes - Coffee,2.75'}
        ]

    expected = [
        {'order': [
            {'product_name': 'Frappes - Coffee',
             'product_price': '2.75',
             'product_size': 'Standard'}]
         }]

    actual = extract.create_orders_dictionary(test_list)
    
    assert expected == actual
