# Secure Map Viewer Platform

A Django-based web application for secure viewing of maps in PDF, KMZ, and KML formats. This platform provides a view-only interface that prevents downloading, copying, or saving maps while allowing users to browse through multiple departments and their hierarchical categories.

## Features

### Core Functionality
- **Secure Map Viewing**: View-only access with disabled download, copy, and save functions
- **Multiple Format Support**: PDF, KMZ, and KML file formats
- **Dynamic Category Hierarchy**: Unlimited depth category structure for each department
- **Multiple Departments**: Support for various departments (Police, Railway, PWD, Electricity Board, etc.)

### User Interface
- **Home Page**: Browse departments and recently added maps
- **About Us Page**: Information about the platform and its features
- **Contact Page**: Submit inquiries and view contact information
- **Forum Page**: Request specific maps or departments
- **Department Browsing**: Navigate through departments and their category hierarchies
- **Responsive Design**: Works on desktop, tablet, and mobile devices

### Admin Panel
- Full CRUD operations for:
  - Departments
  - Categories (with unlimited depth)
  - Maps (upload PDF, KMZ, KML files)
  - Forum submissions
  - Contact messages
- User activity tracking
- Map view count statistics

### Security Features
- Disabled right-click context menu
- Blocked keyboard shortcuts (Ctrl+S, Ctrl+P, Ctrl+C)
- Disabled print functionality
- Prevented text selection and copying
- X-Frame-Options deny header
- No-cache headers for map files
- Inline content disposition (no downloads)

## Technology Stack

- **Backend**: Django 4.2
- **Database**: SQLite3
- **Frontend**: HTML, CSS, JavaScript
- **Python**: 3.13

## Installation

### 1. Clone or extract the project

```bash
cd /path/to/project
```

### 2. Create and activate virtual environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create admin superuser

```bash
python manage.py createsuperuser
```

Or use the provided script:

```bash
python create_superuser.py
```

This creates:
- Username: `admin`
- Password: `admin123`
- Email: `admin@example.com`

### 6. Load sample data (optional)

```bash
python load_sample_data.py
```

This creates sample departments and categories for:
- Police Department
- Electricity Board
- Railway Department
- PWD (Public Works Department)

### 7. Run the development server

```bash
python manage.py runserver
```

Visit: http://localhost:8000/

## Usage

### Admin Panel

Access the admin panel at: http://localhost:8000/admin/

Default credentials (if using create_superuser.py):
- Username: `admin`
- Password: `admin123`

#### Adding Departments

1. Go to "Departments" in the admin panel
2. Click "Add Department"
3. Fill in name and description
4. Save

#### Creating Categories

1. Go to "Categories" in the admin panel
2. Click "Add Category"
3. Select a department
4. Optionally select a parent category (for subcategories)
5. Fill in name and description
6. Save

**Note**: You can create unlimited hierarchy depth by setting categories as parents of other categories.

#### Uploading Maps

1. Go to "Maps" in the admin panel
2. Click "Add Map"
3. Fill in:
   - Title
   - Description (optional)
   - Department
   - Category
   - File (PDF, KMZ, or KML)
   - File format (select from dropdown)
   - Thumbnail (optional)
4. Save

### Frontend Usage

#### For Visitors

1. **Browse Departments**: Navigate to "Departments" to see all available departments
2. **Explore Categories**: Click on a department to see its categories and subcategories
3. **View Maps**: Click on a map card to open the secure viewer
4. **Submit Requests**: Use the Forum page to request specific maps
5. **Contact**: Use the Contact page to reach out for purchases or inquiries

#### Security Notice

When viewing maps, users will see:
- A security notice indicating view-only access
- Disabled browser functionality for downloading/copying
- Prevented screenshot capabilities (where possible)
- Disabled print functionality

## Project Structure

```
project/
├── mapviewer/              # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── maps/                   # Main application
│   ├── migrations/
│   ├── templates/maps/     # HTML templates
│   │   ├── base.html
│   │   ├── home.html
│   │   ├── about.html
│   │   ├── contact.html
│   │   ├── forum.html
│   │   ├── departments.html
│   │   ├── department_detail.html
│   │   ├── category_detail.html
│   │   └── map_viewer.html
│   ├── admin.py           # Admin panel configuration
│   ├── models.py          # Database models
│   ├── views.py           # View functions
│   └── urls.py            # URL routing
├── static/                # Static files (CSS, JS, images)
├── media/                 # User uploaded files
├── db.sqlite3            # SQLite database
├── manage.py             # Django management script
├── requirements.txt      # Python dependencies
├── create_superuser.py   # Script to create admin user
└── load_sample_data.py   # Script to load sample data
```

