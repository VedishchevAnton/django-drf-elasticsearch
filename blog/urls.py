from django.urls import path, include
from rest_framework import routers

from blog.views import UserViewSet, CategoryViewSet, ArticleViewSet

router = routers.DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'category', CategoryViewSet)
router.register(r'article', ArticleViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

# /blog/user/ перечисляет всех пользователей
# /blog/user/<USER_ID>/выбирает конкретного пользователя
# /blog/category/ перечисляет все категории
# /blog/category/<CATEGORY_ID>/ выбирает определенную категорию
# /blog/article/ перечисляет все статьи
# /blog/article/<ARTICLE_ID>/ выбирает конкретную статью
