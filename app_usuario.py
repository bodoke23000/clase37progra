usuarios_list=[]

def validar_sexo(sexo):
    if sexo in ["M","F"]:
        return True
    else:
        print("Error, el sexo solo debe ser F o M")
        return False

def validar_password(password):
    if " " in password.strip().lower():
        print("Error, la contraseña no debe llevar espacios en blanco")
        return False
    elif len(password.strip().lower())<8:
        print("Error, la contraseña debe tener almenos 8 caracteres")
        return False
    elif [1,2,3,4,5,6,7,8,9,0] not in password.strip().lower():
        print("Error, la contraseña debe tener al menos 1 numero")
        return False
    elif ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"] not in password.strip().lower():
        print("Error, la contraseña debe tener al menos una letra")
        return False
    else:
        return True

def imprimir_usuario(usuario):
    print(f"""
        ---------------------------------
        Nombre usuario: {usuario["nombre_usuario"]}
        Sexo: {usuario["sexo"]}
        Password: {usuario["password"]}""")

def validar_texto_vacio(texto):
    if len(texto.strip())>0:
        return True
    else:
        print("Error, la contraseña no puede ir vacia")
        return False

def agregrar_usuario():
    nombre_usuario=str(input("Ingrese el nombre de usuario:\n")).strip().lower()
    while not validar_texto_vacio(nombre_usuario):
        nombre_usuario=str(input("Ingrese el nombre de usuario:\n")).strip().lower()
    
    sexo=str(input("Ingrese su sexo:\n")).strip().lower()
    while not validar_sexo(sexo):
        sexo=str(input("Ingrese su sexo:\n")).strip().lower()
    
    password=str(input("Ingrese su contraseña:\n")).strip().lower()
    while not validar_password(password):
        password=str(input("Ingrese su contraseña:\n")).strip().lower()
    
    usuario={
        "nombre":nombre_usuario,
        "sexo":sexo,
        "password":password,
    }