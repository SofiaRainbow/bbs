from django.contrib.admin import forms
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.utils.translation import ugettext_lazy as _
from users.models import User


class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        """
        1.接收参数
        2.验证参数
        3.密码的加密
        4.数据入库
        5.返回响应
        """
        # 1.接收参数
        username = request.POST.get('username')
        user = User.objects.filter(username=username).count()
        password = request.POST.get('password1')
        password2 = request.POST.get('password2')
        # 2.验证参数
        # 3.密码的加密
        from django.contrib.auth.hashers import make_password
        hash_password = make_password(password)
        # 4.数据入库
        if user == 0:
            if password == password2 and password != '':
                User.objects.create(username=username, password=hash_password)
                # 5.返回响应
                return redirect(reverse('login'))
            else:
                # raise forms.ValidationError("パスワードが一致しませんでした。パスワードを入力し直してください。")
                error = _('パスワードが一致しませんでした。パスワードを入力し直してください。')
                return render(request, 'register.html', {'error': error})
        else:
            error = _('このユーザーは既に登録されています。')
            # raise forms.ValidationError("このユーザーは既に登録されています。")
            return render(request, 'register.html', {'error': error})


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        """
        1.接收数据
        2.验证数据
        3.根据用户查询用户
        4.判断密码
        5.设置登录状态
        6.跳转到首页
        """
        # 1.接收数据
        username = request.POST.get('username')
        password = request.POST.get('password1')
        # 2.验证数据
        # 3.根据用户查询用户
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return render(request, 'login.html')
        # 4.判断密码
        from django.contrib.auth.hashers import check_password
        # check_password(密码,加密密码)
        if not check_password(password, user.password):
            return render(request, 'login.html')
        # 5.设置登录状态
        request.session['id'] = user.id
        request.session['name'] = user.username
        # 6.跳转到首页
        # bbs/home/urls.py name=index即首页
        return redirect(reverse('index'))


def test(request):
    context = {'msg': _("Welcome to China")}
    return render(request, 'test.html', context)
