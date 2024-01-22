from calculator.parser import evaluate


def calculate():
    while True:
        try:
            print("Result:", evaluate(input("Insert expression: ")))
        except EOFError:
            print("Message: Shutting down...")
            return
        except Exception as e:
            print(f"Error: {type(e).__name__}, Message: {e}")


def main():
    calculate()


if __name__ == '__main__':
    main()
