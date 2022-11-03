from tkinter import *

ventana_principal = Tk()

ventana_principal.title("Ejercicos Tkinter")

ventana_principal.geometry("550x450")

ventana_principal.resizable(0,0)

ventana_principal.config(bg="black")

frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg="navy", width=550, height=450)
frame_entrada.place(x=10,y=10)
frame_operaciones= Frame(ventana_principal)
frame_operaciones.config(bg="white", width=200, height=200)
frame_operaciones.place(x=10,y=10)
frame_operaciones1= Frame(ventana_principal)
frame_operaciones1.config(bg="white", width=200, height=200)
frame_operaciones1.place(x=10,y=250)
frame_operaciones2= Frame(ventana_principal)
frame_operaciones2.config(bg="white", width=300, height=200)
frame_operaciones2.place(x=250,y=10)
frame_operaciones3= Frame(ventana_principal)
frame_operaciones3.config(bg="white", width=300, height=200)
frame_operaciones3.place(x=250,y=250)
frame_resultado1= Frame(ventana_principal)
frame_resultado1.config(bg="red", width=180, height=180)
frame_resultado1.place(x=10,y=10)
frame_resultado2= Frame(ventana_principal)
frame_resultado2.config(bg="red", width=180, height=180)
frame_resultado2.place(x=10,y=270)
frame_resultado3= Frame(ventana_principal)
frame_resultado3.config(bg="red", width=280, height=180)
frame_resultado3.place(x=270,y=10)
frame_resultado4= Frame(ventana_principal)
frame_resultado4.config(bg="red", width=280, height=180)
frame_resultado4.place(x=270,y=270)

titulo = Label(frame_resultado1, text="NORUEGA")
titulo.config(bg="white", fg="black", font=("Times New Roman", 16))
titulo.place(x=10,y=10)

ventana_principal.mainloop()