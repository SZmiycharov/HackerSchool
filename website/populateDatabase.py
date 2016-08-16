from store.models import Category, Product

fields = ['maker', 'model', 'description', 'price', 'category', 'product_logo', 'is_in_shopCart']
pics = ['cpu_amd.jpeg', 'cpu_intel.jpeg', 'GPU.jpeg', 'index.jpeg', 'keyboard.jpg'] 

for i in range(5):
	for j in pics:
		currmaker = 'maker' + str(i) + str(j)
		currmodel = 'model' + str(i) + str(j)
		currdescr = 'descr' + str(i) + str(j)
		currprice = i + j
		currcategory = i
		currlogo = j
		row = [currmaker, currmodel, currdescr, currprice, currcategory, currlogo, True]
