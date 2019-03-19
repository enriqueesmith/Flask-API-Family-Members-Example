import os
from flask import Flask, jsonify
  
app = Flask(__name__)

person1= {
    "id": 1,
    "name": "John",
    "lastname": "Doe",
    "age": 33,
    "gender": "Male",
    "lucky_numbers": [7, 13, 22]
}
person2= {
    "id": 2,
    "name": "Jane",
    "lastname": "Doe",
    "age": 35,
    "gender": "Female",
    "lucky_numbers": [10, 14, 3],
}
person3= {
    "id": 3,
    "name": "Jimmy",
    "lastname": "Doe",
    "age": 5,
    "gender": "Male",
    "lucky_numbers": [1]
} 

family={
    "lastname": "Doe",
    "members": [person1, person2, person3]
}

all_lucky_numbers = person1["lucky_numbers"]+person2["lucky_numbers"]+person3["lucky_numbers"]


sum_lucky_numbers = sum(person1["lucky_numbers"]+person2["lucky_numbers"]+person3["lucky_numbers"])


@app.route('/members')
def hello():
    return jsonify({
        "status_code": 200,
        "data":{
            "members": family["members"],
            "family_name": "Doe",
            "lucky_numbers": all_lucky_numbers,
            "sum_of_lucky":sum_lucky_numbers
        }
    })
  
@app.route('/members/<int:m_id>')
def get_member(m_id):
  if m_id > 0:
    member = {}
    for m in family["members"]:
      if m["id"] == m_id:
        member = m
    
    if "name" in member:
      return jsonify({"status_code": 200, "data": member})
    else:
      response = jsonify({"error": 400, "message":"No member found" })
      response.status_code = 400
      return response
  
  
  
app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))