m=int(abs(raw_input('Ingresar monto: ')))
cant=0
cant+=m/500
m=m%500
cant+=m/100
m=m%100
cant+=m/20
m=m%20
cant+=m/5
m=m%5
cant+=m/1
print cant