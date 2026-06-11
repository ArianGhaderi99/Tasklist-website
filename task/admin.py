from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Task

class TaskInline(admin.TabularInline):
    model = Task
    extra = 0  # تعداد ردیف‌های خالی اضافی
    fields = ('title', 'end_date', 'end_time', 'completed', 'created_at')
    readonly_fields = ('created_at',)
    show_change_link = True
    can_delete = True

# تعریف مجدد UserAdmin برای اضافه کردن inlines
class CustomUserAdmin(UserAdmin):
    inlines = [TaskInline]

# حذف ثبت پیش‌فرض User و ثبت دوباره با تنظیمات جدید
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

# ثبت مدل Task به صورت معمولی (اختیاری)
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'end_date', 'end_time', 'completed', 'created_at')
    list_filter = ('completed', 'user')
    search_fields = ('title', 'user__username')
    readonly_fields = ('created_at',)