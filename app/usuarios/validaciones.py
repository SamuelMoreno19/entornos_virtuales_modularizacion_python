def validar_nombre(nombre):
    return len(nombre.strip()) >= 3

def validar_edad(edad_str):
    try:
        edad = int(edad_str)
        return 0 <= edad <= 110
    except ValueError:
        return False