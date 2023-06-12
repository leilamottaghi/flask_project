import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort
from flask import Flask
from flask import jsonify
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
options = Options()
from trendyol_one_link import make_ready_trendyol
from woocommerce import API

import boto3
import logging 

logging.basicConfig(level=logging.INFO)

try:
    s3_resource = boto3.resource(
        's3',
        endpoint_url='',
        aws_access_key_id='',
        aws_secret_access_key=''
    )
except Exception as exc:
    logging.info(exc)



# import boto3
# import logging
# from botocore.exceptions import ClientError


# logging.basicConfig(level=logging.INFO)

# try:
#     s3_resource = boto3.resource(
#         's3',
#         endpoint_url='https://s3.ir-thr-at1.arvanstorage.com',
#         aws_access_key_id='43ebc7d9-3d6c-4ced-beeb-61bb6152fa5c',
#         aws_secret_access_key='5b1c94bd24d791b2810f5512ba008ffa63776144b9035e57a7b019abc024ff75'
#     )
# except Exception as exc:
#     logging.error(exc)
# else:
#     try:
#         bucket_name = 'trendyolshahremun22'
#         bucket = s3_resource.Bucket(bucket_name)
#         bucket.create(ACL='public-read') # ACL='private'|'public-read'
#     except ClientError as exc:
#         logging.error(exc)




import boto3
import logging
from botocore.exceptions import ClientError

# Configure logging
def save_s3(image_string):
    logging.basicConfig(level=logging.INFO)
    images_list = image_string.split("|")
    for img in images_list:
        print("image path 000000000000000000+++***0000000000000000666",img)
        image = img.replace("\\","/")
        image_path = str(image)
        image_name1 = image_path.rfind("/") 
        image_name = image_path[image_name1:].replace("/","")
        try:
            s3_resource = boto3.resource(
                's3',
                endpoint_url='https://s3.ir-thr-at1.arvanstorage.com',
                aws_access_key_id='43ebc7d9-3d6c-4ced-beeb-61bb6152fa5c',
                aws_secret_access_key='5b1c94bd24d791b2810f5512ba008ffa63776144b9035e57a7b019abc024ff75'
            )

        except Exception as exc:
            logging.error(exc)
        else:
            try:
                bucket = s3_resource.Bucket('trendyolshahremun22')
                file_path = str(image_path)
                object_name = image_name

                with open(file_path, "rb") as file:
                    bucket.put_object(
                        ACL='public-read',
                        Body=file,
                        Key=object_name
                    )
            except ClientError as e:
                logging.error(e)




import boto3
import logging
from botocore.exceptions import ClientError
def get_images_from_s3(image_string):
    logging.basicConfig(level=logging.INFO)
    images_list = image_string.split("|")
    image_s3_list = []
    for img in images_list:
        # print("image path 0000000000000000000000000000000000666",img.replace("\\","/"))
        image = img.replace("\\","/")
        image_path =str(image)
        print("image_path --------------000000000000088",image_path)
        image_name1 = image_path.rfind("/") 
        image_name = image_path[image_name1:].replace("/","")

        file_path = image_path
        # object_name = image_name

        object_name = image_name
        download_path = file_path.replace("\\","/")
        print("download_pathwwwwww",download_path)
        try:
            s3_resource = boto3.resource(
                's3',
                endpoint_url='https://s3.ir-thr-at1.arvanstorage.com',
                aws_access_key_id='43ebc7d9-3d6c-4ced-beeb-61bb6152fa5c',
                aws_secret_access_key='5b1c94bd24d791b2810f5512ba008ffa63776144b9035e57a7b019abc024ff75'
            )
        except Exception as exc:
            logging.error(exc)
        else:
            try:
                # bucket
                bucket = s3_resource.Bucket('trendyolshahremun22')   
                try:
                    s3_resource = boto3.resource(
                        's3',
                        endpoint_url=settings.AWS_S3_ENDPOINT_URL,
                        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY
                    )

                except Exception as exc:
                    logging.info(exc)

                bucket.download_file(
                    object_name,
                    download_path
                )
            
                # logging.info(f"object_name: {bucket}")
                for obj in bucket.objects.all():
                    # logging.info(f"object_name: {obj.key}, last_modified: {obj.last_modified}")
                    # print("obj",obj.key)
                    obj_image = obj.key
                    if obj_image == image_name:
                        print("https://trendyolshahremun22.s3.ir-thr-at1.arvanstorage.com"+str(obj.key))
                        image_url_s3 = "https://trendyolshahremun22.s3.ir-thr-at1.arvanstorage.com"+"/"+str(obj.key)
                        # return image_url_s3
                        image_s3_list.append(image_url_s3)


            except ClientError as e:
                logging.error(e)

    print(image_s3_list)
    return image_s3_list



