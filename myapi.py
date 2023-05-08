from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

todo = {
    1: {
        "Task": "Testing",
        "Description": "Testing description"
    }
}

class Todos(BaseModel):
    Task: str
    Description: str

class UpdateTodos(BaseModel):
    Task: Optional[str] = None
    Description: Optional[str] = None

# Returns a dictionary with a message key set to "Hello World".
@app.get("/")
def index():
    return {"message": "Hello World"}

# Retrieves a single todo item based on the provided ID.
@app.get("/get-todo/{todo_id}")
def get_todo(todo_id: int):
    return todo[todo_id]

# Given a task, return the first todo item that has that task.
@app.get("/get-by-tasks")
def get_todo(Task: str):
    for todo_id in todo:
        if todo[todo_id]["Task"] == Task:
            return todo[todo_id]
    return {"message": "Task not found"}

# Creates a new todo task with the given todo_id and data provided in the request body.
@app.post("/create-todo/{todo_id}")
def create_todo(todo_id: int, todos: Todos):
    if todo_id in todo:
        return {"Error": "Task already exist"}
    
    todo[todo_id] = todos
    return todo[todo_id]

# Updates a specific todo item in the todo list with the provided todo ID. 
# The updated todo item is provided as a parameter in the request body. 
# Returns the updated todo item if it exists in the todo list, otherwise returns an error message.
@app.put("/update-todo/{todo_id}")
def update_todo(todo_id: int, todos: UpdateTodos):
    if todo_id not in todo:
        return {"Error": "Task not found"}
    
    todo[todo_id] = todos
    return todo[todo_id]


# Deletes a task from the todo list.
@app.delete("/delete-task/{todo_id}")
def delete_todo(todo_id: int):
    if todo_id not in todo:
        return {"Error": "Task not found"}
    del todo[todo_id]
    return {"Message": "Deleted success."}