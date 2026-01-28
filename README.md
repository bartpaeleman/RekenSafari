# Rekensafari: Verloren Dieren Avontuur! 🦁🐘

Rekensafari is een interactieve, educatieve web-applicatie ontworpen om kinderen (groep 3/4/5) te helpen bij het automatiseren van rekensommen. Door middel van gamification, vrolijke thema's en een beloningssysteem met badges, wordt rekenen een spannend avontuur.

## 🌟 Kenmerken

### 🎮 Spelmodi
De app ondersteunt vijf verschillende rekenoperaties:
*   **Splitsen**: Visuele weergave van splitsingen (bijv. "Splits 8: 3 en ...").
*   **Optellen (+) & Aftrekken (-)**.
*   **Vermenigvuldigen (x) & Delen (:)**: Met slimme getallengeneratie (geen breuken/rest).

### 📊 Drie Moeilijkheidsgraden
*   **Level 1**: Getallen van 0 tot 10.
*   **Level 2**: Getallen van 1 tot 20.
*   **Level 3**: Getallen tot 100.

### 👨‍👩‍👧‍👦 Mama & Papa Scherm (Instellingen)
Een afgeschermd gedeelte voor ouders om het spel te configureren:
*   **Naam Kind**: Personaliseert de ervaring.
*   **Tijd per Vraag**: Instelbaar (bijv. 10 seconden) voor tijdsdruk of rust.
*   **Vragen per Level**: Bepaal hoe lang een sessie duurt per level.
*   **Drempel (%)**: Percentage goede antwoorden nodig om naar het volgende level te mogen.
*   **Badge Niveau**: Pas de moeilijkheid van badges aan (Makkelijk, Normaal, Moeilijk).
*   **Reset**: Mogelijkheid om alle opgeslagen scores en badges te wissen.

### 🏆 Gamification & Badges
Het spel bevat een uitgebreid badgesysteem om motivatie te stimuleren. Badges worden getoond als pop-ups (die het spel pauzeren) en worden opgeslagen.

**1. Level Badges (Streak binnen 1 level)**
*   🐣 **Kuiken**: 25% goed.
*   🐱 **Miauw**: 50% goed.
*   🐶 **Woef**: 75% goed.
*   🐰 **Konijn**: 100% foutloos!

**2. Sessie Badges (Over meerdere levels heen)**
*   🐝 **Bezige Bij**: Level 1 voltooid.
*   🐭 **Snelle Muis**: Gemiddeld sneller dan 5 seconden per vraag.
*   🐻 **Sterke Beer**: Level 2 bereikt.
*   🦊 **Sluwe Vos**: Level 3 bereikt.

**3. Levenslang Badges (Historische prestaties)**
*   🐼 **Panda**: 5 spellen gespeeld.
*   🐯 **Tijger**: 100 vragen in totaal goed beantwoord.
*   🦁 **Leeuw**: 500 vragen goed.
*   🦄 **Unicorn**: 1000 vragen goed (Legendarisch!).

### 📱 Responsive Design
De app is volledig responsive en werkt op desktops, tablets en mobiele telefoons. Het past zich aan aan de schermgrootte en oriëntatie.

---

## 🚀 Hoe te gebruiken

1.  Open `index.html` in een moderne webbrowser (Chrome, Firefox, Safari, Edge).
2.  **Ouders**: Klik op de "Mama & Papa" knop (of stel dit de eerste keer in) om de naam en voorkeuren in te stellen. Klik op "Opslaan & Start".
3.  **Kind**:
    *   Kies wat je wilt oefenen (bijv. Splitsen of Keer).
    *   Kies tot welk level je wilt gaan.
    *   Klik op **"Start Avontuur!"**.
4.  **Spelen**:
    *   Typ het antwoord in en het wordt direct gecontroleerd (geen Enter nodig).
    *   Verzamel dieren en badges!
    *   Als een level klaar is, klik op "Start Level" om verder te gaan.

## 🛠️ Technische Details

*   **Single File Application**: Alles zit in één `index.html` bestand (HTML, CSS, JS). Geen installatie of server nodig.
*   **Opslag**: Scores en instellingen worden lokaal opgeslagen in de browser (`localStorage`).
*   **Offline**: Werkt volledig zonder internet (behalve voor de initiële inlaad van de audio-bestanden indien niet gecached).
*   **Audio**: Gebruikt externe geluidseffecten voor positieve feedback en badges.
