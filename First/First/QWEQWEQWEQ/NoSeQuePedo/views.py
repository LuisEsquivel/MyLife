from django.shortcuts import render_to_response, redirect
from django.http import HttpResponse
from First.QWEQWEQWEQ.NoSeQuePedo.models import Publicaciones,AñadirUsuarios
import pymysql.cursors, pymysql
from django.views.generic import ListView,UpdateView


import time

# Create your views here.

#Esta funcion sirve para llamar a la interfaz
def home(request):
    return render_to_response("login.html")

#Esta tambien sirve pa' lo mismo que la de arriba
def welcome(request):
        return render_to_response("inicio.html")

#Esta funcion sirve para poder REGISTAR USUARIOS
def añadirUsers(request):
    name = request.GET.get('nombre')
    apellido = request.GET.get('apellido')
    email = request.GET.get('email')
    pswd = request.GET.get('pswd')

    print (len(name))
    print (len(apellido))
    print (len(email))
    print(len(pswd))



    db = pymysql.connect(host='localhost',
                             user='root',
                             password='0925',
                             db='Facebuk',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

    #Comprobacion de que no hayan valores nulos y que no sobrepasen el limite de caracteres
    if (len(name)== 0 or len(name)>50):
        response = HttpResponse()
        response.write("<script>"
                       "alert('Datos invalidos. Puede ser porque ingresaste valores nulos o porque sobrepasaste el "
                       "limite de caracteres permitidos (max 50).\\n"
                       "Intentalo de nuevo por favor.');"
                       "</script>"
                       "<meta http-equiv='refresh' content='0;URL=http://127.0.0.1:8000/'>")
        return response
    if (len(apellido)== 0 or len(apellido)>50):
        response = HttpResponse()
        response.write("<script>"
                       "alert('Datos invalidos. Puede ser porque ingresaste valores nulos o porque sobrepasaste el "
                       "limite de caracteres permitidos (max 50).\\n"
                       "Intentalo de nuevo por favor.');"
                       "</script>"
                       "<meta http-equiv='refresh' content='0;URL=http://127.0.0.1:8000/'>")
        return response
    if (len(email)== 0 or len(email)>50):
        response = HttpResponse()
        response.write("<script>"
                       "alert('Datos invalidos. Puede ser porque ingresaste valores nulos o porque sobrepasaste el "
                       "limite de caracteres permitidos (max 50).\\n"
                       "Intentalo de nuevo por favor.');"
                       "</script>"
                       "<meta http-equiv='refresh' content='0;URL=http://127.0.0.1:8000/'>")
        return response
    if (len(pswd)== 0 or len(pswd)>20):
        response = HttpResponse()
        response.write("<script>"
                       "alert('Datos invalidos. Puede ser porque ingresaste valores nulos o porque sobrepasaste el "
                       "limite de caracteres permitidos (max 50).\\n"
                       "Intentalo de nuevo por favor.');"
                       "</script>"
                       "<meta http-equiv='refresh' content='0;URL=http://127.0.0.1:8000/'>")
        return response



    query = db.cursor()
    while True:
        if query.execute("INSERT INTO nosequepedo_añadirusuarios (Nombrazo,Apellidos, Email, Contraseña) values "
                             "('" + name + "','" + apellido + "','" + email + "','" + pswd + "');"):
            db.commit()
            return redirect('welcome')
            # Se usa break para romper el ciclo while
            break
        else:
            db.commit()
            return HttpResponse('Datos invalidos')

#Esta funcion es el sistema de LOGIN
def login(request):
    email = request.GET.get('email')
    pswd = request.GET.get('pswd')

    db = pymysql.connect(host='localhost',
                         user='root',
                         password='0925',
                         db='Facebuk',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)
    query = db.cursor()
    while True:
        if query.execute("SELECT * FROM nosequepedo_añadirusuarios WHERE Email='" + email + "'AND Contraseña='" + pswd + "'"):
            db.commit()
            return redirect('welcome')
            # Se usa break para romper el ciclo while
            break
        else:
            response = HttpResponse()
            response.write("<script>"
                           "alert('Datos incorrectos.\\n"
                           "Intentalo de nuevo por favor.');"
                           "</script>"
                           "<meta http-equiv='refresh' content='0;URL=http://127.0.0.1:8000/'>")
            return response

#Retorna la interfaz de messages.html
def mensajes(request):
    return render_to_response("messages.html")

#Función para enviar mensajes
def enviar(request):
    userRemitente = request.POST.get('Remitente')
    userDestinatario = request.POST.get('Destinatario')
    msg = request.POST.get('msg')
    fecha = time.strftime('%Y-%m-%d %H:%M:%S')

    print (userRemitente)
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='0925',
                         db='Facebuk',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)
    query = db.cursor()

    if query.execute("INSERT INTO messages (horaEnvio,msg,userDestinatario,userRemitente) values ('" + fecha + "','"
                             + msg + "','"
                             + userDestinatario + "','"
                             + userRemitente + "');"):
            db.commit()
            return redirect('messages')

