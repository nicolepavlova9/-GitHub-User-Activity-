import requests


def is_request_valid(request, user) -> bool:
    if request.status_code == 200:
        return True
    else:
        if request.status_code == 404:
            print("Invalid username")
        elif request.status_code == 503:
            print("Service unavailable, please try again later")
        return False


def app_controller():
    username_input = input("Enter your username: ")
    response = requests.get(
        "https://api.github.com/users/" + username_input + "/events"
    )
    if is_request_valid(response, username_input):
        pass
    else:
        app_controller()


if __name__ == "__main__":
    app_controller()
