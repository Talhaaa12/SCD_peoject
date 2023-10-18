# data_collector.py

def get_user_data():
    data = set()
    while True:
        user_input = input("Enter data (or 'exit' to quit): ")
        if user_input.lower() == 'exit':
            break
        data.add(user_input)

    return data

def main():
    data = get_user_data()

    with open('user_data.txt', 'w') as file:
        for item in data:
            file.write(item + '\n')

    print("Data collected and stored in user_data.txt")

if __name__ == "__main__":
    main()
