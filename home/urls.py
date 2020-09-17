from django.urls import path, include
from home.views import HelloView, IndexView, ListView

urlpatterns = [
    # 参数1即路由,参数2即视图函数名
    path('hello/', HelloView.as_view()),
    path('', IndexView.as_view(), name='index'),
    path('list/', ListView.as_view(), name='list'),
]
