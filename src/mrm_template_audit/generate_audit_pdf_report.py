import os
from datetime import datetime
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib.enums import TA_CENTER, TA_LEFT

# Define professional business colors
COLOR_PRIMARY = colors.HexColor("#2C3E50")  # Dark Blue/Grey
COLOR_SECONDARY = colors.HexColor("#95A5A6") # Grey
COLOR_PASS = colors.HexColor("#27AE60")      # Green
COLOR_WARNING = colors.HexColor("#F39C12")   # Orange
COLOR_FAIL = colors.HexColor("#C0392B")      # Red
COLOR_TEXT = colors.HexColor("#333333")


def get_corporate_styles():
    """Defines and returns custom ParagraphStyles for the report."""
    styles = getSampleStyleSheet()
    
    # Title (Business Report Header)
    styles.add(ParagraphStyle(
        name='CorporateTitle',
        parent=styles['Title'],
        fontName='Helvetica-Bold',
        fontSize=26,
        leading=32,
        textColor=COLOR_PRIMARY,
        alignment=TA_CENTER,
        spaceAfter=30
    ))
    
    # Subtitle (File Names)
    styles.add(ParagraphStyle(
        name='CorporateSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=12,
        textColor=COLOR_SECONDARY,
        alignment=TA_CENTER,
        spaceAfter=50
    ))

    # Section Headers (1. Executive Summary, 2. Integrity)
    styles.add(ParagraphStyle(
        name='SectionHeader',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=18,
        textColor=COLOR_PRIMARY,
        spaceBefore=20,
        spaceAfter=15,
        borderWidth=1,
        borderColor=COLOR_SECONDARY,
        borderPadding=5,
        backColor=colors.HexColor("#ECF0F1")
    ))

    # Subsection Headers (A. Compliance Gaps)
    styles.add(ParagraphStyle(
        name='SubSectionHeader',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=14,
        textColor=COLOR_PRIMARY,
        spaceBefore=15,
        spaceAfter=10
    ))

    # Standard body text
    styles.add(ParagraphStyle(
        name='CorporateBody',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=11,
        textColor=COLOR_TEXT,
        leading=14,
        spaceAfter=10
    ))

    # Bulleted lists
    styles.add(ParagraphStyle(
        name='BulletText',
        parent=styles['CorporateBody'],
        leftIndent=20,
        firstLineIndent=-10,
        spaceBefore=5
    ))
    
    # Status Icons (Pass/Fail)
    styles.add(ParagraphStyle(
        name='StatusPass',
        parent=styles['CorporateBody'],
        fontName='Helvetica-Bold',
        textColor=COLOR_PASS,
        fontSize=12
    ))
    styles.add(ParagraphStyle(
        name='StatusFail',
        parent=styles['CorporateBody'],
        fontName='Helvetica-Bold',
        textColor=COLOR_FAIL,
        fontSize=12
    ))

    return styles


