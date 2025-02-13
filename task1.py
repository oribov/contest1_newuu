def kwargsAcceptFun(**event):
        if not event:
            print("No any information entered")
        else:
            print("Available parameters:")
            for a, b in event.items():
                print(f"{a}: {b}") 


