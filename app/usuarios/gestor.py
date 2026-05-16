usuarios_db = []

def registrar_usuario(nombre, edad):
    # Aquí podríamos lanzar una excepción propia si quisiéramos
    usuario = {"nombre": nombre, "edad": edad}
    usuarios_db.append(usuario)
    return f"✅ Usuario '{nombre}' registrado."

def listar_usuarios():
    if not usuarios_db:
        return "⚠️  No hay usuarios en el sistema."
    
    salida = "\n--- Lista de Usuarios ---"
    for i, user in enumerate(usuarios_db):
        salida += f"\nID: {i} | Nombre: {user['nombre']} | Edad: {user['edad']}"
    return salida

def eliminar_usuario(indice):
    # Intentamos eliminar por índice
    eliminado = usuarios_db.pop(indice)
    return f"❌ Usuario '{eliminado['nombre']}' eliminado."