"""
This module contains the Flask API for managing backups.
"""

import json
from flask import Flask, abort, jsonify
from backup import backup

app = Flask(__name__)
app.secret_key = b'o\xe8\xc3VS\xf3\xf8\x0c\x80Y\xad\xb6\x86\xb3\x7f\xee\x98l\x80\xe47\xfb]}'

@app.route("/backups", methods=["GET"])
def get_backups():
    """
    Retrieve all backups.

    Returns:
        JSON response: A JSON response containing all backups.
    """
    with open("state.json", "r", encoding="utf-8") as file:
        backups = json.load(file)
        file.close()

    return jsonify(backups)

@app.route("/backups/<backup_id>", methods=["GET"])
def get_backup(backup_id=None):
    """
    Retrieve a specific backup.

    Args:
        backup_id (str): The ID of the backup to retrieve.

    Returns:
        JSON response: A JSON response containing the specified backup.

    Raises:
        404: If the backup with the specified ID does not exist.
    """
    with open("state.json", "r", encoding='utf-8') as file:
        backups = json.load(file)
        file.close()

    if backup_id in backups:
        results = jsonify(backups[backup_id])
        return results

    abort(404)

@app.route("/backup", methods=["POST"])
def post_backup():
    """
    Create a new backup.

    Returns:
        JSON response: A JSON response indicating that the backup has been created.
    """
    backup()
    return jsonify({"message": "Backup created"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)