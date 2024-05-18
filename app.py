from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1')
def ejercicio1():
    return render_template('ejercicio1.html')

@app.route('/calcular_descuento', methods=['POST'])
def calcular_descuento():
    nombre = request.form['nombre']
    edad = int(request.form['edad'])
    cantidad_tarros = int(request.form['cantidad_tarros'])

    precio_por_tarro = 9000
    total_sin_descuento = cantidad_tarros * precio_por_tarro

    if edad >= 18 and edad <= 30:
        descuento = 0.15
    elif edad > 30:
        descuento = 0.25
    else:
        descuento = 0

    total_con_descuento = total_sin_descuento - (total_sin_descuento * descuento)

    total_sin_descuento = float("{:.2f}".format(total_sin_descuento))  # Convierte a número de punto flotante y redondea a 2 decimales
    total_con_descuento = float("{:.2f}".format(total_con_descuento))  # Convierte a número de punto flotante y redondea a 2 decimales

    if total_con_descuento is not None:
        return render_template('ejercicio1.html', nombre=nombre, total_sin_descuento=total_sin_descuento, descuento=total_sin_descuento - total_con_descuento, total_con_descuento=total_con_descuento)
    else:
        return render_template('ejercicio1.html')  # Puedes manejar el caso cuando no hay resultados como prefieras
@app.route('/ejercicio2')
def ejercicio2():
    return render_template('ejercicio2.html')

@app.route('/autenticar_usuario', methods=['POST'])
def autenticar_usuario():
    usuario = request.form['usuario']
    contrasena = request.form['contrasena']

    if usuario == 'juan' and contrasena == 'admin':
        mensaje = 'Bienvenido administrador juan'
    elif usuario == 'pepe' and contrasena == 'user':
        mensaje = 'Bienvenido usuario pepe'
    else:
        mensaje = 'Usuario o contraseña incorrectos'

    return render_template('ejercicio2.html', mensaje=mensaje)

if __name__ == '__main__':
    app.run(debug=True, port=5500)
