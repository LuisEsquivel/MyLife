import js2py
import pymysql.cursors
import pymysql



email = ('angel@mylife.com')
pswd = ('12e34')

db = pymysql.connect(host='localhost',
                         user='root',
                         password='angeel98',
                         db='Facebuk',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)
query = db.cursor()
while True:
        if query.execute("SELECT * FROM nosequepedo_añadirusuarios WHERE Email='" + email + "'AND Contraseña='" + pswd + "'"):
            db.commit()
            print('Done')
            # Se usa break para romper el ciclo while
            break
        else:
            db.commit()
            js = """
            <script>
              alert('Datos incorrectos   ');
            </script>
            """
            result = js2py.eval_js(js)  # executing JavaScript and converting the result to python string
            print(result)
            break
