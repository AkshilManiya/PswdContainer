from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

connection = mysql.connector.connect( host='localhost', user='root',  password='',  database='pswd')
if connection.is_connected():
    print("Connected to MySQL database")

def run_query(query, query_type="select"):
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query)
        if query_type.lower() == "select":
            result = cursor.fetchall()
            cursor.close()
            return jsonify(result), True
        else:
            connection.commit()
            cursor.close()
            return {"message": "Query executed successfully."}, True
    except mysql.connector.Error as e:
        return {"error": str(e)}, False

@app.route('/pswd')
def pswd():
    return render_template("PswdContainer.html")


@app.route('/pswd/save', methods=['POST'])
def pswd_save():
    try:
        title = request.form.get('Title')
        title_desc = request.form.get('Title_desc')
        password = request.form.get('Password')
        desc = request.form.get('Desc')

        if not title or not password:
            return jsonify({"success": False, "msg": "Title and Password are required."})

        query = f"""INSERT INTO pswd (Title, Title_desc, Password, `Desc`)
                    VALUES ('{title}', '{title_desc}', '{password}', '{desc}')"""
        response , success = run_query(query, query_type="insert")

        if success:
            return jsonify({"success": True, "msg": "Data inserted successfully."})
        else:
            return jsonify({"success": False, "msg": "Data insertion failed."})
    except Exception as e:
        return jsonify({"success": False, "msg": str(e)})


@app.route('/pswd/update', methods=['POST'])
def pswd_update():
    try:
        pswd_id = request.form.get('pswd_id')
        title = request.form.get('Title')
        title_desc = request.form.get('Title_desc')
        password = request.form.get('Password')
        desc = request.form.get('Desc')

        if not pswd_id or not pswd_id.isdigit():
            return jsonify({"success": False, "msg": "Invalid or missing pswd_id."})

        query = f"""UPDATE pswd SET Title = '{title}', Title_desc = '{title_desc}',
                    Password = '{password}', `Desc` = '{desc}'
                    WHERE Pswd_id = '{pswd_id}'"""
        _, success = run_query(query, query_type="update")

        if success:
            return jsonify({"success": True, "msg": "Data updated successfully."})
        else:
            return jsonify({"success": False, "msg": "Data update failed."})
    except Exception as e:
        return jsonify({"success": False, "msg": str(e)})


@app.route('/pswd/delete', methods=['POST'])
def pswd_delete():
    try:
        pswd_id = request.form.get('pswd_id')

        query = f"DELETE FROM pswd WHERE Pswd_id={pswd_id}"
        _, success = run_query(query, query_type="delete")

        if success:
            return jsonify({"success": True, "msg": "Data deleted successfully."})
        else:
            return jsonify({"success": False, "msg": "Data deletion failed."})
    except Exception as e:
        return jsonify({"success": False, "msg": str(e)})


@app.route('/pswd/fetch', methods=['POST'])
def pswd_fetch():
    try:
        pswd_id = request.form.get('pswd_id')

        query = f"SELECT * FROM pswd WHERE Pswd_id={pswd_id}"
        response, success = run_query(query, query_type="select")
        
        if success:
            return jsonify({"success": True, "data": response.get_json()})
        else:
            return jsonify({"success": False, "msg": "No data available."})
    except Exception as e:
        return jsonify({"success": False, "msg": str(e)})


@app.route('/pswd/fetch_all', methods=['GET'])
def pswd_fetch_all():
    try:
        query = "SELECT * FROM pswd"
        response, success = run_query(query, query_type="select")

        if success:
            return jsonify({"success": True, "data": response.get_json()})
        else:
            return jsonify({"success": False, "msg": "No data available."})
    except Exception as e:
        return jsonify({"success": False, "msg": str(e)})
    
if __name__ == "__main__":
    app.run(debug=True)
