def view(save_data):
    try:
        with open(save_data, "r") as file:
            contents = file.read()
            print(contents)
    except Exception:
        print("No save file currently exists")
    