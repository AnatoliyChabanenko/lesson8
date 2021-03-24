
# Create your models here.


class Categori_news(models.Model):
    name =  models.CharField(max_length=255)

class Tags(models.Model):
    tags = models.CharField(max_length=100)

class News(models.Model):
    name = models.CharField(max_length=255)
    text = models.TextField()
    categori = models.ForeignKey(Categori_news,on_delete=models.PROTECT)
    tags = models.ManyToManyField(Tags)
    def __str__(self):
        return self.name, self.text

class Avtor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=30)
    my_news = models.ForeignKey(News, on_delete=models.PROTECT)
