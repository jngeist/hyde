from fabric.api import local, task
from gntp.notifier import mini


def notify(msg):
    try:
        mini(msg)
    except:
        print(msg)


@task
def gen(r=False):
    if r:
        local("hyde gen -r")
    else:
        local("hyde gen")
    notify("Generation complete.")


@task
def serve():
    notify("Launching server.")
    local("hyde serve")


@task
def pub():
    gen()
    notify("Publishing.")
    local("hyde publish")
    notify("Publication complete.")


@task
def reserve():
    gen(r=True)
    serve()


@task
def regen():
    gen(r=True)


@task
def repub():
    gen(r=True)
    pub()
