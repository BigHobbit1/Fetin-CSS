#!/bin/bash

# Script para enviar o e-mail com as informações do pipeline

# Recebe o e-mail de destino como argumento
TO_EMAIL=$1
SUBJECT="Pipeline Jenkins - Status da execução"
BODY=$2  # Corpo do e-mail passado como argumento

# Envia o e-mail usando o comando 'mail' do mailutils
echo "$BODY" | mail -s "$SUBJECT" "$TO_EMAIL"

# Exibe uma mensagem de confirmação no console
echo "E-mail enviado para: $TO_EMAIL"
