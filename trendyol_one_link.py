import platform
from selenium import webdriver
import sys, os
sys.path.append(os.path.abspath(os.path.join('..')))
from dict_all_size_guide import dict_sizeguide
from setting import tl_price
from woocommerce import API
import json
import sqlite3
import requests
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument('--headless')
# options.binary_location='C:\Program Files\Google\Chrome Beta\Application\chrome.exe'
options.add_extension('../cyberghost.crx')
# #-------------------------------------------------------------------#
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--disable-dev-shm-usage')
# # chrome_options.add_argument("user-agent=whatever you want")
userAgent_list = [
'Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36',
'Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
'Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2919.83 Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2866.71 Safari/537.36',
'Mozilla/5.0 (X11; Ubuntu; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2820.59 Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2762.73 Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2656.18 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/44.0.2403.155 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.17 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.62 Safari/537.36',
'Mozilla/5.0 (X11; CrOS i686 4319.74.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.57 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1464.0 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36',
'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36',
'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11',
'Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11',
'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11','Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11',
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11',
'Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11',
'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_5_8) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11',

]
import random
userAgent = random.choice(userAgent_list)
# chrome_options.add_argument(f'user-agent={userAgent}')

# chrome_options.add_experimental_option( "prefs", {'profile.default_content_settings.images': 2})

if platform.system() == 'Windows':
    PHANTOMJS_PATH = './phantomjs.exe'
    CHROME_PATH = '../chromedriver.exe'
    FIREFOX_PATH = './firefox.exe'
else:
    PHANTOMJS_PATH = './phantomjs'
    CHROME_PATH = './chromedriver'
    FIREFOX_PATH = './firefox'




# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.options import Options
# options = Options()
# # options.binary_location='..\chromedriver'
# options.add_argument('headless')
# # options.add_experimental_option( "prefs", {'profile.default_content_settings.images': 2})






wcapi = API(
	url="https://shahremun.com",
	consumer_key="",
	consumer_secret="",
	# consumer_key="",
	# consumer_secret="",
    version="wc/v3",
    timeout= 160
)


conn_costdb = sqlite3.connect('../shipping_cost.db',check_same_thread=False)
c_cost = conn_costdb.cursor()
def create_tables_cost():
	c_cost.execute('''CREATE TABLE IF NOT EXISTS categori_sku
			 (id integer primary key, name text , slug text,id_categori integer ,cost integer)''')
# create_tables_cost()



conn_dictdb = sqlite3.connect('trendyol_dict.db')
# conn.text_factory = str
c_dict = conn_dictdb.cursor()
def create_tables_dict():

	c_dict.execute('''CREATE TABLE IF NOT EXISTS looper
			 (id integer primary key, name text UNIQUE, name_fa text ,category_id integer,warranty text)''')
	c_dict.execute('''CREATE TABLE IF NOT EXISTS color
			 (id integer primary key, tr text UNIQUE, fa text ,brandname_dict text)''')
	c_dict.execute('''CREATE TABLE IF NOT EXISTS material
			 (id integer primary key, tr text UNIQUE, fa text,brandname_dict text)''')
	c_dict.execute('''CREATE TABLE IF NOT EXISTS care
			 (id integer primary key, tr text UNIQUE, fa text,brandname_dict text)''')
	c_dict.execute('''CREATE TABLE IF NOT EXISTS description
			 (id integer primary key, tr text UNIQUE, fa text,brandname_dict text)''')

create_tables_dict()




# conn = sqlite3.connect('stock.db')
# c = conn.cursor()	
# def create_tables():
# 	c.execute('''CREATE TABLE IF NOT EXISTS urls
# 			 (id integer primary key, url text UNIQUE, barcode text,title text, categorie_id int,gharanti text,done int,tag_name text,tag_slug text,tag_id int)''')
# 	c.execute('''CREATE TABLE IF NOT EXISTS prev_stock
# 			 (id integer primary key, barcode text UNIQUE, price int, wp_id int, qty int, in_stock int)''')
# 	c.execute('''CREATE TABLE IF NOT EXISTS pre_process
# 			 (id integer primary key, barcode text, size text, price int,sales_price int, done int, title text, url text,image_list text, product_color text, country text,description text,gharanti text,supplier text,categorie_id text,image_name text,image_alt text,slug text,tag_name text,tag_slug text,tag_id int)''')
# 	c.execute('''CREATE TABLE IF NOT EXISTS product_sku
# 			 (id integer primary key, wp_sku text UNIQUE, wp_id integer, variation_id integer)''')






