# Secure Map Viewer - Installation & Setup Guide

This guide will walk you through setting up the Secure Map Viewer platform from scratch.

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Basic command line knowledge

## Step-by-Step Installation

### Step 1: Navigate to Project Directory

```bash
cd /path/to/project
```

### Step 2: Set Up Python Virtual Environment

**On Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

You should see `(venv)` at the beginning of your command prompt.

### Step 3: Install Required Packages

```bash
pip install -r requirements.txt
```

This installs:
- Django 4.2
- Pillow (for image handling)
- django-ckeditor
- pykml

### Step 4: Run Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

This creates the SQLite database (`db.sqlite3`) and all necessary tables.

### Step 5: Create Admin Superuser

**Option A: Using the provided script (Recommended for testing)**

```bash
python create_superuser.py
```

This creates:
- Username: `admin`
- Email: `admin@example.com`
- Password: `admin123`

**Option B: Create your own superuser**

```bash
python manage.py createsuperuser
```

Follow the prompts to set:
- Username
- Email address
- Password (you'll type it twice)

### Step 6: Load Sample Data (Optional but Recommended)

```bash
python load_sample_data.py
```

This creates sample departments and categories:
- Police Department (with Metro and Rural regions)
- Electricity Board (with multiple boards and regions)
- Railway Department (Central and Western railways)
- PWD (Highways, Urban Roads, Bridges)

### Step 7: Start the Development Server

```bash
python manage.py runserver
```

You should see:
```
Starting development server at http://127.0.0.1:8000/
```

### Step 8: Access the Application

Open your web browser and visit:

**Main Website:**
- http://localhost:8000/ or http://127.0.0.1:8000/

**Admin Panel:**
- http://localhost:8000/admin/
- Login with the superuser credentials created in Step 5

## Post-Installation Setup

### Adding Your First Map

1. Go to http://localhost:8000/admin/
2. Log in with your superuser credentials
3. Click on "Maps" under the MAPS section
4. Click "Add Map" button
5. Fill in the form:
   - Title: Name of the map
   - Description: Brief description
   - Department: Select from dropdown
   - Category: Select from dropdown
   - File: Upload your PDF, KMZ, or KML file
   - File format: Select the format of your file
   - Thumbnail: (Optional) Upload a preview image
6. Click "Save"

### Creating Custom Categories

If you need a different category structure:

1. Go to http://localhost:8000/admin/
2. Click on "Categories"
3. Click "Add Category"
4. Fill in:
   - Name: Category name
   - Department: Select the department
   - Parent: Leave blank for top-level, or select another category to nest
   - Description: Optional description
5. Click "Save"

**Example Hierarchy:**

For Electricity Board with structure: Board → Region → Circle → Division

1. Create "Northern Board" (parent: None)
2. Create "Region A" (parent: Northern Board)
3. Create "Circle 1" (parent: Region A)
4. Create "Division X" (parent: Circle 1)

You can nest as many levels as needed!

## Verification Checklist

After installation, verify:

- [ ] Admin panel loads at http://localhost:8000/admin/
- [ ] You can log in with superuser credentials
- [ ] Home page loads at http://localhost:8000/
- [ ] Sample departments appear on the home page (if you loaded sample data)
- [ ] You can navigate to the Departments page
- [ ] You can navigate to About, Contact, and Forum pages
- [ ] No error messages in the terminal where the server is running

## Common Issues and Solutions

### Issue: "python: command not found"
**Solution:** Use `python3` instead of `python`

### Issue: "pip: command not found"
**Solution:** Use `python3 -m pip` instead of `pip`

### Issue: "Permission denied"
**Solution:** You might need to use `sudo` on Linux/Mac, or run Command Prompt as Administrator on Windows

### Issue: "Port 8000 already in use"
**Solution:** Either:
- Stop the other application using port 8000, or
- Use a different port: `python manage.py runserver 8080`

### Issue: Static files not loading
**Solution:**
1. Make sure the `static` folder exists: `mkdir static`
2. Run: `python manage.py collectstatic`

### Issue: Can't upload files in admin
**Solution:**
1. Make sure the `media` folder exists: `mkdir media`
2. Check folder permissions: `chmod 755 media`

## File Structure After Installation

```
project/
├── venv/                   # Virtual environment (auto-created)
├── db.sqlite3             # Database (auto-created)
├── media/                 # Uploaded files (create if missing)
├── static/                # Static files (create if missing)
├── staticfiles/           # Collected static files
├── maps/                  # Main app
├── mapviewer/             # Project settings
├── manage.py              # Django management
├── requirements.txt       # Dependencies
├── create_superuser.py    # Helper script
├── load_sample_data.py    # Sample data script
└── README.md              # Documentation
```

## Next Steps

Now that installation is complete:

1. **Add Departments**: Create your actual departments in the admin panel
2. **Set Up Categories**: Build your category hierarchy for each department
3. **Upload Maps**: Start uploading your PDF, KMZ, or KML files
4. **Test Viewing**: Navigate the website and test map viewing functionality
5. **Customize**: Modify templates and styling as needed

## Production Deployment Notes

**DO NOT use these settings in production:**
- Change `DEBUG = False` in settings.py
- Update `SECRET_KEY` in settings.py
- Add your domain to `ALLOWED_HOSTS`
- Use PostgreSQL or MySQL instead of SQLite
- Set up proper web server (Nginx + Gunicorn)
- Enable HTTPS
- Use environment variables for sensitive settings

## Getting Help

If you encounter issues:

1. Check the error message in the terminal
2. Review this guide's Common Issues section
3. Check the README.md for more details
4. Verify all commands were run in the correct order
5. Make sure the virtual environment is activated (you should see `(venv)` in your prompt)

## Quick Start Summary

For a fast setup (copy and paste these commands):

```bash
# Navigate to project
cd /path/to/project

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up database
python manage.py migrate

# Create superuser
python create_superuser.py

# Load sample data
python load_sample_data.py

# Start server
python manage.py runserver
```

Then visit: http://localhost:8000/

Admin panel: http://localhost:8000/admin/ (username: admin, password: admin123)

## Success!

If you can access the website and admin panel, installation is complete. You're ready to start using the Secure Map Viewer platform!
