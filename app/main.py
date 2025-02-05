import os


def move_file(command):
    new_file = command.split()[-1]
    file = command.split([1])
    if "/" in command:
        new_file_path = command.split()
        new_file_path = "/".join(new_file_path[-1].split("/")[:-1])
        new_file = f"{new_file_path}/{command.split('/')[-1]}"

        try:
            os.makedirs(new_file_path)
        except FileExistsError:
            pass

    with open(file, "r") as f, open(new_file, "w") as ff:
        ff.write(f.read())
    os.remove(file)
