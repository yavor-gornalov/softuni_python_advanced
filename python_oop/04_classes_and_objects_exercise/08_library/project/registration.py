from project.user import User
from project.library import Library


class Registration:
    def add_user(self, user: User, library: Library):
        if user in library.user_records:
            return f"User with id = {user.user_id} already registered in the library!"
        library.user_records.append(user)

    def remove_user(self, user: User, library: Library):
        if user not in library.user_records:
            return "We could not find such user to remove!"
        library.user_records.remove(user)

    def change_username(self, user_id: int, new_username: str, library: Library):
        current_user = None
        for user in library.user_records:
            if user.user_id == user_id:
                current_user = user
                break

        if not current_user:
            return f"There is no user with id = {user_id}!"
        if current_user.username == new_username:
            return f"Please check again the provided username - it should be different than the username used so far!"

        if current_user.username in library.rented_books:
            library.rented_books[new_username] = library.rented_books[current_user.username]
            del library.rented_books[current_user.username]
        current_user.username = new_username
        return f"Username successfully changed to: {new_username} for user id: {user_id}"
