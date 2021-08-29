from django.urls import path
from .views import (
  ArticleListView,
  ArticleDetailView,
  ArticleCreateView,
  ArticleUpdateView,
  ArticleDeleteView,
)

# 1 create an article detail view 
# 1.1 create a matching template
# 2 create an article create view
# 3 create an article update view
# 4 create an article delete view
# 5 create urlpatterns to map to all of our views.
# to view an articles detail, were going to go to /<int:pk>/
# to create an article were going ot go to: /new/
# to update an article were going ot go to: /<int:pk>/update/
# to delete an article were going ot go to: /<int:pk>/delete/


urlpatterns = [
  path('', ArticleListView.as_view(), name= "article_list"),
  path('<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
  path('new/', ArticleCreateView.as_view(), name='article_create'),
  path('<int:pk>/update/', ArticleUpdateView.as_view(), name='article_update'),
  path('<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
]