import sqlite3
connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()
 
cur.execute("INSERT INTO posts (link,sizes_available,size_selected,shahremun_link, barcode,price,sales_price,title,slug,product_color,image_name,image_alt,image_list,gharanti,supplier,descriptions,image_string) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
            ( 'Content for the first post','sizes','my select size','shahremun link','barcode','price','sales_price','title','slug','product_color','image_name','image_alt','image_list','gharanti','supplier','descriptions','image_string')
            )

# cur.execute("INSERT INTO posts (title, content) VALUES ( ?)",
#             ( 'Content for the second post',)
#             )

connection.commit()
connection.close()