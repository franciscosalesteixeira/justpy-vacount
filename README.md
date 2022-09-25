# Voice Actor Count
This is a small unofficial website that uses AniList's API to get the total number of characters voiced by a voice actor, based on a user's completed anime list. In AniList's stats page for Staff, only main characters are counted towards statistics, which leads to some differences if every character were to be counted. 
You can try it [**here**](https://va-count.onrender.com/) - if you do not have an AniList account, you can use the username **vacount** to test it.

## Tools Used

This project uses a different number of tools:

- [**JustPy**](https://justpy.io/) - An object-oriented, component based, high-level Python Web Framework
- [**Tailwind CSS**](https://tailwindcss.com/) - A utility-first CSS framework
- [**Gunicorn**](https://gunicorn.org/) - A Python WSGI HTTP Server for UNIX
- [**Render**](https://render.com/) - Cloud application hosting for developers
- [**AniList's GraphQL API**](https://github.com/AniList/ApiV2-GraphQL-Docs) - Provides quick and powerful access to over 500k anime and manga entries, including character, staff, and live airing data

## Installing requirements

```sh
pip install -r requirements.txt
```

## Running locally
There are two main components that can be run, with different uses:

### [app.py](./app.py) 
Launches the website locally
```sh
python3 app.py
```

Verify by navigating to the server address in your preferred browser

```sh
127.0.0.1:8000
```

### [va.py](./va.py)
Writes to a file a full list of voice actors sorted by number of characters voiced, based on an user's list

```sh
python3 va.py [-h] username
```

Output file is **valist.txt**

## Other components

### [voiceactor.py](./src/voiceactor.py)

Contains several functions used by the main components, as well as the queries and requests pertaining to AniList's API

### [utilities.py](./src/utilities.py)

Contains auxiliary functions used to write and format output files

### [parse_html.py](./src/parse_html.py)

Given an HTML file, outputs equivalent code that can be used by the JustPy framework

```sh
python3 parse_html.py path_to_html_file
```
