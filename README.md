# MRM Documentation Audit

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 630" width="100%">
  <defs>
    <linearGradient id="bgGradient" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0F172A"/>
      <stop offset="50%" stop-color="#1E293B"/>
      <stop offset="100%" stop-color="#090D16"/>
    </linearGradient>
    <linearGradient id="accentGradient" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#38BDF8"/>
      <stop offset="50%" stop-color="#818CF8"/>
      <stop offset="100%" stop-color="#C084FC"/>
    </linearGradient>
    <linearGradient id="cardGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1E293B" stop-opacity="0.8"/>
      <stop offset="100%" stop-color="#0F172A" stop-opacity="0.9"/>
    </linearGradient>
    <linearGradient id="badgeGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0EA5E9" stop-opacity="0.2"/>
      <stop offset="100%" stop-color="#6366F1" stop-opacity="0.2"/>
    </linearGradient>
    <filter id="dropShadow" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="12" stdDeviation="16" flood-color="#000000" flood-opacity="0.5"/>
    </filter>
    <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M 40 0 L 0 0 0 40" fill="none" stroke="#334155" stroke-width="0.5" stroke-opacity="0.3"/>
    </pattern>
  </defs>

  <!-- Background Layer -->
  <rect width="1200" height="630" fill="url(#bgGradient)"/>
  <rect width="1200" height="630" fill="url(#grid)"/>

  <!-- Main Card -->
  <rect x="80" y="70" width="1040" height="490" rx="24" fill="url(#cardGrad)" stroke="#334155" stroke-width="1.5" filter="url(#dropShadow)"/>
  <rect x="80" y="70" width="1040" height="6" rx="3" fill="url(#accentGradient)"/>

  <!-- Badge Header -->
  <g transform="translate(130, 130)">
    <rect x="0" y="0" width="260" height="36" rx="18" fill="url(#badgeGrad)" stroke="#38BDF8" stroke-opacity="0.4" stroke-width="1"/>
    <path d="M 20 10 L 28 14 V 20 C 28 24.5 24.5 27.5 20 29 C 15.5 27.5 12 24.5 12 20 V 14 L 20 10 Z" fill="none" stroke="#38BDF8" stroke-width="2" stroke-linejoin="round"/>
    <text x="38" y="23" font-family="system-ui, sans-serif" font-size="13" font-weight="700" fill="#38BDF8" letter-spacing="1.5">MODEL RISK MANAGEMENT</text>
  </g>

  <!-- Main Title -->
  <text x="130" y="235" font-family="system-ui, sans-serif" font-size="54" font-weight="800" fill="#F8FAFC">MRM Documentation Audit</text>
  <text x="130" y="285" font-family="system-ui, sans-serif" font-size="20" font-weight="400" fill="#94A3B8">Comprehensive Governance, Validation &amp; Regulatory Compliance Assessment</text>

  <!-- Metrics / Features -->
  <g transform="translate(130, 335)">
    <rect x="0" y="0" width="270" height="76" rx="14" fill="#0F172A" fill-opacity="0.7" stroke="#334155"/>
    <text x="68" y="34" font-family="system-ui, sans-serif" font-size="14" font-weight="700" fill="#F1F5F9">SR 11-7 / OCC 2011-12</text>
    <text x="68" y="53" font-family="system-ui, sans-serif" font-size="12" font-weight="400" fill="#64748B">Regulatory Standard</text>
  </g>
  <g transform="translate(420, 335)">
    <rect x="0" y="0" width="270" height="76" rx="14" fill="#0F172A" fill-opacity="0.7" stroke="#334155"/>
    <text x="68" y="34" font-family="system-ui, sans-serif" font-size="14" font-weight="700" fill="#F1F5F9">Documentation Quality</text>
    <text x="68" y="53" font-family="system-ui, sans-serif" font-size="12" font-weight="400" fill="#64748B">Completeness &amp; Traceability</text>
  </g>
  <g transform="translate(710, 335)">
    <rect x="0" y="0" width="270" height="76" rx="14" fill="#0F172A" fill-opacity="0.7" stroke="#334155"/>
    <text x="68" y="34" font-family="system-ui, sans-serif" font-size="14" font-weight="700" fill="#F1F5F9">Independent Review</text>
    <text x="68" y="53" font-family="system-ui, sans-serif" font-size="12" font-weight="400" fill="#64748B">Verification &amp; Sign-off</text>
  </g>

  <!-- Footer Info -->
  <g transform="translate(130, 480)">
    <rect x="0" y="0" width="110" height="26" rx="6" fill="#10B981" fill-opacity="0.15" stroke="#10B981" stroke-opacity="0.4"/>
    <text x="24" y="17" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#34D399">AUDIT READY</text>
    <text x="135" y="17" font-family="system-ui, sans-serif" font-size="13" font-weight="600" fill="#64748B">Version: <tspan fill="#94A3B8">v2.4</tspan></text>
    <text x="250" y="17" font-family="system-ui, sans-serif" font-size="13" font-weight="600" fill="#64748B">Scope: <tspan fill="#94A3B8">Enterprise Tier 1 &amp; Tier 2 Models</tspan></text>
  </g>
