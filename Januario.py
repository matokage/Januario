#!/usr/bin/env python3

# ircecho.py
# Copyright (C) 2011 : Robert L Szkutak II - http://robertszkutak.com
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

#Importa os comandos
import sys
import socket
import string
import time
import random

#configuração da rede
HOST = "irc.rizon.net"
PORT = 6667

#configuração do Bot
NICK = "Januario"
IDENT = "Anuario"
REALNAME = "Janu"
MASTER = "Matokage"
CHANNEL = "#TavernaTeste"

#magia negra da connexão
readbuffer = ""

s=socket.socket( )
s.connect((HOST, PORT))

s.send(bytes("NICK %s\r\n" % NICK, "UTF-8"))
s.send(bytes("USER %s %s bla :%s\r\n" % (IDENT, HOST, REALNAME), "UTF-8"))
s.send(bytes("JOIN" + CHANNEL + "\n", "UTF-8"));
s.send(bytes("PRIVMSG %s :Hello Master\r\n" % MASTER, "UTF-8"))

#loop começa
while 1:

#destina uma variavel para as menssagens e retira o comando \n
    readbuffer = readbuffer+s.recv(1024).decode("UTF-8")
    temp = str.split(readbuffer, "\n")
    readbuffer=temp.pop( )
#é pego então o restante e ele é separado em uma lista chamada line
    for line in temp:
        line = str.rstrip(line)
        line = str.split(line)
#Resposta do Ping usando o Elemento 1 da lista "Line"
        if(line[0] == "PING"):
            s.send(bytes("PONG %s\r\n" % line[1], "UTF-8"))
            s.send(bytes("JOIN " + CHANNEL + "\n", "UTF-8"))
#Line então é enumerado em indice e printado uma palavra depois da outra          
        for index, i in enumerate(line):
            print(line[index])

#Triggers gerais
            if(line[index] == ":VERSION"):
                usur = str.split(line[0],"!")
                usu = str.split(usur[0],":")
                s.send(bytes("NOTICE "+ usu[1] +" :\001VERSION Januario Ver.0.5.3 Python 3.6.4\001\r\n", "UTF-8"))
            if(line[index] == "JOIN"):
                usur = str.split(line[0],"!")
                usu = str.split(usur[0],":")
                if(usu[1] != "Januario"):
                    time.sleep(0.5)
                    s.send(bytes("NOTICE "+ usu[1] +" :Olá, %s! Seja bem vindo a Taverna! Cheque o nosso !menu\r\n" % usu[1], "UTF-8"))
                else:
                    s.send(bytes("PRIVMSG "+ CHANNEL +" :Cheguei.\r\n", "UTF-8"))
            if(line[index] == "PART"):
                usur = str.split(line[0],"!")
                usu = str.split(usur[0],":")
                if(usu[1] != "Januario"):
                    time.sleep(0.5)
                    s.send(bytes("PRIVMSG "+ usu[1] +" :Volte sempre!\r\n", "UTF-8"))
            if(line[index] == ":sopa")|(line[index] == ":Sopa")|(line[index] == ":SOPA"):
                time.sleep(0.5)
                s.send(bytes("PRIVMSG "+ CHANNEL +" :Infelizmente a sopa acabou :^(\r\n", "UTF-8"))
            if(line[index] == ":Opa")|(line[index] == ":opa")|(line[index] == ":OPA")|(line[index] == ":Opa!")|(line[index] == ":OPA!")|(line[index] == ":opa!"):
                time.sleep(0.5)
                s.send(bytes("PRIVMSG "+ CHANNEL +" :Só nas arte, né?\r\n", "UTF-8"))
            if(line[index] == ":ayy")|(line[index] == ":Ayy")|(line[index] == ":AYY"):
                time.sleep(0.5)
                s.send(bytes("PRIVMSG "+ CHANNEL +" :lmao\r\n", "UTF-8"))
