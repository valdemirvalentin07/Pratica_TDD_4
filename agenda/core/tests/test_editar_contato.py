from django.test import TestCase
from django.urls import reverse
from core.models import Contato

class EditarContatoTestCase(TestCase):

    def setUp(self):
        # Cria um contato inicial para edição
        self.contato = Contato.objects.create(
            nome="João da Silva",
            email="joao@example.com",
            telefone="11999999999"
        )
        self.url = reverse('editar_contato', args=[self.contato.id])

    def test_pagina_editar_contato_carrega(self):
        """Verifica se a página de edição é acessível."""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Editar Contato")

    def test_editar_contato_sucesso(self):
        """Verifica se o contato é editado e redireciona corretamente."""
        dados_atualizados = {
            'nome': 'João Atualizado',
            'email': 'joao_atualizado@example.com',
            'telefone': '11988888888',
        }
        response = self.client.post(self.url, dados_atualizados)

        # Deve redirecionar para lista_edita
        self.assertRedirects(response, reverse('lista_edita'))

        # Verifica se o contato foi realmente atualizado no banco
        self.contato.refresh_from_db()
        self.assertEqual(self.contato.nome, 'João Atualizado')
        self.assertEqual(self.contato.email, 'joao_atualizado@example.com')
        self.assertEqual(self.contato.telefone, '11988888888')

    def test_editar_contato_campos_invalidos(self):
        """Verifica se o formulário mostra erro ao enviar dados inválidos."""
        response = self.client.post(self.url, {
            'nome': '',  # Campo obrigatório
            'email': 'email_invalido',
            'telefone': '',
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Este campo é obrigatório")
