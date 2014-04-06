# Import
import requests
import zipfile
import io


class GitApi():
    """docstring for GitApi"""

    def __init__(self):

        print('but firstly you need to set user to explore:')
        self.user = input("SET USER>")
        self.user_info = self.get_user_git()
        self.repo_list = None

    def get_user_git(self):
        url = 'https://api.github.com/users/{}'.format(self.user)
        self.r = requests.get(url)
        return self.r

    def git_user_info(self):

        print('')
        print('Here is all info for git user {}'.format(self.user))
        return self.user_info.json()

    def get_repos(self):

        get_repos = self.user_info.json()['repos_url']
        r = requests.get(get_repos)
        repos = r.json()
        list_of_repos = [repo["name"] for repo in repos]
        self.repo_list = list_of_repos
        print('')
        print("User {} has the following repos: ".format(self.user))

        for i in range(len(list_of_repos)):
            print('[{}] {}'.format(i + 1, list_of_repos[i]))

        return "These are all of {} repos".format(self.user)

    def get_zip(self, repo_num):

        url = 'https://github.com/{}/{}/archive/master.zip'.format(self.user, self.repo_list[int(repo_num) - 1])

        repo = requests.get(url)

        zfile = io.BytesIO(repo.content)

        read_zfile = zipfile.ZipFile(zfile, 'r')

        for name in read_zfile.namelist():
            print("File: ", name)

        read_zfile.close()

        return "All files in his repo"

    def create_help(self):
        help_menu = [
            '',
            'Here is full list of commands:',
            '',
            '*user_repo',
            '*get_repos',
            '*user_zipfiles <repo ID>',
            '*exit']

        return '\n'.join(help_menu)

    def unknown_command(self):
        false_command = [
            ''
            'you have entered invalid command',
            'type "help" to get all available commands']

        return '\n'.join(false_command)

    def parse_command(self, command):
        return tuple(command.split(" "))

    def is_command(self, command_tuple, command_string):
        return command_tuple[0] == command_string


def create_menu():
    menu = [
        '',
        'Welcome to this brainfuck app',
        'if you are confused, just type "help"']

    return '\n'.join(menu)


def main():

    print(create_menu())
    spy = GitApi()

    while True:

        print('')
        command = spy.parse_command(input("Enter command>"))

        if spy.is_command(command, "help"):
            print(spy.create_help())

        elif spy.is_command(command, "user_repo"):
            print(spy.git_user_info())

        elif spy.is_command(command, "get_repos"):
            print(spy.get_repos())

        elif spy.is_command(command, "user_zipfiles"):
            print(spy.get_zip(command[1]))

        elif spy.is_command(command, "exit"):
            break

        else:
            print(spy.unknown_command())

    # elif is_command(command, "list"):
    #     trigger_list(command)

if __name__ == '__main__':
    main()
