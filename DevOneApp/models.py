from email.policy import default
from django.db import models
from imagekit.models import ImageSpecField

# Create your models here.
class TemplateImages(models.Model):
    ios_image = models.ImageField(default='',blank=True, upload_to='ios_img')
    android_image = models.ImageField(default='',blank=True, upload_to='android_img')
    win_image = models.ImageField(default='',blank=True, upload_to='win_img')
    mac_image = models.ImageField(default='',blank=True, upload_to='mac_img')
    linux_image = models.ImageField(default='',blank=True, upload_to='linux_img')
    name = models.TextField(default='', max_length=100)
    slug = models.SlugField(blank=True, default='')
    thumbnails = ImageSpecField(source='ios_image, android_image, win_image, mac_image, linux_image', processors=[ResizeToFill(350, 200)], options={'quality': 100})

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = sugify(self.title)
        super(TemplateImages, self).save()

    def get_absolute_url():
        return reverse('temmp_images', args=[str(self.slug)])