#Esta funcion sirve para BUSCAR registros
def buscar(request):
    keys = request.GET.get('buscar')
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='0925',
                         db='Facebuk',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)

    query = db.cursor()
    while True:
        if query.execute("SELECT Nombrazo as Nombre,Apellidos FROM nosequepedo_añadirusuarios WHERE Nombrazo='"+keys +
                                 "' or Apellidos='" + keys + " ' ;"):

            rows = query.fetchall()
            response=HttpResponse()
            # Response del encabezado
            response.write("<head>"
                           "<title>Busqueda</title>"
                             "<link rel='shortcut icon' href='http://s2.subirimagenes.com/imagen/previo/thump_9823042cats.png'>"
                           "</head>"
                           )
            # Response de la barra negra
            response.write("<style>"
                           "body {"
                           "margin: 0 auto;"
                           "}"
                           "nav {"
                           " width: 100%;"
                           "height: 60px;"
                           "background:black repeat-x  100%;"
                           "padding: 0;"
                           "margin: 0 auto;"
                           "border: 0;"
                           "}"
                           "</style>")
            # Response del estilo del texto MyLife de la barra negra
            response.write("<style>"
                           "nav header strong {"
                           "position: relative;"
                           "margin-left: 150px;"
                           "top: 8px;"
                           "font-family: 'verdana';"
                           "font-size: 35px;"
                           "color: white ;"
                           "}"
                           "</style>")

            # Response del textbox Buscar
            response.write("<style>"
                           ".Buscar {"
                           "position: relative;"
                            "margin-left: 480px;"
                            "font-family: 'verdana';"
                            "font-size: 15px;"
                            "color: white;"
                            "bottom: 33px;"
                           "}"
                           
                           ".textbox {"
                            "border: 1px solid #DBE1EB;"
                            "font-size: 15px;"
                            "font-family: Arial, Verdana;"
                            "padding-left: 15px;"
                            "padding-right: 15px;"
                            "padding-top: 3px;"
                            "padding-bottom: 5px;"
                            "border-radius: 4px;"
                            "v-moz-border-radius: 4px;"
                            "-webkit-border-radius: 4px;"
                            "-o-border-radius: 4px;"
                            "background: #FFFFFF;"
                            "background: linear-gradient(left, #FFFFFF, #F7F9FA);"
                            "background: -moz-linear-gradient(left, #FFFFFF, #F7F9FA);"
                            "background: -webkit-linear-gradient(left, #FFFFFF, #F7F9FA);"
                            "background: -o-linear-gradient(left, #FFFFFF, #F7F9FA);"
                            "color: #2E3133;"
                            "margin-top: 10px;"
                            "}"
                            ".textbox:focus"
                            "{"
                            "color: #2E3133;"
                            "border-color: #FBFFAD;"
                            "}"
                            "</style>")
            # Response de las Opciones
            response.write("<style>"
                           ".opciones"
                           "{"
                           "position: relative;"
                           "margin-left: 950px;"
                           "font-family: 'verdana';"
                           "font-size: 15px;"
                           "bottom: 70px;"
                           "}"

                           ".opciones a"
                           "{"
                           "vtext-decoration: none;"
                           "color:white;"
                           "padding: 10px;"
                           " }"

                           " .opciones a:hover"
                           "{"
                           "color: black;"
                           "text-decoration-color: black;"
                           "background-color:  white ;"
                           "border-radius: 30px;"
                           "cursor:  pointer;"
                           "}"
                           "</style>")
            # Response de todo de la barra negra
            response.write("<nav class='nav'>"
                           "<a href='http://127.0.0.1:8000/welcome' style='text-decoration: none;'> <header><strong>MyLife</strong></header></a>"
                           "<form action='' method='get'>"
                           "<div class='Buscar'>"
                           "<input type='text' class='textbox' name='buscar' placeholder='Buscar' id='buscar' size='45'>"
                           "<input type='hidden' value='buscar'>"
                           "</div> </form>"
                           "<div class='opciones'>"
                           "<a href='http://127.0.0.1:8000/welcome'style='text-decoration:none'>Inicio</a>"
                           "<a href='http://127.0.0.1:8000/profile/'style='text-decoration:none'>Perfil</a>"
                           "<a href='http://127.0.0.1:8000/messages/' style='text-decoration:none'>Mensajes</a>"
                           "<a href='http://127.0.0.1:8000/solicitudes/'style='text-decoration:none'>Solicitudes</a>"
                           "<a href='http://127.0.0.1:8000/logout' style='text-decoration:none'>Cerrar sesión</a>"
                           "</div> </nav> </body> </html>")
            response.write("<style>"
                           ".results {"
                           "text-align: left;"
                            
                           "font-size: 30px;"
                           "font-family:'Comic Sans MS';"
                           "}"
                          ".resultsError {"
                           "text-align: left;"
                           "font-size: 25px;"
                           "font-family:'Comic Sans MS';"
                           "}"
                           "</style>")
            response.write("<div class='results'> Resultados de busqueda</div><br>")
            response.write("<div class='resultsError'>")

            final = str(rows).lstrip("[{.")
            final2 = str(final).replace("'","")
            final3 = str(final2).replace(",",". ")
            final4 = str(final3).rstrip("}].")
            response.write(final4)
            response.write("</div>")
            return response
            # Se usa break para romper el ciclo while
            break
        else:
            response = HttpResponse()
            # Response del encabezado
            response.write("<head>"
                           "<title>Busqueda</title>"
                           # "<link rel='shortcut icon' href='http://s2.subirimagenes.com/imagen/previo/thump_9823042cats.png'>"
                           "</head>")
            # Response de la barra negra
            response.write("<style>"
                           "body {"
                           "margin: 0 auto;"
                           "}"
                           "nav {"
                           " width: 100%;"
                           "height: 60px;"
                           "background:black repeat-x  100%;"
                           "padding: 0;"
                           "margin: 0 auto;"
                           "border: 0;"
                           "}"
                           "</style>")
            # Response del estilo del texto MyLife de la barra negra
            response.write("<style>"
                           "nav header strong {"
                           "position: relative;"
                           "margin-left: 150px;"
                           "top: 8px;"
                           "font-family: 'verdana';"
                           "font-size: 35px;"
                           "color: white ;"
                           "}"
                           "</style>")
            # Response del textbox Buscar
            response.write("<style>"
                           ".Buscar {"
                           "position: relative;"
                           "margin-left: 480px;"
                           "font-family: 'verdana';"
                           "font-size: 15px;"
                           "color: white;"
                           "bottom: 33px;"
                           "}"

                           ".textbox {"
                           "border: 1px solid #DBE1EB;"
                           "font-size: 15px;"
                           "font-family: Arial, Verdana;"
                           "padding-left: 15px;"
                           "padding-right: 15px;"
                           "padding-top: 3px;"
                           "padding-bottom: 5px;"
                           "border-radius: 4px;"
                           "v-moz-border-radius: 4px;"
                           "-webkit-border-radius: 4px;"
                           "-o-border-radius: 4px;"
                           "background: #FFFFFF;"
                           "background: linear-gradient(left, #FFFFFF, #F7F9FA);"
                           "background: -moz-linear-gradient(left, #FFFFFF, #F7F9FA);"
                           "background: -webkit-linear-gradient(left, #FFFFFF, #F7F9FA);"
                           "background: -o-linear-gradient(left, #FFFFFF, #F7F9FA);"
                           "color: #2E3133;"
                           "margin-top: 10px;"
                           "}"
                           ".textbox:focus"
                           "{"
                           "color: #2E3133;"
                           "border-color: #FBFFAD;"
                           "}"
                           "</style>")
            # Response de las Opciones
            response.write("<style>"
                           ".opciones"
                           "{"
                           "position: relative;"
                           "margin-left: 950px;"
                           "font-family: 'verdana';"
                           "font-size: 15px;"
                           "bottom: 70px;"
                           "}"

                           ".opciones a"
                           "{"
                           "vtext-decoration: none;"
                           "color:white;"
                           "padding: 10px;"
                           " }"

                           " .opciones a:hover"
                           "{"
                           "color: black;"
                           "text-decoration-color: black;"
                           "background-color:  white ;"
                           "border-radius: 30px;"
                           "cursor:  pointer;"
                           "}"
                           "</style>")
            # Response de todo de la barra negra
            response.write("<nav class='nav'>"
                           "<a href='http://127.0.0.1:8000/welcome' style='text-decoration: none;'><header><strong>MyLife</strong></header>"
                           "<form action='' method='get'>"
                           "<div class='Buscar'>"
                           "<input type='text' class='textbox' name='buscar' placeholder='Buscar' id='buscar'size='45'>"
                           "<input type='hidden' value='buscar'>"
                           "</div> </form>"
                           "<div class='opciones'>"
                           "<a href='http://127.0.0.1:8000/welcome'style='text-decoration:none'>Inicio</a>"
                           "<a href='http://127.0.0.1:8000/profile/'style='text-decoration:none'>Perfil</a>"
                           "<a href='http://127.0.0.1:8000/messages/' style='text-decoration:none'>Mensajes</a>"
                           "<a href='http://127.0.0.1:8000/solicitudes/'style='text-decoration:none'>Solicitudes</a>"
                           "<a href='http://127.0.0.1:8000/logout' style='text-decoration:none'>Cerrar sesión</a>"
                           "</div> </nav> </body> </html>")
            response.write("<style>"
                           ".results {"
                           "text-align: left;"
                           "font-size: 30px;"
                           "font-family:'Comic Sans MS';"
                           "}"
                           ".resultsError{"
                           "text-align: left;"
                           "font-size: 25px;"
                           "font-family:'Comic Sans MS';"
                           "}"
                           "</style>")
            response.write("<div class='results'> Resultados de la busqueda:</div><br>")
            response.write("<div class='resultsError'>No     se encontraron registros</div><br>")
            return response

