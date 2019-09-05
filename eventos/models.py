from django.db import models


class Rota(models.Model):
    ponto_inicial = models.CharField(max_length=50)
    ponto_final = models.CharField(max_length=255)

    def __str__(self):
        return self.ponto_inicial


class PontoParada(models.Model):
    class Meta:
        verbose_name_plural = 'Pontos de Parada'

    descricao = models.CharField(max_length=255)
    latitude = models.CharField(max_length=50)
    longitude = models.CharField(max_length=50)
    rota = models.ForeignKey(Rota, models.CASCADE)

    def __str__(self):
        return self.descricao


class Pais(models.Model):

    class Meta:
        verbose_name_plural = 'Países'

    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Regiao(models.Model):

    class Meta:
        verbose_name_plural = 'Regiões'

    nome = models.CharField(max_length=100)
    pais = models.ForeignKey('Pais', models.CASCADE)

    def __str__(self):
        return self.nome


class Estado(models.Model):
    nome = models.CharField(max_length=100)
    codigouf = models.IntegerField()
    uf = models.CharField(max_length=2)
    regiao = models.ForeignKey(Regiao, models.CASCADE)

    def __str__(self):
        return self.nome


class Cidade(models.Model):
    estado = models.ForeignKey(Estado, models.CASCADE)
    nome = models.CharField(max_length=100)
    codigo = models.IntegerField()
    uf = models.CharField(max_length=2)

    def __str__(self):
        return self.nome


class Endereco(models.Model):
    class Meta:
        verbose_name_plural = 'Endereços'

    cidade = models.ForeignKey(Cidade, models.CASCADE)
    rua = models.CharField(max_length=100)
    numero = models.IntegerField()
    complemento = models.CharField(max_length=255)
    bairro = models.CharField(max_length=100)
    cep = models.CharField(max_length=9)

    def __str__(self):
        return self.rua


class Instituicao(models.Model):
    class Meta:
        verbose_name_plural = 'Instituições'

    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    endereco = models.ForeignKey(Endereco, models.CASCADE)

    def __str__(self):
        return self.nome


class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    cpf = models.CharField(max_length=50)
    telefone = models.CharField(max_length=20)
    login = models.CharField(max_length=50)
    senha = models.CharField(max_length=255)
    endereco = models.ForeignKey(Endereco, models.CASCADE)
    instituicao = models.ForeignKey(Instituicao, models.CASCADE)

    def __str__(self):
        return self.nome


class Evento(models.Model):
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    data_ida = models.DateField()
    data_volta = models.DateField()
    responsavel = models.ForeignKey(Usuario, models.CASCADE)

    # rota_ida = models.ForeignKey(Rota, models.CASCADE)
    # rota_volta = models.ForeignKey(Rota, models.CASCADE)

    def __str__(self):
        return self.titulo


class ParticipanteEvento(models.Model):
    class Meta:
        verbose_name_plural = 'Participantes dos eventos'

    pagamento = models.IntegerField()
    sugestao = models.CharField(max_length=255)
    avaliacao = models.IntegerField()
    evento = models.ForeignKey(Evento, models.CASCADE)
    usuario = models.ForeignKey(Usuario, models.CASCADE)

    def __str__(self):
        return str(self.usuario)
