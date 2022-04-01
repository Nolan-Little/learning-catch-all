from django.shortcuts import render, redirect
from .forms import HashForm
from .models import Hash
from django.http import JsonResponse
import hashlib


def home(request):
    if request.POST:
        form = HashForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('hash', hash=form.instance.hash)
    form = HashForm()
    return render(request, "hashing/home.html", {"form": form})

def hash(request, hash):
    hash = Hash.objects.get(hash=hash)
    return render(request, "hashing/hash.html", {"hash": hash})

def quick_hash(request):
    text = request.GET.get("text", "")
    print(text)
    hash = hashlib.sha256(text.encode('utf-8')).hexdigest()
    return JsonResponse({"hash": hash})
