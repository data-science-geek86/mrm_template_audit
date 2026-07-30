import pandas as pd
from datetime import datetime

def generate_audit_professional_report(audit_results, model_name, template_name):
    """
    Generates a professional text-based summary report of the document audit.
    
    Args:
        audit_results (dict): The output dictionary from audit_model_document.
        model_name (str): The name/filename of the model document.
        template_name (str): The name/filename of the template used as a reference.
        
    Returns:
        str: A formatted string containing the audit report.
    """
    report = []
    report.append("="*80)
    report.append(f"DOCUMENT AUDIT REPORT: {model_name}")
    report.append(f"Reference Template: {template_name}")
    report.append(f"Date of Audit: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    report.append("="*80)
    report.append("\n")

    # --- SECTION 1: EXECUTIVE SUMMARY ---
    int_errs = len(audit_results["internal_discrepancies"])
    tpl_errs = len(audit_results["template_discrepancies"])
    status = "⚠️ ATTENTION REQUIRED" if (int_errs + tpl_errs) > 0 else "✅ COMPLIANT"
    
    report.append("## 1. EXECUTIVE SUMMARY")
    report.append(f"Overall Status: {status}")
    report.append(f"- Internal Integrity Issues (TOC vs Body): {int_errs}")
    report.append(f"- Template Compliance Issues: {tpl_errs}")
    report.append("\n" + "-"*40)

    # --- SECTION 2: INTERNAL INTEGRITY ---
    report.append("## 2. INTERNAL INTEGRITY (TOC SYNCHRONIZATION)")
    if int_errs == 0:
        report.append("✅ PASS: The literal Table of Contents is fully synchronized with the document body.")
    else:
        for idx, err in enumerate(audit_results["internal_discrepancies"], 1):
            report.append(f"{idx}. [{err['issue']}] {err['details']}")
    report.append("\n" + "-"*40)

    # --- SECTION 3: TEMPLATE COMPLIANCE ---
    report.append("## 3. TEMPLATE COMPLIANCE & STRUCTURE")
    
    # Categorize Template Findings
    missing = [e for e in audit_results["template_discrepancies"] if "Missing" in e['issue']]
    numbering = [e for e in audit_results["template_discrepancies"] if "Numbering" in e['issue']]
    extra = [e for e in audit_results["template_discrepancies"] if "Extra" in e['issue']]
    
    # Successful Findings (Non-discrepancies)
    # We identify these by checking template_map items not in the "missing" list
    all_tpl_sections = {item['heading_text'].lower() for item in audit_results["template_structure"]}
    missing_texts = {e['section'].lower() for e in missing}
    passed_sections = all_tpl_sections - missing_texts

    # Reporting Passed Sections
    report.append("### ✅ Standardized Sections Found (Compliant):")
    if passed_sections:
        report.append(", ".join([s.title() for s in sorted(passed_sections)]))
    else:
        report.append("No compliant standard sections found.")

    # Reporting Discrepancies
    if tpl_errs > 0:
        report.append("\n### ❌ Structural Discrepancies:")
        if missing:
            report.append(f"\n--- MISSING MANDATORY SECTIONS ({len(missing)}) ---")
            for m in missing: report.append(f"- {m['section']}")
        
        if numbering:
            report.append(f"\n--- INCORRECT NUMBERING HIERARCHY ({len(numbering)}) ---")
            for n in numbering: report.append(f"- {n['section']}: {n['details']}")
            
        if extra:
            report.append(f"\n--- NON-STANDARD SECTIONS DETECTED ({len(extra)}) ---")
            for ex in extra: report.append(f"- {ex['section']}: {ex['details']}")
    else:
        report.append("\n✅ PASS: Document follows the mandated structure and numbering of the template.")

    report.append("\n" + "="*80)
    report.append("END OF REPORT")
    
    return "\n".join(report)

