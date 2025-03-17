.. PANDAN_project documentation master file, created by
   sphinx-quickstart on Mon Mar 17 02:10:46 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

PANDAN_project Documentation
=============================

Welcome to the **PANDAN Project** documentation!

This documentation provides an overview of the **PANDAN project**. It includes setup instructions, usage, and the API reference.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   

Overview
--------

The **PANDAN project** is a tool for efficient disk scanning and management. It offers utilities to scan directories, analyze file contents, and manage disk space efficiently. This project is aimed at developers and system administrators looking for a powerful disk scanner with various customizable options.

Key Features:
- Fast and efficient scanning of directories.
- Various file and disk management utilities.
- Integrates with the backend services and applications via the `scanner` module.
  
Core Modules
-------------

The **PANDAN project** consists of several core modules:

- **scanner**: The main module for scanning directories and files. The `scanner.Scanner` class is responsible for initiating scans and generating reports.
- **models**: Defines the data structures and database models for storing scan results and other related information.
- **views**: Contains views and controllers for interacting with the scanning process and presenting results to the user.
- **utils**: Utility functions to support various functionalities across the project.

Installation
------------

To install the **PANDAN project**, use the following pip command:

.. code-block:: bash

   pip install pandan

For detailed installation instructions, visit the `installation` section.

Usage
-----

To start using the **PANDAN project**, follow these instructions:

1. Import the `scanner` module into your project:

   .. code-block:: python

      import scanner

2. Scan a directory for file information:

   .. code-block:: python

      scan = scanner.Scanner('/path/to/directory')
      scan.scan()  # Run the scan on the specified directory
      scan.report()  # Generate a report of the scanned files

For advanced usage, refer to the `usage` section.

API Reference
-------------

The **PANDAN project** provides several methods and classes for disk scanning.

Classes:
- `Scanner`: The main class for scanning directories and files. This class is located in the `scanner` module.
- `Report`: A class used to generate and format reports on disk usage.

Methods:
- `scan()`: Initiates the scanning process on a directory.
- `report()`: Generates a report based on the scanned data.

For detailed information, refer to the `api_reference` section.

Migrations
----------

The **PANDAN project** uses database migrations to manage changes to the database schema over time. This is particularly important if you're using Django's ORM for data management.

To apply migrations, run the following command:

.. code-block:: bash

   python manage.py migrate

This will apply any new migrations to the database. Migrations are stored in the `migrations/` directory and are automatically created when you modify models in the project.

For detailed information on managing migrations, refer to the official Django migration documentation.

Tests
-----

The **PANDAN project** includes a suite of tests to ensure the project works as expected. The tests are located in the `tests.py` file.

To run the tests, use the following command:

.. code-block:: bash

   python manage.py test

This will run all the tests and output the results. For more advanced testing options, refer to the `tests` section.

Django Setup
------------

The **PANDAN project** is built with Django. If you're using Django for the backend, you need to ensure that your Django settings are correctly configured.

1. Set up Django in your environment:

   .. code-block:: bash

      pip install django

2. Make sure your `settings.py` file is configured with the proper database and app settings.

3. To start the Django server:

   .. code-block:: bash

      python manage.py runserver

This will start the Django development server. For detailed instructions on setting up Django, refer to the official Django documentation.

