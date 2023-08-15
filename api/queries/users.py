class UsersQueries:
    users = []

    def get_users(self):
        return self.users

    def create_user(self, user):
        dict_user = dict(user)
        self.users.append(dict_user)

    def get_user_by_id(self, user_id):
        for user in self.users:
            if user["id"] == user_id:
                return user
        return None

    def update_user(self, updated_user, user_id):
        for user in self.users:
            if user["id"] == user_id:
                user.update(updated_user)
                return user
        return None

    def delete_user(self, user_id):
        for user in self.users:
            if user["id"] == user_id:
                self.users.remove(user)
                return True
        return False
