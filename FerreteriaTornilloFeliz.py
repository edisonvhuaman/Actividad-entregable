from tkinter import *

#------dando funcionalidad a boton guardar--------------------
def codigoGuardar():
	guardarDni=obtenerDni.get()
	guardarApellido=obtenerApellido.get()
	guardarNombre=obtenerNombre.get()
	guardarDir=obtenerDir.get()
	guardarTel=obtenerTel.get()
	guardarCod1=cod1.get()
	guardarCod2=cod2.get()
	guardarCod3=cod3.get()
	#guardando el nombre del producto
	guardarDes1=des1.get()
	guardarDes2=des2.get()
	guardarDes3=des3.get()
	#guardando el precio de subtotal
	"""guardarSub1=sub1.get()
	guardarSub2=sub2.get()
	guardarSub3=sub3.get()
	#guardando el precio total"""
	#guardarttotal=ttotal.get()


	newFile = open("Sistema de Registro.txt", "a")
	newFile.write("\nDNI 	 : ")
	newFile.write(guardarDni)
	newFile.write("\nApellidos: ")
	newFile.write(guardarApellido)
	newFile.write("\nNombre   : ")
	newFile.write(guardarNombre)
	newFile.write("\nDirección: ")
	newFile.write(guardarDir)
	newFile.write("\nTeléfono : ")
	newFile.write(guardarTel)
	newFile.write("\n")
	newFile.write("""\nProductos:\n{}: {}  \n{}: {}  \n{}: {}
		""".format(guardarCod1,guardarDes1,guardarCod2,guardarDes2,guardarCod3,guardarDes3))

	#newFile.write("\nPrecio Total: ")
	#newFile.write(str(guardarttotal))
	newFile.write("\n")
	newFile.write("\n")
	newFile.write("\n")
	
	newFile.close()


	#print("\n","DNI 	  : ", guardarDni, "\n", "Apellidos: ", guardarApellido, "\n", "Nombre   : ", guardarNombre, "\n", "Dirección: ", guardarDir, "\n", "Teléfono : ",  guardarTel)
	
	tDni.delete(0,END)
	tApellido.delete(0,END)
	tNombre.delete(0,END)
	tDireccion.delete(0,END)
	tTel.delete(0,END)
	#eliminando datos del codigo
	tCodigo1.delete(0,END)
	tCodigo2.delete(0,END)
	tCodigo3.delete(0,END)

	#----eliminando datos del producto
	tDes1.delete(0,END)
	tDes2.delete(0,END)
	tDes3.delete(0,END)

	tUni1.delete(0,END)
	tUni2.delete(0,END)
	tUni3.delete(0,END)

	tPrecio1.delete(0,END)
	tPrecio2.delete(0,END)
	tPrecio3.delete(0,END)

	#----eliminando  datos de cantidad y el subtotal
	tCantidad1.delete(0,END)
	tCantidad2.delete(0,END)
	tCantidad3.delete(0,END)

	tSubtotal1.delete(0,END)
	tSubtotal2.delete(0,END)
	tSubtotal3.delete(0,END)
	#eliminando el total
	tTotal.delete(0, END)



	obtenerDatos1.set("""DATOS REGISTRADOS CON ÉXITO DE:\nNombre : {}\nDNI        : {}\nTeléfono: {}
		\ncompro {}, {}, {} 
\n\nLOS DATOS SE GUARDARAN EN UN BLOCK DE NOTAS en la carpeta donde esta el codigo""".format(guardarNombre,guardarDni,guardarTel,guardarDes1, guardarDes2, guardarDes3))
	#obtenerDatos1.set(guardarNombre)
	
 
#-----------creando funcionalidad de advertencia------------

#--------------------------------------------------------	
root = Tk()
root.title('Sistema de Registro de Pedidos por Teléfono')

#------Configurando el root------------------------------
#root.iconbitmap("iconoIco.ico")
root.config(bg="#33FFAF")

#-------creando el FRAME para el titulo-------------------
miFrame2=Frame(root)
miFrame2.config(bg="#33FFAF")
miFrame2.pack()
#---------Titulo de FERRETERIA TORNILLO FELIZ--------------
lTitulo=Label(miFrame2, text='FERRETERÍA TORNILLO FELIZ')
lTitulo.grid(row=0, column=1, columnspan=4, pady=5, padx=5)
lTitulo.config(justify="right", fg="#21228B", font=("Courier New", 15, "bold", "italic"), bg="#33FFAF")
#--productos de la ferreteria----
lProductos = Label(miFrame2, text="""Productos de la ferreteria:
	\nCodigo:\tProducto\n 1:\tClavos\n 2:\tCables\n3:\tFocos""")
