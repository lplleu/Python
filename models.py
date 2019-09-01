from django.db import models

clsss Category():
  name = models.CharField(max_length=64, null=False, blank=False)
  
  def __str__(self):
    return self.name

class Briefs(models.Model):
  title = models.CharField(max_length=255, null=Fals, blank=False)
  category = models.ForeignKey(Category, on_delete=models.CASCADE)
  
  
  
