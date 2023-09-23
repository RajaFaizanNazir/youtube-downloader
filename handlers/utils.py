import os


class Utils:
    OUTPUT_FOLDER = './DOWNLOADED'

    @staticmethod
    def make_dir(name=None):
        if name is None:
            name = Utils.OUTPUT_FOLDER
        else:
            name = Utils.OUTPUT_FOLDER + "/" + name.split()[0]
        if not os.path.exists(name):
            os.makedirs(name)
        return name
