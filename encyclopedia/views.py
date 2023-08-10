from django.shortcuts import render
from django.http import HttpResponse
from markdown2 import Markdown

from . import util 

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    entry = util.get_entry(title)
    if entry is None:
        return render(request, "encyclopedia/error.html", {
            "title": title
        })
    html = Markdown().convert(entry)
    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "content": html
    })