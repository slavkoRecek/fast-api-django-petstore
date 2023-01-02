from django.contrib.auth.hashers import make_password

from application.users.models import User
from application.users.payloads import UserIn, UserOut


class UserService:
    def register_user(self, user: UserIn) -> UserOut:
        self._validate_password(user.password, user.repeated_password)
        self._validate_email_uniqueness(user.email)
        hashed_password = self._hash_password(user.password)
        user = User.objects.create(
            first_name=user.first_name,
            last_name=user.last_name,
            email=user.email,
            password=hashed_password,
            phone=user.phone,
            is_active=False
        )
        return UserOut.from_model(user)

    @staticmethod
    def _validate_password(password, repeated_password):
        if password != repeated_password:
            raise ValueError("Passwords don't match")
            # raise HTTPException(status_code=422, detail="Passwords don't match")

    @staticmethod
    def _validate_email_uniqueness(email):
        if User.objects.filter(email=email).exists():
            raise ValueError("Email already exists")

    @staticmethod
    def _hash_password(password):
        return make_password(password)


user_service: UserService = UserService()
