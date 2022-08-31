from Homework.celery import app
from os.path import isfile
from orders.models import Order
from products.models import Product

filename = 'users_logs.txt'

if not isfile(filename):
    with open(filename, 'wt') as writer:
        writer.write('Users activity:\n\n')

@app.task
def user_record(user_agent, ip, now, place):
    ''' Record data about page visits to a file '''

    for_record = f'User {ip} at {now} visited {place} by browser {user_agent};\n'
    with open(filename, 'at') as writer:
        writer.write(for_record)


@app.task
def order_per_product():
    ''' Regular calculation of the ratio of orders and products '''
    try:
        products_count = Product.objects.count()
        orders_count = Order.objects.count()
    except Product.DoesNotExist:
        print('There are no products...')
    except Order.DoesNotExist:  
        print('There are no orders...') 
    else:
        correlation = round(orders_count / products_count, 1)
        if correlation > 3 :
            msg = 'Good work!'
        elif correlation > 1 :
            msg = 'It could be better...'
        else :
            msg = 'There will be no premium...'
        print(f'{correlation} orders per product. {msg}')