# import boto3
# import logging
# from botocore.exceptions import ClientError

# # Configure logging
# def get_images_s3(image_string):
#     logging.basicConfig(level=logging.INFO)

#     try:
#         # S3 resource
#         s3_resource = boto3.resource(
#             's3',
#             endpoint_url='https://s3.ir-thr-at1.arvanstorage.com',
#             aws_access_key_id='43ebc7d9-3d6c-4ced-beeb-61bb6152fa5c',
#             aws_secret_access_key='5b1c94bd24d791b2810f5512ba008ffa63776144b9035e57a7b019abc024ff75'
#         )

#     except Exception as exc:
#         logging.error(exc)
#     else:
#         try:
#             bucket_name = 'leilam3'
#             bucket = s3_resource.Bucket(bucket_name)

#             for obj in bucket.objects.all():
#                 logging.info(f"object_name: {obj.key}, last_modified: {obj.last_modified}")
#                 print("https://leilam3.s3.ir-thr-at1.arvanstorage.com/"+str(obj.key))
                

#         except ClientError as e:
#             logging.error(e)




wcapi = API(
	url="https://shahremun.com",
	consumer_key="ck_d06f06ed78809ba78c288ee7e34bb6dd729f5cdd",
	consumer_secret="cs_008d6ac981f1441351cead04a4106a13fe6410e0",
    version="wc/v3",
    timeout= 160
)






















import sqlite3
from urllib.request import Request, urlopen
import requests
import PIL
import numpy
from PIL import Image
from PIL import Image
import glob
import glob, os


def Convert_images_to_list():
	connection = sqlite3.connect("database.db")
	crsr = connection.cursor()
	crsr.execute('SELECT * FROM posts ')
	result = crsr.fetchall()
	barcode_list =[]
	for row in result:
		barcode = row[6]
		print(barcode)
		barcode_list.append(str(barcode).lower())
	image_list = []
	for barcode in barcode_list:
		image_str_list =[]		
		for file in glob.glob("img/%s"%(barcode)):
			for image in glob.glob("img/%s/*.jpeg"%(barcode)):
				image_str_list.append(image)
		# print(image_str_list)
		image_list.append(image_str_list)
		# images_str = "|".join(image_list)

	# print(image_list)
	# print(images_str)

	dict_images = dict(zip(barcode_list, image_list))
	print(dict_images)

def Convert(string):
    li = list(string.split("|"))
    return li
  
def download_images():
	connection = sqlite3.connect("database.db")
	crsr = connection.cursor()
	crsr.execute('SELECT * FROM posts ')
	result = crsr.fetchall()
	
	for row in result:
		image_list = row[14]
		barcode = row[6]
		try:
			if len(image_list) != 0:
				img_list = Convert(image_list)
				alphab = ['a','b','c','d','e','f','g','h','i','j','k','l']
				for img in img_list:
					print(img)
					if img != '':
						req = Request(str(img), headers={'User-Agent': 'Mozilla/5.0'})
						f = urlopen(req)
						parent_dir = "static/images/"
						directory = str(barcode)
						history_directoy = parent_dir + directory			
						if not os.path.isdir(history_directoy):
							path = os.path.join(parent_dir, directory)
							os.mkdir(path)
							print("Directory '%s' created" % directory)
						# with open(str(history_directoy)+"/"+"%s-lcwikiki-%s.webp"%(barcode,alphab[0]), "wb") as local_file:			
				
						with open(str(history_directoy)+"/"+"%s-trendyol-%s.jpeg"%(barcode,alphab[0]), "wb") as local_file:			
						# with open("img/%s/%s%s.jpeg"%(barcode,barcode,alphab[0]), "wb") as local_file:
							local_file.write(f.read())
						local_file.close()
						alphab.pop(0)
			else:
				break
				# continue
		except Exception as e:
			print(e)
	connection.commit()
	connection.close()










