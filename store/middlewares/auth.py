from django.shortcuts import redirect

def auth_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        print(request.session.get('customer')) #현재 사용자의 세션에 저장된 값을 확인한다. 로그인상태를 유지하기위함.
        returnUrl = request.META['PATH_INFO'] #현재 요청 정보를 나타낸다. 로그인이 필요한 페이지 접근할 때, 원래 요청한 경로를 기억하기 위함.
        print(request.META['PATH_INFO'])
        if not request.session.get('customer'): #customer 값이 없다면 로그인 페이지 접근으로 판단
           return redirect(f'login?return_url={returnUrl}')

        response = get_response(request)#customer값이 있거나 로그인이 필요없는 페이지라면 뷰함수 호출
        return response #최종 반환되는 응답.

    return middleware

#사용자 인증을 처리하고, 인증 되자 않은 사용자가 특정 페이지에 접근하는 것을 방지하기 위해 사용된다.
# 로그인되어있지 않으면 로그인 페이지로 리다이렉트시키는 역할
