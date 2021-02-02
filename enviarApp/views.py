from django.shortcuts import render
from .models import Post,Anpost,Comprar
import pandas as pd
from django.core import serializers
import sqlite3
from json import dumps
import json
import datetime
from django.http import JsonResponse
from django.http import HttpResponse

def chDate(fecha):
	fechaN=fecha.replace('-','')
	fechaN=fechaN.replace(':','')
	fechaN=fechaN.replace('.','')
	fechaN=fechaN.replace(' ','')

	return fechaN

def createpost(request):
        if request.method == 'POST':
            if request.POST.get('title') and request.POST.get('content'):
                post=Post()
                post.title= request.POST.get('title')
                post.content= request.POST.get('content')
                post.save()
                df= pd.DataFrame(list(Post.objects.all().values()))
                return render(request, 'createpost.html',{"daticos":df.to_html()})
        else:
            return render(request,'createpost.html')

def createanpost(request):
        if request.method == 'POST':
            if request.POST.get('titled'):
                borrar=request.POST['titled']
                Post.objects.filter(title=borrar).delete()
                df= pd.DataFrame(list(Post.objects.all().values()))
                return render(request, 'createpost.html',{"daticos":df.to_html()})

        else:
                return render(request,'createpost.html')

def createpostCheckB(request):
	if request.method == 'POST':
			if request.POST.get('title') and request.POST.get('content'):
				post=Post()
				post.title= request.POST.get('title')
				post.content= request.POST.get('content')
				post.save()
				df= pd.DataFrame(list(Post.objects.all().values()))
				longitud=len(df)

				titles=df.title.values.tolist()
				#Agrrelo pasa a ser una cadena STR
				arreglo = ','.join(titles)
				return render(request, 'createpostCheckB.html',
                {"daticos":df.to_html(), "longitud":longitud , "arreglo":arreglo})
	else:
		df= pd.DataFrame(list(Post.objects.all().values()))
		longitud=len(df)

		titles=df.title.values.tolist()
		#Agrrelo pasa a ser una cadena STR
		arreglo = ','.join(titles)
		return render(request,'createpostCheckB.html',
		{"longitud":longitud , "arreglo":arreglo})

def deletepostCheckB(request):
	if request.method == 'POST':
			listProd=request.POST.getlist('products[]')
			listProd=[int(i) for i in listProd]
			print('listProd:',listProd)

			df= pd.DataFrame(list(Post.objects.all().values()))
			print("Este debe ser un df normal y completo: \n", df)
			df = df.drop(listProd)
			print("Este debe ser un df despues de => df.drop(listProd) : \n", df)
			longitud=len(df)
			titles=df.title.values.tolist()
			#Agrrelo pasa a ser una cadena STR
			arreglo = ','.join(titles)

			conexion= sqlite3.connect('db.sqlite3')
			df.to_sql('enviarApp_post',conexion, if_exists='replace', index=False)
			return render(request, 'createpostCheckB.html',
            {"daticos":df.to_html(),"longitud":longitud,"arreglo":arreglo})
	else:
		df= pd.DataFrame(list(Post.objects.all().values()))
		longitud=len(df)
		titles=df.title.values.tolist()
		#Agrrelo pasa a ser una cadena STR
		arreglo = ','.join(titles)

		return render(request,'createpostCheckB.html',
		{"daticos":df.to_html(),"longitud":longitud,"arreglo":arreglo})

def Papeleria(request):

    df=pd.read_csv('enviarDatos/artpict.csv')
    list1=df.name.values.tolist()
    arreglo = ','.join(list1)
    json1 = df.to_json(orient ='records')
    return render(request, "Papeleria.html",
    {"arreglo":arreglo ,"json1":json1})

def createpostButton(request):
        if request.method == 'POST':
            if request.POST.get('title') and request.POST.get('content'):
                post=Post()
                post.title= request.POST.get('title')
                post.content= request.POST.get('content')
                post.save()
                df= pd.DataFrame(list(Post.objects.all().values()))
                longitud=len(df)
                return render(request, 'createpostButton.html',
                {"daticos":df.to_html(), "longitud":longitud})
        else:
            df= pd.DataFrame(list(Post.objects.all().values()))
            return render(request,'createpostButton.html',
            {"daticos":df.to_html()})

def deletepostButton(request):
	if request.method == 'POST':
			str_carrito="Carrito de Compra"
			listProd=request.POST.getlist('products[]')
			listProd=[int(i) for i in listProd]
			print('listProd:',listProd)
			df= pd.DataFrame(list(Post.objects.all().values()))
			df_iloc = df.iloc[listProd]
			print("DF ILOC\n",df_iloc)
			df_iloc.to_csv("file_iloc.csv")

			longitud=len(df)
			return render(request, 'carritoCompra.html',
            {"daticos":df.to_html(),
             "carrito":df_iloc.to_html(),
             "longitud":longitud,
             "str_carrito":str_carrito})
	else:
			df= pd.DataFrame(list(Post.objects.all().values()))
			longitud=len(df)
			return render(request,'createpostButton.html',
            {"daticos":df.to_html(),"longitud":longitud})

def createCatalogo(request):
        df=pd.read_csv('Post.csv')
        titles=df.title.values.tolist()
        arreglo = ','.join(titles)
        print("Resultado del .join: \n", type(arreglo), arreglo)
        longitud=len(df)
        json_records = df.reset_index().to_json(orient ='records')
        #data = []
        data = json.loads(json_records)
        print("\n\nEsto es json.loads(Una lista)", type(data))
        return render(request,'createCatalogo.html',
                      {"daticos":df.to_html(classes='table table-striped'),
                       "longitud":longitud,"titles":titles, "arreglo":arreglo,
                       'd': data, "json_records":json_records})

