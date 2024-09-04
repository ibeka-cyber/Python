from django.db import models

class Author(models.Model):
    def __str__(self):
        return self.name
    
    name =models.CharField(max_length=50) #yazar adı
    created = models.DateTimeField('date Created') #yazarın ne zaman  kaydedildiği

class Book(models.Model):
    def __str__(self):
        return self.name
    
    name  = models.CharField(max_length=50)
    created = models.DateTimeField('date Created')

    #on_delete veritabanından bir yazar silindiği zaman yazarın bütün kitaplarının silinmesini sağlar.
    author=models.ForeignKey(Author,on_delete = models.CASCADE)

    #decimal_places virgülden sonra kaç basamak gösterilecek onu gösterir.
    #max_digits de sayının kaç basamaklı olacağını gösterir.
    price = models.DecimalField(decimal_places=2,max_digits=4,null=True) 