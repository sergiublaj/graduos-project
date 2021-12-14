from django.shortcuts import render


def handle_not_found_error(request, _):
    return render(request, 'pages/not_found.html')
