from django.contrib import admin

from materials.models import Course, Lesson, Subscription


@admin.register(Course)
class UserCourse(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'owner')


@admin.register(Lesson)
class UserLesson(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'course', 'owner')


@admin.register(Subscription)
class UserSubscription(admin.ModelAdmin):
    list_display = ('id', 'course', 'user')


