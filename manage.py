import logging
import unittest
import os
from flask_cli import FlaskGroup
from src.main import create_app
from src import blueprint
from flask import Flask, jsonify, make_response

app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')
app.register_blueprint(blueprint)
app.app_context().push()

cli = FlaskGroup(app)


@app.route("/health")
def health_check():
    """try:
        data = ChatsTable.query.all()
        return jsonify({"status": 200})
    except Exception as e:
        # If any check fails, return an error message with a status code of 500"""
    return jsonify({"status": 200})


@app.route("/")
def home():
   
    return jsonify({"massege": "Add /ai/api/v1/agent/ to get the endpoints"})


@cli.command("run")
def run():
    # del os.environ["FLASK_RUN_FROM_CLI"]
    app.run(host="0.0.0.0", port=5000)

@cli.command("db_create_all")
def db_create_all():
    """Initialize the database."""
    # db.create_all()
    return "db created successifull"


@cli.command("test")
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1



if __name__ == '__main__':
    cli()
