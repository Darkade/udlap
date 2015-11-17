#!/usr/bin/env python
# coding=UTF-8

import pygtk
pygtk.require('2.0')
import gtk

import string
from tabu import *

class GUI():
	t_solucion_inicial="random"	

	def callback(self, widget, data=None):
		resultado = {
		"radio1":	lambda: "random",
		"radio2":	lambda: "up",
		"radio3":	lambda: "usuario"
		}[data]()
		self.t_solucion_inicial=resultado

	def run_programa(self,widget,buffer_modelo,buffer_resultado,iteraciones,tabu,txt2_v1,progreso,txt_peso):
		progreso.set_fraction(0)
		Texto = string.split(buffer_modelo.get_text(buffer_modelo.get_start_iter(),buffer_modelo.get_end_iter()))
		if self.t_solucion_inicial=="usuario":
			col2=[float(Texto[i]) for i in range(len(Texto)) if i in [0+3*j for j in range(len(Texto))] ]
			col1=[float(Texto[i]) for i in range(len(Texto)) if i in [1+3*j for j in range(len(Texto))] ]
			col3=[float(Texto[i]) for i in range(len(Texto)) if i in [2+3*j for j in range(len(Texto))] ]		
		else:			
			col2 = [float(Texto[i]) for i in range(len(Texto)) if i % 2 ==0 ]
			col1 = [float(Texto[i]) for i in range(len(Texto)) if i % 2 !=0 ]
			col3= []
		col2.append("<")
		print int(txt_peso.get_text())
		col2.append(int(txt_peso.get_text()))
		resolver_modelo(col1,[col2],col3,self.t_solucion_inicial,iteraciones.get_value_as_int(),tabu.get_value_as_int(),buffer_resultado,progreso)


	def __init__(self):
		v_principal = gtk.Window()
		v_principal.set_title("Busqueda Tabú")
		v_principal.set_border_width(25)
		v_principal.set_default_size(800, 600)
		caja_jefe=gtk.VBox(True, 5)
		caja_h1=gtk.HBox(False, 5)
		caja_v1=gtk.VBox(False, 1)
		caja_v2=gtk.VBox(False, 5)
		caja_vframe=gtk.VBox(False, 5)
		correr = gtk.Button("Resolver", gtk.STOCK_EXECUTE)
		progreso = gtk.ProgressBar(None)
		progreso.set_fraction(0)
		progreso.set_orientation(gtk.PROGRESS_LEFT_TO_RIGHT)
		progreso.set_text("Resolviendo") 
		image = gtk.Image()
		image.set_from_file("./udla.jpg")
	
	
		
		scrolled_txt1 = gtk.ScrolledWindow(None, None)
		scrolled_txt2 = gtk.ScrolledWindow(None, None)	
	
		scrolled_txt1.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
		scrolled_txt2.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)

		buffer_modelo=gtk.TextBuffer()
		buffer_resultado=gtk.TextBuffer()
		txt1_v1=gtk.TextView(buffer_modelo)
		txt2_v1=gtk.TextView(buffer_resultado)
		txt_peso = gtk.Entry(0)

		label_modelo=gtk.Label("Datos del Problema")
		label_solucion=gtk.Label("Solución")
		label_peso=gtk.Label("Capacidad de la mochila")



		
		ajuste_iter=gtk.Adjustment(20, 5, 1000000, 1, 10)
		lista_tabu=gtk.Adjustment(7, 3, 25, 1, 5)
	
		label_iteraciones = gtk.Label("Número de Iteraciones")
		label_tabu = gtk.Label("Número de Elementos en Lista Tabu")
		soluciones = gtk.Frame("Tipo de Solución Inicial")
		soluciones.set_label_align(0.5, 0.0)

		spn_iteraciones = gtk.SpinButton(ajuste_iter, .5, 0)
		spn_tabu = gtk.SpinButton(lista_tabu, .2, 0)

		radio_inicial = gtk.RadioButton(None, "Solucion Random")
		caja_vframe.pack_start(radio_inicial, True, True, 0)
		radio_inicial.connect("toggled", self.callback, "radio1")
		radio_inicial.show()

		radio_inicial = gtk.RadioButton(radio_inicial, "Solucion U/P")
		caja_vframe.pack_start(radio_inicial, True, True, 0)
		radio_inicial.connect("toggled", self.callback, "radio2")
		radio_inicial.show()

		radio_inicial = gtk.RadioButton(radio_inicial, "Solucion Usuario")
		caja_vframe.pack_start(radio_inicial, True, True, 0)
		radio_inicial.connect("toggled", self.callback, "radio3")
		radio_inicial.show()
	
		v_principal.add(caja_jefe)
		caja_jefe.pack_start(caja_h1, False, True, 0)
		scrolled_txt1.add_with_viewport(txt1_v1)
		scrolled_txt2.add_with_viewport(txt2_v1)
		caja_h1.pack_start(caja_v1, True, True, 0)
		caja_h1.pack_start(caja_v2, False, True, 0)
		caja_v1.pack_start(label_modelo, False, True, 0)
		caja_v1.pack_start(scrolled_txt1, True, True, 0)
		caja_v1.pack_start(label_solucion, False, True, 0)
		caja_v1.pack_start(scrolled_txt2, True, True, 0)
		caja_v2.pack_start(label_iteraciones, False, True, 0)
		caja_v2.pack_start(spn_iteraciones, False, True, 0)
		caja_v2.pack_start(label_tabu, False, True, 0)
		caja_v2.pack_start(spn_tabu, False, True, 0)
		caja_v2.pack_start(soluciones, False, True, 0)
		soluciones.add(caja_vframe)
		caja_v2.pack_start(label_peso,False,True,0)
		caja_v2.pack_start(txt_peso,False,True,0)
		caja_v2.pack_start(correr, False, True, 0)
		caja_v2.pack_start(progreso, False, False, 0)
		caja_v2.pack_start(image, True, False, 0)
	
		v_principal.connect("destroy", gtk.main_quit)
		v_principal.connect("delete_event", gtk.main_quit)
###############################
		correr.connect("clicked", self.run_programa,buffer_modelo,buffer_resultado,spn_iteraciones,spn_tabu,txt2_v1,progreso,txt_peso)
###############################
		label_peso.show()
		txt_peso.show()
		soluciones.show()
		correr.show()
		progreso.show()
		image.show()
		scrolled_txt1.show()
		scrolled_txt2.show()
		label_modelo.show()
		label_solucion.show()
		txt1_v1.show()
		txt2_v1.show()
		label_iteraciones.show()
		label_tabu.show()
		spn_iteraciones.show()
		spn_tabu.show()
		caja_jefe.show()
		caja_h1.show()
		caja_v1.show()
		caja_v2.show()
		caja_vframe.show()
		v_principal.show()
	
	
	def main(self):
		gtk.main()
		return 0
