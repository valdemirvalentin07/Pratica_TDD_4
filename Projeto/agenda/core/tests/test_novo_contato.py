from django.test import TestCase
from django.urls import reverse
from core.models import Contato

class NovoContatoTestCase(TestCase):
    def setUp(self):
        self.url = reverse('novo_contato')

    def test_pagina_novo_contato_carrega(self):
        """Verifica se a página de novo contato abre corretamente."""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Novo Contato")

    def test_criar_novo_contato_sucesso(self):
        """Verifica se um novo contato é criado corretamente."""
        dados = {
            'nome': 'Carlos Souza',
            'email': 'carlos@example.com',
            'telefone': '11988888888'
        }
        response = self.client.post(self.url, dados)

        # Verifica se redirecionou após o cadastro
        self.assertRedirects(response, reverse('listar_contatos'))

        # Verifica se o contato foi criado no banco
        contato = Contato.objects.filter(email='carlos@example.com').first()
        self.assertIsNotNone(contato)
        self.assertEqual(contato.nome, 'Carlos Souza')
        self.assertEqual(contato.telefone, '11988888888')

    def test_criar_contato_campos_obrigatorios(self):
        """Verifica se o sistema impede o cadastro com campos vazios."""
        dados = {'nome': '', 'email': '', 'telefone': ''}
        response = self.client.post(self.url, dados)

        # Deve retornar o formulário com erro (status 200 e sem redirecionar)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Este campo é obrigatório")

        # Nenhum contato deve ser criado
        self.assertEqual(Contato.objects.count(), 0)
