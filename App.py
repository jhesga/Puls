import eventlet
eventlet.monkey_patch()

from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from flask_socketio import SocketIO, emit
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'omnicobros-pro-key-2026')

socketio = SocketIO(app, cors_allowed_origins="*", async_mode='eventlet')

@app.route('/')
def index():
    try:
        return render_template('index.html')
    except Exception as e:
        return f"""
        <div style="font-family: Arial, sans-serif; padding: 40px; text-align: center; background-color: #f8f9fa;">
            <h1 style="color: #0d6efd;">OmniCobros Pro - Backend Activo</h1>
            <p style="font-size: 18px; color: #333;">El servidor está conectado y funcionando correctamente en la nube.</p>
            <hr style="max-width: 500px; margin: 20px auto; border: 0; border-top: 1px solid #ddd;">
            <p style="color: #6c757d; font-size: 14px;">Aviso: Asegúrate de tener tu archivo <code>index.html</code> dentro de la carpeta <code>templates</code>.</p>
            <p style="color: #dc3545; font-size: 12px;">Detalle técnico: {str(e)}</p>
        </div>
        """, 200

@app.route('/api/status')
def api_status():
    return jsonify({"status": "success", "message": "API de micro-créditos operando al 100%"})

@socketio.on('connect')
def handle_connect():
    print('Cliente conectado exitosamente vía WebSocket')

@socketio.on('disconnect')
def handle_disconnect():
    print('Cliente desconectado del servidor')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    socketio.run(app, host='0.0.0.0', port=port, debug=False)
