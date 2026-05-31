from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

USUARIOS_DB = {
    "admin": "12345",
    "arturo": "sistemas2026"
}

PRODUCTOS_DB = {
    "P001": {
        "nombre": "Laptop HP Pavilion 15", 
        "precio": "S/. 2500", 
        "stock": 15, 
        "categoria": "Laptops",
        "imagen": "https://images.unsplash.com/photo-1588872657578-7efd1f1555ed?w=300"
    },
    "P002": {
        "nombre": "Mouse Logitech MX Master 3", 
        "precio": "S/. 385", 
        "stock": 4, 
        "categoria": "Accesorios",
        "imagen": "https://images.unsplash.com/photo-1615663245857-ac93bb7c39e7?w=300"
    },
    "P003": {
        "nombre": "Teclado Mecánico RGB Custom", 
        "precio": "S/. 280", 
        "stock": 22, 
        "categoria": "Accesorios",
        "imagen": "https://images.unsplash.com/photo-1587829741301-dc798b83add3?w=300"
    },
    "P004": {
        "nombre": "Monitor Gamer Asus 27'", 
        "precio": "S/. 1150", 
        "stock": 8, 
        "categoria": "Monitores",
        "imagen": "https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=300"
    },
    "P005": {
        "nombre": "Auriculares HyperX Cloud II", 
        "precio": "S/. 320", 
        "stock": 0, 
        "categoria": "Audio",
        "imagen": "https://images.unsplash.com/photo-1546435770-a3e426bf472b?q=80&w=400"
    },
    "P006": {
        "nombre": "Disco Sólido SSD NVMe 1TB", 
        "precio": "S/. 410", 
        "stock": 50, 
        "categoria": "Componentes",
        "imagen": "https://images.unsplash.com/photo-1591488320449-011701bb6704?q=80&w=400"
    }
}

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json(silent=True) or request.form
    username = data.get('username')
    password = data.get('password')
    
    if username in USUARIOS_DB and USUARIOS_DB[username] == password:
        return jsonify({"success": True, "user": username}), 200
    return jsonify({"success": False, "message": "Usuario o contraseña incorrectos"}), 401


@app.route('/api/productos', methods=['GET'])
def listar_productos():
    return jsonify({"success": True, "productos": PRODUCTOS_DB}), 200

@app.route('/api/productos/<codigo>', methods=['GET'])
def buscar_producto(codigo):
    codigo_limpio = codigo.strip().upper()
    if codigo_limpio in PRODUCTOS_DB:
        return jsonify({"success": True, "codigo": codigo_limpio, "producto": PRODUCTOS_DB[codigo_limpio]}), 200
    return jsonify({"success": False, "message": f"Código '{codigo_limpio}' no registrado"}), 404

if __name__ == '__main__':
    app.run(debug=True, port=5000)