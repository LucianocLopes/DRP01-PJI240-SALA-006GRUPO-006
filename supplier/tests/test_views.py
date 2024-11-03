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
    
    
    def test_supplier_not_acess_page_index(self):
        """_Teste de acesso direto a pagina home sem login gera erro """
        
        response = self.client.get(reverse('supplier-index'))
        self.assertEqual(response.status_code, 302)
    
    
    def test_supplier_not_login_redirect_login_page(self):
        """_Teste de redirecionamento à pagina de login"""
        self.client.get(reverse('supplier-index'))
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
    
    
    def test_supplier_page_after_login_home(self):
        """_Teste de redirecionamento à pagina de login"""
        # faz o Login
        self.client.login(username='myuser', password=self.senha_aut)
        
        self.client.get(reverse('supplier-index'))
        
        response = self.client.get(reverse('supplier-index'))
        self.assertEqual(response.status_code, 200)
    