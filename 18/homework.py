# TASK 1
class Bot:
    def __init__(self, name):
        self.name = name

    def send_message(self, message):
        print(message)

    def say_name(self):
        print(self.name)


# TASK 2
class TelegramBot(Bot):
    def __init__(self, name, url=None, chat_id=None):
        super().__init__(name)
        self.url = url
        self.chat_id = chat_id

    def set_url(self, url):
        self.url = url

    def set_chat_id(self, chat_id):
        self.chat_id = chat_id

    def send_message(self, message):
        print(f'{self.name} bot says {message} to chat {self.chat_id} using {self.url}')


# TASK 3
class MyStr(str):

    def __init__(self, string):
        self.string = string

    def __str__(self):
        return self.string.upper()


# TASK 4
class User:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name.lower() == other.name.lower()


# TASK 5
def init_func1(self, name):
    self.name = name


def send_message_func1(self, message):
    print(message)


def say_name_func(self):
    print(self.name)


Bot_t = type(
    '',
    (),
    {
        '__init__': init_func1,
        'send_message': send_message_func1,
        'say_name': say_name_func
    }
)


def init_func2(self, name, url=None, chat_id=None):
    self.name = name
    self.url = url
    self.chat_id = chat_id


def set_url_func(self, url):
    self.url = url


def set_chat_id_func(self, chat_id):
    self.chat_id = chat_id


def send_message_func2(self, message):
    print(f'{self.name} bot says {message} to chat {self.chat_id} using {self.url}')


TelegramBot_t = type(
    '',
    (Bot_t,),
    {
        '__init__': init_func2,
        'set_url': set_url_func,
        'set_chat_id': set_chat_id_func,
        'send_message': send_message_func2
    }
)

