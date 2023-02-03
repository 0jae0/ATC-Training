import random; import time

for i in range(1,1000):
    icao = random.choice(['AAR', 'AAL', 'ABL', 'APZ', 'ASV', 'DAL', 'EOK', 'ESR', 'ETD', 'ETH', 'JJA', 'JNA', 'KAL', 'KLM', 'UAE', 'UPS'])
    numb = random.randrange(100, 8000)
    print(icao + str(numb))