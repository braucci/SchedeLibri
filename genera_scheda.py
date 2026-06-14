# -*- coding: utf-8 -*-
"""
=====================================================================
  GENERATORE SCHEDE DI LETTURA  -  motore fisso, dati intercambiabili
=====================================================================

COME SI USA
-----------
1) Modifica SOLO il dizionario LIBRO qui sotto: titolo, autore, sinossi,
   personaggi, relazioni, temi, ecc. NON toccare il codice sotto la riga
   "==== MOTORE ====": e' cio' che garantisce l'omogeneita' grafica.
2) Esegui:  python genera_scheda.py
3) Trovi il PDF nella cartella corrente (nome = campo "output", oppure
   generato in automatico dal cognome dell'autore + titolo).

REGOLE DI COMPILAZIONE
----------------------
- Nei testi puoi usare markup: <b>grassetto</b>, <i>corsivo</i>.
- Campi opzionali: imposta None (o stringa/lista vuota) per OMETTERE la
  relativa sezione. Opzionali: titolo_senso, personaggi_minori,
  relazioni, temi, contesto_titolo/contesto_testo, chiave.
- "personaggi": quanti ne vuoi. Il colore della striscia e' assegnato
  in automatico (ciclico); puoi forzarlo col campo "colore".
- Parafrasa sempre i contenuti del libro: niente testo riprodotto.
- ADATTAMENTO PER GENERE: per saggi/poesia cambia solo le etichette in
  "etichette" (es. personaggi -> "Le tesi / I concetti chiave").
"""

