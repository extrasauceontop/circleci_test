from main import add_stuff

def test_add():
    assert add_stuff(2, 3) == 5
    assert add_stuff(3, 3) == 5
    print("worked")

if __name__ == "__main__":
    test_add()

