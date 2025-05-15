from django.test import TestCase
from django.urls import reverse
from .models import Projects, Cv, Refrences, CoverLetter

class BlogViewsTestCase(TestCase):

    def setUp(self):
        # Set up initial data for tests
        self.project = Projects.objects.create(
            title="Test Project",
            description="Test Description",
            full_description="Test Full Description",
            url="https://example.com",
            git_hub="https://github.com/example",
            image="images/test_image.jpg",
            slug="test-project"
        )
        self.cv = Cv.objects.create(
            title="Test CV",
            description="Test Description",
            url="https://example.com",
            image="images/test_image.jpg",
            start_date="2023-01-01",
            end_date="2023-12-31"
        )
        self.skill = self.cv.skills.create(skills="Test Skill")
        self.refrence = Refrences.objects.create(
            ref_name="Test Refrence",
            refrence="Test Description",
            date="2023-01-01"
        )
        self.coverletter = CoverLetter.objects.create(
            my_name="Test Name",
            picture="images/test_image.jpg",
            coverletter="Test Cover Letter"
        )

    def test_home_page_view(self):
        response = self.client.get(reverse('homepage'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/homepage.html')

    def test_projects_view(self):
        response = self.client.get(reverse('projects'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/projects.html')
        self.assertContains(response, self.project.title)

    def test_project_view(self):
        response = self.client.get(reverse('project', args=[self.project.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/project.html')
        self.assertContains(response, self.project.full_description)

    def test_cv_view(self):
        response = self.client.get(reverse('cv'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/cv.html')
        self.assertContains(response, self.cv.title)

    def test_refrences_view(self):
        response = self.client.get(reverse('refrences'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/refrences.html')
        self.assertContains(response, self.refrence.ref_name)
        self.assertContains(response, self.coverletter.my_name)