from flask import Flask, render_template
from db import getTaskList
app = Flask(__name__)

#tasklist = [["Walk Dog", True], ["Wash Dishes", False], ["Take Out Trash", True]]
tasklist = getTaskList()

@app.route("/")
def home():
    return render_template("tasklist.html", TaskList=tasklist)


app.run()
