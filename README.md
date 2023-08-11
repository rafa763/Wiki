# Wiki Encyclopedia

This project is a web-based encyclopedia where users can access, create, search, edit, and view encyclopedia entries. Each entry is written in Markdown and can be accessed through the URL or searched using the sidebar search functionality. The project is built using Django, a Python web framework.

## Getting Started

1. Download the distribution code from [here](https://cdn.cs50.net/web/2020/spring/projects/1/wiki.zip) and unzip it.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Start the application by running `python manage.py runserver`.

## Background

Wikipedia serves as an inspiration for this project. It allows users to access encyclopedia entries by visiting specific URLs. To make content creation and editing user-friendly, we use Markdown as the markup language for entries.

## Understanding

- The `encyclopedia` app contains views, templates, and utilities for managing encyclopedia entries.
- URL routing is defined in `encyclopedia/urls.py`.
- The `util.py` file provides functions for listing entries, saving entries, and retrieving entry content.
- Entries are stored as Markdown files in the `entries/` directory.
- Templates for rendering pages are located in `encyclopedia/templates/`.

## Features

### Entry Page

- Accessing `/wiki/TITLE` renders the content of the specified encyclopedia entry.
- Non-existent entries show an error page.
- Existing entries display their content with the title in the page header.

### Index Page

- The index page (`index.html`) lists entry names.
- Clicking on an entry name takes the user to that entry's page.

### Search

- The sidebar allows users to search for entries.
- If a query matches an entry's title, the user is redirected to that entry.
- If not, a search results page displays entries with the query as a substring.

### New Page

- "Create New Page" in the sidebar leads to a page for creating entries.
- Users provide a title and Markdown content.
- Saving the page adds the entry to the collection.

### Edit Page

- Each entry page includes a link to edit the entry.
- Editing page displays a textarea with pre-populated Markdown content.
- Users can save their changes, updating the entry.

### Random Page

- "Random Page" in the sidebar leads to a random encyclopedia entry.

## Usage

1. Access the application in a web browser.
2. Search for existing entries or create new ones.
3. Click on entry names to read or edit the content.
4. Enjoy exploring the encyclopedia!

## Credits

This project is part of the CS50 Web Programming with Python and JavaScript course by Harvard University.
