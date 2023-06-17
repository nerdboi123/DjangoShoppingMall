from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from store.models.customer import Customer
from django.views import View


class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')
        # validation
        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }
        error_message = None

        customer = Customer(first_name=first_name,
                            last_name=last_name,
                            phone=phone,
                            email=email,
                            password=password)
        error_message = self.validateCustomer(customer)

        if not error_message:
            print(first_name, last_name, phone, email, password)
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('homepage')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'signup.html', data)

    def validateCustomer(self, customer):
        error_message = None;
        if (not customer.first_name):
            error_message = "이름을 적어주세요!!"
        elif not customer.last_name:
            error_message = '성씨를 적어주세요!!'
        elif not customer.phone:
            error_message = '전화번호를 적어주세요'
        elif len(customer.password) < 6:
            error_message = '비밀번호는 적어도 7자 이상이어야 합니다.'
        elif len(customer.email) < 5:
            error_message = '이메일은 적어도 6자 이상이어야 합니다.'
        elif customer.isExists():
            error_message = '이미 가입한 이메일 입니다.'
        # saving

        return error_message
