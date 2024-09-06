import subprocess


def test_cli():
    assert (
        subprocess.check_output(["foodles", "aa cc bb aa", "2"], text=True)
        == "[('aa', 2), ('bb', 1)]\n"
    )
