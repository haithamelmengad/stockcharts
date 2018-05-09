To run the project, install python 3 then on your command line run:

pip install flask
python3 -m venv venv
cd into the project
then run: 
export FLASK_APP=api.py
flask run -p 7777

To test on the terminal: curl http://localhost:7777/?stock=oil
        or open http://localhost:7777/?stock=oil

Otherwise, in your browser go to localhost:7777/
test endpoints at localhost:7777/?stock=coal, localhost:7777/?stock=gas

Technologies used: 
Flask, Jinja2, Plotly

Languages:
Python3, JavaScript, HTML