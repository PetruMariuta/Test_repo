from flask import Flask,send_file,render_template,redirect,jsonify
import requests,json
from faker import Faker
import time
from dotenv import load_dotenv
import os


print("here")

main_app = Flask(__name__, template_folder='templates')
@main_app.route('/')
def app():
    print("here1")
    load_dotenv()
    api_key=os.environ.get("api_key")
    print("here2")  
    faker = Faker()  
    ip_addr = faker.ipv4() 


    url = f'https://api.openweathermap.org/data/2.5/weather?q=Bordeaux&appid={api_key}&units=metric' #you can add any desired city instead of Bucharest and the api will provide the information
    data = json.loads(requests.get(url).content) 
    print((data))
    
    weather = data["weather"][0]["main"]

    print(weather)
    hour = time.strftime("%H:%M")
    print(hour)

    r = requests.post(
        "https://api.deepai.org/api/text2img",
        data={ 'text': f'Bordeaux wine field at {hour} weather is  {weather}',},
        #data={ 'text': f'Wide Sunflower Field in daylight with clear sky and 2 main sunflowers close-up',},
        headers={'api-key': 'quickstart-QUdJIGlzIGNvbWluZy4uLi4K',
                  'X-Forwarded-For': ip_addr}
    )
    link_url = str(r.json()['output_url'])
    print(link_url) 
   
    print(jsonify({'status': 'ok'}),"common")
    
    return render_template('front.html', link_url=link_url, hour = hour, weather = weather)


@main_app.route('/liveness')
def liveness():
   return(jsonify({'status': 'ok'}))
       



if __name__ == "__main__":
    #main_app.run()
    main_app.run(port=8000,host="0.0.0.0")
    #Flask.run(main_app, port=80, host="0.0.0.0")

