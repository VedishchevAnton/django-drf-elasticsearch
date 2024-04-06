from django.urls import path

from search.views import SearchArticles, SearchCategories, SearchUsers

urlpatterns = [
    path('user/<str:query>/', SearchUsers.as_view()),
    path('category/<str:query>/', SearchCategories.as_view()),
    path('article/<str:query>/', SearchArticles.as_view()),
]


# http://127.0.0.1:8000/search/user/mike/	Возвращает пользователя 'mike13'
# http://127.0.0.1:8000/search/user/jess_/	Возвращает пользователя 'jess_'
# http://127.0.0.1:8000/search/category/seo/	Возвращает категорию "SEO-оптимизация"
# http://127.0.0.1:8000/search/category/progreming/	Категория возврата "Программирование"
# http://127.0.0.1:8000/search/article/linux/	Возвращает статью «Установка последней версии Ubuntu».
# http://127.0.0.1:8000/search/article/java/	Возвращает статью «Какой язык программирования лучший?»