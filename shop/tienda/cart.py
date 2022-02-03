class Cart:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        cart = self.session.get('cart')
        if not cart:
            cart = self.session['cart'] = {}
        self.cart = cart
    
    def add(self, product, quantity):
        if str(product.id) not in self.cart.keys():
            self.cart[product.id] = {
                'product_id': product.id,
                'title': product.title,
                'quantity': quantity,
                'price': str(product.price),
                'image': product.image.url,
                'total': str(quantity * product.price),
            }
        else:
            for key, value in self.cart.items():
                if key == str(product.id):
                    value["quantity"] = str(int(value["quantity"]) + quantity)
                    value["total"] = str(float(value["quantity"]) * float(value["price"]))
                    break
        self.save()

    def save(self):
        self.session['cart'] = self.cart
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()
            
    def clear(self):
        self.session['cart'] = {}