def generate_audit_pdf_report(
                                audit_results, 
                                #model_filename, 
                                #template_filename, 
                                output_filename):
    """
    Generates a professional, visually appealing PDF business report explaining audit findings.
    
    This function structures findings (internal discrepancies, template compliance gaps, 
    and successful alignments) into a branded PDF format with corporate styling.

    Args:
        audit_results (dict): The dictionary output from audit_model_document.
        #model_filename (str): The filename of the model document audited.
        #template_filename (str): The filename of the template used as reference.
        output_filename (str): The desired path/filename for the generated PDF.
    """
    
    # 1. Initialize Document Template and Styles
    doc = SimpleDocTemplate(output_filename, pagesize=LETTER,
                            rightMargin=inch, leftMargin=inch,
                            topMargin=inch, bottomMargin=inch)
    styles = get_corporate_styles()
    story = [] # The container for Platypus objects (paragraphs, tables, charts)
    
    # Define timestamps for referencing
    generation_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # =========================================================================
    # --- REPORT HEADER (Branding) ---
    # =========================================================================
    model_filename = audit_results["audited_file_name"]
    template_filename = audit_results["template_file_name"]
    story.append(Paragraph("DOCUMENT AUDIT REPORT", styles['CorporateTitle']))
    story.append(Paragraph(f"Model: {model_filename}<br/>Template: {template_filename}", styles['CorporateSubtitle']))
    
    # Reference Information Table (Branded style)
    ref_data = [
        [Paragraph("<b>Audit ID:</b>", styles['CorporateBody']), Paragraph(f"AUDIT-{datetime.now().strftime('%Y%m%d %H%M%S')}", styles['CorporateBody'])],
        [Paragraph("<b>Report Generated:</b>", styles['CorporateBody']), Paragraph(f"{generation_date}", styles['CorporateBody'])],
        [Paragraph("<b>Analysis Basis:</b>", styles['CorporateBody']), Paragraph("WordprocessingML Structure, Headings & Numbering Resolution", styles['CorporateBody'])]
    ]
    ref_table = Table(ref_data, colWidths=[1.8*inch, 4.2*inch])
    ref_table.setStyle(TableStyle([
        ('GRID', (0, 0), (-1, -1), 0.5, COLOR_SECONDARY),
        ('BACKGROUND', (0, 0), (0, -1), colors.HexColor("#F8F9F9")),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
    ]))
    story.append(ref_table)
    story.append(Spacer(1, 0.5*inch))


    # =========================================================================
    # --- 1. EXECUTIVE SUMMARY ---
    # =========================================================================
    story.append(Paragraph("1. EXECUTIVE SUMMARY", styles['SectionHeader']))
    
    # Calculate key metrics
    int_errs = len(audit_results["internal_discrepancies"])
    tpl_errs = len(audit_results["template_discrepancies"])
    total_issues = int_errs + tpl_errs
    
    # Set overall status branding
    if total_issues == 0:
        status_text = "<b><font color='{}'>✅ COMPLIANT</font></b>".format(COLOR_PASS.hexval())
        summary_details = "The audit detected zero critical deviations. The model document adheres to internal integrity standards and matches the structural mandates of the reference template."
    else:
        status_text = "<b><font color='{}'>⚠️ ATTENTION REQUIRED</font></b>".format(COLOR_FAIL.hexval())
        summary_details = f"The audit detected {total_issues} structural or integrity issues requiring remediation. Please review Section 2 and Section 3 for specific details."

    story.append(Paragraph(f"<b>Overall Audit Status:</b> {status_text}", styles['CorporateBody']))
    story.append(Paragraph(summary_details, styles['CorporateBody']))
    story.append(Spacer(1, 0.2*inch))


    # =========================================================================
    # --- 2. INTERNAL INTEGRITY (TOC Sync) ---
    # =========================================================================
    story.append(Paragraph("2. INTERNAL INTEGRITY (TOC SYNCHRONIZATION)", styles['SectionHeader']))
    
    if int_errs == 0:
        story.append(Paragraph("✅ <b>PASS:</b> The literal Table of Contents is fully synchronized with the actual document headings.", styles['StatusPass']))
    else:
        story.append(Paragraph(f"❌ <b>{int_errs} Discrepancy(ies) Detected:</b> TOC is out of sync with body content.", styles['StatusFail']))
        
        # Build Table for Discrepancies
        discrepancy_data = [["#", "Issue Type", "Location (TOC)", "Technical Details"]]
        for idx, err in enumerate(audit_results["internal_discrepancies"], 1):
            discrepancy_data.append([
                Paragraph(str(idx), styles['CorporateBody']),
                Paragraph(f"<b>{err['issue']}</b>", styles['CorporateBody']),
                Paragraph(err['toc_location'] if 'toc_location' in err else "N/A", styles['CorporateBody']),
                Paragraph(err['details'], styles['CorporateBody'])
            ])
            
        discrepancy_table = Table(discrepancy_data, colWidths=[0.4*inch, 1.8*inch, 1.2*inch, 2.6*inch])
        discrepancy_table.setStyle(TableStyle([
            ('GRID', (0, 0), (-1, -1), 0.5, COLOR_SECONDARY),
            ('BACKGROUND', (0, 0), (-1, 0), COLOR_PRIMARY), # Header row blue
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 10),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
            ('TOPPADDING', (0, 0), (-1, -1), 6),
        ]))
        story.append(discrepancy_table)

    story.append(Spacer(1, 0.3*inch))


    # =========================================================================
    # --- 3. TEMPLATE COMPLIANCE & STRUCTURE ---
    # =========================================================================
    story.append(Paragraph("3. TEMPLATE COMPLIANCE & STRUCTURE", styles['SectionHeader']))
    
    # Sub-Categorize Findings for easier reference
    missing = [e for e in audit_results["template_discrepancies"] if "Missing Mandatory" in e['issue']]
    numbering = [e for e in audit_results["template_discrepancies"] if "Incorrect Section Numbering" in e['issue']]
    extra = [e for e in audit_results["template_discrepancies"] if "Extra/Non-Standard" in e['issue']]
    
    # 3A. Successful Pass (Compliant Sections)
    story.append(Paragraph("A. Compliant Standard Sections", styles['SubSectionHeader']))
    
    # Identify passed sections (Template items NOT in missing list)
    all_tpl_sections = {item['heading_text'].lower() for item in audit_results["template_structure"]}
    missing_texts = {e['section'].lower() for e in missing}
    passed_sections = all_tpl_sections - missing_texts

    if passed_sections:
        story.append(Paragraph("✅ The following sections exist, are correctly numbered, and follow standard mandates:", styles['StatusPass']))
        passed_list = " | ".join([s.title() for s in sorted(passed_sections)])
        story.append(Paragraph(f"<i>{passed_list}</i>", styles['CorporateBody']))
    else:
        story.append(Paragraph("⚠️ No compliant standard sections were detected in the model document.", styles['StatusPass']))
    
    story.append(Spacer(1, 0.15*inch))
    
    # 3B. Structural Gaps (Critical Discrepancies)
    story.append(Paragraph("B. Structural & Compliance Gaps", styles['SubSectionHeader']))
    
    if tpl_errs == 0:
        story.append(Paragraph("✅ <b>PASS:</b> No critical structural gaps were detected between the Model and the Template.", styles['StatusPass']))
    else:
        story.append(Paragraph(f"❌ <b>{tpl_errs} Non-Compliance Issues Detected:</b> Action is required to meet corporate standards.", styles['StatusFail']))
        story.append(Spacer(1, 0.1*inch))
        
        # Build Findings Table
        findings_data = [["Category", "Section Text", "Discrepancy Description"]]
        
        # Missing (Red Highlight)
        for m in missing:
            findings_data.append([
                Paragraph(f"<b><font color='{COLOR_FAIL.hexval()}'>Missing Mandatory</font></b>", styles['CorporateBody']),
                Paragraph(m['section'], styles['CorporateBody']),
                Paragraph("Section required by template but omitted.", styles['CorporateBody'])
            ])
            
        # Numbering (Orange Highlight)
        for n in numbering:
             findings_data.append([
                Paragraph(f"<b><font color='{COLOR_WARNING.hexval()}'>Incorrect Hierarchy</font></b>", styles['CorporateBody']),
                Paragraph(n['section'], styles['CorporateBody']),
                Paragraph(n['details'], styles['CorporateBody'])
            ])
             
        # Extra (Grey/Info Highlight)
        for ex in extra:
            # CORRECT
            findings_data.append([
                Paragraph(f"<b>Extra Section</b>", styles['CorporateBody']), # Removed the rogue </font>
                Paragraph(ex['section'], styles['CorporateBody']),
                Paragraph("Section is not defined in standard template.", styles['CorporateBody'])
            ])
            
        findings_table = Table(findings_data, colWidths=[1.8*inch, 1.8*inch, 2.4*inch])
        findings_table.setStyle(TableStyle([
            ('GRID', (0, 0), (-1, -1), 0.5, COLOR_SECONDARY),
            ('BACKGROUND', (0, 0), (-1, 0), COLOR_SECONDARY), # Grey header row
            ('TEXTCOLOR', (0, 0), (-1, 0), COLOR_TEXT),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
            ('TOPPADDING', (0, 0), (-1, -1), 6),
        ]))
        story.append(findings_table)


    story.append(PageBreak()) # Move Disclaimer to own page for professional look
    
    # =========================================================================
    # --- DISCLAIMER ---
    # =========================================================================
    story.append(Spacer(1, 2*inch))
    story.append(Paragraph("Audit Notes & Disclaimers", styles['SubSectionHeader']))
    disclaimer_text = """
    This automated document audit is based on parsing Microsoft WordprocessingML (XML) structures 
    and interpreting user-defined styles (Heading 1-9) and numbering instances. While highly reliable for 
    detecting structural and hierarchy mismatches, this audit does not assess the *semantic content* or accuracy 
    of the text within those sections. Deviations may result from improper use of styles in the source document 
    or custom manual numbering overrides that bypass standard Word definitions. This report is part of the model 
    governance process and should be reviewed alongside human validation.
    """
    story.append(Paragraph(disclaimer_text, styles['CorporateBody']))


    # =========================================================================
    # --- PDF GENERATION ---
    # =========================================================================
    # Create the PDF
    try:
        doc.build(story)
        print(f"✅ Success: Professional Audit PDF Report generated at: {os.path.abspath(output_filename)}")
    except Exception as e:
        print(f"❌ Error: PDF generation failed. {e}")


