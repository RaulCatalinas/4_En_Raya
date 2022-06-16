import sys
import tkinter
from tkinter import Label, Button
from tkinter.messagebox import askquestion

import pygame as pg

negro = "#000000"
azulEtiquetas = "#33FFFF"
verdeEtiquetas = "#00CC66"


class Salir:
    """Controla el cierre del juego, muestra un diálogo de confirmación de que si el usuario está
    seguro de cerrar el juego, y si da a que si está seguro entonces destruye la ventana actual"""

    def __init__(self):
        self.seguirJugando = None
        self.cerrar = None
        self.Tk = None

    def FuncionSalir(self, ventanaACerrar):
        self.Tk = ventanaACerrar

        self.cerrar = askquestion(
            "Salir del juego", "¿Seguro que quieres salir del juego?"
        )

        if self.cerrar == "yes":
            self.Tk.destroy()

    def FuncionSalirPygame(self, ventanaACerrar, variableQueControlaElJuego):
        self.Tk = ventanaACerrar
        self.seguirJugando = variableQueControlaElJuego

        self.cerrar = askquestion(
            "Salir del juego", "¿Seguro que quieres salir del juego?"
        )

        if self.cerrar == "yes":
            self.seguirJugando = False
            pg.quit()
            sys.exit()


class CambiarColor:
    """
    Cambia el color de los botones al pasar el ratón por encima.
    """

    @staticmethod
    def FuncionCambiarColor(button, colorRatonDentro, colorRatonFuera):
        button.bind(
            "<Enter>",
            func=lambda e: button.config(background=colorRatonDentro, cursor="hand2"),
        )

        button.bind("<Leave>", func=lambda e: button.config(background=colorRatonFuera))


class Botones:
    """
    Clase que crea los botones, los coloca en la ventana y los cambia de color al pasar el ratón por encima de ellos.
    """

    class BotonPosicionAbsoluta(tkinter.Button):
        def __init__(
            self,
            texto,
            y,
            ancho,
            colorFondo,
            funcion,
            fuente,
            tamañoFuente,
            ventana,
            colorRatonDentro,
            colorRatonFuera,
        ):
            """
            Crea un botón con los parámetros dados y luego llama a la función “CambiarColor” para cambiar el color del 4
            botón
            cuando el mouse está sobre él.
            @param texto - El texto que se mostrará en el botón.
            @param y - La distancia entre el botón y el widget anterior.
            @param ancho - ancho del botón
            @param colorFondo - color de fondo
            @param funcion - La función que se ejecutará cuando se presione el botón.
            @param fuente - La fuente del texto.
            @param tamañoFuente - El tamaño de la fuente.
            @param ventana - La ventana en la que estará el botón.
            @param colorRatonDentro - El color del botón cuando el mouse está sobre él.
            @param colorRatonFuera - El color del botón cuando el mouse no está sobre él.
            """
            super().__init__()
            self.cambiarColor = CambiarColor()

            # Crea el botón con los parámetros dados
            self.texto = texto
            self.y = y
            self.ancho = ancho
            self.colorFondo = colorFondo
            self.fuente = fuente
            self.tamañoFuente = tamañoFuente
            self.ventana = ventana
            self.colorRatonDentro = colorRatonDentro
            self.colorRatonFuera = colorRatonFuera
            self.funcion = funcion

            Button(
                self.ventana,
                text=self.texto,
                bg=self.colorFondo,
                font=(self.fuente, self.tamañoFuente),
                command=self.funcion,
                width=self.ancho,
            )

            self.pack(pady=self.y)

            self.cambiarColor.FuncionCambiarColor(
                Button, self.colorRatonDentro, self.colorRatonFuera
            )

    class BotonPosicionRelativa(tkinter.Button):
        def __init__(
            self,
            texto,
            x,
            y,
            ancho,
            colorFondo,
            funcion,
            fuente,
            tamañoFuente,
            ventana,
            colorRatonDentro,
            colorRatonFuera,
        ):
            """
            Crea un botón con los parámetros dados y luego llama a la función “CambiarColor” para cambiar el color del
            botón
            cuando el mouse está sobre él.
            @param texto - El texto que se mostrará en el botón.
            @param x - La distancia entre el botón y el widget anterior.
            @param y - La distancia entre el botón y el widget anterior.
            @param ancho - ancho del botón
            @param colorFondo - color de fondo
            @param funcion - La función que se ejecutará cuando se presione el botón.
            @param fuente - La fuente del texto.
            @param tamañoFuente - El tamaño de la fuente.
            @param ventana - La ventana en la que estará el botón.
            @param colorRatonDentro - El color del botón cuando el mouse está sobre él.
            @param colorRatonFuera - El color del botón cuando el mouse no está sobre él.
            """
            super().__init__()
            self.cambiarColor = CambiarColor()

            # Crea el botón con los parámetros dados
            self.texto = texto
            self.y = y
            self.ancho = ancho
            self.colorFondo = colorFondo
            self.fuente = fuente
            self.tamañoFuente = tamañoFuente
            self.ventana = ventana
            self.colorRatonDentro = colorRatonDentro
            self.colorRatonFuera = colorRatonFuera
            self.funcion = funcion

            Button(
                self.ventana,
                text=self.texto,
                bg=self.colorFondo,
                font=(self.fuente, self.tamañoFuente),
                command=self.funcion,
                width=self.ancho,
            )

            self.place(x=x, y=y)

            self.cambiarColor.FuncionCambiarColor(
                Button, self.colorRatonDentro, self.colorRatonFuera
            )


