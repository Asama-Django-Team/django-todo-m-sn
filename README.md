# MyTechBlog Django Project

## Overview

This Django project is designed to create, store, and display articles about the tech industry. The project includes a blog app connected to a database where articles are stored and then displayed on a blog page.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/mytechblog.git
   cd mytechblog
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Apply migrations to create the database:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. Create a superuser account:

   ```bash
   python manage.py createsuperuser
   ```

   Follow the prompts to create a superuser account, as this will be used to log in to the Django admin interface.

## Usage

1. Run the development server:

   ```bash
   python manage.py runserver
   ```

   The application will be accessible at `http://127.0.0.1:8000/`.

2. Access the Django admin interface:

   Go to `http://127.0.0.1:8000/admin/` and log in with the superuser account created earlier. Here, you can add and manage articles.

3. Create articles:

   Navigate to the Django admin interface, click on the "Blog" app, and then add new articles with titles and content related to the tech industry.

4. View the blog:

   Visit `http://127.0.0.1:8000/blog/` to see a list of all articles published on the blog.

## Project Structure

- `mytechblog/`: Django project folder.
  - `blog/`: Django app for managing articles.
    - `models.py`: Defines the Article model.
    - `views.py`: Handles the views for displaying articles.
    - `urls.py`: Defines URL patterns for the blog app.
    - `templates/`: Contains HTML templates for rendering views.
  - `mytechblog/`: Main project settings and configurations.
  - `manage.py`: Django management script.

## Dependencies

- Django: version x.x.x

## Contributing

If you would like to contribute to this project, please follow the standard guidelines for contributing. Create a new branch for your work, submit a pull request, and ensure that your code passes all tests.

## License

This project is licensed under the [MIT License](LICENSE).

Feel free to customize this README according to your specific project details and requirements.
