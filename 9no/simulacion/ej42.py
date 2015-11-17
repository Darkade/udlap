#!/usr/bin/python
observaciones=[3]
for i in range(0,30):
	observaciones.append(3*observaciones[-1]%200)
print observaciones
