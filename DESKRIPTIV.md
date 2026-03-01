# Deskriptive Analyse der Smart Home Technologies (SHT) Umfrage

## Einleitung

Der vorliegende Datensatz basiert auf einer Umfrage zum Thema Smart Home Technologies (SHT). Er umfasst **960 Beobachtungen** (Teilnehmer) und **283 Variablen** (Fragen). Von diesen unzähligen Merkmalen ist uns für diese Auswertung jedoch nur ein relevanter Bruchteil im Detail bekannt.

---

## Data Cleaning

Im Vorfeld wurden die Ausprägungen bereinigt und den korrekten Datentypen zugewiesen. Da es sich um Umfragedaten handelt, liegen hier vorwiegend ordinale Daten in Form von Likert-Skalen vor.

---

## Überblick

Um einen ersten fundierten Eindruck über die Struktur des Datensatzes zu gewinnen, wurden die demografischen Variablen sowie alle wesentlichen Fragenblöcke der Umfrage deskriptiv visualisiert.

---

## Demographische Daten

![Demographie](output/plots/demographic.png)

---

## Hauptfragen

Wie bei den demografischen Daten wurden auch die inhaltlichen Blöcke der Umfrage visualisiert, um allgemeine Meinungstrends und Tendenzen zu identifizieren.

---

### Wichtigkeit der Vorteile durch Nutzung von SHT

![Vorteile durch Nutzung SHT](output/plots/vorteile_sht.png)

Es zeigt sich insgesamt ein sehr ausgeglichenes Bild bei den wahrgenommenen Vorteilen. Ein spannendes Detail: Der reine Unterhaltungsfaktor wird im Vergleich von den Befragten am unwichtigsten eingestuft.

---

### Verfügbarkeit und Interesse an SHT

![Verfügbarkeit und Interesse an SHT](output/plots/verfuegbarkeit-interesse-sht.png)

Ein interessanter Kontrast: Obwohl der Unterhaltungsfaktor zuvor als eher unwichtig bewertet wurde, zeigt sich hier, dass die meisten Befragten bereits smarte "Unterhaltungsgeräte" besitzen. SHT-Lösungen im Bereich E-Autos (z. B. smarte Wallboxen) stoßen bei den Teilnehmern derzeit auf nahezu gar kein Interesse.

---

### Komfortgewinn durch Nutzung SHT

![Komfortgewinn durch Nutzung SHT](output/plots/komfortgewinn-sht.png)

Bis auf die Ausreißer beim E-Auto sehen die meisten Teilnehmer einen klaren Komfortgewinn durch den Einsatz von SHT-Produkten in ihrem Alltag.

---

### Assistenz durch SHT

![Assistenz durch SHT](output/plots/assistenz-sht.png)

Dieser Fragenblock ist zwar durch viele abbrechende Antworten (fehlende Werte / NAs) geprägt, dennoch lässt sich ein Muster erkennen: Die Mehrheit der Befragten, die geantwortet haben, fühlt sich durch die Nutzung von SHT im Alltag gut unterstützt.

---

### Auswirkung der Nutzung von SHT auf Energieeinsparung

![Auswirkung Energieersparnis](output/plots/auswirkung-energieeinsparung.png)

Auch hier gibt es viele fehlende Antworten. Das Gesamtbild zeigt jedoch deutlich, dass die meisten Teilnehmer das Potenzial sehen, vor allem in den Bereichen Strom und Heizenergie durch SHT merklich einsparen zu können.

---

### Auswirkung auf Sicherheit durch Nutzung SHT

![Auswirkung auf Sicherheit](output/plots/auswirkung-sicherheit.png)

Ein interessantes Ergebnis: Die Teilnehmer sind mehrheitlich der Meinung, dass SHT sich *nicht* zwingend positiv auf die persönliche Sicherheit auswirkt.

---

### Auswirkung auf Spaß und Unterhaltung durch Nutzung SHT

![Auswirkung Spaß/Unterhaltung](output/plots/auswirkung-spass-unterhaltung.png)

Dieser Block ist bei bestimmten Fragen leicht verwirrend, da schwer nachvollziehbar ist, wie sich z. B. eine smarte PV-Anlage auf den direkten Spaß- oder Unterhaltungsfaktor auswirken soll. 

Geht es jedoch allgemeiner um den Bereich Entertainment, stimmen immerhin ~40% der Teilnehmer zu, dass sich SHT positiv auf Unterhaltung und Spaß auswirkt.

---

### Auswirkung auf Kosteneinsparung durch Nutzung SHT

![Auswirkung Ersparnis SHT](output/plots/einsparung-kosten.png)

Wie schon bei der Energieeinsparung stimmen viele Teilnehmer zu, dass sich durch SHT Kosteneinsparungen – primär bei Strom und Energie – erzielen lassen.

---

### Meinungen zu SHT

Der folgende Fragenblock wurde für die Auswertung in zwei inhaltliche Bereiche unterteilt, da diese durch die unterschiedlichen Fragestellungen gut voneinander abgrenzbar sind.

#### Technikaffinität

[Technikaffinität](output/plots/meinung-technikaffinitaet.png)

Der Großteil der Befragten würde sich tendenziell als technikaffin beschreiben und zeigt erfreulicherweise wenig Berührungsängste oder Sorgen gegenüber neuen Technologien.

#### Energiesparmaßnahmen

[Energiesparmaßnahmen](output/plots/meinung-energiesparen.png)

Die Teilnehmer stimmen überwiegend zu, dass auch herkömmliche, rein analoge Maßnahmen (wie z. B. Stoßlüften) absolut wirksam sind, um Energie zu verringern.

---

### Steuerung SHT

![Steuerung SHT](output/plots/steuerung-sht.png)

Eine Steuerung über das eigene Smartphone ist bei den Teilnehmern die mit Abstand am meisten präferierte Lösung.

---

### Finanzierung SHT

![Finanzierung SHT](output/plots/finanzierung_sht.png)

---

### Informationsgewinn SHT

![Information SHT](output/plots/art_information_sht.png)

---

### Design SHT

![Design SHT](output/plots/design_sht.png)

---

### Steuerung SHT *(weitere)*

![Steuerung SHT](output/plots/steuerung_sht.png)

---

### Nachhaltigkeit SHT

![Nachhaltigkeit SHT](output/plots/nachhaltigkeit_sht.png)

---

### Klima- & Umweltbewusstsein SHT

![Umweltbewusstsein](output/plots/umweltbewusstsein_sht.png)

---

## Korrelationen der Hauptthemen

Um Zusammenhänge auf Makro-Ebene zu finden, wurde für jede Hauptfrage der Median der jeweiligen Teil-Antworten gebildet und korreliert. Starke und logische Korrelationen (z. B. zwischen hoher Technikaffinität und starken Kaufinteresse) bildeten in weiterer Folge die Basis, um bei gezielteren Fragestellungen in die explorative Modellierung zu gehen.

![Korrelation Themen](output/plots/korr-hauptfragen_sht.png)
