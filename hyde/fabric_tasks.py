from fabric.api import local, task
from gntp.notifier import mini


def notify(msg):
    try:
        mini(msg)
    except:
        print(msg)


@task
def clear():
    local("if [ -e 'deploy' ] ; then rm -r deploy ; fi")


@task
def gen():
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
    clear()
    gen()
    serve()


@task
def regen():
    clear()
    gen()


@task
def repub():
    clear()
    gen()
    pub()
