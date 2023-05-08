from fastapi import FastAPI

app = FastAPI()

todo = {
    1: {
        "Task": "Testing"
    }
}


@app.get("/")
def index():
    return {"message": "Hello World"}


@app.get("/get-todo/{todo_id}")
def get_todo(todo_id: int):
    return todo[todo_id]

@app.get("/get-by-tasks")
def get_todo(Task: str):
    for todo_id in todo:
        if todo[todo_id]["Task"] == Task:
            return todo[todo_id]
    return {"message": "Task not found"}

@app.post("/create-task/{todo_id}")
def create_task(todo_id: int, Task: str):
    if todo_id in todo:
        return {"Error": "ID already exists"}
    
    todo["Task"] = Task
    return todo[todo_id]