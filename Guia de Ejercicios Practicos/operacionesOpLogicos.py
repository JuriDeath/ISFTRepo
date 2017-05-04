#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#
# ----------------------------------------------------------------------
# Expresiones con operadores lógicos
# ----------------------------------------------------------------------
# 1) x = ( ( y and z ) or p ) and not z
# 2) x = ( not p or z ) and ( not z and p )
# 3) x = not y and z
# 4) x = ( not y and z ) or ( p and not z )
# 5) x = y or not p
# 6) x = ( q and p ) or not y
# 7) x = p or not q
# 8) x = ( q and z ) and ( not p or not q )
# 9) x = not ( y or not q )
# 10) x = ( p and q ) or not p
# 11) x = ( z or y ) or not p
# 12) x = not ( p and q )
# 13) x = p and not q
# 14) x = z or not y
# 15) x = not ( y and not z ) or ( not y and z )
#
#
import os

def resolverEjercicios( p, q, y, z ):
	p = p
	q = q
	y = y
	z = z
	x = ( ( y and z ) or p ) and not z
	print "El resultado de la primera operacion logica es:", x
	x = ( not p or z ) and ( not z and p )
	print "El resultado de la segunda operacion logica es:", x
	x = not y and z
	print "El resultado de la tercera operacion logica es:", x
	x = ( not y and z ) or ( p and not z )
	print "El resultado de la cuarta operacion logica es:", x
	x = y or not p
	print "El resultado de la quinta operacion logica es:", x
	x = ( q and p ) or not y
	print "El resultado de la sexta operacion logica es:", x
	x = p or not q
	print "El resultado de la septima operacion logica es:", x
	x = ( q and z ) and ( not p or not q )
	print "El resultado de la octava operacion logica es:", x
	x = not ( y or not q )
	print "El resultado de la novena operacion logica es:", x
	x = ( p and q ) or not p
	print "El resultado de la decima operacion logica es:", x
	x = ( z or y ) or not p
	print "El resultado de la decimo primera operacion logica es:", x
	x = not ( p and q )
	print "El resultado de la decimo segunda operacion logica es:", x
	x = p and not q
	print "El resultado de la decimo tercera operacion logica es:", x
	x = z or not y
	print "El resultado de la decimo cuarta operacion logica es:", x
	x = not ( y and not z ) or ( not y and z )
	print "El resultado de la decimo quinta operacion logica es:", x

p = raw_input("Ingrese el valor de p (True o False):")
p = bool(p)
q = raw_input("Ingrese el valor de q (True o False):")
q = bool(q)
y = raw_input("Ingrese el valor de y (True o False):")
y = bool(y)
z = raw_input("Ingrese el valor de z (True o False):")
z = bool(z)
os.system("cls")
resolverEjercicios( p, q, y, z )