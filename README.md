# Toribotti
Scrapee toria ja laittaa tiedon telegrammilla uusista asioista

# Miten päästä alkuun
- Kloonaa repo
- Luo repon juureen url.txt ja tori_ids.txt
- Lisää url.txt tiedostoon haluttu url.
  - https://www.tori.fi/uusimaa/viihde-elektroniikka/pelikonsolit_ja_pelaaminen?ca=18&cg=5020&c=5027&ps=4&w=114&st=s&st=k&st=u&st=h&st=g&gc=switch
  - Voit lisätä useamman. Yksi url per yksi rivi.
- Tee telegram botti ja lisää sen tokeni toribotti.py TELEGRAM_BOT_TOKEN muuttujaan.
  - https://core.telegram.org/bots/tutorial
-  Hae telegrammista oman käyttäjän id ja lisää toribotti.py TELEGRAM_OWN_USER_ID muuttujaan.
   - Etsi käyttäjä @userinfobot
   - kirjoita viesti /help
   - kopioi id
