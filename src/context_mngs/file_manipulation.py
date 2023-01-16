import os


class CreateFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self):
        self.file = open(self.filename, "w")
        return self.file

    def __exit__(self):
        if self.file:
            self.file.close()


class ChangeDir:
    def __init__(self, dir: str) -> None:
        self.dir = dir

    def __enter__(self) -> bool:
        os.chdir(self.dir)
        pass

    def __exit__(self, *args, **kwargs) -> None:
        dir_to_main = len(self.dir.split("/"))
        where_to = ".."

        if dir_to_main == 1:

            os.chdir(where_to)

        elif dir_to_main > 1:

            for i in range(dir_to_main):
                where_to += "/.."

            os.chdir(where_to)
