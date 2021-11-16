from django.shortcuts import render

def handler400(request, exception):
   return render(request, 'pages/not_found.html')

def handler403(request, exception):
   return render(request, 'pages/not_found.html')

def handler404(request, exception):
   return render(request, 'pages/not_found.html')

def handler500(request, *args, **argv):
    return render(request, 'pages/not_found.html')