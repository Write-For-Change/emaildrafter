from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import UserForm


def index(request):
    if request.method == "POST":
        form = UserForm(request.POST)

        if form.is_valid():
            empty_templates = get_existing_templates()
            emails = draft_templates(empty_templates, name, postcode, address)
            return render("all-topics.html", emails=emails)

    return render(request, "landing.html")


def aboutus(request):
    return render(request, "aboutus.html")
