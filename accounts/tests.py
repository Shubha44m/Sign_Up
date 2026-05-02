from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

class AuthTests(TestCase):
    def setUp(self):
        # Setup a test client
        self.client = Client()
        # Create a user for login tests
        self.test_user = User.objects.create_user(
            username='testuser', 
            email='test@example.com', 
            password='testpassword123'
        )

    def test_signup_page_status_code(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signup.html')

    def test_signup_successful(self):
        response = self.client.post(reverse('signup'), {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'newpassword123',
            'confirm_password': 'newpassword123'
        })
        # After successful signup, should redirect to login page
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login'))
        # Check if user was actually created
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_signup_password_mismatch(self):
        response = self.client.post(reverse('signup'), {
            'username': 'baduser',
            'email': 'bad@example.com',
            'password': 'password123',
            'confirm_password': 'differentpassword'
        })
        # Should render signup page again with an error
        self.assertEqual(response.status_code, 200)
        self.assertFormError(response.context['form'], 'confirm_password', 'Passwords do not match.')
        # User should not be created
        self.assertFalse(User.objects.filter(username='baduser').exists())

    def test_login_page_status_code(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_login_successful(self):
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'testpassword123'
        })
        # Successful login redirects to home
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))
        
        # Check if session has user ID (meaning user is logged in)
        self.assertTrue('_auth_user_id' in self.client.session)

    def test_login_invalid_credentials(self):
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'wrongpassword'
        })
        # Should stay on login page and show error
        self.assertEqual(response.status_code, 200)
        
        # Check if session is NOT authenticated
        self.assertFalse('_auth_user_id' in self.client.session)

    def test_logout_functionality(self):
        # Login first
        self.client.login(username='testuser', password='testpassword123')
        
        # Then test logout
        response = self.client.get(reverse('logout'))
        # Should redirect to login page
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login'))
        
        # Session should not have auth user anymore
        self.assertFalse('_auth_user_id' in self.client.session)

    def test_home_page_requires_login(self):
        # Accessing home without logging in
        response = self.client.get(reverse('home'))
        # Should redirect to login with 'next' parameter
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/login/?next=/')

    def test_home_page_accessible_if_logged_in(self):
        # Login
        self.client.login(username='testuser', password='testpassword123')
        # Access home
        response = self.client.get(reverse('home'))
        # Should load correctly
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        self.assertContains(response, 'testuser')
