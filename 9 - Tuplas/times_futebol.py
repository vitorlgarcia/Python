times = ("Sao Paulo", "Palmeiras", "Corinthians", "Atletico-GO", "Bahia", "Santos", "Juventude", "Criciúma", "Internacional", "Grêmio")

print("=-" * 30)
print(f"Lista de times do brasileirão: {times}")
print("=-" * 30)
print(f"Os 5 primeiros são {times[0:5]}")
print("=-" * 30)
print(f"Os 4 ultimos são {times[-5:-1]}")
print("=-" * 30)
print(f"Times em ordem alfabética{sorted(times)}")
print("=-" * 30)
print(f"O {times[8]} está na {times.index("Internacional") + 1} posição") # Lembrando que a posição de tuplas ou listas sempre começam no zero