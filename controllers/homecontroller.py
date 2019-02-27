from root import application

@application.route("/", methods=["GET"])
def api_home():
    return "Welcome to Questionaire API"