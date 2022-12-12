from django import template
register=template.Library()
@register.filter(name='cart_quantity')
def cart_quantity(dish,cart):
	keys=cart.keys()
	for name in keys:
		if name == dish.dname:
			return cart.get(name)
	return 0	

@register.filter(name='price_total')
def price_total(dish,cart):
	return dish.price * cart_quantity(dish,cart)		

@register.filter(name='total_cart_price')
def total_cart_price(dish,cart):
	
	sum=0;
	for d in dish:
		sum+=price_total(d,cart)

	return sum		


