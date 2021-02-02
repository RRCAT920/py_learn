def racelamp(content):
    from os import system
    from time import sleep

    while True:
        system('clear')
        print(content)
        sleep(0.2)

        content = content[1:] + content[0]