# ====================================================================
#  DATI DEL LIBRO  ->  MODIFICA SOLO QUESTO BLOCCO
# ====================================================================
LIBRO = {
    # --- testata ---
    "titolo": "Divorzio di velluto",
    "autore": "Jana Kar\u0161aiov\u00e1",
    "tagline": "Un romanzo di separazioni \u2013 fra due paesi, fra due persone, "
               "fra s\u00e9 e le proprie radici.",

    # --- scheda tecnica (lascia None i campi non pertinenti) ---
    "autore_info": "Bratislava, 1978",
    "editore": "Feltrinelli \u2013 I Narratori, 2022",
    "pagine": "160",
    "lingua": "scritto in italiano",          # es. "trad. dal francese: Nome Cognome"
    "riconoscimenti": "Dozzina Premio Strega 2022",

    # --- la storia in breve (4-7 frasi, parafrasi) ---
    "sinossi": (
        "Katar\u00edna, slovacca di Bratislava, vive a Praga e torna in patria per "
        "trascorrere il Natale con la famiglia. Al peso delle vecchie incomprensioni con "
        "la madre si somma l\u2019imbarazzo di dover giustificare l\u2019assenza del marito "
        "<b>Eugen</b>, che due mesi prima l\u2019ha lasciata con un biglietto sul tavolo della "
        "cucina. Durante quei giorni ritrova le compagne di universit\u00e0, in particolare "
        "<b>Viera</b>, emigrata in Italia con una borsa di studio: le due amiche si "
        "riavvicinano e si confidano i rispettivi strappi. Tra i ricordi riaffiorano il primo "
        "incontro con Eugen, il matrimonio forse troppo precoce, la fatica di integrarsi a "
        "Praga e un dolore di cui Katar\u00edna ancora non riesce a parlare. Sullo sfondo, la "
        "Bratislava del regime comunista e la fine della Cecoslovacchia: una ricerca di s\u00e9 "
        "della protagonista e del suo paese, entrambi orfani di un passato solido."
    ),

    # --- il senso del titolo (None per omettere) ---
    "titolo_senso": (
        "Il <i>divorzio di velluto</i> \u00e8 la separazione pacifica tra <b>Slovacchia</b> e "
        "<b>Repubblica Ceca</b>, ufficiale il 1\u00b0 gennaio 1993 \u2013 quando Katar\u00edna aveva "
        "circa quindici anni. \u00c8 la chiave metaforica del romanzo: la frattura geopolitica "
        "<i>riverbera</i> le fratture intime dei personaggi \u2013 quella tra Katar\u00edna ed Eugen, "
        "e quella tra Viera e un paese diventato per lei troppo stretto. Separarsi senza "
        "violenza, ma comunque separarsi: \u00e8 questo il filo che lega Storia e biografie."
    ),

    # --- personaggi (quanti vuoi; "colore" opzionale) ---
    "personaggi": [
        {"nome": "Katar\u00edna", "ruolo": "PROTAGONISTA / VOCE NARRANTE",
         "testo": "Slovacca di Bratislava, vive a Praga. Torna a casa per Natale portando con "
                  "s\u00e9 l\u2019assenza del marito e un dolore non ancora dicibile. Rivive a ritroso "
                  "la propria storia: \u00e8 lei l\u2019asse attorno a cui ruotano tutte le altre figure."},
        {"nome": "Eugen", "ruolo": "IL MARITO (ASSENTE)",
         "testo": "Marito di Katar\u00edna, con cui lei aveva tentato la vita a Praga. L\u2019ha "
                  "abbandonata due mesi prima, lasciando solo un biglietto sul tavolo della "
                  "cucina. Presente per tutto il romanzo proprio attraverso la sua assenza, che "
                  "pesa e va spiegata agli altri."},
        {"nome": "Viera", "ruolo": "L\u2019AMICA / IL CONTRALTARE",
         "testo": "Compagna di universit\u00e0 di Katar\u00edna, emigrata in Italia grazie a una borsa "
                  "di studio; torna in Slovacchia sempre pi\u00f9 malvolentieri. Riavvicinandosi a "
                  "Katar\u00edna, ne diventa lo specchio: anche la sua \u00e8 una storia di strappo, "
                  "legata a Barbara."},
        {"nome": "Barbara", "ruolo": "L\u2019INSEGNANTE / IL LEGAME FERITO",
         "testo": "Era stata l\u2019insegnante di italiano di Katar\u00edna e Viera. \u00c8 al centro della "
                  "ferita che Viera si porta dentro: una relazione che ha lasciato un segno e "
                  "che alimenta il filone dei \u201cdesideri temuti e mai pronunciati\u201d del romanzo."},
    ],
    "personaggi_minori": (
        "Compaiono inoltre la <b>madre</b> di Katar\u00edna (a Bratislava, segnata da "
        "incomprensioni di lunga data con la figlia) e le altre <b>compagne di universit\u00e0</b>, "
        "sfondo corale del ritorno a casa."
    ),

    # --- rete delle relazioni: (A, simbolo, B, descrizione) ---
    "relazioni": [
        ("Katar\u00edna", "\u2014\u2715\u2192", "Eugen", "matrimonio interrotto: l\u2019abbandono con il biglietto"),
        ("Katar\u00edna", "\u2194", "Viera", "amicizia universitaria che si riannoda durante il Natale"),
        ("Viera", "\u2014\u2715\u2192", "Barbara", "ex insegnante di italiano: il legame ferito di Viera"),
        ("Katar\u00edna", "\u2248", "la madre", "rapporto teso, vecchie incomprensioni mai sciolte"),
        ("Slovacchia", "\u2014\u2715\u2192", "Rep. Ceca", "il \u201cdivorzio di velluto\u201d (1993): la separazione-cornice"),
    ],
    "relazioni_legenda": "\u2194 legame che si rinsalda \u00b7 \u2014\u2715\u2192 separazione/rottura "
                         "\u00b7 \u2248 rapporto irrisolto.",

    # --- temi: (nome, descrizione) ---
    "temi": [
        ("Sradicamento", "Perdere le radici e doversi reinventare altrove: la condizione di chi "
                         "vive sospeso tra il paese che ha lasciato e quello che lo ha accolto."),
        ("Assenza", "L\u2019assente (Eugen) pesa pi\u00f9 del presente. Il vuoto lasciato da chi se ne "
                    "va diventa il vero protagonista delle giornate di Katar\u00edna."),
        ("Memoria e Storia", "La vicenda privata si intreccia con la grande Storia: il regime, la "
                             "divisione del 1993, un\u2019identit\u00e0 collettiva che si rifonda."),
        ("Strappo e rinascita", "Ogni frattura chiede nuove risorse per essere ricomposta. Non "
                                "c\u2019\u00e8 consolazione facile, ma l\u2019apertura a un nuovo inizio."),
        ("Desideri taciuti", "Tradimenti e desideri \u201ctemuti e mai pronunciati\u201d: ci\u00f2 che resta "
                             "non detto pesa quanto ci\u00f2 che accade."),
        ("Lingua come scelta", "Tema anche autoriale: Kar\u0161aiov\u00e1 scrive in italiano, lingua "
                               "\u201celettiva\u201d \u2014 eco letteraria dello spaesamento dei personaggi."),
    ],

    # --- contesto (titolo + testo; None per omettere) ---
    "contesto_titolo": "Lo sfondo storico \u2013 Bratislava sotto il comunismo",
    "contesto_testo": (
        "Tra i ricordi della protagonista riaffiora la vita quotidiana nella Cecoslovacchia "
        "socialista: l\u2019<b>abolizione delle festivit\u00e0 cattoliche</b>, la <b>censura</b>, le "
        "<b>code</b> interminabili per la carne e per qualunque bene. Nel 1989 la <i>Rivoluzione "
        "di velluto</i> mette fine pacificamente al regime; pochi anni dopo, il 1\u00b0 gennaio 1993, "
        "il <i>divorzio di velluto</i> divide il paese in due Stati indipendenti. \u00c8 il terreno su "
        "cui maturano i personaggi: una generazione cresciuta nel grigiore e poi consegnata, "
        "quasi all\u2019improvviso, a una libert\u00e0 tutta da abitare."
    ),

    # --- chiave di lettura (riquadro evidenziato; None per omettere) ---
    "chiave": (
        "Tieni d\u2019occhio il parallelo costante tra <b>macro e micro</b>: ogni separazione "
        "politica trova un\u2019eco in una separazione intima. Il libro non promette ricuciture "
        "indolori, ma suggerisce che <i>sotto il buio scorre comunque la vita</i> \u2014 anche per "
        "chi, come Katar\u00edna, fatica a vederlo."
    ),

    # --- nota fonti a pie' pagina ---
    "fonti": "dati editoriali dalla scheda Feltrinelli e dalla candidatura al Premio Strega 2022",

    # --- nome file PDF (None = generato in automatico) ---
    "output": None,

    # --- ETICHETTE delle sezioni: cambia solo per adattare il genere ---
    "etichette": {
        "scheda_tecnica": None,                 # la griglia tecnica non ha titolo
        "sinossi": "La storia in breve",
        "titolo_senso": "Il senso del titolo",
        "personaggi": "I personaggi",
        "relazioni": "La rete delle relazioni",
        "temi": "I temi",
        "chiave": "Chiave di lettura",
        # per "contesto" il titolo e' il campo contesto_titolo (variabile per libro)
    },
}


