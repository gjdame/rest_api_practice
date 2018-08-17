#!/usr/bin/python3
'''practice using RESTapi'''
from flask import Flask, render_template
import connexion
# creates app instance using connexion instead Flask
app = connexion.App(__name__, specification_dir='./')

# add swagger api to assist with building endpoints
app.add_api('swagger.yml')

# creates basic url for application
@app.route('/')
def home():
    """responds to localhost:5000/"""
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