# --------------------------------------------crawl with selenium-------------------------------------------------------------

def material_description(browser):
	try:
		detail_border = browser.find_element(By.CLASS_NAME, 'detail-border')
		print("detail_border color  ===>>>",detail_border)
		detailattributestitle = detail_border.find_element(By.XPATH, "//h2[contains(text(), 'Materyal Bileşeni')]") 
		detailattributestitle_text = detailattributestitle.text
		print("detailattributestitle_text ---aaaa-",detailattributestitle_text)
		# input("hhhhh qazz")
		if detailattributestitle_text == "Materyal Bileşeni":
			print("detailattributestitle_text ====>>",detailattributestitle_text)
			# input("ggggg   a")
			Product_description_ul = detailattributestitle.find_element(By.XPATH, "following-sibling::ul")			
			Product_description_li_all = Product_description_ul.find_elements(By.TAG_NAME, 'li')
			print("li ===============>>>>>",Product_description_li_all)
			Product_description_list =[]
			description_split_list=[]
			for li in Product_description_li_all:
				span1 = li.find_elements(By.TAG_NAME, 'span')[0].text
				print("span1 ==>>",span1)
				span2 = li.find_elements(By.TAG_NAME, 'span')[1].text
				print("span2  ==>>",span2)

				c_dict.execute('SELECT fa FROM material where tr = ?',(span1,))
				result_color = c_dict.fetchone()
				if not result_color:
					print("rrrrrrrrrrrrrrrrrrrrrrrr",span1)
					# product_color_fa = translator(translate_url, product_color_tr)
					# print("product_color_fa>>>>>>>>>>>>",product_color_fa)
					strong_li_fa = span1
					c_dict.execute('INSERT OR IGNORE INTO material VALUES (?,?,?,?)',(None,str(span1),str(strong_li_fa),"trendyol"))
					conn_dictdb.commit()
				if result_color:
					print("result>>>>>>>>>>>>>",result_color[0])
					strong_li_fa = str(result_color[0])
				print("product_color_fa>>>>>>>>>>",strong_li_fa)

				c_dict.execute('SELECT fa FROM material where tr = ?',(span2,))
				result_color = c_dict.fetchone()
				if not result_color:
					print("rrrrrrrrrrrrrrrrrrrrrrrr",span2)
					# product_color_fa = translator(translate_url, product_color_tr)
					# print("product_color_fa>>>>>>>>>>>>",product_color_fa)
					product_color_fa = span2
					c_dict.execute('INSERT OR IGNORE INTO material VALUES (?,?,?,?)',(None,str(span2),str(product_color_fa),"trendyol"))
					conn_dictdb.commit()
				if result_color:
					print("result>>>>>>>>>>>>>",result_color[0])
					product_color_fa = str(result_color[0])
				print("product_color_fa>>>>>>>>>>",product_color_fa)

				Dimensions_text_ = "<li>"+ strong_li_fa + ":" +product_color_fa + "</li>"
					
				description_split_list.append(Dimensions_text_)

			description_all_str = ''.join([str(elem) for elem in description_split_list])
			# description_final = "<ul>"+str(description_all_str) + "</ul>"
			description_final = str(description_all_str)

			print("color_final>>>>>>>>>>>>>>>>>>",description_final)
			return description_final


		
	except Exception as e:
		# print(e)
		return None






