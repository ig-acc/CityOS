def run():
    import utils
    while (utils.System.isRun):
        inp = input(">> ")
        if (inp.lower() == "quit"):
            utils.System.isRun = False
