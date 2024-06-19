from task_manager.statuses.models import Status
from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.messages import get_messages
from django.utils.translation import gettext as _


class StatusesTestCase(TestCase):
    fixtures = ["tests/fixtures/test_users.json",
                "tests/fixtures/test_statuses.json"]

    def setUp(self):
        self.user = User.objects.get(username='me')
        self.c = Client()
        self.c.force_login(self.user)
        self.statuses_data = {
            'name': 'new_test_status',
        }

    # list

    def test_statuses_list_response_200(self):
        response = self.c.get(reverse('statuses:statuses-list'))
        self.assertEqual(response.status_code, 200)

    def test_statuses_list_content(self):
        response = self.c.get(reverse('statuses:statuses-list'))
        self.assertContains(response, 'ID')
        self.assertContains(response, _('Name'))
        self.assertContains(response, _('Created at'))
        self.assertContains(response, _('Statuses'))
        self.assertContains(response, _('New status'))

    # create

    def test_create_status_response_200(self):
        response = self.c.post(reverse('statuses:statuses-create'),
                               self.statuses_data, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_check_create_status_content(self):
        response = self.c.get(reverse('statuses:statuses-create'))
        self.assertContains(response, _('Name'))
        self.assertContains(response, _('Create'))
        self.assertRegex(
            response.content.decode('utf-8'),
            _(r'\bCreate status\b')
        )

    def test_created_status_add_to_db(self):
        old_count = Status.objects.count()
        self.c.post(reverse('statuses:statuses-create'),
                    self.statuses_data, follow=True)
        new_count = Status.objects.count()
        self.assertEqual(old_count + 1, new_count)

    def test_check_for_not_create_status_with_same_name(self):
        self.c.post(reverse('statuses:statuses-create'),
                    self.statuses_data, follow=True)
        statuses_count = Status.objects.count()
        self.c.post(reverse('statuses:statuses-create'),
                    self.statuses_data, follow=True)
        new_statuses_count = Status.objects.count()
        self.assertEqual(statuses_count, new_statuses_count)

    def test_check_message_if_same_status_exist(self):
        self.statuses_data = {'name': 'new'}
        response = self.c.post(reverse('statuses:statuses-create'),
                               self.statuses_data, follow=True)
        message = _('Status with this Name already exists.')
        self.assertContains(response, message)

    def test_create_status_with_correct_data(self):
        self.c.post(reverse('statuses:statuses-create'),
                    self.statuses_data, follow=True)
        status = Status.objects.filter(
            name=self.statuses_data['name']).first()
        self.assertEqual(status.name, self.statuses_data['name'])

    def test_success_redirect_when_create_status(self):
        response = self.c.post(reverse('statuses:statuses-create'),
                               self.statuses_data, follow=True)
        self.assertRedirects(response, reverse('statuses:statuses-list'))

    def test_success_message_when_create_status(self):
        response = self.c.post(reverse('statuses:statuses-create'),
                               self.statuses_data, follow=True)
        messages = list(get_messages(response.wsgi_request))
        self.assertGreater(len(messages), 0)
        self.assertEqual(str(messages[0]), _('Status created successfully'))

    def test_can_not_create_status_with_empty_name(self):
        self.statuses_data = {'name': ' '}
        response = self.c.post(reverse('statuses:statuses-create'),
                               self.statuses_data, follow=True)
        self.assertFalse(Status.objects.filter(name=" ").exists())
        message = _('This field is required.')
        self.assertContains(response, message)

    # update

    def test_update_status_response_200(self):
        status = Status.objects.get(name="new")
        response = self.c.post(
            reverse('statuses:statuses-update', args=[status.id]),
            self.statuses_data, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_check_update_status_content(self):
        status = Status.objects.get(name="new")
        response = self.c.get(
            reverse('statuses:statuses-update', args=[status.id]),
            self.statuses_data, follow=True)
        self.assertContains(response, _('Name'))
        self.assertContains(response, _('Edit'))
        self.assertContains(response, _('new'))
        self.assertRegex(
            response.content.decode('utf-8'),
            _(r'\bEdit status\b')
        )

    def test_update_status(self):
        user = User.objects.get(username="he")
        self.c.force_login(user)
        status = Status.objects.get(name="new")
        response = self.c.post(
            reverse('statuses:statuses-update', args=[status.id]),
            self.statuses_data,
            follow=True)
        self.assertEqual(response.status_code, 200)
        status.refresh_from_db()
        self.assertEqual(status.name, self.statuses_data['name'])

    # delete

    def test_delete_status(self):
        user = User.objects.get(username="he")
        self.c.force_login(user)
        status = Status.objects.get(name="new")
        self.c.post(reverse('statuses:statuses-delete',
                            args=[status.id]), follow=True)
        self.assertFalse(Status.objects.filter(name="new").exists())
