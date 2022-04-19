from django.test import TestCase
from .models import NeighbourHood,Profile,Business

# Create your tests here.

class ImageTestClass(TestCase):
    # testing Neighbourhood
    def setUp(self):
        self.neighbourhood= NeighbourHood(hood_name= 'James', image ='John', user= "johny",area ="kanairo")
    # Testing  profile
    def setUp(self):
        self.profile= Profile(userrname="Mzazi", description = "student of life", post_date= "2020", neighbor_hood ="kasarani",email= "jos@yahoo.com" )
        # Testing Business
    def setUp(self):
        self.business= Business(name = 'James', post_date ='2010', user = "Johny",neighbor_hood = "Mombasa", email = "stJ@hotmail.com")
    
    # Testing Save Method
    def test_save_method(self):
        self.neighbourhood.save()
        self.profile.save()
        self.business.save()

    def tearDown(self):        
        NeighbourHood.objects.all().delete()
        Profile.objects.all().delete()
        Business.objects.all().delete()