lProductos.grid(row=0, column=5, columnspan=7,rowspan=1, pady=5, padx=5)
lProductos.config(bg="#33FFAF", font=("Arial Black", 10, "bold"), fg="#530B9B")

#-------creando el FRAME para los datos del cliente--------
miFrame = Frame(root)
miFrame.config(bg="#33FFAF")
miFrame.pack()
#------- Label y entry DNI --------------------------------
obtenerDni=StringVar()
lDni = Label(miFrame, text='DNI:')
lDni.grid(row=1, column=0, sticky='e', pady=5, padx=5)
lDni.config(bg="#33FFAF", font="bold")
tDni = Entry(miFrame,textvariable=obtenerDni)
tDni.grid(row=1, column=1, pady=5, padx=5)
tDni.config(bg="#9BEAC1")

#------- Label y entry Apallido --------------------------------
obtenerApellido=StringVar()
lApellido = Label(miFrame, text='Apellido:')
lApellido.grid(row=2, column=0, sticky='e', pady=5, padx=5)
lApellido.config(bg="#33FFAF", font="bold")
tApellido = Entry(miFrame,textvariable=obtenerApellido)
tApellido.grid(row=2, column=1, pady=5, padx=5)
tApellido.config(bg="#9BEAC1")
#------- Label y entry Nombre --------------------------------
obtenerNombre=StringVar()
lNombre = Label(miFrame, text='Nombre:')
lNombre.grid(row=2, column=2, sticky='e', pady=5, padx=5)
lNombre.config(bg="#33FFAF", font="bold")
tNombre = Entry(miFrame,textvariable=obtenerNombre)
tNombre.grid(row=2, column=3, pady=5, padx=5)
tNombre.config(bg="#9BEAC1")
#------- Label y entry Diección --------------------------------
obtenerDir=StringVar()
lDireccion = Label(miFrame, text='Dirección:')
lDireccion.grid(row=3, column=0, sticky='e', pady=5, padx=5)
lDireccion.config(bg="#33FFAF", font="bold")
tDireccion = Entry(miFrame,textvariable=obtenerDir)
tDireccion.grid(row=3, column=1, columnspan=3, sticky='we',pady=5, padx=5)
tDireccion.config(bg="#9BEAC1")
#------- Label y entry Teléfono --------------------------------
obtenerTel=StringVar()
lTel = Label(miFrame, text='Teléfono:')
lTel.grid(row=4, column=0, sticky='e', pady=5, padx=5)
lTel.config(bg="#33FFAF", font="bold")
tTel = Entry(miFrame,textvariable=obtenerTel)
tTel.grid(row=4, column=1,columnspan=3, sticky='we', pady=5, padx=5)
tTel.config(bg="#9BEAC1")

