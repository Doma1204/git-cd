import subprocess
import os
from click import get_app_dir
import json

class Gitcd():
    def __init__(self):
        self.repo_index = {}

    def get_repo_index(self):
        return self.repo_index

    def get_repo_name_list(self):
        return [k for k in self.repo_index.keys()]

    def get_repo_dir(self, repo_name):
        try:
            return self.repo_index[repo_name]
        except:
            return None

    def read_repo_index(self, fileName=None):
        if fileName is None:
            fileName = os.path.join(get_app_dir("gitcd"), "repo_index.json")

        fileName = os.path.abspath(os.path.expanduser(fileName))
        if not os.path.exists(fileName):
            return False

        with open(fileName, "r") as file:
            self.repo_index = json.load(file)

        return True

    def write_repo_index(self, fileName=None):
        if fileName is None:
            index_dir = get_app_dir("gitcd")
            fileName = os.path.join(index_dir, "repo_index.json")
        else:
            index_dir = os.path.dirname(fileName)
            fileName = os.path.abspath(os.path.expanduser(index_dir))

        if not os.path.exists(index_dir):
            os.makedirs(index_dir)

        with open(fileName, "w") as file:
            json.dump(self.repo_index, file, indent=4)

    def generate_repo_index(self, dir="~"):
        path = os.path.abspath(os.path.expanduser(path))
        if not os.path.exists(path):
            return False

        self.update_repo_index()

        for root, path, _ in os.walk(path):
            if ".git" in path:
                self.repo_index[os.path.basename(root)] = root

        return True

    def update_repo_index(self):
        for repo, path in self.repo_index.items():
            if not os.path.exists(os.path.join(path, ".git")):
                del self.repo_index[repo]
