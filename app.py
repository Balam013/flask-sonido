from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def calcular_velocidad_sonido(temperatura):
    return 331.3 + (0.606 * temperatura)

def calcular_longitud_onda(velocidad, frecuencia):
    if frecuencia <= 0:
        return None
    longitud_onda = velocidad / frecuencia
    return {
        "longitud_completa": longitud_onda,
        "media_longitud": longitud_onda / 2,
        "cuarto_longitud": longitud_onda / 4
    }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcular', methods=['POST'])
def calcular():
    try:
        temperatura = float(request.form['temperatura'])
        frecuencia = float(request.form['frecuencia'])
        velocidad = calcular_velocidad_sonido(temperatura)
        longitudes = calcular_longitud_onda(velocidad, frecuencia)

        if longitudes is None:
            return jsonify({"error": "La frecuencia debe ser mayor que 0 Hz."}), 400

        return jsonify({
            "velocidad": velocidad,
            **longitudes
        })
    except ValueError:
        return jsonify({"error": "Por favor, ingrese valores numéricos válidos."}), 400

if __name__ == '__main__':
    app.run(debug=True)