## Database Models

### Department
- name (unique)
- description
- is_active
- timestamps

### Category
- name
- department (ForeignKey)
- parent (self-referencing ForeignKey for hierarchy)
- description
- is_active
- timestamps

### Map
- title
- description
- department (ForeignKey)
- category (ForeignKey)
- file (FileField)
- file_format (choices: pdf, kmz, kml)
- thumbnail (ImageField)
- is_active
- view_count
- timestamps

### ForumSubmission
- name
- email
- phone
- department (ForeignKey, optional)
- map_interest
- message
- is_resolved
- admin_notes
- timestamp

### ContactMessage
- name
- email
- phone
- subject
- message
- is_read
- timestamp

## Configuration

### Settings (mapviewer/settings.py)

Key configurations:
- `DEBUG = True` (Set to False in production)
- `ALLOWED_HOSTS = []` (Add your domain in production)
- `DATABASES`: SQLite3 by default
- `STATIC_URL` and `STATIC_ROOT`
- `MEDIA_URL` and `MEDIA_ROOT`

### Security Settings

The application includes several security features:
- CSRF protection enabled
- Clickjacking protection (X-Frame-Options: DENY)
- Content type sniffing prevention
- Cache control headers for sensitive content

## API Endpoints

- `/` - Home page
- `/about/` - About us page
- `/contact/` - Contact page
- `/forum/` - Forum submission page
- `/departments/` - List of all departments
- `/department/<id>/` - Department detail with categories
- `/category/<id>/` - Category detail with maps
- `/map/<id>/` - Secure map viewer
- `/map/<id>/file/` - Protected map file serving
- `/admin/` - Admin panel

## Customization

### Adding New Departments

You can add departments with any hierarchy structure. Examples:

#### Simple Hierarchy (2 levels)
```
Department → Category → Maps
```

#### Complex Hierarchy (5+ levels)
```
Department → Board → Region → Circle → Division → Maps
```

### Styling

All CSS is included in the template files for easy customization. Main color scheme:
- Primary: #3498db (blue)
- Secondary: #2c3e50 (dark blue)
- Background: #f5f5f5 (light gray)
- Text: #333 (dark gray)

## Production Deployment

For production deployment:

1. Set `DEBUG = False` in settings.py
2. Configure `ALLOWED_HOSTS` with your domain
3. Use a production database (PostgreSQL recommended)
4. Configure proper static file serving
5. Use a web server (Nginx + Gunicorn recommended)
6. Enable HTTPS
7. Set up proper file permissions for media folder
8. Configure regular database backups
9. Update SECRET_KEY with a secure random string

## Troubleshooting

### Maps not displaying
- Check file permissions in media folder
- Verify file format is correct (PDF, KMZ, or KML)
- Check browser console for errors

### Admin panel not accessible
- Verify superuser was created correctly
- Check database migrations are applied
- Clear browser cache

### Static files not loading
- Run `python manage.py collectstatic`
- Check STATIC_ROOT and STATIC_URL settings
- Verify static folder exists

## Support

For issues or questions:
1. Check the documentation above
2. Review the code comments in models.py, views.py, and admin.py
3. Check Django logs for error messages
4. Verify all migrations are applied

## License

This project is provided as-is for educational and commercial use.

## Security Considerations

- This application provides view-only access with client-side restrictions
- Client-side security can be bypassed by determined users
- For highly sensitive data, consider server-side watermarking or additional protections
- Always use HTTPS in production
- Regularly update Django and dependencies
- Monitor file uploads for malicious content
- Implement user authentication if needed
- Consider adding rate limiting for public endpoints

## Future Enhancements

Potential features to add:
- User authentication and permissions
- Map search functionality
- Advanced filtering options
- Map bookmarking
- Email notifications for forum submissions
- Audit logging
- API endpoints for programmatic access
- Map comparison tool
- Export reports
- Multi-language support
