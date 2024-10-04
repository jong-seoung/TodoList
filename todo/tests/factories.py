import factory
from accounts.tests.factories import UserFactory, ProfileFactory
from todo.models import Todo, SupportTodo, Alarm


class TodoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Todo

    author = factory.SubFactory(UserFactory)
    content = factory.Faker("paragraph")
    deadline_data = factory.Faker("date_between", start_date="today", end_date="+5y")
    is_finished=False


class SupportTodoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = SupportTodo

    send_user = factory.SubFactory(UserFactory)
    todo = factory.SubFactory(TodoFactory)


class AlarmFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Alarm
        
    receiver = factory.SubFactory(UserFactory)
    sender = factory.SubFactory(UserFactory)
    type = factory.Iterator(['follow','support'])
    content = factory.LazyAttribute(lambda alarm: f"{alarm.sender.username}님이 {alarm.receiver.username}님을 {alarm.type}하였습니다.")
