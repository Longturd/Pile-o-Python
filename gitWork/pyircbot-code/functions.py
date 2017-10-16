#!/usr/bin/python
# coding: iso-8859-15

import socket, os, string, sys, linecache, random, time
import config

### METAFUNCIONES ###
#####################
def isInt(str):
   """Is the given string an integer?"""
   try:int(str)
   except ValueError:return 0
   else:return 1

def stats_top5(lines):
   d = {} # Diccionario donde las claves seran los nicks y los valores de las lineas de cada uno.

   for i in lines:
      split = i.split(':')
      split2 = split[2].split('!')

      if(split2[0] in d):
         d[split2[0]] = d.get(split2[0]) + 1
         #print split2[0]+" ya esta en la lista! Tiene "+str(d[split2[0]])+" entradas."
      else:
         #print "Agregando "+split2[0]+" al array general."
         d[split2[0]] = 1

   # Obtenemos los usuarios con mas lineas escritas...
   top5 = [0,0,0,0,0]
   top5_nicks = ['','','','','']
   for nick in d:
      if(d.get(nick) > min(top5)):
         indice = top5.index(min(top5))
         top5[indice] = d.get(nick)
         top5_nicks[indice] = nick

   # ... y ordenamos convenientemente la lista.
   top = []
   top_nicks = []
   while(len(top5) > 0):
      indice = top5.index(max(top5))
      top.append(top5.pop(indice))
      top_nicks.append(top5_nicks.pop(indice))

   return top, top_nicks

def stats_tail5(lines):
   d = {} # Diccionario donde las claves seran los nicks y los valores de las lineas de cada uno.

   for i in lines:
      split = i.split(':')
      split2 = split[2].split('!')

      if(split2[0] in d):
         d[split2[0]] = d.get(split2[0]) + 1
         #print split2[0]+" ya esta en la lista! Tiene "+str(d[split2[0]])+" entradas."
      else:
         #print "Agregando "+split2[0]+" al array general."
         d[split2[0]] = 1

   # Obtenemos los usuarios con menos lineas escritas...
   big = 999999999999
   tail5 = [big,big,big,big,big]
   tail5_nicks = ['','','','','']
   for nick in d:
      if(d.get(nick) < max(tail5)):
         indice = tail5.index(max(tail5))
         tail5[indice] = d.get(nick)
         tail5_nicks[indice] = nick

   # ... y ordenamos convenientemente la lista.
   tail = []
   tail_nicks = []
   while(len(tail5) > 0):
      indice = tail5.index(min(tail5))
      tail.append(tail5.pop(indice))
      tail_nicks.append(tail5_nicks.pop(indice))

   return tail, tail_nicks

def stats_tacos(lines):
   d = {} # Diccionario donde las claves seran los nicks y el nº de tacos de cada uno.

   for i in lines:
      split = i.split(':')
      split2 = split[2].split('!')

      for taco in config.tacos:
         if(split[3].find(taco) != -1):
            #print 'Frase con taco: ' + split[3]
            if(split2[0] in d):
               d[split2[0]] = d.get(split2[0]) + 1
            else:
               d[split2[0]] = 1

   # Obtenemos los usuarios con mas lineas escritas...
   top5_tacos = [0,0,0,0,0]
   top5_nicks_tacos = ['','','','','']
   for nick in d:
      if(d.get(nick) > min(top5_tacos)):
         indice = top5_tacos.index(min(top5_tacos))
         top5_tacos[indice] = d.get(nick)
         top5_nicks_tacos[indice] = nick

   # ... y ordenamos convenientemente la lista.
   top_tacos = []
   top_nicks_tacos = []
   while(len(top5_tacos) > 0):
      indice = top5_tacos.index(max(top5_tacos))
      top_tacos.append(top5_tacos.pop(indice))
      top_nicks_tacos.append(top5_nicks_tacos.pop(indice))

   return top_tacos, top_nicks_tacos

### FUNCIONES ###
#################

def crea_stats(s, line):
   fp = open(config.LOG_FILE, 'r')
   lines = fp.readlines() # lines es una list de urls
   fp.close()

   list = line.split('stats')

   if(list[1].strip() == 'top5'):
      top,top_nicks = stats_top5(lines) # Funcion top5.
      j = 0
      s.send("PRIVMSG %s :Top 5:\r\n" % (config.CHANNEL))
      for i in top_nicks:
         s.send("PRIVMSG %s :%s - %s lineas.\r\n" % (config.CHANNEL,i,top[j]))
         time.sleep(1)
         j +=  1

   elif(list[1].strip() == 'tail5'):
      tail,tail_nicks = stats_tail5(lines) # Funcion down5.
      j = 0
      s.send("PRIVMSG %s :Tail 5:\r\n" % (config.CHANNEL))
      for i in tail_nicks:
         s.send("PRIVMSG %s :%s - %s lineas.\r\n" % (config.CHANNEL,i,tail[j]))
         time.sleep(1)
         j +=  1

   elif(list[1].strip() == 'insults'):
      tacos,tacos_nicks = stats_tacos(lines)
      j = 0
      s.send("PRIVMSG %s :Top malhablados:\r\n" % (config.CHANNEL))
      for i in tacos_nicks:
         s.send("PRIVMSG %s :%s - %s tacos.\r\n" % (config.CHANNEL,i,tacos[j]))
         time.sleep(1)
         j +=  1

