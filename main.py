import random
import json

dic = {
    "ordenes":[],
    "clientes":[],
}

nombres = ['Juan','Adderly','Manuel','Maria','Lucia']
apellidos = ['Abad','Torres','Godoy','Brito']
mail = ['qqqqqq@gmail.com','wwwwww@gmail.com','eeeee@gmail.com','rrrrrr@gmail.com']
telefono = ['1234567890','9999999999','00000000000','0642875319','0998659742']
n_clientes = 10
url = ['https://www.dzoom.org.es/wp-content/uploads/2020/02/portada-foto-perfil-redes-sociales-consejos-810x540.jpg','https://www.planetromeo.com/wp-content/uploads/2019/10/pepp-photo-background-02.jpg','https://www.beauty-shooter.de/wp-content/uploads/Galerie-Portraits-Profilbilder-18.jpg']
for i in range(n_clientes):
    cliente = {
        "id":i,
        "nombres":random.choice(nombres),
        "img":random.choice(url),
        "apellidos":random.choice(apellidos),
        "mail":random.choice(mail),
        "telefono":random.choice(telefono)
    }
    dic.get('clientes').append(cliente)
n_ordenes = 3
for i in range(n_ordenes):
    orden = {
        "id": i,
        "id_cliente": random.randint(0,20),
        "nombre_cliente":random.choice(nombres) + ' '+random.choice(apellidos),
        "telefono":random.choice(telefono),
        "direccion": "Quito - Eloy Alfaro",
        "referencia": "Frente a tu casa",
        "id_estado": random.randint(1,9),
        "estado": "comanda",
        "fecha_registro": "2020-09-25 00:00:00",
        "metodo_pago": "efectivo",
        "cambio": "de 100",
        "fee_domicilio": True,
        "total":200,
        "historico":[
            {
                "nombre":"aprobado",
                "hora":"12:15"
            },{
                "nombre":"commanda",
                "hora":"12:20"
            },{
                "nombre":"enviado",
                "hora":"12:40"
            }
        ],"detail_order": [
            {
                "id_producto": 1,
                "nombre_producto": "Caramel Latte",
                "cantidad": 4,
                "comentario": "Prueba 1",
                "personalizacion": [
                    {
                        "nombre": "12 onzas",
                        "tipo": "Tamano",
                        "precio": 15,
                        "cantidad": 1
                    }
                ],
                "adicionales": [
                    {
                        "nombre": "Azucar",
                        "tipo": "Extras",
                        "precio": 5,
                        "cantidad": 1
                    }
                ]
            },{
                "id_producto": 1,
                "nombre_producto": "Caramel Latte",
                "cantidad": 4,
                "comentario": "Prueba 2",
                "personalizacion": [
                    {
                        "nombre": "12 onzas",
                        "tipo": "Tamano",
                        "cantidad": 1
                    },
                    {
                        "nombre": "Chocolate",
                        "tipo": "Sabor",
                        "cantidad": 1
                    }
                ],
                "adicionales": [
                    {
                        "nombre": "Azucar",
                        "tipo": "Extras",
                        "cantidad": 2
                    },
                    {
                        "nombre": "Miel",
                        "tipo": "Extras",
                        "cantidad": 3
                    }
                ]
            }
        ]
    }
    dic.get('ordenes').append(orden)

with open('db.json', 'w') as json_file:
  json.dump(dic, json_file,indent = 2, sort_keys=True)
print(json.dumps(dic,indent = 2, sort_keys=True))