#!/usr/bin/env python
# coding=UTF-8

import pygtk
pygtk.require('2.0')
import gtk
from libreria import *

class ventana:
	
	binomial=metodo_binomial()

	def funcion_evaluar(self,widget,label_call,label_put,tiempo,nivel):
		var_nivel=int(eval('1.0*' + nivel.get_text()))
		var_tiempo=float(eval('1.0*' + tiempo.get_text()))
		try:
			r1=str(self.binomial.evaluar(var_nivel,var_tiempo,'call'))
			label_call.set_text("El resultado de la valuación, para un call, es: " + r1)
			r2=str(self.binomial.evaluar(var_nivel,var_tiempo,'put'))
			label_put.set_text("El resultado de la valuación, para un put, es: " + r2)
		except ValueError:
			print ValueError

	def numero(self,widget,event,entry,variable):
		try:
			if variable=="u":
				self.binomial.u=float(eval('1.0*' + entry.get_text()))
			elif variable=="d":
				self.binomial.d=float(eval('1.0*' + entry.get_text()))
			elif variable=="x":
				self.binomial.x=float(eval('1.0*' + entry.get_text()))
			elif variable=="r":
				self.binomial.r=float(eval('1.0*' + entry.get_text()))
			elif variable=="spot":
				self.binomial.spot=float(eval('1.0*' + entry.get_text()))
			elif variable=="tiempo":
				float(eval('1.0*' + entry.get_text()))
			elif variable=="niveles":
				float(eval('1.0*' + entry.get_text()))
		except ValueError:
			entry.grab_focus()



	def __init__(self):
		window = gtk.Window()
		window.set_title("Evaluo de opciones mediante el Método Binomial")
		window.set_border_width(25)
		window.set_default_size(500,700)

		mainbox=gtk.HBox(False,0)
		columna_derecha=gtk.VBox(False,0)
		columna_izquierda=gtk.VBox(False,0)

#		mainbox.add(columna_izquierda)
		mainbox.add(columna_derecha)

########ENTRIES DE DATOS
		label_u=gtk.Label("u (Coeficiente de alza del precio)");					entry_u=gtk.Entry(0);		entry_u.set_text(str(self.binomial.u))
		label_d=gtk.Label("d (Coeficiente de baja de precio)");					entry_d=gtk.Entry(0);		entry_d.set_text(str(self.binomial.d))
		label_r=gtk.Label("r (Tasa libre de riesgo, anual continua)");					entry_r=gtk.Entry(0);		entry_r.set_text(str(self.binomial.r))
		label_x=gtk.Label("x (Precio de ejercicio)");					entry_x=gtk.Entry(0);		entry_x.set_text(str(self.binomial.x))
		label_spot=gtk.Label("Precio Spot (Precio al día de hoy)");	entry_spot=gtk.Entry(0);	entry_spot.set_text(str(self.binomial.spot))
		label_tiempo=gtk.Label("Tiempo (Tiempo total para la valuación, en Años)");		entry_tiempo=gtk.Entry(0)
		label_niveles=gtk.Label("Niveles (Niveles del arbol a tomar en cuenta)");		entry_niveles=gtk.Entry(0)

		button_evaluar=gtk.Button("Evaluar",gtk.STOCK_OK)

########IMAGEN
		imagen=gtk.Image()
		imagen.set_from_file("escudo.png")
		columna_derecha.pack_start(imagen,False,False,30)
########TABLA DE DATOS
		table_datos = gtk.Table(8, 2, True)
		columna_derecha.pack_start(table_datos,False,False,0)

		table_datos.attach(label_u,0,1,0,1);		table_datos.attach(entry_u,1,2,0,1)
		table_datos.attach(label_d,0,1,1,2);		table_datos.attach(entry_d,1,2,1,2)
		table_datos.attach(label_r,0,1,2,3);		table_datos.attach(entry_r,1,2,2,3)
		table_datos.attach(label_x,0,1,3,4);		table_datos.attach(entry_x,1,2,3,4)
		table_datos.attach(label_spot,0,1,4,5);		table_datos.attach(entry_spot,1,2,4,5)
		table_datos.attach(label_tiempo,0,1,5,6);	table_datos.attach(entry_tiempo,1,2,5,6)
		table_datos.attach(label_niveles,0,1,6,7);	table_datos.attach(entry_niveles,1,2,6,7)
		table_datos.attach(button_evaluar,0,2,7,8)

		label_call=gtk.Label()
		columna_derecha.pack_start(label_call,False,True,15)
		label_put=gtk.Label()
		columna_derecha.pack_start(label_put,False,True,15)


########CONEXIONES A METODOS
		entry_u.connect("focus-out-event",self.numero,entry_u,"u")
		entry_d.connect("focus-out-event",self.numero,entry_d,"d")
		entry_x.connect("focus-out-event",self.numero,entry_x,"x")
		entry_r.connect("focus-out-event",self.numero,entry_r,"r")
		entry_spot.connect("focus-out-event",self.numero,entry_spot,"spot")
		entry_tiempo.connect("focus-out-event",self.numero,entry_tiempo,"tiempo")
		entry_niveles.connect("focus-out-event",self.numero,entry_niveles,"niveles")

		button_evaluar.connect("clicked",self.funcion_evaluar,label_call,label_put,entry_tiempo,entry_niveles)


########RUN
		window.add(mainbox)
		window.connect("destroy", gtk.main_quit)
		window.show_all()

	def main(self):
		gtk.main()
		return 0

ventana = ventana()
ventana.main()
