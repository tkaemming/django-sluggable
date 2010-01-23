# django-sluggable
Automatically generated unique model slugs for Django models.

* **Author:** Ted Kaemming <ted@kaemming.com>
* **Homepage:** http://www.github.com/tkaemming/django-sluggable/

## Installation
To install `django-sluggable`, simply check out the repository from GitHub
and run `python setup.py install` to install the Python package.

## Usage
To add automatic slugs to a model, just have your model class extend 
`sluggable.models.SluggableModel`.

For example,

    from sluggable.models import SluggableModel
    
    class MyModel(SluggableModel):
        name = models.CharField(max_length=255)
        
        def __unicode__(self):
            return u'%s' % self.name

The `slug` field will be added to your models, and the unique value will be 
automatically generated at model save.

### Using `unique_together` with your Models
`django-sluggable` supports the use of the model's `Meta` attribute
`unique_together` as documented on the Django documentation site:
http://docs.djangoproject.com/en/dev/ref/models/options/#unique-together

When `slug` is specified as one of the fields in a `unique_together` tuple,
the slug will automatically be made unique to meet the constraints of the
`unique_together` definition. An example of this behavior can be seen in the 
`sluggable.tests.tests.TestUniqueTogetherSlug` test case.

### Customizing Slug Creation
By default, the slug is generated from the output of the model's `__unicode__`
method. If you'd like to use a different value for slug creation, override the
`_generate_base_slug` method to return an alternate "slugify-ed" value.