#-------creando el FRAME para el pedido-------------------------
miFrame1 = Frame(root)
miFrame1.config(bg="#33FFAF")
miFrame1.pack()
#------- Label y entry,s Código producto -----------------------
lCodigo = Label(miFrame1, text='Cod_Prod')
lCodigo.grid(row=5, column=0,sticky='e', pady=5, padx=5)
lCodigo.config(bg="#33FFAF")
cod1=StringVar()
tCodigo1 = Entry(miFrame1, width=7, textvariable=cod1)
tCodigo1.grid(row=6, column=0, pady=5, padx=5)
tCodigo1.config(bg="#9BEAC1")
cod2=StringVar()
tCodigo2 = Entry(miFrame1, width=7, textvariable=cod2)
tCodigo2.grid(row=7, column=0, pady=5, padx=5)
tCodigo2.config(bg="#9BEAC1")
cod3=StringVar()
tCodigo3 = Entry(miFrame1, width=7, textvariable=cod3)
tCodigo3.grid(row=8, column=0, pady=5, padx=5)
tCodigo3.config(bg="#9BEAC1")
#------- Label y entry,s Descripción ---------------------------
lDes = Label(miFrame1, text='Nom_Producto')
lDes.grid(row=5, column=1,sticky='ew', pady=5, padx=5)
lDes.config(bg="#33FFAF")
des1=StringVar()
tDes1 = Entry(miFrame1, width=7, textvariable=des1)
tDes1.grid(row=6, column=1, pady=5, padx=5)
tDes1.config(bg="#9BEAC1")
des2=StringVar()
tDes2 = Entry(miFrame1, width=7, textvariable=des2)
tDes2.grid(row=7, column=1, pady=5, padx=5)
tDes2.config(bg="#9BEAC1")
des3=StringVar()
tDes3 = Entry(miFrame1, width=7, textvariable=des3)
tDes3.grid(row=8, column=1, pady=5, padx=5)
tDes3.config(bg="#9BEAC1")
#------- Label y entry,s Unidad --------------------------------
lUni = Label(miFrame1, text='Unidad')
lUni.grid(row=5, column=2,sticky='ew', pady=5, padx=5)
lUni.config(bg="#33FFAF")
uni1=StringVar()
tUni1 = Entry(miFrame1, width=10, textvariable=uni1)
tUni1.grid(row=6, column=2, pady=5, padx=5)
tUni1.config(bg="#9BEAC1")
uni2=StringVar()
tUni2 = Entry(miFrame1, width=10, textvariable=uni2)#width número de caracteres
tUni2.grid(row=7, column=2, pady=5, padx=5)
tUni2.config(bg="#9BEAC1")
uni3=StringVar()
tUni3 = Entry(miFrame1, width=10, textvariable=uni3)
tUni3.grid(row=8, column=2, pady=5, padx=5)
tUni3.config(bg="#9BEAC1")
#------- Label y entry,s Cantidad ------------------------------
lCantidad = Label(miFrame1, text='Cantidad')
lCantidad.grid(row=5, column=3,sticky='ew', pady=5, padx=5)
lCantidad.config(bg="#33FFAF")
can1=StringVar()
tCantidad1 = Entry(miFrame1, width=7, textvariable=can1)
tCantidad1.grid(row=6, column=3, pady=5, padx=5)
tCantidad1.config(bg="#9BEAC1")
can2=StringVar()
tCantidad2 = Entry(miFrame1, width=7, textvariable=can2)#width número de caracteres
tCantidad2.grid(row=7, column=3, pady=5, padx=5)
tCantidad2.config(bg="#9BEAC1")
can3=StringVar()
tCantidad3 = Entry(miFrame1, width=7, textvariable=can3)
tCantidad3.grid(row=8, column=3, pady=5, padx=5)
tCantidad3.config(bg="#9BEAC1")
#------- Label y entry,s Precio --------------------------------
lPrecio = Label(miFrame1, text='Precio_Unidad')
lPrecio.grid(row=5, column=4,sticky='ew', pady=5, padx=5)
lPrecio.config(bg="#33FFAF")
pre1=StringVar()
tPrecio1 = Entry(miFrame1, width=7, textvariable=pre1)
tPrecio1.grid(row=6, column=4, pady=5, padx=5)
tPrecio1.config(bg="#9BEAC1")
pre2=StringVar()
tPrecio2 = Entry(miFrame1, width=7, textvariable=pre2)#width número de caracteres
tPrecio2.grid(row=7, column=4, pady=5, padx=5)
tPrecio2.config(bg="#9BEAC1")
pre3=StringVar()
tPrecio3 = Entry(miFrame1, width=7, textvariable=pre3)
tPrecio3.grid(row=8, column=4, pady=5, padx=5)
tPrecio3.config(bg="#9BEAC1")
#------- Label y entry,s Subtotal ------------------------------
lSubtotal = Label(miFrame1, text='Subtotal')
lSubtotal.grid(row=5, column=5,sticky='ew', pady=5, padx=5)
lSubtotal.config(bg="#33FFAF")
sub1=DoubleVar()
tSubtotal1 = Entry(miFrame1, width=7, textvariable=sub1)
tSubtotal1.grid(row=6, column=5, pady=5, padx=5)
tSubtotal1.config(bg="#9BEAC1")
sub2=DoubleVar()
tSubtotal2 = Entry(miFrame1, width=7, textvariable=sub2)#width número de caracteres
tSubtotal2.grid(row=7, column=5, pady=5, padx=5)
tSubtotal2.config(bg="#9BEAC1")
sub3=DoubleVar()
tSubtotal3 = Entry(miFrame1, width=7, textvariable=sub3)
tSubtotal3.grid(row=8, column=5, pady=5, padx=5)
tSubtotal3.config(bg="#9BEAC1")

