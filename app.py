from flask import Flask, render_template

app = Flask(__name__)


JOBS=[{
  'id':'1',
  'title':"Data Analyst",
  'Location':"Hyderabad, India",
  'Salary':"1000000"
  
},
     {
  'id':'2',
  'title':"Data Scientist",
  'Location':"Hyderabad, India",
  'Salary':"2000000"
  
},{
  'id':'3',
  'title':"Frontend engineer",
  'Location':"Hyderabad, India",
  'Salary':"3000000"
  
},
     {
  'id':'4',
  'title':"Backend Engineer",
  'Location':"Hyderabad, India",
  'Salary':"3000000"
}]

@app.route("/")
def hello_world():
  return render_template('home.html',jobs=JOBS)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
