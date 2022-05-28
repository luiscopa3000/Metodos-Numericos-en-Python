# -*- coding: utf-8 -*-
"""
"""

import sympy as sp
# Definir funcion
x=sp.Symbol('x')
fx=(9.8/15)*x*(1-sp.exp(-(135/x)))-35
# Definimos los limites
xi=1
xs=65
tolerancia=0.0001

fxi=fx.evalf(subs={x:xi})
fxs=fx.evalf(subs={x:xs})
xr=(xi+xs)/2
fxr=fx.evalf(subs={x:xr})
if fxi*fxr<0:
    xs=xr
if fxi*fxr>0:
    xi=xr
print("Xi","\t\t","Xs","\t\t","f(Xi)","\t\t","f(Xs)","\t\t","Xr","\t\t","f(Xr)","\t\t","Error")
error=0
while(True):
    print(xi,"\t",xs,"\t",fxi,"\t",fxs,"\t",xr,"\t",fxr,"\t",error)
    xr_anterior=xr
    fxi=fx.evalf(subs={x:xi})
    fxs=fx.evalf(subs={x:xs})
    xr=(xi+xs)/2
    fxr=fx.evalf(subs={x:xr})
    
    if fxi*fxr<0:
        xs=xr
    if fxi*fxr>0:
        xi=xr
    if fxi*fxr==0:
        break
    error=abs((xr-xr_anterior)/xr)
    if error<tolerancia:
        break
print("***************MÉTODO DE LA BISECCIÓN****************")
print("La raiz encontrada es:",xr)
        


