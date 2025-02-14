from django.test import TestCase
from .models import Member, System

class MemberTestCase(TestCase):
    def setUp(self):
        Member.objects.create(code="M001", full_name="Nguyễn Văn A", birth_date="1990-01-01", active=True)

    def test_member_creation(self):
        member = Member.objects.get(code="M001")
        self.assertEqual(member.full_name, "Nguyễn Văn A")

class SystemTestCase(TestCase):
    def setUp(self):
        System.objects.create(name="Milk System", year=2024, start_date="2024-01-01", end_date="2024-12-31", active=True)

    def test_system_creation(self):
        system = System.objects.get(name="Milk System")
        self.assertTrue(system.active)