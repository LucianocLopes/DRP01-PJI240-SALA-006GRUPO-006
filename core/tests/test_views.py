from django.test.client import Client
from django.test.testcases import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from core import views

class CoreURLSTestCase(TestCase):

    def setUp(self):
        # CRIA USUARIO
        self.senha_aut = 'Us12345$'
        self.my_admin = User.objects.create_superuser('myuser', 'myemail@email.com.br', self.senha_aut)
        self.client = Client()
    
    def test_initial_not_acess_initial_page(self):
        """_Teste de acesso direto a pagina home sem login gera erro """
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 302)
        

    def test_initial_redirect_login_page(self):
        """_Teste de redirecionamento à pagina de login"""
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        
        
    def test_login_redirect_initial_page(self):
        """_Teste após login redirecionando à pagina principal """
        # faz o Login
        self.client.login(username='myuser', password=self.senha_aut)

        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
    
    
    def test_logout_page(self):
        """_Teste após login, solicitnaod logout, redirecionando à pagina logout """
        # faz o Login
        self.client.login(username='myuser', password=self.senha_aut)

        # Faz o Logout
        self.client.logout()

        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 200)
    
    
    def test_rota_url_utiliza_view_login(self):
        self.assertTemplateUsed('registration/login.html')
    
    
    def test_rota_url_utiliza_view_index(self):
        """Teste se a home da aplicação utiliza a função index da view"""
        self.client.login(username='myuser', password=self.senha_aut)

        self.assertTemplateUsed('core/index.html')
        
            
    def test_rota_url_utiliza_view_logout(self):
        self.client.logout()

        self.assertTemplateUsed('registration/logout.html')