#------- Label y entry,s Total --------------------------------
lTotal = Label(miFrame1, text='Total')
lTotal.grid(row=8, column=6,sticky='ew', pady=5, padx=5)
lTotal.config(bg="#33FFAF", font="bold")
ttotal=DoubleVar()
tTotal = Entry(miFrame1, width=7, textvariable=ttotal)
tTotal.grid(row=8, column=7, pady=5, padx=5)
tTotal.config(bg="#9BEAC1", font="bold")


#------ Botón guardar -----------------------------------------
guardar=Button(miFrame1, text='Guradar', command=codigoGuardar, width=10, height=3)
guardar.grid(row=9, column=4, pady=5, padx=5)
guardar.config(bg="#9BEAC1", font="bold")
#------------creando funcion para bucar producto------------
def codigoBuscar():

#------------producto de codigo 1---------------
	a=cod1.get()
	if a=="1":
		des1.set("clavo")
		uni1.set("2 pulg")
		pre1.set("0.30")
	elif a=="2":
		des1.set("cable")
		uni1.set("por/metro")
		pre1.set("3.10")
	elif a=="3":
		des1.set("foco")
		uni1.set("1")
		pre1.set("8")
	else:
		des1.set("  ----")
		uni1.set("  ----")
		pre1.set("  ----")
#------------producto  de codigo 2---------
	b=cod2.get()
	if b=="1":
		des2.set("clavo")
		uni2.set("2 pulg")
		pre2.set("0.30")
	elif b=="2":
		des2.set("cable")
		uni2.set("por/metro")
		pre2.set("3.10")
	elif b=="3":
		des2.set("foco")
		uni2.set("1")
		pre2.set("8")
	else:
		des2.set("  ----")
		uni2.set("  ----")
		pre2.set("  ----")
#------------producto de codigo 3-----------------
	c=cod3.get()
	if c=="1":
		des3.set("clavo")
		uni3.set("2 pulg")
		pre3.set("0.30")
	elif c=="2":
		des3.set("cable")
		uni3.set("por/metro")
		pre3.set("3.10")
	elif c=="3":
		des3.set("foco")
		uni3.set("1")
		pre3.set("8")
	else:
		des3.set("  ----")
		uni3.set("  ----")
		pre3.set("  ----")

	#pass
#----------mostrar por que no hay producto
#--------boton buscar-------------------------------------
bBuscar=Button(miFrame1, text='Buscar Producto', command=codigoBuscar)
bBuscar.grid(row=9, column=2, pady=5, padx=5)
bBuscar.config(bg="#9BEAC1", font="bold")

#--------añadiendo funcion al boton preTotal----
def codigoTotal():

	try:
		e=float(can1.get())
		f=float(pre1.get())
		sub1.set(e*f)
	except ValueError:
		sub1.set(float(0))
#---------------------------		
	try:
		g=float(can2.get())
		h=float(pre2.get())
		sub2.set(g*h)
	except ValueError:
		sub2.set(float(0))
#--------------------------		
	try:
		i=float(can3.get())
		j=float(pre3.get())
		sub3.set(i*j)
	except ValueError:
		sub3.set(float(0))

	try:
		ttotal.set(sub1.get()+sub2.get()+sub3.get())
	except TclError:
		ttotal.set("  ----")
	#pass
#------------boton preTotal---------------------
preTotal=Button(miFrame1, text='Precio Total', command=codigoTotal)
preTotal.grid(row=9, column=3, pady=5, padx=5)
preTotal.config(bg="#9BEAC1", font="bold")

#------creando funcion para el boton limpiar
def codigoLimpiar():
	obtenerDatos1.set("")
#---------boton limpiar-----------------------
bLimpiar=Button(miFrame1, text="Limpiar", command=codigoLimpiar)
bLimpiar.grid(row=11, column=7, pady=5, padx=5)
bLimpiar.config(bg="#9BEAC1", font="bold")
#------salida e impresion de los datos------------------------
miFrame3=Frame(root)
miFrame3.config(bg="#33FFAF")
miFrame3.pack()

obtenerDatos1=StringVar()
lDatos = Label(miFrame3, text='', textvariable=obtenerDatos1)
lDatos.grid(row=10, column=0, sticky="w", pady=5, padx=5)
lDatos.config(bg="#33FFAF",fg="#07730C", font="bold", justify="left")

#-----------------------------------------------------------------
root.mainloop()