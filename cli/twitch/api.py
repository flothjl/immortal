import click
import requests
from .creds import CLIENT_ID, CLIENT_SECRET


class Game:
    def __init__(self, game_id=None, name=None):
        self.game_id = game_id
        self.name = name


class Stream:
    def __init__(self, user_name, game: Game, title: str, viewer_count: int):
        self.user_name = user_name
        self.game = game
        self.title = title
        self.viewer_count = viewer_count


class Twitch:
    def __init__(self):
        self.client_id = CLIENT_ID
        self.client_secret = CLIENT_SECRET

    @property
    def creds(self):
        output = '='*15+'Twitch Credentials'+'='*15
        output += f'\nClient ID: {self.client_id}'
        output += f'\nClient Secret: {self.client_secret}'
        return output

    @property
    def auth(self):
        auth_endpoint = f'https://id.twitch.tv/oauth2/token?client_id={self.client_id}&client_secret={self.client_secret}&grant_type=client_credentials'
        response = requests.post(auth_endpoint)
        if response.status_code != 200:
            raise click.ClickException('Error getting auth token')
        return response.json()['access_token']

    def top_streams(self, auth_token):
        endpoint = f'https://api.twitch.tv/helix/streams'
        games_endpoint = f'https://api.twitch.tv/helix/games'
        headers = {'Client-Id': self.client_id,
                   'Authorization': f'Bearer {auth_token}'}
        response = requests.request('GET', url=endpoint, headers=headers)
        if response.status_code != 200:
            raise click.ClickException(
                'Error requesting top streams. Please try again later')
        data = response.json()['data']
        data = sorted(data, key=lambda x: x['viewer_count'], reverse=True)
        print(data)
        games_endpoint += f'?id={data.pop(0)["game_id"]}'
        games_endpoint += '&id='.join([stream['game_id'] for stream in data])
        response = requests.request('GET', url=games_endpoint, headers=headers)
        if response.status_code != 200:
            raise click.ClickException('Error getting Game Names')
        games = {game['id']: game['name']
                 for game in response.json()['data']}
        streams = list()
        for stream in data[0:10]:
            game = Game(game_id=stream['game_id'],
                        name=games.get(stream['game_id'], 'unknown'))
            stream = Stream(stream['user_name'], game=game,
                            title=stream['title'], viewer_count=stream['viewer_count'])
            streams.append(stream)
        return streams
