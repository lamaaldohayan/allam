from quart import Quart, request, jsonify, send_file
import requests
from sync import allam_storyteller

app = Quart(__name__)

@app.route('/')
async def home():
    return "Welcome to the Chat Agent!"

@app.route('/process_json', methods=['POST'])
async def process_json():
    
    data = await request.get_json() 
    res = await allam_storyteller(data["type"],data["subType"],data["story"],data["name"],data["age"])
    
    return res

if __name__ == '__main__':
    app.run(debug=False)
