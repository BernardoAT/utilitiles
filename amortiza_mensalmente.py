# -*- encoding: utf-8 -*-
''' Calcula um reembolso dum empréstimo que amortiza mensalmente
: Constrói um Quadro de Amortìzaçäo do Crédito prestação POSTECIPADA  | 
Calculate The repayment of the loan amortized monthly
: Build a Credit amortization table'''
import math

while True:
  try:
    prazo = int(raw_input("Prazo (em periodos): ")) # Assegura k o "prazo" é inteiro
    assert prazo > 0 and prazo < 601 	#Assegura k o prazo é positivo e menor do k 601 periodos
    break
  except ValueError:
    print('Error! "Prazo" must be interger number...') # garante k "prazo" é inteiro
  except AssertionError:
    print('Error! "Prazo" must be positive and reasonable ...') # garante k "prazo" > 0

while True:
  try:
    TaxaAnual = float(raw_input("Taxa Anual: "))
    break
  except ValueError:
    print('Error! "Taxa Anual" must be floating number...')

while True:
  try:
    capital= float(raw_input("Capital: ")) # Assegura k o "capital" é float number
    assert capital > 0 	 #Assegura k "capital" é positivo
    break
  except ValueError:
    print('Error! "Capital" must be floating number...') 	# garante k "Capital" é um numero real
  except AssertionError:
    print('Error! "Capital" must be positive...')  # garante k "Capital" > 0


#remaining_balance = capital + imposto_selo_4_por_cento
remaining_balance = capital
ipaid=[]
total_interest = 0
Capital_paid_in_this_IA = []


Taxa = TaxaAnual / 12
t = (1 - (1+Taxa)**(-prazo))/Taxa
Instalment_amount = remaining_balance / t


print "We'd have %5.3f prestacao, %5.3f capital inicial." % (Instalment_amount, capital)
print "De:    Prestação:     Interest Accru.:   Capital:   remaining balance:"         
for num in range(prazo):
  ipaid.append(num)
  Capital_paid_in_this_IA.append(num)
  #sum_balance.append(num)


  ipaid[num] = Taxa * remaining_balance
  total_interest += ipaid[num]
  Capital_paid_in_this_IA[num] = Instalment_amount - ipaid[num]
  remaining_balance = remaining_balance - Capital_paid_in_this_IA[num]
  
  
  print " %3.d \t %7.2f \t %11.2f \t %7.2f \t %12.2f" %(num + 1, Instalment_amount, ipaid[num], Capital_paid_in_this_IA[num], abs(remaining_balance))
