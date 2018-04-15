def message_with_welcome(str):
    def add_welcome():
        return 'Welcome to '
    return add_welcome()+str


def site(site_name):
    return site_name

print(message_with_welcome(site('Geeks for geeks')))