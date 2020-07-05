from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from .forms import UserForm
from .models import EmailTemplate, MP
from .externalapis import lookup_postcode, get_addresses


def draft_templates(templates, user_form):
    for t in templates:
        t.fill(user_form)
    return templates


def index(request):
    if request.method == "POST":
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            templates = EmailTemplate.objects.all()
            emails = draft_templates(templates, user_form)
            context = {"emails": emails}
            return render(request, "all-topics.html", context=context)
    else:
        user_form = UserForm()
    return render(request, "user-form.html", {"form": user_form})


def single_template(request, template_slug):
    """Shell function to implement viewing a single template."""
    return


def aboutus(request):
    return render(request, "aboutus.html")


def postcode(request, postcode):
    post_code_data = lookup_postcode(postcode)
    if post_code_data["status"] == 200:
        r = {
            "constituency": post_code_data["result"]["parliamentary_constituency"],
            "addresses": get_addresses(postcode),
        }
        return JsonResponse(r)
    else:
        j = JsonResponse({"error": "Invalid postcode"})
        j.status_code = 400
        return j
