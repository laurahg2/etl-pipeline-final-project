import src.extract as extract

def test_clear_orders():
    test_list = [
        {'date': '2021-02-23 17:59:04',
        'location': 'Isle of Wight',
        'order': ',Frappes - Coffee,2.75,, \
            Speciality Tea - Darjeeling,1.3,, \
            Smoothies - Berry Beautiful,2.0, \
            Large,Latte,2.45',
        'total': 8.5}
        ]
    
    expected = [
        {'date': '2021-02-23 17:59:04',
        'location': 'Isle of Wight',
        'order': 'Frappes - Coffee, \
            2.75,Speciality Tea - Darjeeling, \
            1.3,Smoothies - Berry Beautiful, \
            2.0,Large-Latte,2.45',
        'total': 8.5}
        ]
    
    actual = extract.clear_orders(test_list)
    
    assert expected == actual


def test_create_orders_dictionary():
    test_list = [
        {'date': '2021-02-23 17:59:04',
        'location': 'Isle of Wight',
        'order': 'Frappes - Coffee, \
            2.75,Speciality Tea - Darjeeling, \
            1.3,Smoothies - Berry Beautiful, \
            2.0,Large-Latte,2.45',
        'total': 8.5}
        ]
    
    expected = [
        {'date': '2021-02-23 17:59:04',
         'location': 'Isle of Wight',
         'order': [
             {'product_name': 'Frappes - Coffee',
              'product_price': '2.75',
              'product_size': 'Standard'},
             
             {'product_name': 'Speciality Tea - Darjeeling',
              'product_price': '1.3',
              'product_size': 'Standard'},
             
             {'product_name': 'Smoothies - Berry Beautiful',
              'product_price': '2.0',
              'product_size': 'Standard'},
             
             {'product_name': 'Latte',
              'product_price':'2.45',
              'product_size': 'Large'}
             ],
         'total': 8.5}
        ]

    actual = extract.create_orders_dictionary(test_list)
    
    assert expected == actual
         