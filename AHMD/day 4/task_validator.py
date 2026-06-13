from pydantic import BaseModel, ValidationError
class Task(BaseModel):
    title: str
    priority: str = "low"
    completed: bool = False
task1 = Task(title="Complete the project")
print("Valid task")
print(task1)
print("Invalid task")
try:
    task2 = Task(title="ahmd", completed="yes")
except ValidationError as e:
    print("Validation error:")
    print(e)