from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.http.request import HttpRequest
from django.http.response import HttpResponse, HttpResponseRedirect

from home.models import CategoryModel, ArticleModel, Reply
from users.models import User
from django.utils.translation import ugettext_lazy as _

'''
class 视图类名(View):
    # get,post,put,delete
    def Http方法名小写(self,request):
        return HttpResponse('内容')
1.要继承自View
2.定义的方法第2个参数是请求的实例对象
3.返回的数据必须是HttpResponse实例或子类实例对象        
'''


class HelloView(View):
    def get(self, request):  # request是HttpRequest的实例对象
        # 返回响应
        return HttpResponse('hello')


class IndexView(View):
    def get(self, request):
        # 假设一个登录标记位
        is_login = request.session.get('id')
        name = request.session.get('name')
        # 假设分类信息
        categories = CategoryModel.objects.all()
        # 获取今天的日期
        from datetime import date
        today = date.today()
        for category in categories:
            category.today = ArticleModel.objects.filter(category=category, publish_time__gte=today).count()
            category.total = ArticleModel.objects.filter(category=category).count()
        title = _('宿題QA_ホーム')
        # 组织上下文
        context = {'is_login': is_login,
                   'name': name,
                   'categories': categories, 'title': title, }
        # render主要是进行模板数据的渲染
        # request即请求对象实例,template_name即模板名字,context即传递给模板的内容
        return render(request, 'index.html', context=context)


class ListView(View):
    def get(self, request):
        """
        1.获取分类id
        2.根据分类id查询分类数据
        3.根据分类id查询文章数据
        4.组织上下文
        """
        is_login = request.session.get('id')
        name = request.session.get('name')
        # 1.获取分类id
        cat_id = request.GET.get('cat_id', 1)
        page_id = request.GET.get('page', 1)
        if cat_id is None:
            return render(request, '404.html')
        # 2.根据分类id查询分类数据
        try:
            category = CategoryModel.objects.get(id=cat_id)
        except CategoryModel.DoesNotExist:
            return render(request, '404.html')
        # 3.根据分类id查询文章数据
        articles = ArticleModel.objects.filter(category=category, status=1)
        paginator = Paginator(articles, 3)
        # page_data是Page对象 里面有当前页面的数据
        page_data = paginator.page(page_id)
        for article in page_data:
            replies = Reply.objects.filter(article=article).order_by('-r_time')
            article.comments = replies.count()
            article.save()
            if replies.count() > 0:
                article.replies = replies[0].r_time
        popular = articles.order_by('-read_count', '-comments')[:5]
        # 获取今天的日期
        from datetime import date
        today = date.today()
        today = ArticleModel.objects.filter(category=category, publish_time__gte=today).count()
        total = ArticleModel.objects.filter(category=category).count()
        title = _('宿題QA_リスト')
        # 4.组织上下文
        context = {
            'articles': articles,
            'category': category,
            'today': today,
            'total': total,
            'is_login': is_login,
            'name': name, 'title': title, 'popular': popular,
            'paginator': paginator, 'page_data': page_data, 'page_id': page_id,
        }
        return render(request, 'list.html', context=context)


def publish(request):
    is_login = request.session.get('id')
    name = request.session.get('name')
    category_id = request.GET.get('category_id')
    category_name = CategoryModel.objects.get(id=category_id)
    context = {
        'is_login': is_login,
        'name': name,
        'category_name': category_name,
        'category_id': category_id,
    }
    return render(request, 'publish.html', context=context)


def save_list(request, cat_id):
    user_id = request.session.get('id')
    if cat_id:
        current_cag = CategoryModel.objects.get(id=cat_id)
        current_user = User.objects.get(id=user_id)
        article = ArticleModel()
        if request.method == 'POST':
            article.title = request.POST.get('title')
            article.content = request.POST.get('content')
            if not article.title_en:
                article.title_en = article.title
                article.content_en = article.content
            if not article.title_ja:
                article.title_ja = article.title
                article.content_ja = article.content
            if not article.title_zh_hans:
                article.title_zh_hans = article.title
                article.content_zh_hans = article.content
            article.status = 1
            article.category = current_cag
            article.user = current_user
            article.save()
    return HttpResponseRedirect(reverse('index'))


def detail(request):
    is_login = request.session.get('id')
    name = request.session.get('name')
    article_id = request.GET.get('id')
    page_id = request.GET.get('page', 1)
    article = ArticleModel.objects.get(id=article_id)
    article.read_count += 1
    article.save()
    replies = Reply.objects.filter(article=article)
    paginator = Paginator(replies, 2)
    # page_data是Page对象 里面有当前页面的数据
    page_data = paginator.page(page_id)
    context = {'article': article, 'is_login': is_login, 'name': name, 'replies': replies, 'paginator': paginator,
               'page_data': page_data}
    return render(request, 'detail.html', context=context)


def reply(request):
    is_login = request.session.get('id')
    name = request.session.get('name')
    article_id = request.GET.get('article_id')
    article = ArticleModel.objects.get(id=article_id)
    #
    context = {'is_login': is_login, 'name': name, 'article': article}
    return render(request, 'reply.html', context=context)


def save_reply(request, article_id):
    user_id = request.session.get('id')
    if article_id:
        current_user = User.objects.get(id=user_id)
        current_article = ArticleModel.objects.get(id=article_id)
        replies = Reply()
        if request.method == 'POST':
            replies.r_content = request.POST.get('content')
            if not replies.r_content_zh_hans:
                replies.r_content_zh_hans = replies.r_content
            if not replies.r_content_ja:
                replies.r_content_ja = replies.r_content
            if not replies.r_content_en:
                replies.r_content_en = replies.r_content
            replies.article = current_article
            replies.user = current_user
            replies.save()
    return HttpResponseRedirect(reverse('index'))


def search_article(request):
    keyword = request.POST.get('keyword', '')
    page_id = request.GET.get('page', 1)
    if keyword:
        articles = ArticleModel.objects.filter(title__contains=keyword)
    else:
        articles = ArticleModel.objects.all()
    paginator = Paginator(articles, 5)
    # page_data是Page对象 里面有当前页面的数据
    page_data = paginator.page(page_id)
    popular = articles.order_by('-read_count', '-comments')[:5]
    context = {'popular': popular, 'page_data': page_data, 'paginator': paginator}
    return render(request, 'search.html', context)


def language_select(request):
    if request.method == 'POST':
        language = request.POST.get("language_code")
    if language == "zh-hans":
        request.session['language'] = "zh-hans"
    elif language == "ja":
        request.session['language'] = "ja"
    elif language == "en":
        request.session['language'] = "en"
    else:
        request.session['language'] = "ja"
    prev_url = request.META['HTTP_REFERER']
    response = redirect(prev_url)
    return response


def save_customize(request):
    if request.method == 'POST':
        row_key = request.POST.get('dropDown')
        row_value = request.POST.get('customize')
        request.session[row_key] = row_value
    prev_url = request.META['HTTP_REFERER']
    response = redirect(prev_url)
    return response