# ====================================================================
#  ==== MOTORE ====  (NON modificare: garantisce l'omogeneita')
# ====================================================================
import re
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                TableStyle, Flowable, KeepTogether, HRFlowable)

# --- palette (standard della libreria) ---
WINE  = colors.HexColor("#6E1F2E")
PAPER = colors.HexColor("#F7F3EC")
CARD  = colors.HexColor("#FBF8F2")
INK   = colors.HexColor("#2B2622")
MUTED = colors.HexColor("#8A7F72")
GOLD  = colors.HexColor("#B08D57")
LINE  = colors.HexColor("#D9CFC0")
# colori striscia personaggi (ciclici)
STRIPE = [WINE, colors.HexColor("#4A5A6A"), colors.HexColor("#7A6A2F"),
          colors.HexColor("#6E3A52"), colors.HexColor("#3E5A4A"),
          colors.HexColor("#73523A")]

PAGE_W, PAGE_H = A4
LM = RM = 18 * mm
content_w = PAGE_W - LM - RM

def _st(name, **kw):
    base = dict(fontName="Times-Roman", textColor=INK, leading=14, fontSize=10)
    base.update(kw)
    return ParagraphStyle(name, **base)

S_kicker = _st("kicker", fontName="Helvetica-Bold", fontSize=8, textColor=GOLD, leading=11)
S_h      = _st("h", fontName="Helvetica-Bold", fontSize=11, textColor=WINE, leading=13, spaceAfter=2)
S_body   = _st("body", fontSize=10.3, leading=15, alignment=TA_JUSTIFY)
S_body_c = _st("bodyc", fontSize=10.3, leading=15)
S_small  = _st("small", fontSize=8.6, leading=11.5, textColor=MUTED)
S_meta   = _st("meta", fontName="Helvetica", fontSize=8.4, textColor=INK, leading=12)
S_metaL  = _st("metaL", fontName="Helvetica-Bold", fontSize=8.4, textColor=WINE, leading=12)
S_name   = _st("name", fontName="Times-Bold", fontSize=12.5, textColor=WINE, leading=14)
S_role   = _st("role", fontName="Helvetica-Bold", fontSize=7.2, textColor=colors.white, leading=10)
S_card   = _st("card", fontSize=9.3, leading=13.2, alignment=TA_JUSTIFY)


