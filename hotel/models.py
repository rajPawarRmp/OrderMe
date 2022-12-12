from djongo import models

# Create your models here.
class Dish(models.Model):
	
		_id=models.ObjectIdField()
		img=models.FileField(upload_to='images/')
		dname=models.CharField(max_length=55)
		type=models.CharField(max_length=11)
		price=models.IntegerField()
		def __str__(self):
				return self.dname

		@staticmethod
		def get_dish_by_name(name):
			return Dish.objects.filter(dname__in=name)
		
