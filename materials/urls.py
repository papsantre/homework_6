from django.urls import path
from rest_framework.routers import SimpleRouter

from materials.views import CourseViewSet, LessonListAPIView, LessonReviewAPIView, LessonCreateAPIView, \
    LessonDestroyAPIView, LessonUpdateAPIView, SubscriptionCreateAPIView
from materials.apps import MaterialsConfig

app_name = MaterialsConfig.name

router = SimpleRouter()
router.register('', CourseViewSet, basename='materials')

urlpatterns = [
    path('lesson/', LessonListAPIView.as_view(), name='lesson_list'),
    path('lesson/<int:pk>/', LessonReviewAPIView.as_view(),name='lesson_review'),
    path('lesson/create/', LessonCreateAPIView.as_view(),name='lesson_create'),
    path('lesson/<int:pk>/delete/', LessonDestroyAPIView.as_view(),name='lesson_delete'),
    path('lesson/<int:pk>/update/', LessonUpdateAPIView.as_view(),name='lesson_update'),
    path('course_subscription/', SubscriptionCreateAPIView.as_view(),name='course_subscription'),
]

urlpatterns += router.urls
