from menu import Pizza, Burger, Drinks, Menu
from Resturant import Resturant
from Resturant_management_project import Chef, Customer, Server, Manager
from order import Order

def main():
    menu = Menu()
    pizza_1 = Pizza('Shutki pizza', 600, 'large', ['shutki', 'onions'])
    menu.add_menu_items('pizza', pizza_1)
    pizza_2 = Pizza('Alur vorta pizza', 400, 'large', ['potato', 'onions', 'oil'])
    menu.add_menu_items('pizza', pizza_2)
    pizza_3 = Pizza('Dal pizza', 500, 'large', ['Dal', 'onions', 'oil'])
    menu.add_menu_items('pizza', pizza_3)


    # adding burger to menu
    burger_1 = Burger('Naga Burger', 1000, 'chicken', ['bread', 'chili'])
    menu.add_menu_items('burger', burger_1)
    burger_2 = Burger('Beef Burger', 1200, 'beef', ['goru', 'haddi'])
    menu.add_menu_items('burger', burger_2)
    

    #add drinks to menu 
    coke = Drinks('coke', 50 , True)
    menu.add_menu_items('drinks', coke)
    coffee = Drinks('Mocha Coffee', 300, False)
    menu.add_menu_items('drinks', coffee)

    # show menu
   # menu.show_menu()



    resturant = Resturant('sai baba resturent', 2000, menu)

    manager = Manager('Kalia Manager', 171003, 'kala@chan.com', 'kalia pur', 1500, 'jan 1, 2020', 'core' )
    resturant.add_employee('manager', manager)
    chef = Chef('Rustom Baburchi', 2263673, 'rustam@gamil.com', 'sokhi pur', 3500, 'Feb 22, 2020', 'chef', 'Everything')
    resturant.add_employee('chef', chef)
    server = Server('Chotu server', 2336738, 'chotu@gmail.com', 'aftaf nagar', 200, 'March 1, 2020', 'server')
    resturant.add_employee('server', server)

    # showing employees
    #resturant.show_employees()

    # customer 1 placing an order 
    customer_1 = Customer('Shakib', 6, 'king@khan.com', 'banani', 100000)
    order_1 = Order(customer_1, [pizza_3, coffee])
    customer_1.pay_for_order(order_1)
    resturant.add_orders(order_1)
    # customer_1 paying for order_1
    resturant.receive_payment(order_1, 200, customer_1)


    print( 'revenue and balance after 1st customer' ,resturant.revenue, resturant.balance)


    # customer 2 placing an order 
    customer_2 = Customer('Akib', 6, 'akib@khan.com', 'badda', 8000)
    order_2 = Order(customer_2, [pizza_2, coke])
    customer_2.pay_for_order(order_2)
    resturant.add_orders(order_2)
    # customer_1 paying for order_1
    resturant.receive_payment(order_2, 1000, customer_2)

    print( 'revenue and balance after 2nd customer' ,resturant.revenue, resturant.balance)


    # pay rent
    resturant.pay_expense(resturant.rent, 'Rent')
    print('after rent', resturant.revenue, resturant.balance, resturant.expense)

    resturant.pay_salary(chef)
    print('after salary', resturant.revenue, resturant.balance, resturant.expense)

# call the main
if __name__ == '__main__':
    main()