class Etiqueta(tkinter.Label):
    def __init__(self, texto, y, ancho, colorFondo, fuente, tamañoFuente, ventana):
        """
        Crea una etiqueta con los parámetros dados y luego la coloca en la ventana.
        @param texto - El texto que se mostrará en la etiqueta.
        @param y - La posición del eje y de la etiqueta.
        @param ancho - El ancho de la etiqueta.
        @param colorFondo - El color de fondo de la etiqueta.
        @param fuente - La fuente a utilizar.
        @param tamañoFuente - Tamaño de la fuente.
        """
        # Crea una etiqueta con los parámetros dados
        super().__init__()
        self.texto = texto
        self.y = y
        self.ancho = ancho
        self.colorFondo = colorFondo
        self.fuente = fuente
        self.tamañoFuente = tamañoFuente
        self.ventana = ventana

        # Crear la etiqueta
        Label(
            self.ventana,
            text=self.texto,
            font=(self.fuente, self.tamañoFuente),
            width=self.ancho,
            bg=self.colorFondo,
        )
        # Colocar la etiqueta en la ventana
        self.pack(pady=self.y)


class VentanaTkinter(tkinter.Tk):
    def __init__(self, titulo, ancho, alto, colorFondo, icono=None):
        """
        Crea una ventana con los parámetros dados.
        @param titulo - El título de la ventana.
        @param ancho - El ancho de la ventana.
        @param alto - El alto de la ventana.
        """
        self.titulo = titulo
        self.ancho_ventana = ancho
        self.alto_ventana = alto
        self.colorFondo = colorFondo
        self.icono = icono

        super().__init__()
        self.title(titulo)

        # Si se indica un icono, se lo asigna a la ventana
        if not self.icono:
            self.iconbitmap(self.icono)

        # Poner el color de fondo + fijar el tamaño de la ventana
        self.config(bg=self.colorFondo)
        self.resizable(False, False)

        # Centrar ventana
        self.x_ventana = self.winfo_screenwidth() // 2 - self.ancho_ventana // 2
        self.y_ventana = self.winfo_screenheight() // 2 - self.alto_ventana // 2
        self.posicion = (
            str(self.ancho_ventana)
            + "x"
            + str(self.alto_ventana)
            + "+"
            + str(self.x_ventana)
            + "+"
            + str(self.y_ventana)
        )
        self.geometry(self.posicion)


class Main:
    def __init__(self):
        self.etiquetaTitulo = None
        self.ventana = None
        self.boton = Botones()

    def FuncionMain(self):
        self.ventana = VentanaTkinter("4 En Raya", 1280, 720, negro)
        self.ventana.mainloop()


menu = Main()

menu.FuncionMain()
