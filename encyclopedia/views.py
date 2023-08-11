from django.shortcuts import redirect, render
from django.urls import reverse
from markdown2 import Markdown
import random as rand

from . import util

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    entry = util.get_entry(title)
    if entry is None:
        return render(request, "encyclopedia/error.html", {
            "error_msg": f"Entry with title '{title}' does not exist."
        })
    html = Markdown().convert(entry)
    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "content": html
    })

def search(request):
    query = request.GET.get('q')
    if query is not None:
        entries = util.list_entries()
        results = []
        for entry in entries:
            if query.lower() in entry.lower():
                results.append(entry)
        return render(request, "encyclopedia/search.html", {
            "query": query,
            "results": results
        })
    return render(request, "encyclopedia/search.html", {
            "query": query,
            "results": results
        })

def new(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        if util.get_entry(title) is None:
            util.save_entry(title, content)
            return redirect(reverse("encyclopedia:entry", args=[title]))
        else:
            return render(request, "encyclopedia/error.html", {
                "error_msg": f"Entry with title '{title}' already exists."
            })
    return render(request, "encyclopedia/new.html")

def edit(request, title):
    if request.method == 'POST':
        content = request.POST.get('content')
        util.save_entry(title, content)
        return redirect(reverse("encyclopedia:entry", args=[title]))


    entry = util.get_entry(title)
    if entry is None:
        return render(request, "encyclopedia/error.html", {
            "error_msg": f"Entry with title '{title}' does not exist."
        })
    return render(request, "encyclopedia/edit.html", {
            "title": title,
            "content": util.get_entry(title)
        })

def random():
    entries = util.list_entries()
    title = rand.choice(entries)
    return redirect(reverse("encyclopedia:entry", args=[title]))