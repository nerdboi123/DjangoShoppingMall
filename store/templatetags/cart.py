from django import template

register = template.Library() #템플릿 라이브러리 객체를 생성하여 register 변수에 할당

@register.filter(name='is_in_cart') #커스텀 필터를 등록하는 데코레이터(decorator)
#product , cart 두 인자를 받아 해당 상품이 장바구니에 있는지 여부 확인 역할
def is_in_cart(product  , cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return True
    return False;


@register.filter(name='cart_quantity')
def cart_quantity(product  , cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return cart.get(id)
    return 0;


@register.filter(name='price_total')
def price_total(product  , cart):
    return product.price * cart_quantity(product , cart)


@register.filter(name='total_cart_price')
def total_cart_price(products , cart):
    sum = 0 ;
    for p in products:
        sum += price_total(p , cart)

    return sum
    