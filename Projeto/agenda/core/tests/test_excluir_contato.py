from django.test import TestCase
from django.urls import reverse
from core.models import Contato

class ExcluirContatoTestCase(TestCase):
    def setUp(self):
        # Cria um contato para testar exclusão
        self.contato = Contato.objects.create(
            nome="Maria Oliveira",
            email="maria@example.com",
            telefone="11977777777"
        )
        self.url = reverse('excluir_contato', args=[self.contato.id])

    def test_pagina_excluir_contato_carrega(self):
        """Verifica se a página de exclusão é acessível."""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Tem certeza que deseja excluir")

    def test_excluir_contato_sucesso(self):
        """Verifica se o contato é excluído com sucesso e redireciona corretamente."""
        response = self.client.post(self.url)

        # Verifica se foi redirecionado para lista_exclui
        self.assertRedirects(response, reverse('lista_exclui'))

        # O contato deve ter sido removido do banco
        existe = Contato.objects.filter(id=self.contato.id).exists()
        self.assertFalse(existe)

    def test_excluir_contato_inexistente(self):
        """Verifica se tentar excluir um contato inexistente gera 404."""
        url_invalida = reverse('excluir_contato', args=[999])
        response = self.client.get(url_invalida)
        self.assertEqual(response.status_code, 404)
