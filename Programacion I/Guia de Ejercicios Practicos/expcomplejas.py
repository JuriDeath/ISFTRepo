#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#
# ----------------------------------------------------------------------
# Expresiones Linealizadas
# ----------------------------------------------------------------------
# 1) X = ( a + b / c ) / ( a / b + c )
# 2) X = ( a + b + a / b ) / c
# 3) X = ( a / ( a + b ) ) / ( a / ( a - b ) )
# 4) X = ( a + ( b / ( a + b + ( b / c ) ) ) ) / ( a + b / ( c + a ) )
# 5) X = ( a + b + c ) / ( a + ( b / c ) )
# 6) X = ( a + b + ( c / ( d * a ) ) / ( a + ( b * ( c / d ) ) ) )
# 7) X = ( a + ( b / c ) + d ) / a
# 8) X = ( ( a / b ) + ( b / c ) ) / ( ( a / b ) - ( b / c ) )
# 9) X = a + ( ( a + ( ( a + b ) / ( c + d ) ) ) / ( a + ( a / b ) ) )
# 10) X = a + b + ( c / d ) + ( ( a / ( b - c ) ) / ( a / ( b + c ) ) )
#
# ----------------------------------------------------------------------
# Valores Dados
# ----------------------------------------------------------------------
# 1) a = 2, b = 2, c = 2
# 2) a = 5, b = 2, c = 3
# 3) a = 4, b = 3
# 4) a = 4, b = 2, c = 3
# 5) a = 6, b = 5, c = 4
# 6) a = 5, b = 4, c = 10, d = 2
# 7) a = 3, b = 2, c = 1, d = 4
# 8) a = 10, b = 6, c = 2
# 9) a = 5, b = 4, c = 3, d = 2
# 10) a = 9, b = 8, c = 7, d = 6
#
#
# Primer
a = 2
b = 2
c = 2
x = ( a + b / c ) / ( a / b + c )
print "El resultado de la primera ecuacion es:", x
# Segundo
a = 5
b = 2
c = 3
x = ( a + b + a / b ) / c
print "El resultado de la segundo ecuacion es:", x
# Tercero
a = 4
b = 3
x = ( a / ( a + b ) ) / ( a / ( a - b ) )
print "El resultado de la tercero ecuacion es:", x
# Cuarto
a = 4
b = 2
c = 3
x = ( a + ( b / ( a + b + ( b / c ) ) ) ) / ( a + b / ( c + a ) )
print "El resultado de la cuarto ecuacion es:", x
# Quinto
a = 6
b = 5
c = 4
x = ( a + b + c ) / ( a + ( b / c ) )
print "El resultado de la quinto ecuacion es:", x
# Sexto
a = 5
b = 4
c = 10
d = 2
x = ( a + b + ( c / ( d * a ) ) / ( a + ( b * ( c / d ) ) ) )
print "El resultado de la sexto ecuacion es:", x
# Septimo
a = 3
b = 2
c = 1
d = 4
x = ( a + ( b / c ) + d ) / a
print "El resultado de la septimo ecuacion es:", x
# Octavo
a = 10
b = 6
c = 2
x = ( ( a / b ) + ( b / c ) ) / ( ( a / b ) - ( b / c ) )
print "El resultado de la octavo ecuacion es:", x
# Noveno
a = 5
b = 4
c = 3
d = 2
x = a + ( ( a + ( ( a + b ) / ( c + d ) ) ) / ( a + ( a / b ) ) )
print "El resultado de la noveno ecuacion es:", x
# Decimo
a = 9
b = 8
c = 7
d = 6
# x = a + b + ( c / d ) + ( ( a / ( b - c ) ) / ( a / ( b + c ) ) ) DIVIDE POR CERO
print "El resultado de la decimo ecuacion es: NO TIENE PORQUE DIVIDE POR CERO"
