from django.shortcuts import render


def handle_client_error(request, _):
    return render(request, 'pages/not_found.html')


def handle_server_error(_):
    return render('D:\\Ana-Maria\\Facultate\\An_3\\IS_An3_sem1\\graduos-project\\templates\pages\\not_found.html')
