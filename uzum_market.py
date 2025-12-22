import psycopg2


def get_connection():
    return psycopg2.connect(
        dbname="market",
        user="postgres",
        password="A0B1D9E2",
        host="localhost",
        port=5432
    )


def see():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM product")
    data = cursor.fetchall()

    for d in data:
        print(f"id: {d[0]} | title: {d[1]} | price: {d[2]}")

    cursor.close()
    connection.close()


def add_product(title, price):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO product (title, price)
        VALUES (%s, %s)
    """, (title, price))

    connection.commit()
    cursor.close()
    connection.close()

    print("Product added")


def update_product(product_id, new_price):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE product
        SET price = %s
        WHERE id = %s
    """, (new_price, product_id))

    connection.commit()
    cursor.close()
    connection.close()

    print("Product updated")


def work():
    while True:
        print("""
1 - See products
2 - Add product
3 - Update product
0 - Exit
        """)

        option = input("Choose: ")

        if option == "1":
            see()

        elif option == "2":
            title = input("Enter product title: ")
            price = float(input("Enter product price: "))
            add_product(title, price)

        elif option == "3":
            product_id = int(input("Enter product id: "))
            new_price = float(input("Enter new price: "))
            update_product(product_id, new_price)

        elif option == "0":
            print("Bye")
            break

        else:
            print("Invalid option")

work()

