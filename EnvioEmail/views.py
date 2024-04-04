from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from django.core.mail import BadHeaderError, send_mail
from django.core.exceptions import ValidationError
from django.http import HttpResponse

class EmailAPIView(APIView):
    def post(self, request, *args, **kwargs):
        subject = request.POST.get("subject", "A sessão do whatsApp expirou")
        message = request.POST.get("message", "Não consigo mais acessar o whatsApp, pois o meu celular está quebrado e no computador foi desconectado")
        recipient_list = ["ju.bm.barros@gmail.com", "martinsbarroskaua@gmail.com", "joaovictor239090@gmail.com"]
        from_email = "martinsbarroskaua85@gmail.com"
        try:
            send_mail(
                subject,
                message,
                recipient_list=recipient_list,
                from_email=from_email,
            )
        except BadHeaderError:
            return HttpResponse("Cabeçalho inválido!")
        except ValidationError as e:
            return HttpResponse(str(e))
        return HttpResponse(
            {'Email enviado com sucesso'}, status = status.HTTP_200_OK)