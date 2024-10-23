import factory
from django.contrib.auth.hashers import make_password
from accounts.models import User

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
        django_get_or_create = ("username",)
        skip_postgeneration_save = True  # 'postgeneration 훅이 더 이상 객체를 자동으로 저장하지 않도록 변경될 예정'경고 해결


    username = factory.Sequence(lambda n: f"user{n}")
    email = factory.LazyAttribute(lambda user: f"{user.username}@example.com")

    raw_password = factory.Faker("password")

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        raw_password = kwargs.pop("raw_password", None)
        if raw_password:
            kwargs["password"] = make_password(raw_password)
        return super()._create(model_class, *args, **kwargs)