def other_description(browser):
	# input("other_description-------------enter ...")
	try:
		detail_border = browser.find_element(By.CLASS_NAME, 'detail-border')
		print("detail_border ===>>>",detail_border)
		detailattributestitle = detail_border.find_element(By.XPATH, "//h2[contains(text(), 'Ürün Özellikleri')]") 
		detailattributestitle_text = detailattributestitle.text
		print("detailattributestitle_text---000,",detailattributestitle_text)
		if detailattributestitle_text == "Ürün Özellikleri":
			# input("--rün Özellikler-----------enter ...")
			print("detailattributestitle_text ====>>",detailattributestitle_text)
			Product_description_ul = detailattributestitle.find_element(By.XPATH, "following-sibling::ul")			
			Product_description_li_all = Product_description_ul.find_elements(By.TAG_NAME, 'li')
			print("li ===============>>>>>",Product_description_li_all)
			Product_description_list =[]
			description_split_list=[]
			for li in Product_description_li_all:
				span1 = li.find_elements(By.TAG_NAME, 'span')[0].text
				print("span1 ==>>",span1)
				span2 = li.find_elements(By.TAG_NAME, 'span')[1].text
				print("span2  ==>>",span2)

				c_dict.execute('SELECT fa FROM material where tr = ?',(span1,))
				result_color = c_dict.fetchone()
				if not result_color:
					print("rrrrrrrrrrrrrrrrrrrrrrrr",span1)
					# product_color_fa = translator(translate_url, product_color_tr)
					# print("product_color_fa>>>>>>>>>>>>",product_color_fa)
					strong_li_fa = span1
					c_dict.execute('INSERT OR IGNORE INTO material VALUES (?,?,?,?)',(None,str(span1),str(strong_li_fa),"trendyol"))
					conn_dictdb.commit()
				if result_color:
					print("result>>>>>>>>>>>>>",result_color[0])
					strong_li_fa = str(result_color[0])
				print("product_color_fa>>>>>>>>>>",strong_li_fa)

				c_dict.execute('SELECT fa FROM material where tr = ?',(span2,))
				result_color = c_dict.fetchone()
				if not result_color:
					print("rrrrrrrrrrrrrrrrrrrrrrrr",span2)
					# product_color_fa = translator(translate_url, product_color_tr)
					# print("product_color_fa>>>>>>>>>>>>",product_color_fa)
					product_color_fa = span2
					c_dict.execute('INSERT OR IGNORE INTO material VALUES (?,?,?,?)',(None,str(span2),str(product_color_fa),"trendyol"))
					conn_dictdb.commit()
				if result_color:
					print("result>>>>>>>>>>>>>",result_color[0])
					product_color_fa = str(result_color[0])
				print("product_color_fa>>>>>>>>>>",product_color_fa)

				Dimensions_text_ = "<li>"+ strong_li_fa + ":" +product_color_fa + "</li>"
					
				description_split_list.append(Dimensions_text_)

			description_all_str = ''.join([str(elem) for elem in description_split_list])
			# description_final = "<ul>"+str(description_all_str) + "</ul>"
			description_final = str(description_all_str)

			print("color_final>>>>>>>>>>>>>>>>>>",description_final)
			return description_final


		
	except Exception as e:
		# print(e)
		return None







def get_images(browser):
	try:
		product_details = browser.find_element(By.CLASS_NAME, 'styles-module_sliderBase__swkx1.product-slide-container')
		if product_details:
			images_ul = product_details.find_elements(By.TAG_NAME, 'img')
			print("images_ul",images_ul)	
			

			images_pre_list =[]
			for img in images_ul:
				# image= img.get_attribute("src").replace("/128/192/","/1200/1800/")
				image= img.get_attribute("src")

				print("image>>>>>>>>>",image)
				if image:
					images_pre_list.append(image)
			print("images_pre_list=======>>>",images_pre_list)
			image_list = '|'.join([str(elem) for elem in images_pre_list])
			print(image_list)
			return image_list
		else:
			return None

	except Exception as e:
		# base_product_image = browser.find_element(By.CLASS_NAME, 'base-product-image').find_element(By.TAG_NAME, 'img').get_attribute("src").replace("ty41","mnresize/1200/1800/ty41")
		base_product_image = browser.find_element(By.CLASS_NAME, 'base-product-image').find_element(By.TAG_NAME, 'img').get_attribute("src").replace("ty41","mnresize/1200/1800/ty41")
		if base_product_image:
			print("base_product_image",base_product_image)	
			images_pre_list =[]
			images_pre_list.append(base_product_image)
			image_list = '|'.join([str(elem) for elem in images_pre_list])
			print(image_list)
			return image_list
		else:
			return None



