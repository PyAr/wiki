import email.Parser
import os, sys, shutil
import urllib
import StringIO
import MySQLdb
import time

class foto(object):
    '''El class foto recibe como parametro un email multipart conteniendo la imagen, comentario y titulo'''
    def __init__(self, mail):
        self.imagen = None
        self.titulo = None
        self.comentario = None
        self.mensaje = None
        self._parsear(mail)

    def __del__(self):
        os.remove(self.imagen)
    
    def __get_userpass(self):
        if not None == self.mensaje:
            [(userpass, vacio)] = self.mensaje.get_params(header='Subject')
            return userpass
        else:
            return ''
    #El usuario y el password para el login (ReadOnly), es equivalente al Subject del mail
    userpass = property(__get_userpass)
    
    def _parsear(self, mail):
        '''Parsear el mail para obtener un email.Message'''
        elmail = StringIO.StringIO(mail)
        parseador = email.Parser.Parser()
        self.mensaje = parseador.parse(elmail)
        elmail.close()
    
    def desempacar(self):
        '''desempacar el contenido de self.mail para obtener los textos e imagenes'''
        
        #cada 'parte' es un email.Messaje
        for parte in self.mensaje.walk():
            #el primer main type que se encuentre va a ser el multipart global
            if parte.get_main_type() == 'multipart':
                continue
            
            #chequear que el tipo de imagen sea valido
            #si es valido, generar el archivo con la imagen en el mismo directorio
            #que el programa
            #y guardar el path en self.imagen
            if parte.get_type() in ('image/jpeg', 'image/png', 'image/gif'):
                self.imagen = '%s/img_temp' % os.path.dirname(os.path.abspath(sys.argv[0]))
                arch = open(self.imagen, 'wb')
                arch.write(parte.get_payload(decode=1))
                arch.close()
            
            #si esta parte es el texto, separar el titulo del comentario
            if parte.get_main_type() == 'text':
                texto = StringIO.StringIO(parte.get_payload(decode=1))
                self.titulo = texto.readline()
                self.comentario = texto.read()
                #si solo hay titulo, se cambia por el comentario
                if not self.comentario:
                    self.comentario = self.titulo
                    self.titulo = 'Una foto muy interesante'
        #chequear que se hallan creado todas las partes necesarias
        if not self.comentario or not self.titulo or not self.imagen:
            raise 'UNPACK_ERROR'
    
    def _subir_imagen(self, dir_fotos, nomb_dest):
        '''Resizear la imagen temporal, y subirla a cada directorio dir_fotos/(full|thumb)/nomb_dest'''
        #imagen fullsize
	os.system("convert -size 640x480 %(imagen)s -resize 640x480 jpg:%(imagen)s" % {'imagen':self.imagen})
	shutil.copy(self.imagen, '%s/full/%s' % (dir_fotos, nomb_dest))
	os.system("chmod ugo+r %s/full/%s" % (dir_fotos, nomb_dest))
        #subo imagen thumbsize
	os.system("convert -size 130x130 %(imagen)s -resize 130x130 jpg:%(imagen)s" % {'imagen':self.imagen})
	shutil.copy(self.imagen, '%s/thumb/%s' % (dir_fotos, nomb_dest))
	os.system("chmod ugo+r %s/thumb/%s" % (dir_fotos, nomb_dest))
    
    def _subir_textos(self, db, fotolog):
        '''Subir los textos a la base de datos db
        #return el id donde se subio la imagen'''
        
        sql = "INSERT INTO FOTOS (id_fotolog, comentario, titulo, fecha) VALUES (%i,'%s','%s',%i)"\
                % (fotolog, self.comentario, self.titulo, time.time())
	db.execute(sql)
	sql = "SELECT id FROM FOTOS WHERE id_fotolog=%i ORDER BY id DESC LIMIT 1" % fotolog
	db.execute(sql)
	((last_id,),) = db.fetchall()
	return last_id
    
    def subir(self, db, fotolog, dir_fotos):
        '''subir todas las partes de la foto'''
        #los textos
        id_foto = self._subir_textos(db, fotolog)
        #la imagen
        self._subir_imagen(dir_fotos, '%i.jpg'%id_foto)
        
def login(user, passwd, db):
    '''Autenticar un user y un passwd contra la basa de datos db, devolver el id de fotolog correspondiente'''
    #Obtengo el password encriptado de los datos que ingreso el usuario
    f = urllib.urlopen('http://localhost/fotomail/encriptar.php?parm1=%s&parm2=%s' % (passwd, user))
    pass_enc1 = f.readline()
    #obtengo los datos encriptados de la base de datos
    res = db.execute("SELECT FOTOLOGS.id, USUARIOS.pass FROM USUARIOS \
                      INNER JOIN FOTOLOGS ON FOTOLOGS.id_usuario = USUARIOS.id \
                      WHERE nickname='%s' LIMIT 1" % user)

    #si no hay lineas, hay error en el login
    if not res: 
        raise 'LOGIN_ERROR'
    #fetch el password y el id del fotolog
    ((id_flog, pass_enc2),) = db.fetchall()

    if pass_enc1 == pass_enc2:
        return id_flog
    else:
        raise 'LOGIN_ERROR'
    
if __name__=='__main__':
    
    #conexion a la base de datos
    db_conn = MySQLdb.connect(host='localhost', port=3306, user='comunidad', passwd='choco', db='fotolog')
    db = db_conn.cursor()
    
    #crear la foto
    una_foto = foto(sys.stdin.read())
    
    #loguear al usuario
    user, passwd = una_foto.userpass.split()
    try:
        id_flog = login(user, passwd, db)
    except 'LOGIN_ERROR':
        db_conn.close()
        sys.exit()

    #desempacar la foto
    try:
        una_foto.desempacar()
    except 'UNPACK_ERROR':
        db_conn.close()
        sys.exit()

    #Subir la foto
    una_foto.subir(db, id_flog, '/var/www/html/fotolog/fotos')

    #finalizar
    db_conn.close()
    
