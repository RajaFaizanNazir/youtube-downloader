from datetime import datetime


class Logger:
    class Color:
        RED = 91
        GREEN = 92
        WHITE = 00

    @staticmethod
    def print_colored(message, color):
        timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print("\033[{}m{}\033[{}m" .format(
            color, f"{timestamp} \t {message}", Logger.Color.WHITE))

    @staticmethod
    def info(message, color=Color.WHITE):
        Logger.print_colored(message, color)

    @staticmethod
    def error(message, color=Color.RED):
        Logger.print_colored(message, color)