def carritoCompra(request):
    if request.method == 'POST':
            listProd=request.POST.getlist('products[]')
            listProd=[int(i) for i in listProd]
            print('listProd:',listProd)
            df= pd.read_csv('Post.csv')

            print("Primer DF: ", df)
            df_iloc = df.iloc[listProd]
            print("DF ILOC\n",df_iloc)
            df_iloc.to_csv("file_iloc.csv",index=False)

            longitud=len(df)
            df_carrito=pd.read_csv("file_iloc.csv")
            print(df_carrito)
            return render(request, 'carritoCompra.html',
            {"carrito":df_carrito.to_html()})

def agregarCompra(request):
	df=pd.read_csv("nuevo.csv")
	#longitud=len(df)

	cant= str(request.POST.get('cantidad'))
	orden=chDate(str(datetime.datetime.now()))

	df_list=pd.read_csv("file_iloc.csv")
	row_iloc = df_list.iloc[0]
	row_list=row_iloc.values.tolist()
	row_list.append(cant)
	row_list.append(orden)
	modDfobj = df.append(pd.Series(row_list,index=df.columns),  ignore_index=True)
	modDfobj.to_csv("nuevo.csv",index=False)
	longitud=len(modDfobj)

	# /// TITULOS ///
	titles=modDfobj.title.values.tolist()
	# #Agrrelo pasa a ser una cadena STR
	titulos = ','.join(titles)
	print('titulos: \n', titulos)

	# /// CANTIDAD ///
	cants=str(modDfobj.cantidad.values.tolist())
	cants=cants.replace(".0", "")
	# #Agrrelo pasa a ser una cadena STR
	print('cants: \n', cants)
	# cantidades = ','.join(cants)
	cantidades = cants
	print('cantidades: \n', cantidades)
    #Primero paso cantidades , PERO 'cant'
	#todavia no es parte de cantidades
	return render(request, 'agregarCompra.html',
	{"lista":modDfobj.to_html(),"longitud":longitud,"titulos":titulos,
	 "cantidades":cantidades})




def borrarCompra(request):
	if request.method == 'POST':
		listProd=request.POST.getlist('products[]')
		listProd=[int(i) for i in listProd]
		print('listProd:',listProd)
		df=pd.read_csv("nuevo.csv")
		print('Df normal: \n ', df)
		dfTrash=df
		#Aqui deberia borrar
		dfTrash = dfTrash.drop(listProd)
		longitud=len(dfTrash)
		titles=dfTrash.title.values.tolist()
		# #Agrrelo pasa a ser una cadena STR
		titulos = ','.join(titles)

		cants=str(dfTrash.cantidad.values.tolist())
		cants=cants.replace(".0", "")
		cantidades = cants



		dfTrash.to_csv("nuevo.csv",index=False)

		return render(request, 'agregarCompra.html',
		{"lista":dfTrash.to_html(),"longitud":longitud,"titulos":titulos,
		 "cantidades":cantidades})

def send_dictionary(request):
    # create data dictionary
    dataDictionary = {
        'hello': 'World',
        'geeks': 'forgeeks',
        'ABC': 123,
        456: 'abc',
        14000605: 1,
        'list': ['geeks', 4, 'geeks'],
        'dictionary': {'you': 'can', 'send': 'anything', 3: 1}
    }
    # dump data
    dataJSON = dumps(dataDictionary)
    return render(request, 'landing.html', {'data': dataJSON})


def opposites(request):
    # create data dictionary
    data = [
        ["Laugh", "Cry"],
        ["Even", "Odd"],
        ["Hot", "Cold"],
        ["Light", "Dark"],
        ["Opposite", "Same"],
        ["Far", "Near"],
        ["Give", "Take"],
        ["Night", "Day"],
        ["Import", "Export"],
        ["Hard", "Easy"],
        ["Never", "Always"],
        ["Late", "Early"],
        ["Less", "More"],
        ["Male", "Female"],
        ["Happiness", "Sadness"],
        ["Fast", "Slow"],
        ["Old", "Young"],
        ["Boy", "Girl"],
        ["Up", "Down"],
        ["Left", "Right"],
        ["Rich", "Poor"],
        ["Love", "Hate"],
        ["Inside", "Outside"],
        ["Bad", "Good"],
        ["Short", "Tall"],
    ]
    data = dumps(data)
    return render(request, "opposites.html", {"data": data})


def headerTemplate(request):

    return render(request, 'header.html')

def notPosting(request):
	json.loads(request.body.decode('utf-8'))
	return render(request, 'notPosting.html')

def send_json(request):
        if request.method == 'POST':
                data = [{'name': 'Peter', 'email': 'peter@example.org'},
                        {'name': 'Julia', 'email': 'julia@example.org'}]
                return JsonResponse(data, safe=False)

# Cookie Tutorial.
def home(request):
        return HttpResponse("Welcome")

def setting_cookie(request):
        #ya el archivo html(getcookie.hmtl) tiene los scripts 
        #necesarios para crear la cookie
        return render(request, "getcookie.html")

def getting_cookie(request):
        #tomo el cookie string 
        first_test  = request.COOKIES['compra']
        #lo convierto en json
        d = json.loads(first_test)
        print(d)
        #'{"3":{"quantity":2},"1":{"quantity":1},"2":{"quantity":1}}
        # Con pgadmin puedes ver el key
        print("Este es las id: ", d.keys())
        print("Item ", d.items())

        print("Este for imprime cada key y qty de d.items()")
        for key,qty in d.items():
                product = Comprar.objects.get(id=key)
                product.quantity = product.quantity-d[key]["quantity"]
                product.save() 
                
                print(product)
               
       
        return render(request, "getcookie.html")



def slider(request):
        return render(request, 'slider.html',{})