def get_price(browser,categorie_id):
	try:
		price_all = browser.find_element(By.CLASS_NAME, 'product-price-container')
		print(price_all)
		try:

			print("mm")
			price_sal_str = price_all.find_element(By.CSS_SELECTOR, 'span.prc-dsc')
			price_string = price_sal_str.text.replace(".","").replace("TL","")
			sales_price = price_string[:price_string.find(",")]			
			price_str = price_all.find_element(By.CSS_SELECTOR, 'span.prc-org')
			price_string = price_str.text.replace(".","").replace("TL","")
			price = price_string[:price_string.find(",")]
			print(price, sales_price)
			c_cost.execute('SELECT cost FROM categori_sku where id_categori = ?',(categorie_id,))
			result = c_cost.fetchone()
			if result:
				cost = int(result[0])
				print("cost>>>>>>>>>>>>>>>>>>",cost)
				return int(((int(price) + 12 ) * tl_price + cost)/1000) * 1000,int(((int(sales_price) + 12 ) * tl_price + cost)/1000) * 1000
			else:
				return int(((int(price) + 12 ) * tl_price + 200000)/1000) * 1000,int(((int(sales_price) + 12 ) * tl_price + 200000 )/1000) * 1000


		except Exception as e:
			price_str = price_all.find_element(By.CSS_SELECTOR, 'span.prc-dsc')
			print("price_str",price_str.text)
			price_string = price_str.text.replace(".","").replace("TL","")
			price = price_string[:price_string.find(",")]
			sales_price = price
			print(price, sales_price)
			c_cost.execute('SELECT cost FROM categori_sku where id_categori = ?',(categorie_id,))
			result = c_cost.fetchone()
			if result:
				cost = int(result[0])
				print("cost>>>>>>>>>>>>>>>>>>",cost)
				return int(((int(price) + 12 ) * tl_price + cost)/1000) * 1000,int(((int(sales_price) + 12 ) * tl_price + cost)/1000) * 1000
			else:
				# return int(((int(round(price)) + 12 ) * 5200 + cost)/1000) * 1000,int(((int(round(sales_price)) + 12 ) * 5200 + cost)/1000) * 1000

				return int(((int(price) + 12 ) * tl_price + 200000)/1000) * 1000,int(((int(sales_price) + 12 ) * tl_price + 200000 )/1000) * 1000


	except Exception as e:
		# print(e)
		return None
 





def get_color(browser):
	try:
		detail_border = browser.find_element(By.CLASS_NAME, 'detail-border')
		print("detail_border ===>>>",detail_border)
		detailattributestitle = detail_border.find_element(By.XPATH, "//h2[contains(text(), 'Ürün Özellikleri')]") 
		detailattributestitle_text = detailattributestitle.text
		print("detailattributestitle_text---000,",detailattributestitle_text)
		if detailattributestitle_text == "Ürün Özellikleri":
			# input("--rün Özellikler-----------enter ...")
			print("detailattributestitle_text ====>>",detailattributestitle_text)
			Product_description_ul = detailattributestitle.find_element(By.XPATH, "following-sibling::ul")			
			Product_description_li_all = Product_description_ul.find_elements(By.TAG_NAME, 'li')
			print("li ===============>>>>>",Product_description_li_all)
			Product_description_list =[]
			description_split_list=[]
			for li in Product_description_li_all:
				span1 = li.find_elements(By.TAG_NAME, 'span')[0].text
				print("span1 ==>>",span1)
				span2 = li.find_elements(By.TAG_NAME, 'span')[1].text
				print("span2  ==>>",span2)
				if span1 =="Renk":
					c_dict.execute('SELECT fa FROM material where tr = ?',(span1,))
					result_color = c_dict.fetchone()
					if not result_color:
						print("rrrrrrrrrrrrrrrrrrrrrrrr",span1)
						# product_color_fa = translator(translate_url, product_color_tr)
						# print("product_color_fa>>>>>>>>>>>>",product_color_fa)
						strong_li_fa = span1
						c_dict.execute('INSERT OR IGNORE INTO material VALUES (?,?,?,?)',(None,str(span1),str(strong_li_fa),"trendyol"))
						conn_dictdb.commit()
					if result_color:
						print("result>>>>>>>>>>>>>",result_color[0])
						strong_li_fa = str(result_color[0])
					print("product_color_fa>>>>>>>>>>",strong_li_fa)

					c_dict.execute('SELECT fa FROM material where tr = ?',(span2,))
					result_color = c_dict.fetchone()
					if not result_color:
						print("rrrrrrrrrrrrrrrrrrrrrrrr",span2)
						# product_color_fa = translator(translate_url, product_color_tr)
						# print("product_color_fa>>>>>>>>>>>>",product_color_fa)
						product_color_fa = span2
						c_dict.execute('INSERT OR IGNORE INTO material VALUES (?,?,?,?)',(None,str(span2),str(product_color_fa),"trendyol"))
						conn_dictdb.commit()
					if result_color:
						print("result>>>>>>>>>>>>>",result_color[0])
						product_color_fa = str(result_color[0])
					print("product_color_fa>>>>>>>>>>",product_color_fa)

					# Dimensions_text_ = "<li>"+ strong_li_fa + ":" +product_color_fa + "</li>"
					Dimensions_text_ = product_color_fa

						
					description_split_list.append(Dimensions_text_)

			description_all_str = ''.join([str(elem) for elem in description_split_list])
			# description_final = "<ul>"+str(description_all_str) + "</ul>"
			description_final = str(description_all_str)

			print("color_final>>>>>>>>>>>>>>>>>>",description_final)
			return description_final


		
	except Exception as e:
		# print(e)
		return None





