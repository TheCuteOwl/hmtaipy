import requests
import json
class pyhmtai:
    def __init__(self):
        self.function_name = None
        self.url = None

    def __str__(self):
        return self.url if self.url else ''

    def download(self):
        if self.url:
            response = requests.get(self.url)
            response_content = response.content.decode('utf-8')
            response_json = json.loads(response_content)
            url = response_json['url']
            file_name = 'image.jpg'
            with open(file_name, 'wb') as file:
                file.write(requests.get(url).content)
            print('Downloaded image successfully.')
        else:
            print('No valid URL to download.')

    def sfw(self, arg=None):
        sfw_functions = [
            'wave', 'wink', 'tea', 'bonk', 'punch', 'poke', 'bully', 'pat', 'kiss', 'kick', 'blush',
            'feed', 'smug', 'hug', 'cuddle', 'cry', 'slap', 'five', 'glomp', 'happy', 'hold', 'nom',
            'smile', 'throw', 'lick', 'bite', 'dance', 'boop', 'sleep', 'like', 'kill', 'nosebleed',
            'threaten', 'tickle', 'depression', 'wolf_arts', 'jahy_arts', 'neko_arts', 'coffee_arts',
            'wallpaper', 'mobileWallpaper'
        ]
        if arg is not None:
            if arg in sfw_functions:
                self.function_name = arg
                self.url = f'https://hmtai.hatsunia.cfd/sfw/{arg}'
            else:
                print('Invalid input, go check the documentation for any help...')
        return self

    def nsfw(self, arg=None):
        nsfw_functions = [
            'anal', 'ass', 'bdsm', 'cum', 'classic', 'creampie', 'manga', 'femdom', 'hentai', 'incest',
            'masturbation', 'public', 'ero', 'orgy', 'elves', 'yuri', 'pantsu', 'glasses', 'cuckold',
            'blowjob', 'boobjob', 'footjob', 'handjob', 'boobs', 'thighs', 'pussy', 'ahegao', 'uniform',
            'gangbang', 'tentacles', 'gif', 'nsfwNeko', 'nsfwMobileWallpaper', 'zettaiRyouiki'
        ]
        if arg is not None:
            if arg in nsfw_functions:
                self.function_name = arg
                self.url = f'https://hmtai.hatsunia.cfd/nsfw/{arg}'
            else:
                print('Invalid input, go check the documentation for any help...')
        return self
