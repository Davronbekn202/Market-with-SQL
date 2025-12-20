import psycopg2


def get_connection():
    return psycopg2.connect(
        dbname="market",
        user='postgres',
        password="yourpassword",
        host='localhost',
        port=5432
    )


def create_table_product(user, parol):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""
    select * from users where username=%s and password=%s""", (user, parol))
    user = cursor.fetchone()
    if user:
        print(user)
    else:
        print("bunady malumot mavjud emas")


def add_category(titles):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""insert into category (title)
    values (%s)""", (titles,))
    connection.commit()
    print("yaratildi")


# add_category("sabzavodlar")

def get_cat():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""
    select * from category""")
    data = cursor.fetchall()
    for d in data:
        print(f"id {d[0]} title {d[1]}")


def add_product(title,description,price,quantity,cat_id):
    connection = get_connection()
    cursor = connection.cursor()
    get_cat()
    cursor.execute("""insert into product  (title,description,price,quantity,cat_id)
    values (%s,%s,%s,%s,%s)""",(title,description,price,quantity,cat_id))
    connection.commit()
    print(f"{title} qoshildi")

add_product("olma","shirin",10000,10,1)