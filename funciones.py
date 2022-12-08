pip install numpy
pip install pandas
pip install ntk
from os import name
from urllib.request import urlopen
import re
import numpy as np
import pandas as pd
import nltk

nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

#Funcion para normalizar el texto, eliminacion caracteres especiales, texto en minusculas, etc
raza = ["negro","color carbón","esto no es África","se te acabó la tinta","sin derechos","indio verga","mono","mono verga","mono hijo de puta","negro cabrón","negro hijo de puta", 
"indio mama verga","negro enfermo","serrano bobo","costeño ladrón","gringo imbécil","serrano hijo de puta","mono ediondo","mono conche tu madre","negro pendejo",
"negro esclavo","negro verga", "negro de mierda", "mono infeliz", "indio estúpido", "negro ignorante", "negro asqueroso", "indio infeliz","indio imbécil", "longo", 
"longo feo", "negro miedo", "indio asqueroso", "longo estúpido", "negro puerco", "longo pasposo", "longo pendejo ", "mono infeliz", "mono puto", "longo verga", "negro puto",
"india puerca", "negra asco", "asco de negros", "indios sucios ", "longos asquerosos" ,"indio","longa", "mono asco","imbecil", "hijo puta","mamaracho", "adefesioso",
"ruliman","paisano","indio mmvrg","indio hdp","indio hp","mono mmvrg","mono hp","mono cvrg","mono vrg","mono hdp","negro sucio","indio sucio","mono sucio",
"anda vender cocada","negro mal parido","costeño mal parido","indio come papa"]

genero = ["loca", "puta", "sirvienta", "marrana", "ignorante", "mujer tenías que ser", "a cocinar", "mamacita", "perra", "puto", "zorra", "indecente", "cochina","cochino", 
"zafada", "loco","zafado", "hombre tenías que ser", "patán", "cojuda", "cojudo", "desgraciado", "desgraciada", "analfabeto","analfabeta", "cornudo", "cornuda","cornudos", 
"perra de mierda","facilota","chucha","reflechucha","chepa","verga","mierda","cabron","cabrón","gil","retrasado","lelo","porqueria","apestoso","maldito","a la cocina","menso",
"mensa","estupida","estupido","cachudo","cachuda","bruto","delicada","delicado","bruta","tonta","tonto","zopenco","zopenca","tarado","tarada","imbécil","puta barata",
"chucha apestoza","sapa de mrd","sapo cabrón", "idiota","putita","putota","reputa","triplehijueputa"]

orientacion = ["maricon de mierda","virado","maricon", "marica de mierda", "del otro bando", "menestra puto", "maricon imbécil", "gay asco", "gay de verga", 
"maricas asquerosos", "pedazos putos", "traga pitos","muerde almohadas", "culo flojo", "maricon imbecil", "marica", "gay", "menestron", "menestra","pajero",
"huevon","puñal","marimacha","afeminado","nena","nenita","niña","princesa","princeso","veado","boiola","bolleras","locas","sopla nucas","intento macho","chupamela","chupa pitos","hembra",
"reculeado","chullo huevo","puto de mierda","puto cagón","come pitos","marica reflechuchatumadre","chucha floja","triple homosexual","tetranutra","chupa huevos","chupa bolas","tortillera","lesbiana la puta tu madre",
"puñeta","falta de huevos","lesbiana de mrd","jabancho","lamebolas","hermafrodita","femina","machona","mixto","mariposon","maricota","invertido","joto","muerdealmohadas","mariquita",
"pinche joto","mamapinga","mariconcito","putito"]

