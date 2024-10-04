import base64
import pytest

from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.response import Response
from rest_framework.test import APIClient

from accounts.tests.factories import UserFactory
from todo.models import Todo
from todo.tests.factories import TodoFactory, AlarmFactory


def create_user(raw_password):
    return UserFactory(raw_password=raw_password)


def get_api_client_with_basic_auth(user, raw_password):
    base64_data = f"{user.username}:{raw_password}".encode()
    authorization_header = base64.b64encode(base64_data).decode()

    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION=f"Basic {authorization_header}")
    return client


@pytest.fixture
def unauthenticated_api_client():
    return APIClient()


@pytest.fixture
def api_client_with_new_user_basic_auth(faker):
    raw_password = faker.password()
    user = create_user(raw_password)
    api_client = get_api_client_with_basic_auth(user, raw_password)
    return api_client


@pytest.fixture
def new_user():
    return create_user()


@pytest.fixture
def new_todo():
    return TodoFactory()

@pytest.mark.describe("투두 조회 API 테스트")
class TestTodoRetrieveGroup:
    @pytest.mark.it(
        "투두 목록 조회: 비인증 조회가 가능해야하며, 생성한 투두의 갯수만큼 응답"
    )
    @pytest.mark.django_db
    def test_todo_list(self, unauthenticated_api_client):
        todo_list = [TodoFactory() for _ in range(10)]
        
        url = reverse("todo:todo-api-v1:todo-list")
        response: Response = unauthenticated_api_client.get(url)
        assert status.HTTP_200_OK == response.status_code
        assert len(todo_list) == len(response.data)


@pytest.mark.describe("투두 생성 API 테스트")
class TestTodoCreateGroup:
    @pytest.mark.it(
        "투두 생성: 인증되지 않은 사용자는 투두 생성 불가"
    )
    @pytest.mark.django_db
    def test_unauthenticated_user_cannot_create_todo(self, unauthenticated_api_client):
        url = reverse("todo:todo-api-v1:todo-list")
        response = unauthenticated_api_client.post(url, data={})
        assert status.HTTP_403_FORBIDDEN == response.status_code

    @pytest.mark.it(
        "투두 생성: 인증된 사용자는 투두 생성 가능"
    )
    @pytest.mark.django_db
    def test_authenticated_user_can_create_todo(self, api_client_with_new_user_basic_auth, faker):
        url = reverse("todo:todo-api-v1:todo-list")
        data = {"content":faker.paragraph(),
            "deadline_data": faker.date_between(start_date="today", end_date="+5y"), 
                "is_finished":False}
        response = api_client_with_new_user_basic_auth.post(url, data=data)
        assert status.HTTP_201_CREATED == response.status_code
        assert data['content'] == response.data['content']
        assert data['deadline_data'].strftime("%Y-%m-%dT%H:%M:%S") == response.data['deadline_data']
        assert data['is_finished'] == response.data['is_finished']


@pytest.mark.describe("투두 수정 API 테스트")
class TestTodoUpdateGroup:
    @pytest.mark.it(
        "투두 수정: 작성자가 아닌 유저가 수정 요청하면 거부"
    )
    @pytest.mark.django_db
    def test_non_author_cannot_update_todo(self, new_todo, api_client_with_new_user_basic_auth):
        url = reverse("todo:todo-api-v1:todo-detail", args=[new_todo.pk])
        response = api_client_with_new_user_basic_auth.patch(url, data={})
        assert status.HTTP_403_FORBIDDEN == response.status_code

    @pytest.mark.it(
        "투두 수정: 작성자가 수정 요청하면 성공 "
    )
    @pytest.mark.django_db
    def test_author_can_uodate_todo(self, faker):
        raw_password=faker.password()
        author = create_user(raw_password=raw_password)
        created_todo = TodoFactory(author=author)

        url = reverse("todo:todo-api-v1:todo-detail", args=[created_todo.pk])
        api_client = get_api_client_with_basic_auth(author, raw_password)
        data = {'content': faker.paragraph()}
        
        response=api_client.patch(url, data=data)
        assert status.HTTP_200_OK == response.status_code
        assert data['content'] == response.data['content']


