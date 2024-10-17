from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation
from django.urls import reverse


user = get_user_model()

class category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class brand(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class base_product(models.Model):
    name = models.CharField(max_length=255,null=True)
    price = models.PositiveIntegerField(null=True)
    count = models.PositiveIntegerField(null=True)
    category = models.ForeignKey(category , on_delete=models.CASCADE , null= True)
    brand = models.ForeignKey(brand , on_delete= models.CASCADE ,null=True)
    images = GenericRelation('image')
    is_suggested = models.BooleanField(default=False)
    title_fa = models.CharField(max_length=100,null=True)
    title_en = models.CharField(max_length=100,null=True)
    code_number = models.CharField(max_length=50,null=True)
    reviews = models.TextField(null = True , blank = True)
    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(default=0 , decimal_places=0 ,max_digits=20)


    @property
    def images(self):
        return image.objects.filter(object_id = self.id ,
                                    content_type = ContentType.objects.get_for_model(self.__class__).id
                                    )

 
    def get_absolute_url(self):
        return reverse("store_app:single-priduct", args=(self.id))
    

    def __str__(self):
        return f'{self.id} {self.name}'    

    class Meta:
        abstract = True


class digital_product(base_product):
    category = models.ManyToManyField(category)
    colors = models.ManyToManyField('Color', related_name='digital_colors' , blank = True)
    descriptions = models.ManyToManyField('Description', related_name='digital_descriptions' , blank = True)
    specifications = models.ManyToManyField('Specifications', related_name='digital_specifications')
    special_features = models.ManyToManyField('SpecialFeature', related_name='digital_features')
    


class clothes_product(base_product):
    category = models.ManyToManyField(category)
    descriptions = models.ManyToManyField('Description', related_name='clothes_descriptions' , blank = True)
    specifications = models.ManyToManyField('Specifications', related_name='clothes_specifications')
    special_features = models.ManyToManyField('SpecialFeature', related_name='clothes_features')
    


class banner(models.Model):
    title = models.CharField(max_length=255 , null=True)

    def __str__(self):
        return self.title
    
    @property
    def images(self):
        return image.objects.filter(
            object_id=self.id , content_type = ContentType.objects.get_for_model(self.__class__).id
            )
        


class image(models.Model):
    image = models.ImageField(upload_to='store/images/' , null=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE , null=True , related_name='store_app_images')
    object_id = models.PositiveIntegerField(null=True)
    content_object = GenericForeignKey("content_type", "object_id")

    def __str__(self):
        return self.image.url



class Color(models.Model):
    color_code = models.CharField(max_length=20,null=True)
    color_name = models.CharField(max_length=20 , null= True)

    def __str__(self):
        return self.color_name

    
class SpecialFeature(models.Model):
    category = models.ForeignKey(category, on_delete=models.CASCADE , null=True)
    title = models.CharField(max_length=100)
    detail = models.TextField()

    def __str__(self):
        return f"{self.title} {self.detail}"

# class DetailDescription(models.Model):
#     image = models.ForeignKey(image, on_delete=models.CASCADE, related_name='detail_descriptions')
#     detail = models.TextField()

#     def __str__(self):
#         return f"{self.image} - {self.detail[:30]}..."

class Description(models.Model):
    product = models.TextField(null= True)
    title = models.CharField(max_length=100,null=True)
    # description_detail = models.ManyToManyField(DetailDescription, related_name='descriptions')

    def __str__(self):
        return f"{self.title} - {self.product}"

class SpecificationDetail(models.Model):
    name = models.CharField(max_length=100)
    detail = models.TextField()
    autocomplete_fields = ['specification_detail'] 

    def __str__(self):
        return f"{self.name} - {self.detail}"

class Specifications(models.Model):
    product = models.TextField(null=True)
    title = models.CharField(max_length=100)
    specification_detail = models.ManyToManyField(SpecificationDetail, related_name='specifications')

    def __str__(self):
        return f"{self.title} - {self.product}"

    
    
class Favorite(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE, related_name='favorites')
    # product = models.ForeignKey(base_product, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE , null=True , related_name='store_app_favorites')
    object_id = models.PositiveIntegerField(null=True)
    product = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return f"{self.user.username} - {self.product}"

