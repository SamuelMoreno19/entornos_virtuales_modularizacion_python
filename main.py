import sys
from app.config.settings import Config
from app.usuarios import gestor
from app.usuarios.validaciones import validar_nombre, validar_edad

def menu():
    Config.cargar_configuracion()
    
    while True:
        print(f"\n--- {Config.APP_NAME} | Admin: {Config.ADMIN} ---")
        print("1. Agregar usuario")
        print("2. Listar usuarios")
        print("3. Eliminar usuario")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")

        try:
            if opcion == "1":
                nombre = input("Nombre: ")
                # TRAP: Si meten letras en edad, el int() fallará y saltará al except
                edad = int(input("Edad: ")) 
                
                if validar_nombre(nombre) and validar_edad(str(edad)):
                    print(gestor.registrar_usuario(nombre, edad))
                else:
                    print("🚫 Datos inválidos (Nombre muy corto o edad fuera de rango).")

            elif opcion == "2":
                print(gestor.listar_usuarios())

            elif opcion == "3":
                print(gestor.listar_usuarios())
                # TRAP: Si el índice no existe o no es número, saltará al except
                idx = int(input("Ingrese el ID a eliminar: "))
                print(gestor.eliminar_usuario(idx))

            elif opcion == "4":
                print("Saliendo...")
                break
            else:
                print("❓ Opción no válida.")

        except ValueError:
            print("❌ ERROR: Debes ingresar un número válido para la edad o el ID.")
        except IndexError:
            print("❌ ERROR: Ese ID de usuario no existe en la lista.")
        except Exception as e:
            print(f"❌ OCURRIÓ UN ERROR INESPERADO: {e}")
        finally:
            print("-" * 30)

if __name__ == "__main__":
    try:
        menu()
    except KeyboardInterrupt:
        print("\nCierre forzado por el usuario.")
        sys.exit()