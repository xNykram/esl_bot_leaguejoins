import json


class DataApp:
    def __init__(self, username, password, delay):
        self.username = username
        self.password = password
        self.delay = delay
    def readData(self):
            file = open('data.json')
            data = json.loads(file.read())
            for u in data['users']:
                self.username = u['email']
                self.password = u['password']
                self.delay = u['delay']
            return self.username, self.password, self.delay
            file.close()
    def saveData(self):
        data = {}
        data['users'] = []
        data['users'].append({
            'email': self.username,
            'password': self.password,
            'delay': self.delay
        })
        with open('data.json', 'w') as outfile:
            json.dump(data, outfile)
        outfile.close()
