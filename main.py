import requests
from flask import Flask, jsonify, request, send_file
from registrants import RegistrantClass
from participants import ParticipantClass

app = Flask(__name__)
app.config['DEBUG'] = True

zoomUrl = "http://localhost:8080"
# zoomUrl = 'https://api.zoom.us/v2'
registrants = RegistrantClass()
participants = ParticipantClass()


@app.route('/myMeeting', methods=['GET'])
def meeting():
    if 'id' in request.args:
        meetingid = str(request.args['id'])
    else:
        return "Error: No meeting id provided."

    registered = registrants.get_registrant_count(zoomUrl, meetingid)
    participating = participants.get_participant_count(zoomUrl, meetingid)

    return '<h1>My Meeting (<i>' + meetingid + ')</i></h1>' + \
            '<h3>Registered: ' + registered + '</h3>' + \
            '<h3>Participating: ' + participating + '</h3>'


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(port=8000)
