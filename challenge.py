class Direccion:
    def peticion(self, latlng):
        import requests
        a=requests.get(params={"latlng":latlng,"key": "AIzaSyAUWq7xFmgZzGXKr48PIgvv0l1m4fUGHe0"}, url="https://maps.googleapis.com/maps/api/geocode/json").json()
        
        numero=a["results"][0]["address_components"][0]["long_name"]
        calle=a["results"][0]["address_components"][1]["long_name"]
        colonia=a["results"][0]["address_components"][2]["long_name"]
        localidad=a["results"][0]["address_components"][3]["long_name"]
        estado=a["results"][0]["address_components"][6]["long_name"]
        pais=a["results"][0]["address_components"][7]["long_name"]
        codigo=a["results"][0]["address_components"][8]["long_name"]

        print "El numero de la direccion es: "+numero
        print "La calle de la direccion es: "+calle
        print "La colonia es: "+colonia
        print "La localidad es: "+localidad
        print "El estado es: "+estado
        print "El codigo postal es: "+codigo
        print "El pais es: "+pais

print "Programa que otorga los elementos de una direccion a partir de las cordenadas"

latlng=raw_input("Dame la latitud y longitud")



dir=Direccion()
dir.peticion(latlng)
