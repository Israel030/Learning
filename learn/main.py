#IMPORTAR LA LIBRERIA FLASK Y LA CONFIGURACION
from flask import Flask, jsonify, request
app = Flask(__name__)

'''
GET    --> Obtener informacion
POST   --> Crear informacion
PUT    --> Actualizar informacion
DELETE --> Borrar informacion
'''


@app.route("/")
def saludar():
    return "Hola Mundo!"

@app.route("/users/<user_id>")
def get_user(user_id):
    user = {"id": user_id, "name": "Israel", "Telefono":"435-100-7268"}
    #/users/2643?query=query_test
    query = request.args.get('query')
    if query:
        user['query'] = query
    return jsonify(user),200
    

@app.route('/users', methods=["post"])
def createUser():
    data = request.get_json()
    data["status"]="user created"
    return jsonify(data),201    


#Ejecutamos la aplicacion
if __name__ == '__main__':
    app.run(debug=True)
    