edad = ["enano cara verga","guambra caca","come verga enano","niño hijo de puta","enano castroso","tu madre te cagó","enano hijo de puta","guambra asco", 
"enano gil", "viejo de mierda", "enano ciego", "vieja inútil", "chamo imbécil", "guambra verga", "mocosa", "viejos", "verga de chamos", "guambra coco", 
"chamo coco", "enano puto", "majadero", "majadera", "adoptada", "adoptado", "aborto", "cara de vrga" , "hijo de puta" , "mocoso pendejo", "guambra majadero", "guambra majadera", 
"mocosa inútil ", "mocoso malagradecido", "mocoso malagradecido ","mal agradecida", "mocoso mantenido", "mimado", "mocosa mantenida", "mimada",  "jodida", "jodido", "altanero",
"altanera", "verga de juventud", "viejo lento","enano verga","guambra caca", "mocoso", "viejo verga", "flacido","enano","marrano","gordo", "puerco","cerdo",
"chancho","esqueleto","guambra vrg","mocosa mal parida","guambra metido","condon roto","enano cabrón","mocoso gil","chamo vrg","viejo metido","viejo sapo","viejo chismoso",
"mocoso bueno para nada","guambra castroso","guambra","viejo mal parido","mocoso mal educado"]
raza = list(set(raza))

genero = list(set(genero))

orientacion = list(set(orientacion))

edad = list(set(edad))


#NORMALIZAR LISTAS FIJAS
def eliminar_stopwords(texto, stopwords):
  return ' '.join([word for word in texto.split(' ') if word not in stopwords])


def normList(text):
  vec = []
  for i in range(len(text)):
    a, b = 'áéíóúüñÁÉÍÓÚÜÑ', 'aeiouunAEIOUUN'
    til = str.maketrans(a, b)
    s = text[i].translate(til)
    d2 = re.sub('[^A-Za-z0-9]+', ' ', s)
    word = d2.lower()
    n = stopwords.words("spanish")
    word2 = eliminar_stopwords(word, n)
    word2 = word2.split()
    stemmer = PorterStemmer()
    l = []
    for i in word2:
      l.append(stemmer.stem(i))
    vec.append(l)
  return vec


def normalizar(text):
  a, b = 'áéíóúüñÁÉÍÓÚÜÑ', 'aeiouunAEIOUUN'
  til = str.maketrans(a, b)
  s = text.translate(til)
  d2 = re.sub('[^A-Za-z0-9]+', ' ', s)
  word = d2.lower()
  n = stopwords.words("spanish")
  n.append("si")
  n.append("asi")
  n.append("un")
  n.append("eres")
  word2 = eliminar_stopwords(word, n)
  word2 = word2.split()
  stemmer = PorterStemmer()
  l = []
  for i in word2:
    l.append(stemmer.stem(i))
  return l


raza = normList(raza)
print(len(raza))
genero = normList(genero)
print(len(genero))
orientacion = normList(orientacion)
print(len(orientacion))
edad = normList(edad)
print(len(edad))


def jaccard(grupo1, grupo2):
  interseccion = len(set(grupo1).intersection(set(grupo2)))
  union = len(set(grupo1).union(set(grupo2)))
  return interseccion / union


def discriminatorio(text):
  text = normalizar(text)
  va = []
  vb = []
  vc = []
  vd = []
  vt = []
  for i in range(len(text)):
    t = [text[i]]
    for j in range(len(raza)):
      a = jaccard(t,raza[j])
      b = jaccard(t,genero[j])
      c = jaccard(t,orientacion[j])
      d = jaccard(t,edad[j])
      if a == 1:
        va.append("".join(t))
      elif b == 1:
        vb.append("".join(t))
      elif c == 1:
        vc.append("".join(t))
      elif d == 1:
        vd.append("".join(t))
  su = len(va) + len(vb) + len(vc) +len(vd)
  if len(va)>0:
    r = ["Discriminación por Raza:",", ".join(va), str(round((len(va)*100)/su,2))+"%"]
    vt.append(" ".join(r))
  if len(vb)>0:
    g = ["Discriminación por Género:",", ".join(vb), str(round((len(vb)*100)/su,2))+"%"]
    vt.append(" ".join(g))
  if len(vc)>0:
    o = ["Discriminación por Orientación Sexual:",", ".join(vc), str(round((len(vc)*100)/su,2))+"%"]
    vt.append(" ".join(o))
  if len(vd)>0:
    e = ["Discriminación por Edad:",", ".join(vd), str(round((len(vd)*100)/su,2))+"%"]
    vt.append(" ".join(e))
  return "\n".join(vt)

def read(archivo):
  contenido = []

  with open(archivo) as archivo:
    for linea in archivo:
      contenido.append(linea)

  return contenido
