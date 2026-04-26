from flask import Flask, jsonify, request
import uuid 
from werkzeug.exceptions import NotFound, BadRequest, Conflict, UnprocessableEntity

#===================Si tu veux travailler entièrement avec uuid changer tout ce qui est en rapport.
str(uuid.uuid4())
app = Flask(__name__)
@app.route("/tasks")
def home():
    return tasks



tasks=[]
task1 = { 
    "id": str(uuid.uuid4()),
    "title": "Learn Flask",
    "completed": False
    }
task2={
    "id": str(uuid.uuid4()),
    "title": "Build API",
    "completed": False
    }
task3={
    "id": str(uuid.uuid4()),
    "title": "Test with Postman",
    "completed": True
    }
        
tasks.append(task1)
tasks.append(task2)
tasks.append(task3)


@app.errorhandler(NotFound)
def handle_type_error(e):
    return jsonify({
        "error": str(e)
    }), 404

@app.errorhandler(BadRequest)
def handle_type_error(e):
    return jsonify({
        "error": str(e)
    }), 400
    
@app.errorhandler(UnprocessableEntity)
def handle_type_error(e):
    return jsonify({
        "error": str(e)
    }), 422
    
@app.errorhandler(ValueError)
def handle_type_error(e):
    return jsonify({
        "error": str(e)
    }), 422    

@app.route("/tasks/<num_id>")
def id(num_id):
   
    for u in tasks:
      if num_id != u["id"]:
       raise ValueError("dude error Task not found")
      return  jsonify(u)

@app.route("/tasks", methods=["POST"])
def create_task():
   

    data = request.get_json(silent=True)

    # if not data:
    #     ValueError("Title must be a string")
        
    if not isinstance(data, str):
        raise BadRequest("dude Title must be a string")    

    if "title" not in data:
        raise ValueError("error you need title")

    new_task = {
        "id": str(uuid.uuid4()),
        "title": data["title"],
        "completed": False
    }

    tasks.append(new_task)
    

    return jsonify(new_task), 201
    

@app.route("/tasks/<id>", methods=["PUT"])
def put_task(id):
 
    data = request.get_json() 
    if not isinstance(data, str):
        raise BadRequest("Title must be a string") 

    if "title" not in data:
       raise ValueError("error you need title")   
    
    
    for task in tasks:
        if id == task["id"]:
           task["title"]=data["title"]
           if "completed" in data:
                task["completed"]=data["completed"]  
        else:
            raise ValueError("error Task not found")
        return jsonify(task), 201
   
   
@app.route("/tasks/<id>", methods=["PATCH"])
def patch_task(id):
 
    data = request.get_json() 
    if not data:
        raise BadRequest("JSON body is required")

    if "completed" not in data:
        raise BadRequest("You need to provide 'completed'")

    if not isinstance(data["completed"], bool):
        raise BadRequest("Completed must be a boolean") 
    
    
    for task in tasks:
        if id == task["id"]:
           task["completed"]=data["completed"] 
        else:
            raise ValueError("error Task not found")
        return jsonify(task), 201

    
@app.route("/tasks/<id>", methods=["DELETE"])
def del_task(id):    
    for task in tasks:
        if id != task["id"]:
            raise ValueError("error Task not found")
            
    tasks.remove(task)
    return jsonify(task), 200

if __name__ == "__main__":
    app.run(debug=True)