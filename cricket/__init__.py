from flask import Flask, request, render_template
import sys

from cricket import cricket

#from cricket.cricket import cricket

def create_app():
    app = Flask(__name__, instance_relative_config=True )
    app.config.from_mapping(
        SECRET_KEY='dev'
    )

    for p in sys.path:
        print(p)

    @app.route('/')
    def index():
        print('Request for index page received')
        return render_template("index.html")

    @app.route('/fixtures', methods=['POST'])
    def cricket_fixtures():

        source_data = request.form.get('source_data')
        fixture_list_type = request.form.get('fixture_list_type')
        args_list = request.form.get('args_list')

        print('Request for fixtures page received with source_data=%s fixture_list_type=%s args_list=%s' % (source_data, fixture_list_type, args_list))
 #       list_of_fixtures = cricket(source_data, fixture_list_type, args_list)
        list_of_fixtures = []

        return render_template("cricket.html", list_of_fixtures=list_of_fixtures)

    return app
