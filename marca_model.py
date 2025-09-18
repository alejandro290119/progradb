# db/marca_model.py

class MarcaModel:
    """
    Modelo para registrar marcas en la base de datos Oracle.
    """
    def __init__(self, conn_manager):
        self.conn_manager = conn_manager  # solo guardamos el manager
        # NO definimos atributos tipo, usuario, etc. aquí

    def create_mark(self, username, tipo, comentario=""):
        try:
            with self.conn_manager.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(
                    "INSERT INTO marcas (usuario, tipo, fecha_hora, comentario) "
                    "VALUES (:u, :t, SYSTIMESTAMP, :c)",
                    u=username, t=tipo, c=comentario
                )
                conn.commit()
        except Exception as e:
            print(f"Error insertando marca: {e}")
            raise e

    def get_all_marks(self, limit=100):
        try:
            with self.conn_manager.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(
                    f"SELECT usuario, tipo, fecha_hora, comentario "
                    f"FROM marcas ORDER BY fecha_hora DESC FETCH FIRST {limit} ROWS ONLY"
                )
                return cursor.fetchall()
        except Exception as e:
            print(f"Error obteniendo marcas: {e}")
            return []
