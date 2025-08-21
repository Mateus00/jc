from django.db import models

class Pagina(models.Model):
    nome = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='pagina/', blank=True, null=True)

class Secao(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    imagem_fundo = models.ImageField(upload_to='secoes/', blank=True, null=True)
    imagem_centro = models.ImageField(upload_to='secoes/', blank=True, null=True)

    def __str__(self):
        return self.titulo
    
class Galeria(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='secoes/', blank=True, null=True)

    def __str__(self):
        return self.titulo

class Categoria(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    imagem = models.ImageField(upload_to='produtos/')
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True, related_name='produtos')
    destaque = models.BooleanField(default=False)

    def __str__(self):
        return self.nome
