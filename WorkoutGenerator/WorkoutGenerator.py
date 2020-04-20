import random
import json

from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)

@app.route('/')
def exerciseGenerator():
    exercises = ['50 Star Jumps','20 Crunches','30 Squats','50 Press Ups','1 Min Wall Sit','10 Burpees','20 Arm Circles',\
    '20 Squats','30 Star Jumps','15 Crunches','10 Press Ups','2 Min Wall Sit','20 Burpees','40 Star Jumps','25 Burpees',\
    '15 Arm Circles','30 Crunches','15 Press Ups','30 Burpees','15 Squats','30 Sec Arm Circles','2 Min Wall Sit','20 Burpees',\
    '60 Star Jumps','10 Crunches','20 Press Ups'
    ]
    howMany = 8
    exerciselist = []
    for i in range(0,int(howMany)):
        randomnumber = random.randint(0,(len(exercises)-1))
        exerciselist.append(exercises[randomnumber])
    return render_template("default.htm", len = len(exerciselist),exerciselist = exerciselist)

#Run
if __name__ == "__main__":
    app.run(port=80,host='0.0.0.0')