def Convert_images_to_list():
	connection = sqlite3.connect("database.db")
	crsr = connection.cursor()
	crsr.execute('SELECT * FROM posts ')
	result = crsr.fetchall()
	barcode_list =[]
	for row in result:
		barcode = row[6]
		print(barcode)
		barcode_list.append(barcode)
	image_list = []
	for barcode in barcode_list:
		image_str_list =[]		
		for file in glob.glob("static/images/%s"%(barcode)):
			for image in glob.glob("static/images/%s/*.jpeg"%(barcode)):
				image_str_list.append(image)
		# print(image_str_list)
		image_list.append(image_str_list)
		# images_str = "|".join(image_list)

	dict_images = dict(zip(barcode_list, image_list))
        
	return dict_images






def new_dict_sizeguide(dict_sizeguide,categori_id,brand_id):
	print("dict_sizeguide>>>",dict_sizeguide)
	new_dict_sizeguide={}
	for key,value in dict_sizeguide.items():
		new_dict = {}
		for key_value,value_value in value.items():
			print("key_value",key_value)
			for tuple_andis in key_value:
				new_dict[str(tuple_andis)]=str(value_value)
		new_dict_sizeguide[key]=new_dict
	try:	
		size_guid = new_dict_sizeguide[brand_id][categori_id]	
		return new_dict_sizeguide[brand_id][categori_id]
		
	except Exception as e:
		return None
		





def imageappender(images_string):
    img_json_list = []
    images_list = images_string
    for image_url in images_list:
        # image_img = "http://65.108.57.202/img/"+str(image_url)
        image_img = str(image_url)
        print(image_img)
        image = image_img.replace("\\","/").replace("static","") 
        print("qqqqqqqqqqqqqqqqqqqqqqq",str(image))
        img_json_list.append(str(image))
    return img_json_list



def image_string(image_strin):

    image_string = '|'.join(str(x) for x in image_strin)
    return image_string











