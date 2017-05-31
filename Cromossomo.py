from util import binario, aleatorioMinMax

class Cromossomo(object):
  
  def __init__(self, quantidade, bits):
    self.criarGenes(quantidade, bits)
    
  def criarGenes(self, quantidade, bits):
    tamanho = quantidade*bits
    self.genes = "".join([binario() for i in range(0, tamanho)])
    self.posicoes = range(0, tamanho, bits)
    self.bits = bits
    self.quantidade = quantidade
    
  def getGene(self, gene):
    posicao = self.posicoes[gene - 1]
    return self.genes[posicao: posicao + self.bits]
  
  @staticmethod
  def reproduzir(x, y):
    posicao = aleatorioMinMax(1, len(x.genes) - 1)
    genesA, genesB = Cromossomo.corte(x, y, posicao)
    cromossomo = x.__class__
    filhoA = cromossomo()
    filhoB = cromossomo()
    filhoA.genes = genesA
    filhoB.genes = genesB
    
    return filhoA, filhoB
  
  @staticmethod
  def corte(x, y, posicao):
    genesA = "%s%s" % (x.genes[:posicao], y.genes[posicao:])
    genesB = "%s%s" % (y.genes[:posicao], x.genes[posicao:])
    return genesA, genesB

  def mutacao(self):
    index = aleatorioMinMax(0, len(self.genes) - 1)
    mutados = list(self.genes)
    gene = mutados[index]
    mutados[index] = "0" if gene == "1" else "1"
    self.genes = "".join(mutados)
   
  def fitness(self):
    raise NotImplementedError("Metodo nao implementado.")
    
  def objetivo(self):
    raise NotImplementedError("Metodo nao implementado.")
  
  def converterGene(self, posicao, gene):
    raise NotImplementedError("Metodo nao implementado.")
    
  def toStr(self):
    return ",".join([self.converterGene(posicao, self.getGene(posicao)) 
                     for posicao in range(1, self.quantidade + 1)])
    
  def __str__(self):
    return "%s - (%d)" % (self.toStr(), self.fitness())
  
  def __repr__(self):
    return self.__str__()
  