#Serviços de taverna
            if(line[index] == ":!menu"):
                s.send(bytes("PRIVMSG "+ CHANNEL +" :\x01ACTION Dá o menu a você\x01\r\n", "UTF-8"))
                time.sleep(2)
                s.send(bytes("PRIVMSG "+ CHANNEL +" :==Menu==\r\n", "UTF-8"))
                s.send(bytes("PRIVMSG "+ CHANNEL +" :Água     | !h2o\r\n", "UTF-8"))
                s.send(bytes("PRIVMSG "+ CHANNEL +" :Feijoada | !nada\r\n", "UTF-8"))
                s.send(bytes("PRIVMSG "+ CHANNEL +" :Amendoin | !mendoin\r\n", "UTF-8"))
                s.send(bytes("PRIVMSG "+ CHANNEL +" :Picanha  | !pica\r\n", "UTF-8"))
                s.send(bytes("PRIVMSG "+ CHANNEL +" :Linguisa | !trap\r\n", "UTF-8"))
                s.send(bytes("PRIVMSG "+ CHANNEL +" :Cerveja  | !cerva\r\n", "UTF-8"))
            if(line[index] == ":!cerva"):
                usur = str.split(line[0],"!")
                usu = str.split(usur[0],":")
                s.send(bytes("PRIVMSG "+ CHANNEL +" :\x01ACTION Serve uma cerveja para %s\x01\r\n" % usu[1], "UTF-8"))
                time.sleep(2)
                s.send(bytes("PRIVMSG "+ CHANNEL +" :Mais alguma coisa?\r\n", "UTF-8"))
            if(line[index] == ":!pica"):
                usur = str.split(line[0],"!")
                usu = str.split(usur[0],":")
                s.send(bytes("PRIVMSG "+ CHANNEL +" :\x01ACTION Dá uma picanha no ponto para %s\x01\r\n" % usu[1], "UTF-8"))
                time.sleep(2)
                s.send(bytes("PRIVMSG "+ CHANNEL +" :Mais alguma coisa?\r\n", "UTF-8"))
            if(line[index] == ":!trap"):
                usur = str.split(line[0],"!")
                usu = str.split(usur[0],":")
                s.send(bytes("PRIVMSG "+ CHANNEL +" :\x01ACTION Dá a linguisa para %s\x01\r\n" % usu[1], "UTF-8"))
                time.sleep(2)
                s.send(bytes("PRIVMSG "+ CHANNEL +" ::^)\r\n", "UTF-8"))
            if(line[index] == ":!cruristin"):
                usur = str.split(line[0],"!")
                usu = str.split(usur[0],":")
                s.send(bytes("PRIVMSG "+ CHANNEL +" :\x01ACTION Dá água a %s\x01\r\n" % usu[1], "UTF-8"))
                time.sleep(2)
                resp = [1,2,3,4,5,6,7,8]
                numb = random.sample(resp,1)
                if(numb[0] == 1):
                    s.send(bytes("PRIVMSG "+ CHANNEL +" :Beba água.\r\n", "UTF-8"))
                if(numb[0] == 2):
                    s.send(bytes("PRIVMSG "+ CHANNEL +" :Água é vida.\r\n", "UTF-8"))
                if(numb[0] == 3):
                    s.send(bytes("PRIVMSG "+ CHANNEL +" :Agora vai ficar tudo bem.\r\n", "UTF-8"))
                if(numb[0] == 4):
                    s.send(bytes("PRIVMSG "+ CHANNEL +" :Água faz bem para a saúde.\r\n", "UTF-8"))
                if(numb[0] == 5):
                    s.send(bytes("PRIVMSG "+ CHANNEL +" :A água é o único liquido que não é bloated.\r\n", "UTF-8"))
                if(numb[0] == 6):
                    s.send(bytes("PRIVMSG "+ CHANNEL +" :Se todo mundo bebesse água não estariam me enchendo o saco.\r\n", "UTF-8"))
                if(numb[0] == 7):
                    s.send(bytes("PRIVMSG "+ CHANNEL +" :Cuidado com esse ácido hidrico.\r\n", "UTF-8"))
                if(numb[0] == 8):
                    s.send(bytes("PRIVMSG "+ CHANNEL +" :.yt oPwnAq2xMUg\r\n", "UTF-8"))
            if(line[index] == ":!nada"):
                usur = str.split(line[0],"!")
                usu = str.split(usur[0],":")
                s.send(bytes("PRIVMSG "+ CHANNEL +" :\x01ACTION Dá uma feijoada com bastante caldo para %s\x01\r\n" % usu[1], "UTF-8"))
                time.sleep(2)
                s.send(bytes("PRIVMSG "+ CHANNEL +" :Nada acontece.\r\n", "UTF-8"))
            if(line[index] == ":!mendoin"):
                usur = str.split(line[0],"!")
                usu = str.split(usur[0],":")
                s.send(bytes("PRIVMSG "+ CHANNEL +" :\x01ACTION Serve uma porção de mendoin para %s\x01\r\n" % usu[1], "UTF-8"))
                time.sleep(2)
                s.send(bytes("PRIVMSG "+ CHANNEL +" :Mais alguma coisa?\r\n", "UTF-8"))
