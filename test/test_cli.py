from click.testing import CliRunner
from gitcd.cli_interface import cli
import pytest
from unittest import mock
import os

test_index = {}
test_repo_name = ["Testing 1", "Testing 2", "Testing 3", "Testing 4"]
test_index_path = {
    "Testing 1": os.path.join("A", "A", "Testing 1"),
    "Testing 2": os.path.join("A", "B", "Testing 2"),
    "Testing 3": os.path.join("B","Testing 3"),
    "Testing 4": "Testing 4"
}

path = None
@pytest.fixture(scope="session", autouse=True)
def setup(tmpdir_factory):
    global path
    path = tmpdir_factory.mktemp("cli")
    print("tmpdir: %s" % path)

def os_system():
    pass

class Test_CLI():
    @classmethod
    def setup_class(cls):
        for key, item in test_index_path.items():
            full_path = os.path.join(path, item)
            os.makedirs(os.path.join(full_path, ".git"))
            test_index[key] = full_path

    @mock.patch("gitcd.Gitcd.generate_repo_index", return_value=True)
    def test_generate(self, _):
        runner = CliRunner()
        result = runner.invoke(cli, ["-i"])
        assert result.exit_code == 0
        assert "Start indexing" in result.output
        assert "Finish indexing" in result.output

    @mock.patch("os.system")
    def test_cd(self, _):
        runner = CliRunner()
        result = runner.invoke(cli, ["gitcd"])
        assert result.exit_code == 0