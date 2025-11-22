from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, FileResponse
from django.contrib import messages
from django.views.decorators.clickjacking import xframe_options_deny
from django.views.decorators.cache import never_cache
from django.db.models import Q
from .models import Department, Category, Map, ForumSubmission, ContactMessage
import mimetypes
from django.core.mail import send_mail
from django.conf import settings

def home(request):
    departments = Department.objects.filter(is_active=True)
    recent_maps = Map.objects.filter(is_active=True).select_related('department', 'category')[:6]
    context = {
        'departments': departments,
        'recent_maps': recent_maps,
    }
    return render(request, 'maps/home.html', context)


def about(request):
    return render(request, 'maps/about.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone', '')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        ContactMessage.objects.create(
            name=name,
            email=email,
            phone=phone,
            subject=subject,
            message=message
        )
        messages.success(request, 'Thank you for contacting us. We will get back to you soon.')
        return redirect('contact')

    return render(request, 'maps/contact.html')


def forum(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone', '')
        department_id = request.POST.get('department')
        map_interest = request.POST.get('map_interest')
        message = request.POST.get('message')

        department = None
        if department_id:
            department = Department.objects.filter(id=department_id).first()

        ForumSubmission.objects.create(
            name=name,
            email=email,
            phone=phone,
            department=department,
            map_interest=map_interest,
            message=message
        )
        messages.success(request, 'Your request has been submitted successfully. We will review and contact you soon.')
        return redirect('forum')

    departments = Department.objects.filter(is_active=True)
    context = {
        'departments': departments,
    }
    return render(request, 'maps/forum.html', context)


def departments_list(request):
    departments = Department.objects.filter(is_active=True).prefetch_related('categories')
    context = {
        'departments': departments,
    }
    return render(request, 'maps/departments.html', context)


def department_detail(request, department_id):
    department = get_object_or_404(Department, id=department_id, is_active=True)
    root_categories = Category.objects.filter(
        department=department,
        parent=None,
        is_active=True
    ).prefetch_related('subcategories')

    context = {
        'department': department,
        'categories': root_categories,
    }
    return render(request, 'maps/department_detail.html', context)


def category_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id, is_active=True)
    subcategories = category.subcategories.filter(is_active=True)
    maps = Map.objects.filter(category=category, is_active=True)

    search_query = request.GET.get('q', '').strip()
    if search_query:
        maps = maps.filter(
            Q(title__icontains=search_query) |
            Q(description__icontains=search_query)
        )
        subcategories = subcategories.filter(
            Q(name__icontains=search_query) |
            Q(description__icontains=search_query)
        )

    context = {
        'category': category,
        'subcategories': subcategories,
        'maps': maps,
        'search_query': search_query,
    }
    return render(request, 'maps/category_detail.html', context)


@xframe_options_deny
@never_cache
def map_viewer(request, map_id):
    map_obj = get_object_or_404(Map, id=map_id, is_active=True)
    map_obj.increment_view_count()

    context = {
        'map': map_obj,
    }
    return render(request, 'maps/map_viewer.html', context)


@never_cache
def serve_map_file(request, map_id):
    map_obj = get_object_or_404(Map, id=map_id, is_active=True)

    file_path = map_obj.file.path
    mime_type, _ = mimetypes.guess_type(file_path)

    response = FileResponse(map_obj.file.open('rb'), content_type=mime_type)
    response['Content-Disposition'] = 'inline'
    response['X-Content-Type-Options'] = 'nosniff'
    response['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response['Pragma'] = 'no-cache'

    return response
