class Direccion:
    def peticion(self, latlng):
        import requests
        a=requests.get(params={"latlng":latlng,"key": "AIzaSyAUWq7xFmgZzGXKr48PIgvv0l1m4fUGHe0"}, url="https://maps.googleapis.com/maps/api/geocode/json").json()

        self.numero=a["results"][0]["address_components"][0]["long_name"]
        self.calle=a["results"][0]["address_components"][1]["long_name"]
        self.colonia=a["results"][0]["address_components"][2]["long_name"]
        self.localidad=a["results"][0]["address_components"][3]["long_name"]
        self.estado=a["results"][0]["address_components"][6]["long_name"]
        self.pais=a["results"][0]["address_components"][7]["long_name"]
        self.codigo=a["results"][0]["address_components"][8]["long_name"]

        print "El numero de la direccion es: "+self.numero
        print "La calle de la direccion es: "+self.calle
        print "La colonia es: "+self.colonia
        print "La localidad es: "+self.localidad
        print "El estado es: "+self.estado
        print "El codigo postal es: "+self.codigo
        print "El pais es: "+self.pais






dir=Direccion()
dir.peticion("19.476384,-99.047263")
