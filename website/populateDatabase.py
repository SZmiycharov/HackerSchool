from store.models import Category, Product

fields = ['maker', 'model', 'description', 'price', 'category', 'product_logo', 'is_in_shopCart']
pics = ['cpu_amd.jpeg', 'cpu_intel.jpeg', 'GPU.jpeg', 'index.jpeg', 'keyboard.jpg'] 



for i in range(5000):
	for j in pics:
		a = Category()
		a.name = 'category' + str(i)
		a.category_logo = j
		a.save()

		b = Product()
		b.maker = 'maker' + str(i)
		b.model = 'model' + str(i)
		b.description = 'descr' + str(i)
		b.price = i
		b.category = a
		b.product_logo = j
		b.is_in_shopCart = True
		b.save()