def get_size(browser):
	try:
		size_box = browser.find_element(By.CLASS_NAME, 'size-variant-wrapper').find_elements(By.CSS_SELECTOR, 'div.sp-itm:not(.so.sp-itm)')		
		size_list = []
		for item in size_box:
			print(item)
			size = item.text
			size_list.append(size)
		print(size_list)
		return size_list
	except Exception as e:
		try:
			print(e)
			button_size = browser.find_element(By.CLASS_NAME, 'product-button-container').find_element(By.CSS_SELECTOR, 'button.add-to-basket')
			if button_size:
				return["تک سایز"]
			else:
				return None
		except:
			return None






def make_ready_trendyol(url,browser):
	browser.get(url)
	browser.refresh()
	time.sleep(5)
	# size
	size = get_size(browser)
	if size:
		size_string = "|".join(size)
		# barcode
		title_contain_barcode = browser.find_element(By.CLASS_NAME, 'pr-new-br').find_element(By.TAG_NAME, 'span').text
		barcode_str = title_contain_barcode[title_contain_barcode.rfind(" "):]
		barcode_strip = barcode_str.strip()
		print("barcode_str ====>>",barcode_str)
		try:
			product_color_tr= browser.find_element(By.CLASS_NAME, 'selected.slc-img').get_attribute("title").replace(" ","-")
			if product_color_tr:
				barcode = barcode_strip + "-" + str(product_color_tr)
				print("barcode ====>>",barcode)
		except:
			barcode = barcode_strip
			print("barcode ====>>",barcode)
		# price

		price,sales_price = get_price(browser,"categorie_id")
		print("sales_price ,price >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>",sales_price,price,"<<<<<<<<<<<<<<<<<<<<<sales_price,price")					
		#title
		title = browser.find_element(By.CLASS_NAME, 'pr-new-br').find_element(By.TAG_NAME, 'span').text
		print("title ---->>>>>>>",title)
		# slug
		slug = title.replace(" ","-") + "-" + barcode
		print("slug--->>>>",slug)
		# color
		product_color = get_color(browser)
		print("product_color",product_color)
		# image name
		# image_name = str(title)+ " "+product_color
		image_name = str(title)
		print("image_name>>>>>>>>>>>>>",image_name)
		image_alt = image_name
		# image_list
		image_list = str(get_images(browser))
		# gharanti
		gharanti = "تعویض و مرجوع 7 روزه"
		supplier = "brandshop"
		# description
		otherr_description  = other_description(browser)
		material = material_description(browser)
		if material:
			descriptionn ='<h3>'+"مشخصات:"+'</h3>'+ '<ul>'+str(otherr_description)+'</ul>'+'<br>'+'<h3>'+"جنس:"+'</h3>'+'<ul>'+ str(material) +'</ul>'
			description = descriptionn.replace("None","").replace("<ul>None</ul>","")
			print("description (((((((((((((((((",description,"))))))))))))))))))))))")	
		else:
			descriptionn ='<h3>'+"مشخصات:"+'</h3>'+ '<ul>'+str(otherr_description)+'</ul>'
			description = descriptionn.replace("None","").replace("<ul>None</ul>","")
			print("description (((((((((((((((((",description,"))))))))))))))))))))))")




		# input("enter")

		print("size_string",size_string)
		print("barcode",barcode)
		print("sales_price,price",sales_price,price)
		print("title",title)
		print("slug",slug)
		print("product_color",product_color)
		print("image_name",image_name)
		print("image_alt",image_alt)
		print("image_list",image_list)
		print("gharanti",gharanti)
		print("supplier",supplier)
		print("description",description)

		return size_string,barcode,price,sales_price,title,slug,product_color,image_name,image_alt,image_list,gharanti,supplier,description
	browser.quit()










# browser = webdriver.Chrome(executable_path=ChromeService(ChromeDriverManager().install()), options=options)
# browser = webdriver.Chrome(executable_path = CHROME_PATH,options = chrome_options)


# browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# url = "https://www.trendyol.com/bershka/desenli-oversize-sweatshirt-p-335640372?boutiqueId=594568&merchantId=104961&filterOverPriceListings=false&sav=true"
# make_ready_trendyol(url,browser)