def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?',
                        (post_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post


app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'


@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    return render_template('post.html', post=post)


@app.route('/buy_trendyol', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        content = request.form['content']
        
        if "trendyol" in str(content):

            conn = get_db_connection()
            conn.execute('INSERT INTO posts (link) VALUES (?)',
                            (content,))
            conn.commit()
            conn.close()

            conn = get_db_connection()
            id_create_product=conn.execute('SELECT * FROM posts  where link = ?',
                            (content,))
            id_product=id_create_product.fetchone()            
            print(id_product[0])

            conn.commit()
            conn.close()

            result =make_ready_trendyol(str(content),browser)
            # size_string,barcode,price,sales_price,title,slug,product_color,image_name,image_alt,image_list,gharanti,supplier,description
            sizes_available = result[0]
            barcode = result[1]
            price = result[2]
            sales_price = result[3]
            title = result[4]
            slug = result[5]
            product_color = result[6]
            image_name = result[7]
            image_alt = result[8]
            image_list = result[9]
            gharanti = result[10]
            supplier = result[11]
            descriptions = result[12]

            conn = get_db_connection()
            conn.execute('UPDATE posts SET sizes_available = ?,barcode = ?,price = ?,sales_price = ?,title = ?,slug = ?,image_name = ?,image_alt = ?,image_list = ?,gharanti = ?,supplier = ?,descriptions = ?'
                                ' WHERE link = ?',
                                (sizes_available,barcode,price,sales_price,title,slug,image_name,image_alt,image_list,gharanti,supplier,descriptions,content))
            conn.commit()
            conn.close()

            return redirect(url_for('product_detail',id=int(id_product[0])))
        else:
            # return jsonify(
            #     greeting=["hello", "world"],
            # )

            conn = get_db_connection()
            conn.execute('INSERT INTO posts (link) VALUES (?)',
                            (content,))
            conn.commit()
            conn.close()

            conn = get_db_connection()
            id_create_product=conn.execute('SELECT * FROM posts  where link = ?',
                            (content,))
            id_product=id_create_product.fetchone()            
            print(id_product[0])

            conn.commit()
            conn.close()

            conn = get_db_connection()
            conn.execute('UPDATE posts SET sizes_available = ?,barcode = ?,price = ?,sales_price = ?,title = ?,slug = ?,image_name = ?,image_alt = ?,image_list = ?,gharanti = ?,supplier = ?,descriptions = ?'
                                ' WHERE link = ?',
                                ("","",None,None,"","","","","","","","",content))
            conn.commit()
            conn.close()

            

            return redirect(url_for('any_product_detail',id=int(id_product[0])))

    return render_template('create.html')


@app.route('/buy_trendyol/<int:id>/any_product_detail', methods=('GET', 'POST'))
def any_product_detail(id):
    if request.method == 'POST':
        post = get_post(id)
        title = request.form['title']
        sales_price = int(request.form['sales_price'])
        sizes_available = request.form['sizes_available']
        descriptions = request.form['descriptions']
        description = descriptions

        if not title:
            flash('Title is required!')
        conn = get_db_connection()
        conn.execute('UPDATE posts SET descriptions =?,sizes_available=?,sales_price = ?,title = ?'
                            ' WHERE id = ?',
                            (descriptions,sizes_available,sales_price,title,id))
        conn.commit()
        conn.close()


        size_selected =sizes_available
        if size_selected:
            post = get_post(id)

            # conn = get_db_connection()
            # created_product=conn.execute('SELECT * FROM posts  where id = ?',
            #                 (id,))
            # barcode=created_product.fetchone()[6]
            barcode = "barcode"

            # conn = get_db_connection()
            # created_product=conn.execute('SELECT * FROM posts  where id = ?',
            #                 (id,))
            # size_list=created_product.fetchone()[4]
            size_list = size_selected

            # conn = get_db_connection()
            # created_product=conn.execute('SELECT * FROM posts  where id = ?',
            #                 (id,))
            # price=created_product.fetchone()[7]

            # conn = get_db_connection()
            # created_product=conn.execute('SELECT * FROM posts  where id = ?',
            #                 (id,))
            # sales_price=created_product.fetchone()[8]
            price = sales_price

            # conn = get_db_connection()
            # created_product=conn.execute('SELECT * FROM posts  where id = ?',
            #                 (id,))

            # # image_string2=created_product.fetchone()[18]
            # s3_save = save_s3(image_string2)
            # # input("s3_save")
            # images_from_s3 = get_images_from_s3(image_string2)  
            # print("images_from_s3 ===============",images_from_s3)
            # # # input("images_from_s3")


            # conn = get_db_connection()
            # created_product=conn.execute('SELECT * FROM posts  where id = ?',
            #                 (id,))
            # product_color=created_product.fetchone()[11]
            product_color = ""

            country=""
            # conn = get_db_connection()
            # created_product=conn.execute('SELECT * FROM posts  where id = ?',
            #                 (id,))
            # title=created_product.fetchone()[9]

            # conn = get_db_connection()
            # created_product=conn.execute('SELECT * FROM posts  where id = ?',
            #                 (id,))
            # slug=created_product.fetchone()[10]
            slug = "slug"

            # conn = get_db_connection()
            # created_product=conn.execute('SELECT * FROM posts  where id = ?',
            #                 (id,))
            # description=created_product.fetchone()[17]

            # conn = get_db_connection()
            # created_product=conn.execute('SELECT * FROM posts  where id = ?',
            #                 (id,))
            # gharanti=created_product.fetchone()[15]
            gharanti = ""

            # conn = get_db_connection()
            # created_product=conn.execute('SELECT * FROM posts  where id = ?',
            #                 (id,))
            # supplier=created_product.fetchone()[16]
            supplier = ""

            categorie_id=None

            # conn = get_db_connection()
            # created_product=conn.execute('SELECT * FROM posts  where id = ?',
            #                 (id,))
            # image_name=created_product.fetchone()[12]
            image_name = ""

            # conn = get_db_connection()
            # created_product=conn.execute('SELECT * FROM posts  where id = ?',
            #                 (id,))
            # image_alt=created_product.fetchone()[13]
            image_alt = ""

            image_guide_categori=""

            tag_name=""

            tag_slug=""

            tag_id=None



            attr_id = None
            wp_id= ""
            # new_json,p_variation = json_product()
            barcode_append = append_random_char(barcode)
            cur_barcode =barcode_append
            # cur_barcode =barcode
            product_color_final = [str(product_color)]
            images_from_s3 = ""
            new_json,p_variation = json_product(cur_barcode,tag_name,tag_slug,tag_id,"attributes","meta_data_product",image_guide_categori,product_color_final,gharanti,supplier,title,slug,description,image_name,image_alt,"country",images_from_s3, size_list, price,sales_price,attr_id)
            json_result = wcapi.post("products", new_json).json()
            print("json_result",json_result)
            if 'id' in json_result:
                wp_id = json_result['id']
                variation_result = wcapi.post("products/%s/variations" % wp_id, p_variation)
                print(variation_result)
                # brand = wcapi.put("products/%s" % wp_id , {'brands':'917'})
                # print("categorie_id")
                # category = wcapi.put("products/%s" % wp_id , {"categories": [{"id": 238}]})
                print("1111111111111111111133333333333333333333")


            json_result_slug =json_result['slug']

            product_link ='https://shahremun.com/product/'+ str(json_result_slug)+'/?attribute_pa_size='+str(size_selected)
            conn = get_db_connection()
            conn.execute('UPDATE posts SET shahremun_link = ?'
                                ' WHERE id = ?',
                                (product_link, id))
            conn.commit()
            conn.close()

            conn = get_db_connection()
            created_product=conn.execute('SELECT * FROM posts  where id = ?',
                            (id,))
            shahremun_product_link=created_product.fetchone()[5]
            # return shahremun_product_link
            return redirect(str(shahremun_product_link), code=302)
            


        return render_template('product_detail.html', post=post,sizes=sizes,size_selected=size_selected,barcode=barcode,price=price,sales_price=sales_price,title=title,product_color=product_color,image_list=images,descriptions=descriptions,gharanti=gharanti,supplier=supplier)



        return render_template('any_product_detail.html', post=post)
    return render_template('any_product_detail.html')


@app.route('/buy_trendyol/<int:id>/product_detail', methods=('GET', 'POST'))
def product_detail(id):
    post = get_post(id)

    # conn = get_db_connection()
    # content_product=conn.execute('SELECT * FROM posts  where id = ?',
    #                 (id,))
    # content=content_product.fetchone()            
    # browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    # result =make_ready_trendyol(str(content[2]),browser)
    # sizes = result

    conn = get_db_connection()
    created_product=conn.execute('SELECT * FROM posts  where id = ?',
                    (id,))
    sizes=created_product.fetchone()[3]
    conn = get_db_connection()
    created_product=conn.execute('SELECT * FROM posts  where id = ?',
                    (id,))
    barcode=created_product.fetchone()[6]
    conn = get_db_connection()
    created_product=conn.execute('SELECT * FROM posts  where id = ?',
                    (id,))
    price=created_product.fetchone()[7]
    conn = get_db_connection()
    created_product=conn.execute('SELECT * FROM posts  where id = ?',
                    (id,))
    sales_price=created_product.fetchone()[8]
    conn = get_db_connection()
    created_product=conn.execute('SELECT * FROM posts  where id = ?',
                    (id,))
    title = created_product.fetchone()[9]
    conn = get_db_connection()
    created_product=conn.execute('SELECT * FROM posts  where id = ?',
                    (id,))
    product_color=created_product.fetchone()[11]
    conn = get_db_connection()
    created_product=conn.execute('SELECT * FROM posts  where id = ?',
                    (id,))
    descriptions=created_product.fetchone()[17]
    conn = get_db_connection()
    created_product=conn.execute('SELECT * FROM posts  where id = ?',
                    (id,))
    gharanti =created_product.fetchone()[15]
    conn = get_db_connection()
    created_product=conn.execute('SELECT * FROM posts  where id = ?',
                    (id,))
    supplier =created_product.fetchone()[16]
    conn = get_db_connection()
    created_product=conn.execute('SELECT * FROM posts  where id = ?',
                    (id,))
    image_list=created_product.fetchone()[14]

    download_imagess = download_images()
    
    dict_images = Convert_images_to_list()
    image_strin = dict_images[barcode]

    images = imageappender(image_strin)

    images_str=image_string(image_strin)



    conn = get_db_connection()
    conn.execute('UPDATE posts SET image_string = ?'
                         ' WHERE id = ?',
                         (images_str, id))
    conn.commit()
    conn.close()

    size_select = request.form.get("radio_button_1")
    conn = get_db_connection()
    conn.execute('UPDATE posts SET size_selected = ?'
                         ' WHERE id = ?',
                         (size_select, id))
    conn.commit()
    conn.close()
    size_selected =size_select
    if size_selected:
        post = get_post(id)

        conn = get_db_connection()
        created_product=conn.execute('SELECT * FROM posts  where id = ?',
                        (id,))
        # size_selected=created_product.fetchone()[4]

    # ....
        conn = get_db_connection()
        created_product=conn.execute('SELECT * FROM posts  where id = ?',
                        (id,))
        barcode=created_product.fetchone()[6]

        conn = get_db_connection()
        created_product=conn.execute('SELECT * FROM posts  where id = ?',
                        (id,))
        size_list=created_product.fetchone()[4]

        conn = get_db_connection()
        created_product=conn.execute('SELECT * FROM posts  where id = ?',
                        (id,))
        price=created_product.fetchone()[7]

        conn = get_db_connection()
        created_product=conn.execute('SELECT * FROM posts  where id = ?',
                        (id,))
        sales_price=created_product.fetchone()[8]

        conn = get_db_connection()
        created_product=conn.execute('SELECT * FROM posts  where id = ?',
                        (id,))
                    
        image_string2=created_product.fetchone()[18]
        s3_save = save_s3(image_string2)
        # input("s3_save")
        images_from_s3 = get_images_from_s3(image_string2)  
        print("images_from_s3 ===============",images_from_s3)
        # input("images_from_s3")

        conn = get_db_connection()
        created_product=conn.execute('SELECT * FROM posts  where id = ?',
                        (id,))
        product_color=created_product.fetchone()[11]

        country=""
        conn = get_db_connection()
        created_product=conn.execute('SELECT * FROM posts  where id = ?',
                        (id,))
        title=created_product.fetchone()[9]

        conn = get_db_connection()
        created_product=conn.execute('SELECT * FROM posts  where id = ?',
                        (id,))
        slug=created_product.fetchone()[10]

        conn = get_db_connection()
        created_product=conn.execute('SELECT * FROM posts  where id = ?',
                        (id,))
        description=created_product.fetchone()[17]

        conn = get_db_connection()
        created_product=conn.execute('SELECT * FROM posts  where id = ?',
                        (id,))
        gharanti=created_product.fetchone()[15]

        conn = get_db_connection()
        created_product=conn.execute('SELECT * FROM posts  where id = ?',
                        (id,))
        supplier=created_product.fetchone()[16]

        categorie_id=None

        conn = get_db_connection()
        created_product=conn.execute('SELECT * FROM posts  where id = ?',
                        (id,))
        image_name=created_product.fetchone()[12]

        conn = get_db_connection()
        created_product=conn.execute('SELECT * FROM posts  where id = ?',
                        (id,))
        image_alt=created_product.fetchone()[13]

        image_guide_categori=""

        tag_name=""

        tag_slug=""

        tag_id=None



        attr_id = None
        wp_id= ""
        # new_json,p_variation = json_product()
        barcode_append = append_random_char(barcode)
        cur_barcode =barcode_append
        # cur_barcode =barcode
        product_color_final = [str(product_color)]
        new_json,p_variation = json_product(cur_barcode,tag_name,tag_slug,tag_id,"attributes","meta_data_product",image_guide_categori,product_color_final,gharanti,supplier,title,slug,description,image_name,image_alt,"country",images_from_s3, size_list, price,sales_price,attr_id)
        json_result = wcapi.post("products", new_json).json()
        print("json_result",json_result)
        if 'id' in json_result:
            wp_id = json_result['id']
            variation_result = wcapi.post("products/%s/variations" % wp_id, p_variation)
            print(variation_result)
            # brand = wcapi.put("products/%s" % wp_id , {'brands':'917'})
            # print("categorie_id")
            # category = wcapi.put("products/%s" % wp_id , {"categories": [{"id": 238}]})
            print("1111111111111111111133333333333333333333")


        json_result_slug =json_result['slug']

        product_link ='https://shahremun.com/product/'+ str(json_result_slug)+'/?attribute_pa_size='+str(size_selected)
        conn = get_db_connection()
        conn.execute('UPDATE posts SET shahremun_link = ?'
                            ' WHERE id = ?',
                            (product_link, id))
        conn.commit()
        conn.close()

        conn = get_db_connection()
        created_product=conn.execute('SELECT * FROM posts  where id = ?',
                        (id,))
        shahremun_product_link=created_product.fetchone()[5]
        # return shahremun_product_link
        return redirect(str(shahremun_product_link), code=302)
        


    return render_template('product_detail.html', post=post,sizes=sizes,size_selected=size_selected,barcode=barcode,price=price,sales_price=sales_price,title=title,product_color=product_color,image_list=images,descriptions=descriptions,gharanti=gharanti,supplier=supplier)




import string
import random
def append_random_char(barcode):
    string.ascii_letters
    random.choice(string.ascii_letters)
    barcode_curr = barcode+"-"+ str(random.choice(string.ascii_letters))
    return barcode_curr




def image_appender(images_from_s3,image_guide_categori,image_name,image_alt):
    img_json_list = []
    # images_list = images_from_s3.split("|")
    images_list = images_from_s3
    # images_list = ["https://trendyolshahremun22.s3.ir-thr-at1.arvanstorage.com/TTTBBK-siyah-trendyol-h.jpeg"]
    image_name =image_name
    image_alt = image_alt
    for image_url in images_list:
        image_img = str(image_url)
        print("image_url",image_url)
        # image_img = str(image_url)
        print(image_img)
        image = image_img.replace("\\","/")
        print("qqqqqqqqqqqqqqqqqqqqqqq",str(image))
        print("image_name",image_name)
        print("image_alt",image_alt)
        img_json_list.append({"src": image,"name": image_name,"alt": image_alt })
        print("image_url",image_url)
    return img_json_list



def tag_appender(tag_name,tag_slug,tag_id):
	if tag_name:
		tag_dict = {
			"id": tag_id,
			"name": str(tag_name),
			"slug": str(tag_slug)
		}

		return [tag_dict]
	else:
		return []
	

# def json_product():
def json_product(barcode,tag_name,tag_slug,tag_id,attributes,meta_data_product,image_guide_categori,product_color_final,gharanti,supplier,title,slug,description,image_name,image_alt,country,images_from_s3,size_list, price,sales_price,attr,on_sale = False):
    if price > sales_price:
        on_sale = True
    variation_data = {
        "regular_price" : str(price),
        "sale_price" : str(sales_price)
        }
    image_list = image_appender(images_from_s3,image_guide_categori,image_name,image_alt)
    # tag_list = tag_appender(tag_name, tag_slug, tag_id)
    data = {
        # "name":title +" "+(str(barcode[:barcode.find("-zard6")]))[:(str(barcode[:barcode.find("-zard6")])).rfind("-")].lower(),
        "name" : title,
        "slug":slug,    
        "sku": barcode,
        "shipping_class": "international-shipping",
        "shipping_class_id": 3830,
        "type": "variable",
        "status": "publish",
        # "status": "draft",
        "description": str(description),
        "managing_stock":True,
        "stock_quantity":2,
        "in_stock":True,
        # "tags": tag_list,
        "tags": [],
        "attributes": [
            {	
                "id": 23,
                "name": "size",
                "slug": "size",
                "visible": False,
                "variation": True,
                "options":[size_list]
            },
            {
            "id": 1,
            "name": "color",
            "slug": "pa_color",
            "position": 1,
            "type": "select",
            "visible": False,
            "variation": False,
            "options":product_color_final
            },
      
            {
            "id": 13,
            "name": "گارانتی",
            "slug": "pa_warranty",
            "type": "select",
            "visible": False,
            "variation": False,
            "options":[gharanti]
            },
            {
            "id": 25,
            "name": "تامین کننده",
            "slug": "pa_supplier",
            "type": "select",
            "visible": False,
            "variation": False,
            "options":[str(supplier)]
            }            	

        ],
        # "images": []
        "images": image_list
    }
    return data,variation_data










# @app.route('/<int:id>/add_to_cart', methods=('POST',))
def add_to_cart(id):
    post = get_post(id)

    conn = get_db_connection()
    created_product=conn.execute('SELECT * FROM posts  where id = ?',
                    (id,))
    size_selected=created_product.fetchone()[4]
# ....
    conn = get_db_connection()
    created_product=conn.execute('SELECT * FROM posts  where id = ?',
                    (id,))
    barcode=created_product.fetchone()[6]

    conn = get_db_connection()
    created_product=conn.execute('SELECT * FROM posts  where id = ?',
                    (id,))
    size_list=created_product.fetchone()[4]

    conn = get_db_connection()
    created_product=conn.execute('SELECT * FROM posts  where id = ?',
                    (id,))
    price=created_product.fetchone()[7]

    conn = get_db_connection()
    created_product=conn.execute('SELECT * FROM posts  where id = ?',
                    (id,))
    sales_price=created_product.fetchone()[8]

    conn = get_db_connection()
    created_product=conn.execute('SELECT * FROM posts  where id = ?',
                    (id,))
                
    image_string2=created_product.fetchone()[18]
    s3_save = save_s3(image_string2)
    # input("s3_save")
    images_from_s3 = get_images_from_s3(image_string2)  
    print("images_from_s3 ===============",images_from_s3)
    # input("images_from_s3")

    conn = get_db_connection()
    created_product=conn.execute('SELECT * FROM posts  where id = ?',
                    (id,))
    product_color=created_product.fetchone()[11]

    country=""
    conn = get_db_connection()
    created_product=conn.execute('SELECT * FROM posts  where id = ?',
                    (id,))
    title=created_product.fetchone()[9]

    conn = get_db_connection()
    created_product=conn.execute('SELECT * FROM posts  where id = ?',
                    (id,))
    slug=created_product.fetchone()[10]

    conn = get_db_connection()
    created_product=conn.execute('SELECT * FROM posts  where id = ?',
                    (id,))
    description=created_product.fetchone()[17]

    conn = get_db_connection()
    created_product=conn.execute('SELECT * FROM posts  where id = ?',
                    (id,))
    gharanti=created_product.fetchone()[15]

    conn = get_db_connection()
    created_product=conn.execute('SELECT * FROM posts  where id = ?',
                    (id,))
    supplier=created_product.fetchone()[16]

    categorie_id=None

    conn = get_db_connection()
    created_product=conn.execute('SELECT * FROM posts  where id = ?',
                    (id,))
    image_name=created_product.fetchone()[12]

    conn = get_db_connection()
    created_product=conn.execute('SELECT * FROM posts  where id = ?',
                    (id,))
    image_alt=created_product.fetchone()[13]

    image_guide_categori=""

    tag_name=""

    tag_slug=""

    tag_id=None



    attr_id = None
    wp_id= ""
    # new_json,p_variation = json_product()
    cur_barcode =barcode
    product_color_final = [str(product_color)]
    new_json,p_variation = json_product(cur_barcode,tag_name,tag_slug,tag_id,"attributes","meta_data_product",image_guide_categori,product_color_final,gharanti,supplier,title,slug,description,image_name,image_alt,"country",images_from_s3, size_list, price,sales_price,attr_id)
    json_result = wcapi.post("products", new_json).json()
    print("json_result",json_result)
    if 'id' in json_result:
        wp_id = json_result['id']
        variation_result = wcapi.post("products/%s/variations" % wp_id, p_variation)
        print(variation_result)
        # brand = wcapi.put("products/%s" % wp_id , {'brands':'917'})
        # print("categorie_id")
        # category = wcapi.put("products/%s" % wp_id , {"categories": [{"id": 238}]})
        print("1111111111111111111133333333333333333333")


    json_result_slug =json_result['slug']

    product_link ='https://shahremun.com/product/'+ str(json_result_slug)+'/?attribute_pa_size='+str(size_selected)
    conn = get_db_connection()
    conn.execute('UPDATE posts SET shahremun_link = ?'
                         ' WHERE id = ?',
                         (product_link, id))
    conn.commit()
    conn.close()

    conn = get_db_connection()
    created_product=conn.execute('SELECT * FROM posts  where id = ?',
                    (id,))
    shahremun_product_link=created_product.fetchone()[5]
    # return shahremun_product_link
    return redirect(str(shahremun_product_link), code=302)
    
