def ayuda(s, line):
   list = line.split('ayuda')

   if(list[1].strip() == ''):
      s.send("PRIVMSG %s :Uso: %s: servicio\r\n" % (config.CHANNEL,config.NICK))
      s.send("PRIVMSG %s :Lista de servicios: %s\r\n" % (config.CHANNEL,config.SERVICIOS))
   elif(list[1].strip() == 'acerca de'):
      s.send("PRIVMSG %s :%s\r\n" % (config.CHANNEL,config.SERVICIO_ACERCADE))
   elif(list[1].strip() == 'quit'):
      s.send("PRIVMSG %s :%s\r\n" % (config.CHANNEL,config.SERVICIO_QUIT))
   elif(list[1].strip() == 'quote'):
      s.send("PRIVMSG %s :%s\r\n" % (config.CHANNEL,config.SERVICIO_QUOTE))
   elif(list[1].strip() == 'saluda'):
      s.send("PRIVMSG %s :%s\r\n" % (config.CHANNEL,config.SERVICIO_SALUDA))
   elif(list[1].strip() == 'stats'):
      s.send("PRIVMSG %s :%s\r\n" % (config.CHANNEL,config.SERVICIO_STATS))
   elif(list[1].strip() == 'url'):
      s.send("PRIVMSG %s :%s\r\n" % (config.CHANNEL,config.SERVICIO_URL))
   else:
      s.send("PRIVMSG %s :Opcion no reconocida.\r\n" % (config.CHANNEL))

def registra_linea(line):
   if(line.find("PRIVMSG "+config.CHANNEL) != -1):
      line = line.replace(" PRIVMSG ", "")
      line = line.replace(config.CHANNEL, "")
      fp = open(config.LOG_FILE, 'a')
      fp.write(time.strftime("%Y-%m-%d:%H-%M-%S")+line+'\n')
      fp.close()

def espia_url(line):
   if(line.find("PRIVMSG "+config.CHANNEL) != -1):
      list = line.split(' ')
      for i in list:
         if((i.find('http://') != -1) or (i.find('ftp://')) != -1):
	         fp = open(config.URLS_FILE, 'a')
	         fp.write(i+'\n')
	         fp.close()
	         break

def lee_urls(s, line):
   # Lee y muestra las urls almacenadas.
   list = line.split('url')
   fp = open(config.URLS_FILE, 'r')
   lines = fp.readlines() # lines es una list de urls
   fp.close()

   if(isInt(list[1])):
      if(int(list[1]) < 11):
         req_urls = int(list[1]) # requested urls
         avail_urls = int(len(lines)) # available urls
         if(req_urls <= avail_urls):
            url_start = avail_urls - req_urls
            lines = lines[url_start:avail_urls] # seleccionamos un rango de elementos, elem inicial:final
            for i in lines:
	           s.send("PRIVMSG %s :%s\r\n" % (config.CHANNEL,i))
	           time.sleep(2) # Bug#3.
      else:
         #s.send("PRIVMSG %s :Peticion fuera de rango! Solo hay %s urls!\r\n" % (config.CHANNEL,len(lines)))
         s.send("PRIVMSG %s :Peticion fuera de rango! Solo se pueden pedir 10 urls (cortesia del puto dedo)!\r\n" % (config.CHANNEL))
   elif((list[1] != '') and (list[1] != ' ')):
      # Busqueda de texto.
      for i in lines:
         if config.DEBUG == 1:
            print i
         if(i.find(list[1].strip()) != -1):
            if config.DEBUG == 1:
               print i
            s.send("PRIVMSG %s :%s\r\n" % (config.CHANNEL,i))
            time.sleep(2) # Bug#3.
   else:
      s.send("PRIVMSG %s :Peticion erronea!\r\n" % (config.CHANNEL))

def anyade_quote(s, line):
   list = line.split('quote add')
   if(list[1] != ''):
      fp = open(config.QUOTES_FILE, 'a')
      fp.write(list[1]+'\n')
      fp.close()
      s.send("PRIVMSG %s :Quote añadido! \r\n" % (config.CHANNEL))
   else:
      s.send("PRIVMSG %s :Debes especificar una cadena como quote! \r\n" % (config.CHANNEL))

def lee_quote(s):
   # Leer una random quote.
   fp = open(config.QUOTES_FILE, 'r')
   lines = fp.readlines() # lines es una list de quotes
   fp.close()
   elems = len(lines)
   rand_num = random.randint(0,elems-1)
   s.send("PRIVMSG %s :%s\r\n" % (config.CHANNEL,lines[rand_num]))

def salir(s, line):
   if(line.find(config.QUITPWD) != -1):
      s.send("PRIVMSG %s :Chao!\r\n" % config.CHANNEL)
      #s.close();
      sys.exit(1)
   else:
      s.send("PRIVMSG %s :Reservado a los privilegiados.\r\n" % config.CHANNEL)

def mostrar_salida(s):
   recvd = s.recv(4096)
   if config.DEBUG == 1:
      print "Recibido: "+recvd

def mandar_pong(s):
   recvd = s.recv(4096)
   recvd = recvd.replace("PING", "PONG")
   s.send(recvd+'\r\n')
