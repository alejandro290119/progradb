"""
user_model.py
Modelo de usuarios para la aplicación MarcaApp
"""

class UserModel:
    def __init__(self, connection_manager):
        """
        Recibe un OracleConnectionManager para ejecutar operaciones en la DB
        """
        self.conn_mgr = connection_manager

    def create_user(self, username, password):
        """
        Crear un nuevo usuario en la base de datos y asignarle rol por defecto
        """
        conn = self.conn_mgr.get_connection()
        cursor = conn.cursor()

        try:
            cursor.execute(f"CREATE USER {username} IDENTIFIED BY {password}")
            cursor.execute(f"GRANT CONNECT, recurso_basico TO {username}")  # Ajusta el rol según tu BD
            conn.commit()
        finally:
            cursor.close()
            conn.close()

    def validate_user(self, username):
        """
        Validar si un usuario existe en la base de datos
        """
        conn = self.conn_mgr.get_connection()
        cursor = conn.cursor()

        try:
            cursor.execute(
                "SELECT username FROM all_users WHERE username = UPPER(:username)",
                [username],
            )
            result = cursor.fetchone()
            return result is not None
        finally:
            cursor.close()
            conn.close()
