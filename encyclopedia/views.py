from django.shortcuts import redirect, render
from django.urls import reverse
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
            "error_msg": f"Entry with title '{title}' does not exist."
        })
    html = Markdown().convert(entry)
    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "content": html
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