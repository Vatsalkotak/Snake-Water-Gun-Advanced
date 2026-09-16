def show_history():
    with open("logs.txt", "r") as f:
        history = f.read()
    print(history)

    return history

