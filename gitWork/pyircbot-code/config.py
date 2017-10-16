#!/usr/bin/python
# coding: iso-8859-15

### VARIABLES ###
#################

# DGBUG info; booleano para activarlo/desactivarlo.
DEBUG = 0

# NICKNAME del bot.
NICK = "jirili"

# SERVER de IRC al que conectarlo y el puerto.
SERVER_NAME = "libres.irc-hispano.org"
SERVER_PORT = "6667"

# ident del bot.
USER = "jirili localhost libres.irc-hispano.org :jirili"

# CANAL al que se asocia el bot.
CHANNEL = "#tty"

# SERVICIOS ofrecidos por el bot.
SERVICIOS = "acerca de, ayuda [comando], quit, quote [add], saluda, stats top5|tail5|insults, url numero|palabra"
SERVICIO_ACERCADE = "Muestra una breve descripcion del bot."
SERVICIO_QUIT = "Desconecta el bot; requiere ciertos privilegios."
SERVICIO_QUOTE = "Muestra un quote aleatorio. Con el parametro add seguido de una frase, añade un quote."
SERVICIO_SALUDA = "Muestra un saludo. Saluda a un destino concreto con un parametro final."
SERVICIO_STATS = "Muestra una pequeña estadistica del canal. Actualmente solo atiende a los parametros top5, tail5 (los 5 nicks con mas y menos lineas escritas, respectivamente) y insults (los mas mal hablados)."
SERVICIO_URL = "Muestra urls. Necesita un parametro. Si este es un número N, muestra las N ultimas urls. Si es una cadena, hace una busqueda de las urls que la contengan para mostrarlas."

# PASSWORD para desconectar el bot.
QUITPWD = "tarantino"

# FICHEROS de url, quotes y demas. Ambos son ficheros de texto plano.
BASE = "/home/jors/.pyircbot2/"
URLS_FILE = BASE+"/urls.txt"
QUOTES_FILE = BASE+"/quotes.txt"
LOG_FILE = BASE+CHANNEL+".log"

# MODULOS a activar/desactivar.
M_AYUDA = 1
M_SALUDA = 1
M_QUOTE = 1
M_URL = 1
M_ACERCADE = 1
M_QUIT = 1
M_URLCATCHER = 1
M_LOGGING = 1
M_STATS = 1

# Variable de insultos; ampliar al gusto.
tacos = ['asno','bastard','bastardo','bitch','burro','borracho','borrico','cabron','caca','cabronazo',
         'cabroncete','caga','cago','cateto','capon','cerdo','cerda','cipote','cimbrel','cirulo','chocho',
         'coñ','desgraciad','kbron','kbronazo','energumeno','fitipaldi','gay','gili','gilipolla','guarro',
         'guarra','hijoputa','hijo de puta','imbecil','impotente','inutil','jamelgo','joputa','joda',
         'jodeputa','joder','joer','juer','julay','julandron','leche','mamon','marica','maricon','memo',
         'merluzo','mierda','miserable','moco','mojon','nabo','ostia','paleto','pedo','pene','perra',
         'polla','puta','puto','pendon','pendejo','polla','pilila','rabo','racano','ramera','rata',
         'rastrero','ruin','satan','serdo','semen','senil','sifilitico','son of a bitch','tarado','tonto',
         'toto','tralla','tranca','tumae','tu mae','tuputamae','tu puta mae','tu puta madre','verga',
         'vomita','warro','warra','whore','xoxo','yoya','zimbrel','zoquete','zorra','zurullo']
