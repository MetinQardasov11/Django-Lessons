from django.contrib import admin
from .models import Student, Category, Teacher

# Register your models here.

class StudentInline(admin.TabularInline):
    model = Student
    extra = 0


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name','age',  'teacher',)
    list_display_links = ('first_name',)
    list_filter = ('category', 'teacher')
    search_fields = ('first_name','last_name',)
    list_per_page = 10
    list_editable = ('teacher',)
    search_help_text = 'Search by first name or last name'
    readonly_fields = ('created_at', 'updated_at')
    autocomplete_fields = ('teacher',)
    ordering = ('created_at',)
    
    def update_first_name(self, request, queryset):
        queryset.update(first_name='Updated')

    actions = ('update_first_name',)

# admin.site.register(Student)
admin.site.register(Category)

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    search_fields = ('full_name',)
    inlines = [StudentInline]