#Esta funcion sirve para poder INSERTAR lo que se desea PUBLICAR en la BD
def publicar(request):
    mensaje = request.GET.get('textarea')
    email = request.GET.get('Remitente')

    print(email)

    if len(mensaje)>280:
        response = HttpResponse()
        response.write("<script>"
                       "alert('Limite de caracteres excedido (max 280)');"
                       "</script>"
                       "<meta http-equiv='refresh' content='0;URL=http://127.0.0.1:8000/welcome'>")
        return response


    db = pymysql.connect(host='localhost',
                         user='root',
                         password='0925',
                         db='Facebuk',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)

    fecha = time.strftime('%Y-%m-%d %H:%M:%S')


    query = db.cursor()
    if query.execute("INSERT INTO nosequepedo_publicaciones (msg,horaPublic,Email) values('"+mensaje+"','"+fecha+"','"+email+"');"):
        db.commit()
        response = HttpResponse()
        response.write("<meta http-equiv='refresh' content='0;URL=http://127.0.0.1:8000/welcome'>")
        return response
    else:
        return HttpResponse('Failed')

#Esta clase sirve para LISTAR las publicaciones
class publicaciones(ListView):
        model = Publicaciones
        template_name = 'inicio.html'

def subirImagen(request):
    ruta = request.POST.get("rutaimg")
    rutaFinal = "C:/Users/angel/Downloads/" + ruta
    imagen = Image.open(rutaFinal)
    imagen.show()
    response = HttpResponse()
    response.write("<img src="+rutaFinal+">")

    return response

