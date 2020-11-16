import datetime
from urllib.parse import urlencode

from django import forms
from django.conf import settings
from django.http import Http404
from django.shortcuts import render
from django_orghierarchy.models import Organization

from .authentication import calculate_signature, join_params
from .models import Resource


# TODO: This is a temporary demonstration. Remove before production deployment.
class HaukiSignedAuthGeneratorForm(forms.Form):
    username = forms.CharField(label="User name", max_length=100)
    resource = forms.ModelChoiceField(queryset=Resource.objects.all(), required=False)
    organization = forms.ModelChoiceField(
        queryset=Organization.objects.all(), required=False
    )


def hauki_signed_auth_link_generator(request):
    if not settings.DEBUG:
        raise Http404

    client_base_url = request.GET.get("client_base_url", "http://localhost:5000/")

    now = datetime.datetime.utcnow()

    context = {}
    if request.method == "POST":
        form = HaukiSignedAuthGeneratorForm(request.POST)
        if form.is_valid():
            params = {
                "username": form.cleaned_data["username"],
                "created_at": now.isoformat() + "Z",
                "valid_until": (now + datetime.timedelta(minutes=60)).isoformat() + "Z",
            }

            if form.cleaned_data["resource"]:
                resource = form.cleaned_data["resource"]
                tprek_origin = resource.origins.filter(data_source_id="tprek").first()

                if tprek_origin:
                    params["resource"] = (
                        f"{tprek_origin.data_source.id}:" f"{tprek_origin.origin_id}"
                    )
                else:
                    params["resource"] = form.cleaned_data["resource"].id

            if form.cleaned_data["organization"]:
                params["organization"] = form.cleaned_data["organization"].id

            data_string = join_params(params)
            calculated_signature = calculate_signature(data_string)

            params["signature"] = calculated_signature
            context["link"] = client_base_url + "?" + urlencode(params)
    else:
        form = HaukiSignedAuthGeneratorForm()

    context["form"] = form

    return render(request, "hours/hauki_signed_auth_link_generator.html", context)


# TODO: This is a temporary demonstration. Remove before production deployment.
