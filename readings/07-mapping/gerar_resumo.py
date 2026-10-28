from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from pathlib import Path

OUT=Path(__file__).with_name('leonardo-freitas.pdf')
W,H=A4
FONT='ManuscritoDigital'
pdfmetrics.registerFont(TTFont(FONT, '/usr/share/fonts/truetype/dejavu/DejaVuSerif-Italic.ttf'))

p = [
"O artigo de Hernán Nina Hanco, José Antonio Pow-Sang e Mónica Villavicencio apresenta um mapeamento sistemático das pesquisas sobre desenvolvimento seguro de software. A ideia central é identificar quais práticas de segurança recebem mais atenção nos estudos e quais ainda precisam ser aprofundadas. A segurança não deve ser tratada só depois que o programa está pronto, mas durante todo o seu desenvolvimento.",
"Os autores utilizaram uma estratégia de busca chamada PICo, considerando desenvolvimento de software, software seguro e o contexto da indústria. Pesquisaram publicações em bases científicas como Scopus, Web of Science, IEEE Xplore e ACM. Foram identificados 867 trabalhos, dos quais 528 foram selecionados para a análise. Assim, o estudo apresenta uma visão ampla das tendências encontradas na literatura.",
"Os resultados foram organizados em quatro etapas do processo. Nos requisitos, destacam-se a identificação das necessidades de segurança e os casos de mau uso, que ajudam a prever possíveis ataques. No projeto, aparecem a modelagem de ameaças, os padrões de segurança e a proteção de sistemas baseados em componentes. Na construção, os assuntos mais frequentes são análise estática de código e detecção de vulnerabilidades. Nos testes, destacam-se a varredura de falhas e os testes de invasão.",
"A pesquisa também observa que muitos desenvolvedores precisam de mais capacitação e apoio especializado para aplicar segurança no dia a dia. Embora existam modelos, metodologias e ferramentas, nenhum recurso isolado resolve todos os problemas. É importante escolher técnicas adequadas à fase do projeto e manter avaliações constantes.",
"Concluo que desenvolver software seguro é uma responsabilidade contínua. O estudo mostra que prevenir falhas exige atenção aos requisitos, ao desenho da solução, à programação e aos testes. Para a Engenharia de Software, a principal lição é integrar a segurança desde o começo, em vez de depender apenas de correções depois da entrega."
]

c=canvas.Canvas(str(OUT), pagesize=A4, pageCompression=1)
c.setTitle('L2-07 - Mapeamento sistemático da literatura sobre desenvolvimento seguro de software - modelo digital')
c.setAuthor('Leonardo Freitas - resumo digital para transcrição manual')
c.setFillColor(HexColor('#FFFEFC'));c.rect(0,0,W,H,stroke=0,fill=1)
# linhas delicadas semelhantes ao papel A4; nao representam manuscrito autentico
c.setStrokeColor(HexColor('#DBE5F2'));c.setLineWidth(.45)
for y in range(92,750,23):c.line(46,y,W-45,y)
blue=HexColor('#25458F')
c.setFillColor(blue)
c.setFont(FONT,19.5)
c.drawString(52,H-61,'L2-07 — Desenvolvimento seguro de software')
c.setStrokeColor(blue); c.line(52,H-67,476,H-67)
c.setFont(FONT,12.5)
c.drawString(52,H-86,'Leonardo Freitas   |   Segurança e Teste de Software')

size=12.7
leading=18.0
y=H-121
maxw=W-106
for para in p:
    words=para.split();line=''
    lines=[]
    for word in words:
        candidate=(line+' '+word).strip()
        if pdfmetrics.stringWidth(candidate, FONT, size) <= maxw:
            line=candidate
        else:
            if line:lines.append(line)
            line=word
    if line:lines.append(line)
    for line in lines:
        if y<107: raise ValueError(f'PDF exceeds page; y={y}; line={line!r}')
        c.setFillColor(blue);c.setFont(FONT,size);c.drawString(52,y,line)
        y-=leading
    y-=9

c.setFillColor(HexColor('#616E86'));c.setFont('Helvetica',7.4)
c.drawCentredString(W/2,65,'MODELO DIGITAL COM TIPOGRAFIA EM ESTILO MANUSCRITO — NÃO É TEXTO ESCRITO À MÃO')
c.drawCentredString(W/2,53,'Artigo: Nina Hanco, Pow-Sang e Villavicencio. IEEE Access 9 (2021), 36852–36867.')
c.drawCentredString(W/2,41,'DOI: 10.1109/ACCESS.2021.3062388  |  Transcrever em A4 para atender à exigência do professor.')
c.save()
print('created',OUT,'last_y',y,'size',OUT.stat().st_size)