</svg>


The package is designed to audit the compliance of the development/validation documentation with prescribed standard templates (development or validation). 
Acceptable file format is MS Word file. It generates a formatted, corporate-branded PDF document summarizing the results of an automated Model Risk Management (MRM) document audit.

---

## 📋 Table of Contents
1. [Overview](#overview)
2. [Usage Example](#usage-example)
3. [Dependencies](#dependencies)
4. [Function Signature](#function-signature)
5. [Input Data Structure](#input-data-structure)
6. [Report Architecture](#report-architecture) 

---

## Overview

This function converts structured output dictionary data from an XML/WordprocessingML document audit into a ReportLab PDF document.

### Features
* **Standardized Report Header:** Dynamic generation date, audit ID, and file references.
* **Executive Summary:** High-level audit status (`COMPLIANT` vs `ATTENTION REQUIRED`).
* **Internal Integrity (TOC Sync):** Tabulated comparison of Table of Contents vs. actual body headings.
* **Template Compliance & Structure:** Categorized analysis for missing mandatory sections, incorrect section numbering, and extra non-standard sections.
* **Audit Disclaimers:** Standard governance disclaimer included on a dedicated final page.

---

## Usage Example

```python
from mrm_template_audit.audit_mrm_doc import audit_model_document
from mrm_template_audit.generate_audit_pdf_report import generate_audit_pdf_report

# --- 1. Define your file paths ---
# (Here, we assume the template file and model document is stored under test folder)
MODEL_DOC = './test/MDD_Submission_v2 - TOC.docx'
TEMPLATE_DOC = './test/2_MDD_Template_TOC_NoManual_Section_Number.docx'

# --- 2. Execution Example ---
audit_output = audit_model_document(MODEL_DOC, TEMPLATE_DOC)

# --- 3. Generate the report ---
generate_audit_pdf_report(
    audit_results=audit_output,
    output_filename="./test/IFRS9_Audit_Report_2026.pdf"
)


```

---

## Dependencies

### Python Libraries
* `reportlab` (`SimpleDocTemplate`, `Paragraph`, `Table`, `TableStyle`, `Spacer`, `PageBreak`, `colors`, `inch`, `LETTER`)
* `datetime` (`datetime`)
* `os` (`os.path.abspath`)

---

## Function Signature 

### A) audit_model_document

```python
def audit_model_document(model_path, template_path):
    """
    Performs a comprehensive audit of a model document against a standard template.
    
    Includes bidirectional checks for missing mandatory sections (template vs model)
    and extra non-standard sections (model vs template).
	
	Args:
        model_path (str): Path of the model development/validation documenation file (MS Word file format) including file name.
        template_path (str): Path of the model development/validation template (MS Word file format) including file name.
    """
```

### B) generate_audit_pdf_report

```python
def generate_audit_pdf_report(audit_results: dict, output_filename: str) -> None

    """
    Generates a professional, visually appealing PDF business report explaining audit findings.
    
    This function structures findings (internal discrepancies, template compliance gaps, 
    and successful alignments) into a branded PDF format with corporate styling.

    Args:
        audit_results (dict): The dictionary output from audit_model_document.
        output_filename (str): The desired path/filename for the generated PDF.
    """
```

## Input Data Structure
The audit_results comes from output of the function `audit_model_document` that has following schema:
You can run first the function `audit_model_document` and then `generate_audit_pdf_report` to generate the audit report as shown in the above example.

```

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
```

## Report Architecture

```

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

```

