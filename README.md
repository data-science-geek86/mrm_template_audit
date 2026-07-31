# Function Documentation: `generate_audit_pdf_report`

The `generate_audit_pdf_report` function generates a formatted, corporate-branded PDF document summarizing the results of an automated Model Risk Management (MRM) document audit.

---

## 📋 Table of Contents
1. [Overview](#overview)
2. [Dependencies](#dependencies)
3. [Function Signature](#function-signature)
4. [Input Data Structure](#input-data-structure)
5. [Report Architecture](#report-architecture)
6. [Usage Example](#usage-example)

---

## Overview

This function converts structured output dictionary data from an XML/WordprocessingML document audit into a ReportLab PDF document.

### Features
* **Branded Report Header:** Dynamic generation date, audit ID, and file references.
* **Executive Summary:** High-level audit status (`COMPLIANT` vs `ATTENTION REQUIRED`).
* **Internal Integrity (TOC Sync):** Tabulated comparison of Table of Contents vs. actual body headings.
* **Template Compliance & Structure:** Categorized analysis for missing mandatory sections, incorrect section numbering, and extra non-standard sections.
* **Audit Disclaimers:** Standard governance disclaimer included on a dedicated final page.

---

## Dependencies

### Python Libraries
* `reportlab` (`SimpleDocTemplate`, `Paragraph`, `Table`, `TableStyle`, `Spacer`, `PageBreak`, `colors`, `inch`, `LETTER`)
* `datetime` (`datetime`)
* `os` (`os.path.abspath`)

### External Styles/Constants
The function expects the following variables/methods in scope:
* `get_corporate_styles()`
* `COLOR_PASS`, `COLOR_FAIL`, `COLOR_WARNING`, `COLOR_PRIMARY`, `COLOR_SECONDARY`, `COLOR_TEXT`

---

## Function Signature

```python
def generate_audit_pdf_report(audit_results: dict, output_filename: str) -> None

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
	
```

The audit_results parameter expects the following schema:
{
  "audited_file_name": "Model_Validation_2026.docx",
  "template_file_name": "Corporate_Model_Template_v2.docx",
  "internal_discrepancies": [
    {
      "issue": "Heading Mismatch",
      "toc_location": "Section 2.1",
      "details": "TOC label does not match document section heading."
    }
  ],
  "template_discrepancies": [
    {
      "issue": "Missing Mandatory Section",
      "section": "3. Risk Assessment",
      "details": "Section missing in target document."
    },
    {
      "issue": "Incorrect Section Numbering",
      "section": "4. Model Testing",
      "details": "Found numbered as 4.1 instead of 4.0."
    },
    {
      "issue": "Extra/Non-Standard Section",
      "section": "5. Appendix C",
      "details": "Section not part of standard template."
    }
  ],
  "template_structure": [
    { "heading_text": "Executive Summary" },
    { "heading_text": "Model Overview" },
    { "heading_text": "Risk Assessment" }
  ]
}


┌───────────────────────────────────────────────┐
│              DOCUMENT AUDIT REPORT            │
│  Model: <Name>  |  Template: <Name>           │
│  Audit ID, Date & Reference Table             │
├───────────────────────────────────────────────┤
│  1. EXECUTIVE SUMMARY                         │
│     - Overall Audit Status (Pass/Fail)        │
│     - High-level Summary Metrics              │
├───────────────────────────────────────────────┤
│  2. INTERNAL INTEGRITY (TOC SYNCHRONIZATION)  │
│     - Synchronization Pass/Fail Status        │
│     - Technical Details Discrepancy Table     │
├───────────────────────────────────────────────┤
│  3. TEMPLATE COMPLIANCE & STRUCTURE           │
│     - A. Compliant Standard Sections          │
│     - B. Structural & Compliance Gaps Table   │
├───────────────────────────────────────────────┤
│  [PAGE BREAK]                                 │
│  Audit Notes & Disclaimers                    │
└───────────────────────────────────────────────┘


```python

from datetime import datetime
import os
from reportlab.lib import colors
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet

# Define required mock styles and colors
COLOR_PASS = colors.HexColor("#28A745")
COLOR_FAIL = colors.HexColor("#DC3545")
COLOR_WARNING = colors.HexColor("#FFC107")
COLOR_PRIMARY = colors.HexColor("#003366")
COLOR_SECONDARY = colors.HexColor("#6C757D")
COLOR_TEXT = colors.HexColor("#212529")

def get_corporate_styles():
    styles = getSampleStyleSheet()
    # Add custom styles matching expected names here
    return styles

# Sample Execution
audit_data = {
    "audited_file_name": "Credit_Risk_Model.docx",
    "template_file_name": "MRM_Standard_Template.docx",
    "internal_discrepancies": [],
    "template_discrepancies": [],
    "template_structure": [{"heading_text": "Executive Summary"}]
}

generate_audit_pdf_report(audit_data, "Audit_Report.pdf")

```