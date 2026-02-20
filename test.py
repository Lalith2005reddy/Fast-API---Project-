import json

def load_data():
    with open('patients.json', 'r') as f:
        data = json.load(f)
    return data

def main():
    data = load_data()
    print(data)

if __name__ == "__main__":
    main()