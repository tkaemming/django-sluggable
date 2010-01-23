from django.template.defaultfilters import slugify
from django.test import TestCase
from sluggable.tests.models import SimpleSluggableModel, \
    MultiFieldSluggableModel, UniqueTogetherSluggableModel

class TestSimpleSlug(TestCase):
    def setUp(self):
        self.alpha_value = 'Lorem ipsum dolor sit amet.'
        self.model_kwargs = {
            'alpha': self.alpha_value
        }
    
    def test_slug_creation(self):
        """Test simple slug creation."""
        slugged_model = SimpleSluggableModel(**self.model_kwargs)
        slugged_model.save()
        
        # The slug should be the same as the result of _generate_base_slug.
        self.assertEquals(slugged_model.slug, slugged_model._generate_base_slug())
    
    def test_unique_slug(self):
        """Test unique slug creation."""
        slugged_model_one = SimpleSluggableModel(**self.model_kwargs)
        slugged_model_one.save()
        
        slugged_model_two = SimpleSluggableModel(**self.model_kwargs)
        slugged_model_two.save()
        
        # When created with identical attribute values, the slug should 
        # be different.
        self.assertNotEqual(slugged_model_one.slug, slugged_model_two.slug)

class TestMultiFieldSlug(TestCase):
    def setUp(self):
        self.alpha_value = 'Lorem ipsum dolor sit amet.'
        self.beta_value = 'Consectetuer adipiscing elit.'
        self.model_kwargs = {
            'alpha': self.alpha_value,
            'beta': self.beta_value
        }
    
    def test_slug_creation(self):
        """Test simple slug creation from multiple fields."""
        slugged_model = MultiFieldSluggableModel(**self.model_kwargs)
        slugged_model.save()
        
        # The slug should be the same as the result of _generate_base_slug.
        self.assertEquals(slugged_model.slug, slugged_model._generate_base_slug())
    
    def test_unique_slug(self):
        """Test unique slug creation from multiple fields."""
        slugged_model_one = MultiFieldSluggableModel(**self.model_kwargs)
        slugged_model_one.save()
        
        slugged_model_two = MultiFieldSluggableModel(**self.model_kwargs)
        slugged_model_two.save()
        
        # When created with identical attribute values, the slug should 
        # be different.
        self.assertNotEqual(slugged_model_one.slug, slugged_model_two.slug)

class TestUniqueTogetherSlug(TestCase):
    def setUp(self):
        self.alpha_value = 'Lorem ipsum dolor sit amet.'
        self.model_kwargs = {
            'alpha': self.alpha_value,
        }
        
        self.beta_value_one = 'Consectetuer adipiscing elit.'
        self.beta_value_two = 'Morbi commodo.'
    
    def test_unique_slug(self):
        """Test unique slug creation with unique_together fields."""
        slugged_model_one = UniqueTogetherSluggableModel(beta=self.beta_value_one, 
            **self.model_kwargs)
        slugged_model_one.save()
        
        slugged_model_two = UniqueTogetherSluggableModel(beta=self.beta_value_one, 
            **self.model_kwargs)
        slugged_model_two.save()
        
        # If the two "beta" values are the same, the slug should be different.
        self.assertEqual(slugged_model_one.beta, slugged_model_two.beta)
        self.assertNotEqual(slugged_model_one.slug, slugged_model_two.slug)
        
        slugged_model_three = UniqueTogetherSluggableModel(beta=self.beta_value_two,
            **self.model_kwargs)
        slugged_model_three.save()
        
        # If the two "beta" values are different, the slug should be the same.
        self.assertNotEqual(slugged_model_one.beta, slugged_model_three.beta)
        self.assertEqual(slugged_model_one.slug, slugged_model_three.slug)