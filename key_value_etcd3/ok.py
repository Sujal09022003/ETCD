import etcd3
import unittest

# Initialize etcd client
etcd_client = etcd3.client()

# CRUD Operations
def list_all_keys():
    try:
        raw_data = list(etcd_client.get_all())
        print(f"Raw key-value pairs: {raw_data}")
        keys = etcd_client.get_all()
        return [wanted.key.decode() for (_, wanted) in keys]
    except Exception as e:
        print(f"Error listing keys: {e}")  # Debugging line for exceptions
        return []

def get_value_for_key(key):
    try:
        value, _ = etcd_client.get(key)
        if value is not None:
            return value.decode('utf-8')
        else:
            return "Key not found"
    except Exception as e:
        return f"Error getting value for key '{key}': {e}"

def put_key_value(key, value):
    try:
        etcd_client.put(key, value)
        print(f"Storing Key: {key} with Value: {value}")  # Logging what's being put
        return "Key stored successfully"
    except Exception as e:
        return f"Error putting key-value pair: {e}"
def delete_key(key):
    try:
        return "Key deleted successfully" if was_deleted else "Key not found"
    except Exception as e:
        return f"Error deleting key '{key}': {e}"

# Command-Line Interface

def print_options():
    print("\nAvailable Options:")
    print("1. Put (store a key-value pair)")
    print("2. Get (retrieve value for a key)")
    print("3. Delete (remove a key-value pair)")
    print("4. List (show all keys)")
    print("5. Exit")

def main():
    print("Welcome to the Key-Value Store Interface!")

    while True:
        print_options()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            key = input("Enter the key: ")
            value = input("Enter the value: ")
            print(put_key_value(key, value))

        elif choice == '2':
            key = input("Enter the key to retrieve its value: ")
            print(get_value_for_key(key))

        elif choice == '3':
            key = input("Enter the key to delete: ")
            print(delete_key(key))

        elif choice == '4':
            keys = list_all_keys()
            print("\nAll Keys:")
            for key in keys:
                print(key)

        elif choice == '5':
            print("Exiting the program...")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

# Unit Testing
class TestEtcdKeyValueStore(unittest.TestCase):
    def test_put_get_delete(self):
        put_key_value('test', 'value')
        self.assertEqual(get_value_for_key('test'), 'value')
        delete_key('test')
        self.assertEqual(get_value_for_key('test'), "Key not found")

if __name__ == '__main__':
    main()
