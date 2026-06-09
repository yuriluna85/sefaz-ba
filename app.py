import os
import json
from flask import Flask, render_template, jsonify, request, send_from_directory

app = Flask(__name__, template_folder='.', static_folder='static')

# Path to the sibling "Concurso SEFAZ" folder containing PDFs
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SEFAZ_FILES_DIR = os.path.abspath(os.path.join(BASE_DIR, 'Concurso SEFAZ'))
PROGRESS_FILE = os.path.join(BASE_DIR, 'progress.json')
QUESTIONS_FILE = os.path.join(BASE_DIR, 'questions.json')
DISCURSIVAS_FILE = os.path.join(BASE_DIR, 'discursivas.json')

# Default progress structure if file does not exist
DEFAULT_PROGRESS = {
    "user_ti": {
        "name": "Irmão TI (Auditor/Agente)",
        "checked": []
    },
    "user_brother": {
        "name": "Irmão Geral (Agente)",
        "checked": []
    }
}

def load_progress():
    if os.path.exists(PROGRESS_FILE):
        try:
            with open(PROGRESS_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception:
            return DEFAULT_PROGRESS
    return DEFAULT_PROGRESS

def save_progress(data):
    try:
        with open(PROGRESS_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"Error saving progress: {e}")
        return False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/files')
def list_sefaz_files():
    """Lists files in the sibling Concurso SEFAZ directory."""
    files_list = []
    if os.path.exists(SEFAZ_FILES_DIR):
        try:
            for filename in os.listdir(SEFAZ_FILES_DIR):
                filepath = os.path.join(SEFAZ_FILES_DIR, filename)
                if os.path.isfile(filepath):
                    size_mb = os.path.getsize(filepath) / (1024 * 1024)
                    files_list.append({
                        "name": filename,
                        "size": f"{size_mb:.2f} MB",
                        "url": f"/files/{filename}"
                    })
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    return jsonify(files_list)

@app.route('/files/<path:filename>')
def download_file(filename):
    """Allows downloading files from the Concurso SEFAZ directory."""
    if not os.path.exists(SEFAZ_FILES_DIR):
        return "Pasta de arquivos não encontrada", 404
    return send_from_directory(SEFAZ_FILES_DIR, filename, as_attachment=True)

@app.route('/api/progress', methods=['GET', 'POST'])
def handle_progress():
    """Gets or updates study progress."""
    progress_data = load_progress()
    if request.method == 'POST':
        req_data = request.get_json()
        if not req_data:
            return jsonify({"error": "Invalid request body"}), 400
        
        # Update progress data
        if "user_ti" in req_data:
            progress_data["user_ti"]["checked"] = req_data["user_ti"].get("checked", [])
        if "user_brother" in req_data:
            progress_data["user_brother"]["checked"] = req_data["user_brother"].get("checked", [])
            
        if save_progress(progress_data):
            return jsonify({"status": "success", "data": progress_data})
        else:
            return jsonify({"error": "Failed to save progress"}), 500
            
    return jsonify(progress_data)

@app.route('/api/questions')
def get_questions():
    """Returns the mock questions list."""
    if os.path.exists(QUESTIONS_FILE):
        try:
            with open(QUESTIONS_FILE, 'r', encoding='utf-8') as f:
                return jsonify(json.load(f))
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    return jsonify([])

@app.route('/api/discursivas')
def get_discursivas():
    """Returns the mock discursivas list."""
    if os.path.exists(DISCURSIVAS_FILE):
        try:
            with open(DISCURSIVAS_FILE, 'r', encoding='utf-8') as f:
                return jsonify(json.load(f))
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    return jsonify([])

if __name__ == '__main__':
    # Running locally
    print(f"Buscando arquivos da pasta SEFAZ em: {SEFAZ_FILES_DIR}")
    app.run(debug=True, port=5000)