def solicitudes(request):
    return render_to_response("solicitudes.html")

def logout(request):
    return redirect('inicio')

def profile(request):
    return render_to_response("profile.html")

def editprofile(request):
    return render_to_response("EditProfile.html")

def confirmEdit(request):
    fechaNac = request.POST.get("fechaNac")
    edad = request.POST.get("edad")
    ocupacion = request.POST.get("ocupacion")
    tel = request.POST.get("tel")
    cdOrigen = request.POST.get("cdOrigen")
    cdActual = request.POST.get("cdActual")
    user = request.POST.get("Remitente")

    db = pymysql.connect(host='localhost',
                         user='root',
                         password='0925',
                         db='Facebuk',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)
    query = db.cursor()

    if query.execute("update nosequepedo_añadirusuarios set FechaNac='"+fechaNac+"', Edad="+edad+", Ocupacion='"+ocupacion+"', Telefono='"
                             +tel+"',Ciudad_Origen='"+cdOrigen+"',Ciudad_Actual='"+cdActual+"' where Email='"+user+"';"):
        db.commit()
        info = query.fetchall()
        response =HttpResponse()
        response.write("<script>"
                           "alert('Perfil actualizado correctamente');"
                           "</script>"
                           "<meta http-equiv='refresh' content='0;URL=http://127.0.0.1:8000/profile'>")
        return response
    else:
        response = HttpResponse()
        response.write("<script>"
                       "alert('Ha ocurido un error. Intentalo de nuevo:)');"
                       "</script>"  
                       "<meta http-equiv='refresh' content='0;URL=http://127.0.0.1:8000/profile'>")
        return response

class profileInfo(ListView):
    model = AñadirUsuarios
    queryset = AñadirUsuarios.objects.filter(Email__icontains='angel@mylife.com')[:1]
    template_name = 'profile.html'

def eliminarPublicacion(request):
    email = request.POST.get("Remitente")
    id = request.POST.get("id")
    autor = request.POST.get("idUser")

    db = pymysql.connect(host='localhost',
                         user='root',
                         password='0925',
                         db='Facebuk',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)

    query = db.cursor()

    if query.execute("SELECT (Email) from nosequepedo_publicaciones where Email='"+email+"' and id="+id+";"):
        query.execute("DELETE FROM nosequepedo_publicaciones where id="+id+";")
        db.commit()
        return redirect('welcome')
    else:
        response = HttpResponse()
        response.write("<script>"
                       "alert('Solo puedes eliminar publicaciones que tu mismo hiciste.\\n"
                       "No puedes borrar las publicaciones de los demas usuarios.');"
                       "</script>"
                       "<meta http-equiv='refresh' content='0;URL=http://127.0.0.1:8000/welcome'>")
        return response
