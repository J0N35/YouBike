from django.db import models

class GzipFile(models.Model):
	zipfile = models.FileField(upload_to="data")
	
	def __unicode__(self):
		return self.zipfile.name

class Station(models.Model):
	sno = models.IntegerField(primary_key = True)
	sna = models.TextField()
	tot = models.IntegerField()
	sbi = models.IntegerField()
	sarea = models.TextField()
	mday = models.DateTimeField()
	lat = models.FloatField()
	lng = models.FloatField()
	ar = models.TextField()
	sareaen = models.TextField()
	snaen = models.TextField()
	aren = models.TextField()
	bemp = models.IntegerField()
	act = models.BooleanField()
	source_path = models.ForeignKey(GzipFile, on_delete = models.CASCADE, null = True)
	
	def __unicode__(self):
		return self.sna

class History(models.Model):
	sno = models.ForeignKey(Station, on_delete = models.CASCADE, null = True)
	mday = models.DateTimeField(null = True)
	sbi = models.IntegerField(null = True)

	def __unicode__(self):
		return unicode(self.sno)


# Create your models here.
