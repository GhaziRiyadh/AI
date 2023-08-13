import json
from channels.generic.websocket import WebsocketConsumer


class VideoConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, video_data):
        video_data_json = json.loads(video_data)
        message = video_data_json['message']

        self.send(video_data=json.dumps({
            'message': message
        }))
