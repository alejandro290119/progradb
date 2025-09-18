

import tkinter as tk
from tkinter import ttk


from ui.login import LoginWindow
from ui.marca_widget import MarcaWidget
from ui.report_widget import ReportWidget
from ui.user_register import UserRegisterWidget
from db.connection import OracleConnectionManager
from db.user_model import UserModel

def main():

    login_win = LoginWindow(dsn="localhost/XEPDB1")
    login_win.mainloop()

 
    if not login_win.username or not login_win.password:
        print("Login cancelado o fallido")
        return

   
    username = login_win.username
    password = login_win.password

   
    conn_mgr = OracleConnectionManager(dsn="localhost/XEPDB1", user=username, password=password)

   
    user_model = UserModel(conn_mgr)
    is_admin = username.lower() == "app_admin"  

  
    root = tk.Tk()
    root.title(f"MarcaApp - Usuario: {username}")
    root.geometry("900x600")

   
    tab_control = ttk.Notebook(root)

   
    marca_tab = tk.Frame(tab_control)
    tab_control.add(marca_tab, text="Marca")
    marca_widget = MarcaWidget(marca_tab, conn_manager=conn_mgr, username=username)
    marca_widget.pack(fill="both", expand=True)

    
    if is_admin:
        report_tab = tk.Frame(tab_control)
        tab_control.add(report_tab, text="Reporte")
        report_widget = ReportWidget(report_tab, conn_manager=conn_mgr, max_rows=100)
        report_widget.pack(fill="both", expand=True)

   
    if is_admin:
        user_tab = tk.Frame(tab_control)
        tab_control.add(user_tab, text="Registro Usuarios")
       
        admin_conn_mgr = OracleConnectionManager(dsn="localhost/XEPDB1", user="app_admin", password="admin_pwd")
        user_register_widget = UserRegisterWidget(user_tab, admin_conn_manager=admin_conn_mgr)
        user_register_widget.pack(fill="both", expand=True)

    tab_control.pack(expand=1, fill="both")

    root.mainloop()


if __name__ == "__main__":
    main()
