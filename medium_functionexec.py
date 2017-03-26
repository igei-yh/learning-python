
while(True):
    print("please input 1 line program or exit!")
    text = raw_input()
    if text == "exit":
        break
    exec(text)
    print("")
