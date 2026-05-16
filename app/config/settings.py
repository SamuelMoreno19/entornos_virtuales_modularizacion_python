import os
from dotenv import load_dotenv

class Config:
    # Definimos las variables como atributos de clase con valores por defecto
    APP_NAME = "Sistema Base"
    VERSION = "1.0.0"
    ADMIN = "Invitado"

    @staticmethod
    def cargar_configuracion():
        try:
            # Intentamos cargar el archivo .env
            if not load_dotenv():
                # Si load_dotenv es False, es porque no encontró el archivo
                raise FileNotFoundError("No se encontró el archivo .env")
            
            print("[CONFIG] Archivo .env cargado correctamente.")
            
        except Exception as e:
            print(f"[ADVERTENCIA] {e}. Se usarán valores predeterminados.")
            
        finally:
            # Asignamos los valores de las variables de entorno a la clase
            Config.APP_NAME = os.getenv("APP_NAME", Config.APP_NAME)
            Config.VERSION = os.getenv("VERSION", Config.VERSION)
            Config.ADMIN = os.getenv("ADMIN_USER", Config.ADMIN)
            print("[CONFIG] Proceso de inicialización finalizado.")