import os
import smtplib
from email.message import EmailMessage
from email_remetente import email_usuario
from senha_acesso import senha_app
from email_envio import email_envio

remetente= email_usuario
sua_senha= senha_app
envio_email= email_envio

mensagem= EmailMessage()
mensagem ["Subject"]= input("Insira o Assunto: ")
mensagem ["From"]= remetente
mensagem ["To"]= envio_email
mensagem.set_content(input("Escreva a mensagem: \n"))

try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(remetente, sua_senha)
        smtp.send_message(mensagem)
        print(f"O e-mail foi enviado para {envio_email}.")
except smtplib.SMTPAuthenticationError:
    print("Ocorreu um erro na authenticação de dados.")
except Exception as e:
    print(f"Ocorreu um erro: \n{e}")