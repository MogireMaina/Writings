from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN

# Create presentation
prs = Presentation()
prs.slide_width = Inches(10)
prs.slide_height = Inches(7.5)

# Slide 1: Title Slide
slide1 = prs.slides.add_slide(prs.slide_layouts[6])  # Blank layout
title_box = slide1.shapes.add_textbox(Inches(1), Inches(2.5), Inches(8), Inches(1.5))
title_frame = title_box.text_frame
title_frame.text = "Qatar as a Legal Chokepoint:\nEconomic Warfare and International Law"
title_para = title_frame.paragraphs[0]
title_para.font.size = Pt(32)
title_para.font.bold = True
title_para.alignment = PP_ALIGN.CENTER

subtitle_box = slide1.shapes.add_textbox(Inches(1), Inches(4.5), Inches(8), Inches(2))
subtitle_frame = subtitle_box.text_frame
subtitle_frame.word_wrap = True
subtitle_text = subtitle_frame.paragraphs[0]
subtitle_text.text = "Good afternoon. My thesis investigates Qatar as a legal chokepoint, examining how economic warfare exposes critical gaps in international law when dominant powers weaponise interdependence at strategic infrastructure nodes."
subtitle_text.font.size = Pt(18)
subtitle_text.alignment = PP_ALIGN.CENTER

# Slide 2: Core Claims
slide2 = prs.slides.add_slide(prs.slide_layouts[6])
title2 = slide2.shapes.add_textbox(Inches(0.5), Inches(0.3), Inches(9), Inches(0.6))
title2.text_frame.text = "Core Claims"
title2.text_frame.paragraphs[0].font.size = Pt(32)
title2.text_frame.paragraphs[0].font.bold = True

content2 = slide2.shapes.add_textbox(Inches(0.5), Inches(1.1), Inches(9), Inches(6))
tf2 = content2.text_frame
tf2.word_wrap = True

p1 = tf2.paragraphs[0]
p1.text = "My research advances three interconnected claims. First, Qatar faces unique transnational legal exposure because it shares the world's largest natural gas reserve with Iran. US sanctions imposed by the Office of Foreign Assets Control operate extraterritorially, overriding Qatar's territorial sovereignty. Even without Qatar's consent, OFAC sets the regulatory boundaries within which Qatar exploits its hydrocarbon resources, reducing sovereignty from substantive to nominal control."
p1.font.size = Pt(16)
p1.space_after = Pt(14)

p2 = tf2.add_paragraph()
p2.text = "Second, I argue this strategic coercion through economic interdependence fundamentally contradicts the dominant legal doctrine of state sovereignty within international law. The weaponisation of interdependence through secondary sanctions and extraterritorial regimes erodes Qatar's sovereign authority, breaching protections under UNCLOS Articles 56 and 77, as well as Qatar's Law No. 8 of 2004 concerning exclusive sovereign rights over maritime resources."
p2.font.size = Pt(16)
p2.space_after = Pt(14)

p3 = tf2.add_paragraph()
p3.text = "Third, Qatar's multi-forum legal strategy during the 2017-2021 blockade—bringing cases simultaneously to the ICJ, ICAO Council, and CERD Committee—revealed that current legal systems provide little protection against economic pressure on chokepoint states, potentially encouraging future blockades."
p3.font.size = Pt(16)

# Slide 3: Research Methodology
slide3 = prs.slides.add_slide(prs.slide_layouts[6])
title3 = slide3.shapes.add_textbox(Inches(0.5), Inches(0.3), Inches(9), Inches(0.6))
title3.text_frame.text = "Research Methodology"
title3.text_frame.paragraphs[0].font.size = Pt(32)
title3.text_frame.paragraphs[0].font.bold = True

content3 = slide3.shapes.add_textbox(Inches(0.5), Inches(1.1), Inches(9), Inches(6))
tf3 = content3.text_frame
tf3.word_wrap = True

m1 = tf3.paragraphs[0]
m1.text = "I employ three methodological frameworks. Doctrinal legal analysis examines sovereignty principles, jurisdictional doctrines, and treaty obligations, revealing that remedies remain procedural rather than substantive. Comparative case studies of Qatar, Russia, Iran, and Taiwan demonstrate that international law distinguishes by legal form—blockade, sanctions, export controls—rather than economic effect. While territorial blockades trigger aviation frameworks, functional blockades via insurance denial or technology export controls have no legal remedy despite identical coercive impact."
m1.font.size = Pt(16)
m1.space_after = Pt(14)

m2 = tf3.add_paragraph()
m2.text = "Following McCrudden's interdisciplinary framework, I integrate economic analysis to understand why economic power overrides legal validity. The Russian oil price cap illustrates this perfectly: it works through market control—the West controls 95% of maritime insurance—not through clear legal authority."
m2.font.size = Pt(16)

# Slide 4: Key Findings
slide4 = prs.slides.add_slide(prs.slide_layouts[6])
title4 = slide4.shapes.add_textbox(Inches(0.5), Inches(0.3), Inches(9), Inches(0.6))
title4.text_frame.text = "Key Findings"
title4.text_frame.paragraphs[0].font.size = Pt(32)
title4.text_frame.paragraphs[0].font.bold = True

content4 = slide4.shapes.add_textbox(Inches(0.5), Inches(1.1), Inches(9), Inches(6))
tf4 = content4.text_frame
tf4.word_wrap = True

f1 = tf4.paragraphs[0]
f1.text = "The ICJ affirmed jurisdiction over Qatar's case in 2020, but the matter settled in 2021 without merits determination or compensation. This reveals that international law provides formal remedies but no practical protection—it is reactive, not preventative."
f1.font.size = Pt(16)
f1.space_after = Pt(14)

f2 = tf4.add_paragraph()
f2.text = "Current law fails to recognize functional equivalence. Fishman's concept of \"invisible infrastructure\"—dollar clearing systems, SWIFT networks, maritime insurance—enables economic warfare without military force, showing how compliance infrastructures have privatised enforcement of state policy."
f2.font.size = Pt(16)

# Slide 5: Lessons Learned and Future Direction
slide5 = prs.slides.add_slide(prs.slide_layouts[6])
title5 = slide5.shapes.add_textbox(Inches(0.5), Inches(0.3), Inches(9), Inches(0.6))
title5.text_frame.text = "Lessons Learned and Future Direction"
title5.text_frame.paragraphs[0].font.size = Pt(28)
title5.text_frame.paragraphs[0].font.bold = True

content5 = slide5.shapes.add_textbox(Inches(0.5), Inches(1.1), Inches(9), Inches(6))
tf5 = content5.text_frame
tf5.word_wrap = True

l1 = tf5.paragraphs[0]
l1.text = "Incorporating feedback from previous sessions significantly strengthened this work. I enhanced specificity throughout my analysis, reorganized research questions from broad to specific, corrected citation formatting, and most critically, strengthened my methodological justification. I clarified why doctrinal analysis alone cannot explain how economic power overcomes legal validity, necessitating comparative and interdisciplinary approaches."
l1.font.size = Pt(16)
l1.space_after = Pt(14)

l2 = tf5.add_paragraph()
l2.text = "My research proposes developing an effect-based taxonomy with empirical thresholds—such as insurance market concentration levels or shipping route extension distances—that courts can apply when chokepoint states allege functional strangulation. This addresses the fundamental gap: international law currently lacks categories adequate to weaponised interdependence at critical infrastructure nodes. Thank you."
l2.font.size = Pt(16)

# Save presentation
prs.save('/home/user/Writings/Qatar_Legal_Chokepoint_Presentation.pptx')
print("Presentation created successfully with prose content!")