class Header(Flowable):
    """Banda di testata bordeaux con titolo, autore e tagline."""
    def __init__(self, w, titolo, autore_riga, tagline):
        super().__init__()
        self.w = w; self.h = 44 * mm
        self.titolo = titolo; self.autore_riga = autore_riga; self.tagline = tagline
    def wrap(self, *a):
        return self.w, self.h
    def draw(self):
        c = self.canv
        c.setFillColor(WINE); c.rect(0, 0, self.w, self.h, fill=1, stroke=0)
        c.setFillColor(GOLD); c.rect(0, 0, self.w, 1.6*mm, fill=1, stroke=0)
        c.setFillColor(GOLD); c.setFont("Helvetica-Bold", 8)
        c.drawString(7*mm, self.h-9*mm, "S C H E D A   D I   L E T T U R A")
        # titolo (riduce il corpo se molto lungo)
        size = 27
        while c.stringWidth(self.titolo, "Times-Bold", size) > self.w-14*mm and size > 15:
            size -= 1
        c.setFillColor(colors.white); c.setFont("Times-Bold", size)
        c.drawString(7*mm, self.h-22*mm, self.titolo)
        c.setFillColor(colors.HexColor("#F0E4D4")); c.setFont("Times-Italic", 13)
        c.drawString(7*mm, self.h-30*mm, self.autore_riga)
        c.setStrokeColor(GOLD); c.setLineWidth(0.6)
        c.line(7*mm, self.h-33.5*mm, self.w-7*mm, self.h-33.5*mm)
        if self.tagline:
            c.setFillColor(colors.HexColor("#E9DAC6")); c.setFont("Helvetica-Oblique", 8.6)
            c.drawString(7*mm, self.h-38*mm, self.tagline)


def _section(title):
    return Paragraph(title.upper(), S_h)

def _rule():
    return HRFlowable(width="100%", thickness=0.6, color=LINE, spaceBefore=2, spaceAfter=6)

def _role_tag(text, bg):
    t = Table([[Paragraph(text, S_role)]])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), bg),
        ("LEFTPADDING", (0,0), (-1,-1), 5), ("RIGHTPADDING", (0,0), (-1,-1), 5),
        ("TOPPADDING", (0,0), (-1,-1), 2.5), ("BOTTOMPADDING", (0,0), (-1,-1), 2.5),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ]))
    return t

def _card(p, color):
    inner = Table([
        [Paragraph(p["nome"], S_name)],
        [_role_tag(p["ruolo"], color)],
        [Spacer(1, 3)],
        [Paragraph(p["testo"], S_card)],
    ], colWidths=[content_w/2 - 12*mm])
    inner.setStyle(TableStyle([
        ("LEFTPADDING", (0,0), (-1,-1), 0), ("RIGHTPADDING", (0,0), (-1,-1), 0),
        ("TOPPADDING", (0,0), (-1,-1), 1), ("BOTTOMPADDING", (0,0), (-1,-1), 1),
        ("ALIGN", (0,1), (0,1), "LEFT"),
    ]))
    wrap = Table([["", inner]], colWidths=[2.4*mm, content_w/2 - 9*mm])
    wrap.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (0,-1), color), ("BACKGROUND", (1,0), (1,-1), CARD),
        ("BOX", (0,0), (-1,-1), 0.5, LINE),
        ("LEFTPADDING", (1,0), (1,-1), 7), ("RIGHTPADDING", (1,0), (1,-1), 7),
        ("TOPPADDING", (1,0), (1,-1), 7), ("BOTTOMPADDING", (1,0), (1,-1), 7),
        ("LEFTPADDING", (0,0), (0,-1), 0), ("RIGHTPADDING", (0,0), (0,-1), 0),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
    ]))
    return wrap

def _slug(s):
    s = s.lower()
    s = (s.replace("\u00e0","a").replace("\u00e1","a").replace("\u00e8","e")
          .replace("\u00e9","e").replace("\u00ec","i").replace("\u00ed","i")
          .replace("\u00f2","o").replace("\u00f3","o").replace("\u00f9","u")
          .replace("\u00fa","u").replace("\u0161","s").replace("\u010d","c")
          .replace("\u017e","z").replace("\u00fd","y"))
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return re.sub(r"-+", "-", s)


