from django.test import TestCase
from django.core.urlresolvers import reverse

from .models import *

class AppTest(TestCase):

    def setUp(self):
        self.pascal = User.objects.create_user('pascal', 'pascal@test.com', 'pascal')
        self.john = User.objects.create_user('john', 'john@test.com', 'john')
        self.jimmi = User.objects.create_user('jimmi', 'jimmi@test.com', 'jimmi')
        self.gaston = User.objects.create_user('gaston', 'gaston@test.com', 'gaston')

        self.fo_team = Team.objects.create(name='Front office team')
        self.fo_team.members.add(self.pascal)
        self.fo_team.members.add(self.john)

        self.bo_team = Team.objects.create(name='Back office team')
        self.bo_team.members.add(self.jimmi)
        self.bo_team.members.add(self.gaston)

        self.fo_backlog = ProductBacklog.objects.create(team=self.fo_team, name="Backlog de l'équipe front")
        self.bo_backlog = ProductBacklog.objects.create(team=self.bo_team, name="Backlog de l'équipe back")

        self.fo_backlog_story_1 = UserStory.objects.create(product_backlog=self.fo_backlog, name="Nouvelle présentation de la fiche article")
        self.fo_backlog_story_2 = UserStory.objects.create(product_backlog=self.fo_backlog, name="Insertion auto de keywords dans les balises alt")

        self.bo_backlog_story_1 = UserStory.objects.create(product_backlog=self.bo_backlog, name="Ajout de l'autocompletion pour la recherche de produits")
    def test_backlog_not_authenticated_user(self):
        response = self.client.get(reverse('chistera:backlog', kwargs={'backlog_id': 1}))
        self.assertTemplateNotUsed(response, 'chistera/backlog.html')
        self.failUnlessEqual(response.status_code, 302)

    def test_backlog_authenticated_user(self):
        self.client.login(username='pascal', password='pascal')
        response = self.client.get(reverse('chistera:backlog', kwargs={'backlog_id': 1})) # L'id 1 correspond au backlog fo_backlog
        self.assertEqual(response.context['backlog'], self.fo_backlog)
        self.assertEqual(type(response.context['stories']), QuerySet)
        self.assertEqual(len(response.context['stories']), 2)
        self.failUnlessEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'chistera/backlog.html')
        self.client.logout()
    