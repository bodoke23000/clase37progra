usuarios_list=[]

def validar_sexo(sexo):
    if sexo in ["M","F"]:
        return True
    else:
        print("Error, el sexo solo debe ser F o M")
        return False

def validar_password(password):
    if len(password.strip())<8:
        print("Error, minimo 8 caracteres")
        return False
    tiene_numero=False
    for numero in password:
        if numero.isnumeric():
            tiene_numero=True
    tiene_letra=False
    for letra in password:
        if letra.isalpha():
            tiene_letra=True
    if " " in password:
        print("Error, no puede llevar espacios en blanco")
        return False
    return tiene_letra and tiene_numero

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
    nombre_usuario=str(input("Ingrese el nombre de usuario:\n")).strip()
    while not validar_texto_vacio(nombre_usuario):
        nombre_usuario=str(input("Ingrese el nombre de usuario:\n")).strip()
    
    sexo=str(input("Ingrese su sexo:\n")).strip()
    while not validar_sexo(sexo):
        sexo=str(input("Ingrese su sexo:\n")).strip()
    
    password=str(input("Ingrese su contraseña:\n")).strip()
    while not validar_password(password):
        password=str(input("Ingrese su contraseña:\n")).strip()
    
    usuario={
        "nombre":nombre_usuario,
        "sexo":sexo,
        "password":password,
    }
    
    usuarios_list.append(usuario)
    print("Usuario agregado exitosamente")