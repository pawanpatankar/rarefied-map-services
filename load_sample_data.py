import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mapviewer.settings')
django.setup()

from maps.models import Department, Category

departments_data = [
    {
        'name': 'Police Department',
        'description': 'Law enforcement and public safety maps',
        'categories': [
            {'name': 'Metro Region', 'subcategories': ['North Zone', 'South Zone', 'East Zone', 'West Zone']},
            {'name': 'Rural Region', 'subcategories': ['District 1', 'District 2', 'District 3']},
        ]
    },
    {
        'name': 'Electricity Board',
        'description': 'Power distribution and infrastructure maps',
        'categories': [
            {'name': 'Northern Board', 'subcategories': ['Region A', 'Region B']},
            {'name': 'Southern Board', 'subcategories': ['Circle 1', 'Circle 2', 'Circle 3']},
            {'name': 'Eastern Board', 'subcategories': ['Zone 1', 'Zone 2']},
        ]
    },
    {
        'name': 'Railway Department',
        'description': 'Railway network and station maps',
        'categories': [
            {'name': 'Central Railway', 'subcategories': ['Main Line', 'Branch Lines']},
            {'name': 'Western Railway', 'subcategories': ['Suburban', 'Long Distance']},
        ]
    },
    {
        'name': 'PWD (Public Works Department)',
        'description': 'Road infrastructure and construction maps',
        'categories': [
            {'name': 'Highways', 'subcategories': ['National Highways', 'State Highways']},
            {'name': 'Urban Roads', 'subcategories': ['City 1', 'City 2', 'City 3']},
            {'name': 'Bridges', 'subcategories': []},
        ]
    },
]

print('Loading sample data...')

for dept_data in departments_data:
    dept, created = Department.objects.get_or_create(
        name=dept_data['name'],
        defaults={'description': dept_data['description']}
    )
    if created:
        print(f'Created department: {dept.name}')

    for cat_data in dept_data['categories']:
        cat, created = Category.objects.get_or_create(
            name=cat_data['name'],
            department=dept,
            parent=None
        )
        if created:
            print(f'  Created category: {cat.name}')

        for subcat_name in cat_data.get('subcategories', []):
            subcat, created = Category.objects.get_or_create(
                name=subcat_name,
                department=dept,
                parent=cat
            )
            if created:
                print(f'    Created subcategory: {subcat.name}')

print('\nSample data loaded successfully!')
print('\nYou can now:')
print('1. Access admin panel at: http://localhost:8000/admin/')
print('   Username: admin')
print('   Password: admin123')
print('2. Upload maps through the admin panel')
print('3. View the website at: http://localhost:8000/')
