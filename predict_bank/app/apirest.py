from flask import Flask, request, jsonify
from predict import ejecutar_flujo_prediccion  
from flask import send_file
import os

app = Flask(__name__)


@app.route("/predecir", methods=["GET"])
def predecir():
    try:
        # Ejecutar predicción
        submission = ejecutar_flujo_prediccion("modelo_entrenado.pkl", "test.csv")

        # Guardar archivo CSV en el servidor
        file_path = os.path.abspath("predicciones.csv")
        submission.to_csv(file_path, index=False)
        
        print("Guardando archivo...")
        print(submission.head())
        # Retornar JSON con vista previa
        return jsonify({
            "mensaje": "Predicción realizada con éxito",
            "predicciones": submission.head().to_dict(orient="records")
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route("/descargar", methods=["GET"])

def descargar_csv():
    file_path = os.path.abspath("predicciones.csv")
    if not os.path.exists(file_path):
        return jsonify({"error": f"El archivo no existe en: {file_path}"}), 404

    return send_file(file_path,
                     as_attachment=True,
                     download_name="predicciones.csv",
                     mimetype="text/csv")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    