def build_scheda(libro, path=None):
    et = libro.get("etichette", {})
    # nome file
    if path is None:
        path = libro.get("output")
    if not path:
        cognome = _slug(libro["autore"].split()[-1])
        titolo = "-".join(_slug(libro["titolo"]).split("-")[:3])
        path = f"{cognome}_{titolo}_scheda.pdf"

    doc = SimpleDocTemplate(path, pagesize=A4, leftMargin=LM, rightMargin=RM,
                            topMargin=12*mm, bottomMargin=12*mm,
                            title=f"{libro['titolo']} \u2013 Scheda di lettura",
                            author="Scheda di lettura")

    def _bg(canvas, d):
        canvas.saveState()
        canvas.setFillColor(PAPER); canvas.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
        canvas.setFillColor(MUTED); canvas.setFont("Helvetica", 7)
        canvas.drawString(LM, 8*mm, f"Scheda di lettura \u00b7 {libro['titolo']}")
        canvas.drawRightString(PAGE_W-RM, 8*mm, "pag. %d" % d.page)
        canvas.restoreState()

    story = []

    # --- testata ---
    autore_riga = libro["autore"]
    if libro.get("editore"):
        autore_riga += "  \u00b7  " + libro["editore"]
    story.append(Header(content_w, libro["titolo"], autore_riga, libro.get("tagline")))
    story.append(Spacer(1, 6))

    # --- scheda tecnica (griglia 2 coppie per riga) ---
    fields = []
    if libro.get("autore_info"):   fields.append(("AUTORE", f"{libro['autore']} ({libro['autore_info']})"))
    elif libro.get("autore"):      fields.append(("AUTORE", libro["autore"]))
    if libro.get("editore"):       fields.append(("EDITORE", libro["editore"]))
    if libro.get("pagine"):        fields.append(("PAGINE", str(libro["pagine"])))
    if libro.get("lingua"):        fields.append(("LINGUA", libro["lingua"]))
    if libro.get("riconoscimenti"):fields.append(("RICONOSCIMENTI", libro["riconoscimenti"]))
    meta_rows = []
    for i in range(0, len(fields), 2):
        l1, v1 = fields[i]
        if i+1 < len(fields):
            l2, v2 = fields[i+1]
        else:
            l2, v2 = "", ""
        meta_rows.append([Paragraph(l1, S_metaL), Paragraph(v1, S_meta),
                          Paragraph(l2, S_metaL) if l2 else "", Paragraph(v2, S_meta) if v2 else ""])
    if meta_rows:
        mt = Table(meta_rows, colWidths=[content_w*0.19, content_w*0.31,
                                         content_w*0.19, content_w*0.31])
        mt.setStyle(TableStyle([
            ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
            ("TOPPADDING", (0,0), (-1,-1), 3), ("BOTTOMPADDING", (0,0), (-1,-1), 3),
            ("LEFTPADDING", (0,0), (-1,-1), 2),
            ("BACKGROUND", (0,0), (-1,-1), CARD), ("BOX", (0,0), (-1,-1), 0.5, LINE),
            ("LINEBELOW", (0,0), (-1,-2), 0.4, LINE),
        ]))
        story.append(mt); story.append(Spacer(1, 10))

    # --- la storia in breve ---
    if libro.get("sinossi"):
        story.append(_section(et.get("sinossi") or "La storia in breve"))
        story.append(_rule())
        story.append(Paragraph(libro["sinossi"], S_body)); story.append(Spacer(1, 9))

    # --- il senso del titolo ---
    if libro.get("titolo_senso"):
        story.append(_section(et.get("titolo_senso") or "Il senso del titolo"))
        story.append(_rule())
        story.append(Paragraph(libro["titolo_senso"], S_body)); story.append(Spacer(1, 11))

    # --- personaggi ---
    pers = libro.get("personaggi") or []
    if pers:
        story.append(_section(et.get("personaggi") or "I personaggi"))
        story.append(_rule())
        cards = []
        for idx, p in enumerate(pers):
            col = colors.HexColor(p["colore"]) if p.get("colore") else STRIPE[idx % len(STRIPE)]
            cards.append(_card(p, col))
        for i in range(0, len(cards), 2):
            left = cards[i]
            right = cards[i+1] if i+1 < len(cards) else ""
            row = Table([[left, right]], colWidths=[content_w/2 - 3*mm, content_w/2 - 3*mm])
            row.setStyle(TableStyle([
                ("VALIGN",(0,0),(-1,-1),"TOP"),
                ("LEFTPADDING",(0,0),(-1,-1),0),("RIGHTPADDING",(0,0),(0,0),6),
                ("RIGHTPADDING",(1,0),(1,0),0),
                ("TOPPADDING",(0,0),(-1,-1),0),("BOTTOMPADDING",(0,0),(-1,-1),0),
            ]))
            story.append(row); story.append(Spacer(1, 6))
        if libro.get("personaggi_minori"):
            story.append(Paragraph(libro["personaggi_minori"], S_small))
        story.append(Spacer(1, 11))

    # --- rete delle relazioni (tenuta insieme) ---
    rel = libro.get("relazioni") or []
    if rel:
        block = [_section(et.get("relazioni") or "La rete delle relazioni"), _rule()]
        rows = [[Paragraph("<b>"+a+"</b>", S_body_c),
                 Paragraph('<font color="#6E1F2E"><b>'+s+'</b></font>', S_body_c),
                 Paragraph("<b>"+b+"</b>", S_body_c),
                 Paragraph(d, S_body_c)] for (a,s,b,d) in rel]
        rt = Table(rows, colWidths=[content_w*0.18, content_w*0.09,
                                    content_w*0.18, content_w*0.55])
        rt.setStyle(TableStyle([
            ("VALIGN",(0,0),(-1,-1),"MIDDLE"), ("ALIGN",(1,0),(1,-1),"CENTER"),
            ("TOPPADDING",(0,0),(-1,-1),4), ("BOTTOMPADDING",(0,0),(-1,-1),4),
            ("LEFTPADDING",(0,0),(-1,-1),6),
            ("ROWBACKGROUNDS",(0,0),(-1,-1),[CARD, PAPER]),
            ("BOX",(0,0),(-1,-1),0.5,LINE), ("LINEBELOW",(0,0),(-1,-2),0.3,LINE),
        ]))
        block.append(rt)
        if libro.get("relazioni_legenda"):
            block.append(Paragraph("Legenda:  " + libro["relazioni_legenda"], S_small))
        story.append(KeepTogether(block)); story.append(Spacer(1, 12))

    # --- temi ---
    temi = libro.get("temi") or []
    if temi:
        story.append(_section(et.get("temi") or "I temi"))
        story.append(_rule())
        rows = [[Paragraph("<b>"+t+"</b>", S_body_c), Paragraph(d, S_body_c)] for (t,d) in temi]
        tt = Table(rows, colWidths=[content_w*0.27, content_w*0.73])
        tt.setStyle(TableStyle([
            ("VALIGN",(0,0),(-1,-1),"TOP"),
            ("TOPPADDING",(0,0),(-1,-1),5), ("BOTTOMPADDING",(0,0),(-1,-1),5),
            ("LEFTPADDING",(0,0),(-1,-1),6), ("RIGHTPADDING",(0,0),(-1,-1),6),
            ("ROWBACKGROUNDS",(0,0),(-1,-1),[CARD, PAPER]),
            ("BOX",(0,0),(-1,-1),0.5,LINE), ("LINEAFTER",(0,0),(0,-1),0.4,LINE),
            ("LINEBELOW",(0,0),(-1,-2),0.3,LINE),
        ]))
        story.append(tt); story.append(Spacer(1, 12))

    # --- contesto ---
    if libro.get("contesto_testo"):
        story.append(_section(libro.get("contesto_titolo") or "Contesto"))
        story.append(_rule())
        story.append(Paragraph(libro["contesto_testo"], S_body)); story.append(Spacer(1, 14))

    # --- chiave di lettura ---
    if libro.get("chiave"):
        kl = Table([[Paragraph((et.get("chiave") or "Chiave di lettura").upper(), S_kicker)],
                    [Paragraph(libro["chiave"], S_body_c)]], colWidths=[content_w-12])
        kl.setStyle(TableStyle([
            ("BACKGROUND",(0,0),(-1,-1), colors.HexColor("#F1E7D6")),
            ("BOX",(0,0),(-1,-1), 0.8, GOLD),
            ("LEFTPADDING",(0,0),(-1,-1),12), ("RIGHTPADDING",(0,0),(-1,-1),12),
            ("TOPPADDING",(0,0),(0,0),10), ("BOTTOMPADDING",(0,1),(0,1),11),
            ("TOPPADDING",(0,1),(0,1),2),
        ]))
        story.append(KeepTogether(kl)); story.append(Spacer(1, 10))

    # --- nota fonti ---
    fonti = libro.get("fonti")
    nota = "Scheda di sintesi a uso personale"
    if fonti:
        nota += "; " + fonti + "."
    else:
        nota += "."
    story.append(Paragraph(nota, S_small))

    doc.build(story, onFirstPage=_bg, onLaterPages=_bg)
    return path


if __name__ == "__main__":
    out = build_scheda(LIBRO)
    print("PDF generato:", out)
