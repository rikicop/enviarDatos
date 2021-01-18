import datetime


def chDate(fecha):

	
	fechaN=fecha.replace('-','')
	fechaN=fechaN.replace(':','')
	fechaN=fechaN.replace('.','')
	fechaN=fechaN.replace(' ','')

	return fechaN

fecha = str(datetime.datetime.now())
print(chDate(fecha))



