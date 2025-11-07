from django.test import TestCase
from django.urls import reverse
from core.models import Contato

class ListarContatosTestCase(TestCase):
    def setUp(self):
        self.url = reverse('listar_contatos')

    def test_pagina_listar_contatos_carrega(self):
        """Verifica se a página de listagem abre corretamente."""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Lista de Contatos")

    def test_lista_vazia_mostra_mensagem(self):
        """Verifica se aparece a mensagem quando não há contatos."""
        response = self.client.get(self.url)
        self.assertContains(response, "Nenhum contato cadastrado ainda.")

    def test_listar_contatos_existentes(self):
        """Verifica se contatos cadastrados aparecem na tabela."""
        Contato.objects.create(nome="João Silva", email="joao@example.com", telefone="11999999999")
        Contato.objects.create(nome="Maria Lima", email="maria@example.com", telefone="11888888888")

        response = self.client.get(self.url)

        # Verifica se os dados aparecem na página
        self.assertContains(response, "João Silva")
        self.assertContains(response, "Maria Lima")
        self.assertContains(response, "11999999999")
        self.assertContains(response, "11888888888")

       