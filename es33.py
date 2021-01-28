'''
In un laboratorio di analisi i pazienti sono sottoposti a un esame specialistico
secondo l'ordine di arrivo (suggerimento: utilizza una struttura di coda per
memorizzare i nomi dei pazienti): scrivi il programma che consenta di registrare
i nomi dei pazienti man mano che arrivano. Visualizza poi il nome del paziente
che deve essere sottoposto all'esame perchè è il primo della coda in attesa
'''
pazienti = []

numero_pazienti = int(input("Quanti pazienti sono? "))

for n in range(numero_pazienti):
    nome_paziente = input("Qual è il nome del paziente? ")
    pazienti.append(nome_paziente)

print("Questo è il primo paziente: ", pazienti.pop(0))