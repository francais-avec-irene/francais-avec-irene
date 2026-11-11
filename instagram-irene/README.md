# Instagram Irene · Francese per italiani

Cartella di lavoro del profilo Instagram « Irene - Francese per italiani » (francese.con…).
Pubblico: italiani di 30-40 anni. Rivolgersi sempre al plurale, valido per tutti (« Siete pronti? »).

## Identità visiva (scelta l'11 novembre 2026)

- **Logo**: `logo/logo-irene-francese.png` (cerchio bianco « Irène FRANCESE » su bandiera francese). Sempre **in alto a sinistra**, rotondo, con bordo bianco.
- **Firma in basso**: « Irene · Francese per italiani » a sinistra, numero slide a destra (« 1/5 · scorri → »).
- **Font**: Bricolage Grotesque (titoli e testo) + font pixel (Silkscreen per i post, Press Start 2P per i reel).
- **Stile dei post**: modello **« foto piena »**: foto vera a tutto schermo, velo colorato, riquadro in vetro in basso con il testo, etichette colorate inclinate.
  - Palette viola (aloni rosa/arancio, etichette rosa #FF5FA2, arancio #FFB86B, azzurro #7FE3FF): post d'amore, « mi manchi ».
  - Palette verde (lime #E5FF3D, menta #3DFFB0, giallo #FFD23F): espressioni, animali.
  - Le palette possono cambiare da un post all'altro, la struttura resta la stessa.
- **Foto**: sempre vere, di Parigi / Francia, con persone. **Foto inclusive**: coppie di ogni tipo, amici, famiglie, persone diverse. Niente immagini etero-normative.
- **Formato**: post 1080×1350 (4:5), reel 1080×1920 (9:16).

## Reel gioco (serie numerata fino a Natale)

- Stile arcade synthwave: griglia neon rosa, sole a righe, scritte pixel, punteggio, cuori, timer, pulsanti arcade.
- La voce è quella di Irene (registrata da lei), lei non compare mai.
- Numerazione: il reel 1 « Falsi amici » contiene i livelli 1, 2, 3 e finisce con « Seguimi ▶ Livello 4 ».
  - **Livello 4 · « LE o LA? »** (genere mer, fleur, printemps, couleur, boss bonheur): schermate pronte in `reel/livello-4_le-o-la/`, finisce con « Seguitemi ▶ Livello 5 ».
  - Prossimo reel: **Livello 5**. Lo speciale di Natale (1° dicembre) è l'ultimo livello numerato.
- 2 reel gioco a settimana fino a Natale + un post al giorno.

## Contenuti già fatti

| Data | Tipo | Cartella |
|---|---|---|
| 11/11 (mer.) | Post « Mi manchi » (5 slide, foto piena viola) | `post/2026-11-11_mi-manchi/` |
| 14/11 (sab.) | Post « 5 espressioni con gli animali » (7 slide, foto piena verde) | `post/2026-11-14_espressioni-animali/` |
| — | Reel livello 1-3 « Falsi amici » (pubblicato) | `reel/livello-1-3_falsi-amici/` |
| 11/11 | Reel livello 4 « LE o LA? »: video finale montato con la voce di Irene (`Reel_livello4_LE_o_LA.mp4`), schermate e conto alla rovescia 3-2-1 | `reel/livello-4_le-o-la/` |

Modelli originali di Irene: `originali-irene/`.

## Testo da registrare · Reel livello 4 « LE o LA? »

1. « Livello 4! LE o LA? In italiano è maschile… e in francese? Avete tre secondi. Siete pronti? Via! »
2. « Il mare… » (3 s) → « La mer! »
3. « Il fiore… » (3 s) → « La fleur! »
4. « La primavera… » (3 s) → « Le printemps! Attenzione, qui è maschile! »
5. « Il colore… » (3 s) → « La couleur! »
6. Power-up: « Il trucco del prof: le parole in -eur sono quasi sempre femminili. La couleur, la fleur, la peur, la douleur… Ma attenzione! Le bonheur, le malheur, l'honneur sono maschili! »
7. « Boss finale! La felicità… » (3 s) → « Le bonheur! Era la trappola! »
8. « Livello 4 superato! Quanti punti avete fatto? Scrivetelo nei commenti, salvate il reel per ripassare… e seguitemi per il livello 5! »

**Didascalia**: LE o LA? 🇫🇷 Livello 4! In italiano è maschile, in francese… no! 😱 Quanti punti avete fatto? Scrivetelo nei commenti 👇 Salvate il reel per ripassare e seguitemi per il livello 5 🎮

**Hashtag**: #francese #imparareilfrancese #francesepertutti #francesepergliitaliani #linguafrancese #lezionidifrancese #parlarefrancese #grammaticafrancese #francesefacile #studiarelefrancese #learnfrench #frenchteacher #giocodellelingue #reelitalia #parigi

## Crediti foto (Wikimedia Commons, licenze libere)

Couple au Trocadéro (2013) · Paris Gay Pride 2013 026 e 042 · Marche des Fiertés LGBT 2010 Kissing · Danse au bord de la Seine, quai St-Bernard (2025) · Rooster portrait, France · Face of a female domestic cat · European rabbit kitten · Mallard Duck Snow · Blue Cochin hen · Poule Sebright, jardin botanique de Tours · People outside Sacré-Cœur (2026) · Promenade des Anglais in Nice · Tulipes au jardin des Tuileries · Saint-Vincent-de-Paul in Paris, spring blossom · Macarons from Ladurée on display.

## Script

`script/` contiene i programmi che generano le immagini (rendering HTML → PNG con Chrome) e la ricerca foto su Wikimedia Commons.

## Montaggio dei reel

Irene registra la voce (m4a) leggendo il testo con pause di 3 secondi dopo ogni domanda. Il video si monta con `script/monta_reel_livello4.py`: schermate al ritmo della voce, conto alla rovescia 3-2-1 durante la pausa, suoni da videogioco (moneta, tic, risposta giusta, power-up, boss, vittoria).

Audio: la voce di Irene va pulita e alzata (highpass 80 Hz, riduzione rumore leggera, compressore, loudnorm a -15 LUFS); effetti sonori dolci (onde sinusoidali) a volume basso, circa 20 dB sotto la voce. Le registrazioni originali sono molto basse (circa -40 dB di media).
