# Bookworm 

Autor: Tomislav Rakuljić
Fakultet: Fakultet informatike u Puli

## Use Case Dijagram
![bm8BUxu](https://github.com/user-attachments/assets/db056164-5c42-40f9-9196-a1b80d38eeac)


## Opis projekta: 
Bookworm je aplikacija koja služi kao privatna to do lista ali namijenjena za pohranjivanje knjiga. Idealna je kada korisnik treba pratiti koliko te koje knjige je pročitao.

## Funkcije:
1. Pohranjivanje knjige gdje je moguće dodati naziv/žanr/autora/natuknice
2. Pretraživanje knjiga ovisno o nazivu, autoru...
3. Filtriranje knjiga po žanru, autoru...
4. Brisanje knjiga
5. Uređivanje knjiga u slučaju dodavanja promjena

## Pokretanje:
1. Kloniranje projekta: 
    git clone https://github.com/Kikindo/bookworm.git
    cd bookworm
   
3. Izgradnja docker slike:
    docker build -t bookworm-flask .
   
5. Pokretanje aplikacije
   docker run -d -p 8000:8000 --name bookworm -v "${PWD}/bookworm-data:/app/app" bookworm-flask