@pytest.mark.describe("투두 삭제 API 테스트")
class TestTodoDeleteGroup:
    @pytest.mark.it(
    "투두 삭저: 작성자가 아닌 유저가 삭제 요청하면 거부"
    )
    @pytest.mark.django_db
    def test_non_author_cannot_delete_todo(self, new_todo, api_client_with_new_user_basic_auth):
        url = reverse("todo:todo-api-v1:todo-detail", args=[new_todo.pk])
        response = api_client_with_new_user_basic_auth.delete(url, data={})
        assert status.HTTP_403_FORBIDDEN == response.status_code

    @pytest.mark.it(
    "투두 삭저: 작성자가 삭제 요청하면 성공"
    )
    @pytest.mark.django_db
    def test_author_can_delete_todo(self, faker):
        raw_password = faker.password()
        author = create_user(raw_password=raw_password)
        created_todo = TodoFactory(author=author)

        url = reverse("todo:todo-api-v1:todo-detail", args=[created_todo.pk])
        api_client = get_api_client_with_basic_auth(author, raw_password)
        response: Response = api_client.delete(url)
        assert status.HTTP_204_NO_CONTENT == response.status_code

        with pytest.raises(ObjectDoesNotExist):
            Todo.objects.get(pk=created_todo.pk)


@pytest.mark.describe("투두 응원 API 테스트")
class TestToggleSupportGroup:
    @pytest.mark.it("투두 응원: 인증되지 않은 사용자는 응원 불가")
    @pytest.mark.django_db
    def test_unauthenticated_user_cannot_support_todo(self, unauthenticated_api_client):
        new_todo = TodoFactory()
        
        url = reverse("todo:support", args=[new_todo.pk])
        response = unauthenticated_api_client.post(url, data={})
        assert status.HTTP_403_FORBIDDEN == response.status_code

    @pytest.mark.it("투두 응원: 인증된 사용자는 응원 가능 / 처음에는 생성, 이후 토글")
    @pytest.mark.django_db
    def test_authenticated_user_can_support_todo(self, faker):
        raw_password = faker.password()
        send_user = create_user(raw_password=raw_password)
        created_todo = TodoFactory()

        url = reverse("todo:support", args=[created_todo.pk])
        api_client = get_api_client_with_basic_auth(send_user, raw_password)
        response = api_client.post(url, data={})
        assert status.HTTP_201_CREATED == response.status_code
        assert response.data['detail'] == "SupportTodo가 생성되었습니다."

        response = api_client.post(url, data={})
        assert status.HTTP_200_OK == response.status_code
        assert response.data['detail'] == "지원 상태가 False로 업데이트되었습니다."

        response = api_client.post(url, data={})
        assert status.HTTP_200_OK == response.status_code
        assert response.data['detail'] == "지원 상태가 True로 업데이트되었습니다."


@pytest.mark.describe("알림 AIP 테스트")
class TestAlarmGroup:
    @pytest.mark.it("알림: 인증되지 않은 사용자가 알림 목록 조회 불가")
    @pytest.mark.django_db
    def test_unauthenticated_user_cannot_alarm_list(self, unauthenticated_api_client):
        url = reverse("todo:alarm-list")
        response = unauthenticated_api_client.get(url, data={})
        assert status.HTTP_403_FORBIDDEN == response.status_code


    @pytest.mark.it("알림: 인증된 사용자 알림 목록 조회 가능")
    @pytest.mark.django_db
    def test_authenticated_user_can_alarm_list(self, api_client_with_new_user_basic_auth):
        url = reverse("todo:alarm-list")

        response = api_client_with_new_user_basic_auth.get(url)
        assert status.HTTP_200_OK == response.status_code
        assert isinstance(response.data, list)

    @pytest.mark.it("알림: 다른 사람의 알림 읽음 처리 불가")
    @pytest.mark.django_db
    def test_other_user_alarm_cannot_patch(self, api_client_with_new_user_basic_auth):
        alarm = AlarmFactory()
        url = reverse("todo:alarm-read", args=[alarm.pk])
        
        response = api_client_with_new_user_basic_auth.post(url, data={})

        assert status.HTTP_404_NOT_FOUND == response.status_code

    @pytest.mark.it("알림: 인증된 사용자가 알림 읽음 처리 가능")
    @pytest.mark.django_db
    def test_authenticated_user_can_patch_alarm(self, faker):
        raw_password = faker.password()
        receiver_user = create_user(raw_password=raw_password)
        alarm = AlarmFactory(receiver=receiver_user)

        url = reverse("todo:alarm-read", args=[alarm.pk])
        api_client = get_api_client_with_basic_auth(receiver_user, raw_password)

        response = api_client.post(url, data={})
        assert status.HTTP_200_OK == response.status_code
        assert response.data['detail'] == f"{alarm.content}를 읽음 처리"