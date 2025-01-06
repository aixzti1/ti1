import datetime

class Logger:
    def __init__(self):
        self.log_file = 'log_1.txt'
    def log(self, message):
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open(self.log_file, 'a+') as f:
            f.write(f'{now} - {message}\n')
