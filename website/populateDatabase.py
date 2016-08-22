from store.models import Category, Product
import random
import string

pics = ['cpu_amd.jpeg', 'cpu_intel.jpeg', 'GPU.jpeg', 'gpu_amd.jpg', 'gpu_nvidia.jpeg', 'index.jpeg', 'keyboard.jpg', 'keyboard_hp.jpg', 'keyboard_razor.png']

IsInShoppingCart = [True, False]
iteration = 0

for i in range(10000):
	for j in pics:
		a = Category()
		a.name = ''.join(random.choice(string.ascii_uppercase) for _ in range(6))
		a.category_logo = random.choice(pics)
		a.save()

		for k in range(10):
			b = Product()
			b.maker = ''.join(random.choice(string.ascii_uppercase) for _ in range(6))
			b.model = ''.join(random.choice(string.digits) for _ in range(6))
			b.description = 'descr' + str(i) + ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(25))
			b.price = ''.join(random.choice(string.digits) for _ in range(3))
			b.category = a
			b.product_logo = random.choice(pics)
			b.is_in_shopCart = random.choice(IsInShoppingCart)
			b.save()
			iteration += 1
			print "iteration: {}".format(iteration)
