from django.contrib import admin
from .models import Department, Category, Map, ForumSubmission, ContactMessage


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active', 'created_at', 'updated_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['name', 'description']
    list_editable = ['is_active']
    ordering = ['name']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'department', 'parent', 'is_active', 'created_at']
    list_filter = ['department', 'is_active', 'created_at']
    search_fields = ['name', 'description']
    list_editable = ['is_active']
    raw_id_fields = ['parent']
    ordering = ['department', 'name']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.select_related('department', 'parent')


@admin.register(Map)
class MapAdmin(admin.ModelAdmin):
    list_display = ['title', 'department', 'category', 'file_format', 'is_active', 'view_count', 'created_at']
    list_filter = ['department', 'file_format', 'is_active', 'created_at']
    search_fields = ['title', 'description']
    list_editable = ['is_active']
    raw_id_fields = ['category']
    readonly_fields = ['view_count', 'created_at', 'updated_at']
    ordering = ['-created_at']

    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'description', 'department', 'category')
        }),
        ('File Information', {
            'fields': ('file', 'file_format', 'thumbnail')
        }),
        ('Status & Statistics', {
            'fields': ('is_active', 'view_count', 'created_at', 'updated_at')
        }),
    )

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.select_related('department', 'category')


@admin.register(ForumSubmission)
class ForumSubmissionAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'department', 'map_interest', 'is_resolved', 'created_at']
    list_filter = ['is_resolved', 'department', 'created_at']
    search_fields = ['name', 'email', 'phone', 'map_interest', 'message']
    list_editable = ['is_resolved']
    readonly_fields = ['created_at']
    ordering = ['-created_at']

    fieldsets = (
        ('Contact Information', {
            'fields': ('name', 'email', 'phone')
        }),
        ('Submission Details', {
            'fields': ('department', 'map_interest', 'message')
        }),
        ('Admin', {
            'fields': ('is_resolved', 'admin_notes', 'created_at')
        }),
    )


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'subject', 'is_read', 'created_at']
    list_filter = ['is_read', 'created_at']
    search_fields = ['name', 'email', 'phone', 'subject', 'message']
    list_editable = ['is_read']
    readonly_fields = ['created_at']
    ordering = ['-created_at']

    fieldsets = (
        ('Contact Information', {
            'fields': ('name', 'email', 'phone')
        }),
        ('Message', {
            'fields': ('subject', 'message')
        }),
        ('Status', {
            'fields': ('is_read', 'created_at')
        }),
    )
