from django.urls import path, include

from .views import cbv, fbv as views

app_name = 'polls'

urlpatterns_cbv = [
    path('', cbv.IndexView.as_view(), name='index'),
]

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),

    # polls/cbv로 시작하는 URL 요청은
    # 위의 urlpatterns_cbv 리스트 내의 내용에서 처
    path('cbv/', include(urlpatterns_cbv))
]