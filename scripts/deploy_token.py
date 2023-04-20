from ape import project

from .helpers import user


def main():
    user.deploy(project.Token, "Gloriso", "SLB")

