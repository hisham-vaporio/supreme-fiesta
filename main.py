#!/bin/env python

def foo(a):  # NonCompliant
    b = 12
    if a == 1:
        return b-1
    return b

from django.http import HttpResponse

def index(request):
    value = request.GET.get("value")
    response = HttpResponse("")
    response["Set-Cookie"] = value  # Noncompliant
    response.set_cookie("sessionid", value)  # Noncompliant
    return response

print("Hello World!")
print("Does this work?")
print(f"{foo(1)}")
