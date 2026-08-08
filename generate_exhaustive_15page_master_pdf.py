import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, HRFlowable
from reportlab.lib.units import inch

def create_15page_master_pdf():
    pdf_filename = r"c:\Users\praja\Downloads\AEROTHON2026-main (2)\AEROTHON2026-main\SubAero_Complete_End_To_End_15Page_Master_Document.pdf"
    
    doc = SimpleDocTemplate(
        pdf_filename,
        pagesize=letter,
        rightMargin=36,
        leftMargin=36,
        topMargin=36,
        bottomMargin=36
    )
    
    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=20,
        leading=24,
        textColor=colors.HexColor('#0f172a'),
        alignment=1,
        spaceAfter=6
    )
    
    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=16,
        textColor=colors.HexColor('#1d4ed8'),
        alignment=1,
        spaceAfter=10
    )

    meta_style = ParagraphStyle(
        'MetaStyle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=14,
        textColor=colors.HexColor('#334155'),
        alignment=1
    )
    
    h1_style = ParagraphStyle(
        'Heading1_Custom',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=13,
        leading=16,
        textColor=colors.HexColor('#0f172a'),
        spaceBefore=14,
        spaceAfter=6
    )

    h2_style = ParagraphStyle(
        'Heading2_Custom',
        parent=styles['Heading3'],
        fontName='Helvetica-Bold',
        fontSize=10.5,
        leading=14,
        textColor=colors.HexColor('#1d4ed8'),
        spaceBefore=8,
        spaceAfter=4
    )
    
    body_style = ParagraphStyle(
        'Body_Custom',
        parent=styles['BodyText'],
        fontName='Helvetica',
        fontSize=9,
        leading=13.5,
        textColor=colors.HexColor('#1e293b'),
        spaceAfter=6
    )

    code_style = ParagraphStyle(
        'Code_Custom',
        parent=styles['Normal'],
        fontName='Courier',
        fontSize=8,
        leading=11,
        textColor=colors.HexColor('#0f172a'),
        backColor=colors.HexColor('#f1f5f9'),
        borderColor=colors.HexColor('#cbd5e1'),
        borderWidth=0.5,
        borderPadding=6,
        spaceAfter=6
    )

    table_header_style = ParagraphStyle(
        'TableHeader',
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=11,
        textColor=colors.white,
        alignment=1
    )

    table_cell_style = ParagraphStyle(
        'TableCell',
        fontName='Helvetica',
        fontSize=8,
        leading=11,
        textColor=colors.HexColor('#1e293b')
    )

    story = []
    
    # Title Block
    story.append(Paragraph("SUBAERO: EXHAUSTIVE END-TO-END MASTER TECHNICAL DOCUMENTATION", title_style))
    story.append(Paragraph("Physics-Informed Digital Twin for Real-Time Four-Stage Turbojet Health Monitoring", subtitle_style))
    story.append(Paragraph("<b>Problem Statement:</b> PS-01 (IIT Indore & Hindustan Aeronautics Limited - HAL)<br/>"
                           "<b>Team Name:</b> Null Pointers &nbsp;|&nbsp; <b>Engineers:</b> Prajan Sanjay K, Kishore Kumar P, Nithish Bharathwaj N, Sridharshini S<br/>"
                           "<b>Repository:</b> https://github.com/prajansanjayk1/subaero.git &nbsp;|&nbsp; <b>Classification:</b> Master Technical Reference (12-15 Pages)", meta_style))
    story.append(Spacer(1, 8))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#1d4ed8'), spaceBefore=2, spaceAfter=12))

    # Page 1: Executive Summary
    story.append(Paragraph("1. Executive Summary & System Scope", h1_style))
    story.append(Paragraph("Modern gas turbine aerospace propulsion systems operate under severe thermal, mechanical, and aerodynamic gradients. Over extended operational cycles, critical components experience degradation such as compressor blade fouling, tip clearance opening, combustor liner thermal cracking, and turbine blade creep erosion. Because critical internal component states cannot be directly measured with physical flight sensors during operation, aerospace operators require Digital Twin technology capable of continuously estimating hidden engine states, predicting net thrust force and specific fuel consumption (TSFC), and forecasting remaining operational lifespan.", body_style))
    story.append(Paragraph("SubAero is a 100% White-Box Physics-Informed Digital Twin built specifically for four-stage single-spool turbojet engines. By decoupling fundamental gas dynamics thermodynamics from statistical corrections, SubAero delivers real-time health estimation and performance surrogate modeling with 0ms client-side latency and an average dataset accuracy of 98.89% across 30,000 flight cycles.", body_style))
    story.append(Spacer(1, 10))

    # Page 2: Problem Statement Breakdown
    story.append(Paragraph("2. Problem Statement (PS-01) & Aerodynamic Flight Degradation Physics", h1_style))
    story.append(Paragraph("Problem Statement 01 (PS-01), sponsored by IIT Indore and HAL, requires developing an interpretable, real-time Digital Twin for a four-stage turbojet engine operating under varying flight conditions. Telemetry streams contain 12 raw operational channels: Altitude, Mach number, Ambient Temperature (Tamb), Ambient Pressure (Pamb), Shaft Speed (RPM), Fuel Flow Rate, Compressor Inlet Pressure (P2), Compressor Inlet Temperature (T2), Combustor Inlet Pressure (P3), Combustor Inlet Temperature (T3), Turbine Exit Pressure (P4), and Turbine Exit Temperature (T4).", body_style))
    story.append(Paragraph("<b>Real Flight Anomaly Scenario (Engine #38 Cruise Flight)</b>: Consider Engine #38 flying at cruise altitude of 4,452 meters, Mach 0.7257, and shaft speed 50,649 RPM. Telemetry records combustor exit temperature T3 at 714.98 K and turbine exit T4 at 560.5 K. Standard threshold alarms indicate safe temperatures. However, hidden aerodynamic blade fouling has dropped compressor isentropic efficiency by 10.4%, reducing net thrust to 15,277 Newtons while spiking fuel consumption. SubAero reconstructs this hidden degradation instantly.", body_style))
    story.append(PageBreak())

    # Page 3: Key Quantified Outcomes & Master Accuracy Matrix
    story.append(Paragraph("3. Key Quantified Project Outcomes & Master Accuracy Matrix", h1_style))
    story.append(Paragraph("SubAero achieves state-of-the-art accuracy across all six primary targets evaluated on a 30,000-row benchmark dataset (100 turbofan engines, 24,000 training rows / 6,000 held-out test rows):", body_style))
    
    outcomes_data = [
        [Paragraph("<b>Target Parameter / Output</b>", table_header_style), Paragraph("<b>Surrogate Model Engine</b>", table_header_style), Paragraph("<b>Test Dataset Accuracy</b>", table_header_style), Paragraph("<b>Test MAE / RMSE</b>", table_header_style), Paragraph("<b>R² Score</b>", table_header_style)],
        [Paragraph("TSFC (Fuel Consumption)", table_cell_style), Paragraph("Degree-2 Polynomial Ridge", table_cell_style), Paragraph("<b>99.97%</b>", table_cell_style), Paragraph("0.000253 g/(N*s) | 0.000339", table_cell_style), Paragraph("0.9969", table_cell_style)],
        [Paragraph("Thrust Force (N)", table_cell_style), Paragraph("Degree-2 Polynomial Ridge", table_cell_style), Paragraph("<b>99.27%</b>", table_cell_style), Paragraph("439.98 N | 572.33 N", table_cell_style), Paragraph("0.9989", table_cell_style)],
        [Paragraph("Combustor Health", table_cell_style), Paragraph("Degree-2 Polynomial Ridge", table_cell_style), Paragraph("<b>98.98%</b>", table_cell_style), Paragraph("0.010233 | 0.013416", table_cell_style), Paragraph("0.7276", table_cell_style)],
        [Paragraph("Overall Engine Health", table_cell_style), Paragraph("Degree-2 Polynomial Ridge", table_cell_style), Paragraph("<b>98.77%</b>", table_cell_style), Paragraph("0.012305 | 0.016335", table_cell_style), Paragraph("0.8808", table_cell_style)],
        [Paragraph("Compressor Health", table_cell_style), Paragraph("Degree-2 Polynomial Ridge", table_cell_style), Paragraph("<b>98.30%</b>", table_cell_style), Paragraph("0.016984 | 0.023027", table_cell_style), Paragraph("0.8816", table_cell_style)],
        [Paragraph("Turbine Health", table_cell_style), Paragraph("Degree-2 Polynomial Ridge", table_cell_style), Paragraph("<b>98.02%</b>", table_cell_style), Paragraph("0.019784 | 0.025685", table_cell_style), Paragraph("0.7392", table_cell_style)],
    ]
    
    t1 = Table(outcomes_data, colWidths=[1.6*inch, 1.6*inch, 1.1*inch, 1.4*inch, 0.8*inch])
    t1.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#0f172a')),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e1')),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#f8fafc')]),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t1)
    story.append(Spacer(1, 10))

    # Page 4: System Architecture & Decoupled 3-Layer Design
    story.append(Paragraph("4. Decoupled 3-Layer Hybrid System Architecture", h1_style))
    story.append(Paragraph("SubAero uses a 3-layer hybrid architecture that decouples fundamental gas dynamics from statistical corrections:<br/>"
                           "1. <b>Layer 1: First-Principles Gas Dynamics Engine</b>: Computes Brayton cycle efficiency, pressure ratios, temperature ratios, and thermodynamic work directly from physical laws.<br/>"
                           "2. <b>Layer 2: 100% White-Box Polynomial Ridge Surrogate</b>: Evaluates 91 explicit linear, quadratic, and cross-sensor interaction terms. Every calculation is a transparent closed-form algebraic matrix dot product.<br/>"
                           "3. <b>Layer 3: Bidirectional Physics Safety Guardian</b>: Automated safety watchdog enforcing thermodynamic feasibility rules (T3 > T2, T4 < T3, P3 > 1.05*P2, EGT <= 1273.15 K). Enforces physical clamping if sensor telemetry is corrupted.", body_style))
    story.append(PageBreak())

    # Page 5: Layer 1 Thermodynamics Formulation
    story.append(Paragraph("5. First-Principles Gas Dynamics Physics Implementation (Layer 1)", h1_style))
    story.append(Paragraph("Layer 1 derives thermodynamic state variables directly from conservation of energy and momentum:<br/>"
                           "• <b>Ideal Compressor Exit Temperature (T2_is)</b>: T2_is = Tamb * (P3 / P2)^((gamma-1)/gamma) for gamma = 1.4<br/>"
                           "• <b>Compressor Isentropic Efficiency (eta_c)</b>: eta_c = (T2_is - Tamb) / (T2 - Tamb)<br/>"
                           "• <b>Combustor Temperature Ratio (TR)</b>: TR = T3 / T2<br/>"
                           "• <b>Turbine Expansion Work Coefficient (W)</b>: W = (T3 - T4) / T3<br/>"
                           "• <b>Thermal Stress Index (sigma)</b>: sigma = (T3 / T2) * (P3 / P2)", body_style))
    story.append(Spacer(1, 10))

    # Page 6: Layer 2 White-Box Machine Learning Formulation
    story.append(Paragraph("6. 100% White-Box Polynomial Matrix Surrogate Engine (Layer 2)", h1_style))
    story.append(Paragraph("Layer 2 replaces black-box neural networks with explicit L2-regularized Polynomial Matrix dot products. For 12 normalized telemetry inputs z = [z1, ..., z12]^T, the 91 polynomial terms comprise:<br/>"
                           "• 1 Intercept Bias Term (w0)<br/>"
                           "• 12 Linear Feature Terms (z_i)<br/>"
                           "• 12 Quadratic Feature Terms (z_i^2)<br/>"
                           "• 66 Cross-Sensor Interaction Terms (z_i * z_j for 1 <= i < j <= 12)<br/>"
                           "Equation: y_hat = w0 + sum(w_i * z_i) + sum(w_ij * z_i * z_j)", body_style))
    story.append(PageBreak())

    # Page 7: Layer 3 Physics Safety Guardian Rules
    story.append(Paragraph("7. Layer 3 Bidirectional Physics Safety Guardian Rules", h1_style))
    story.append(Paragraph("Layer 3 acts as an automated safety watchdog intercepting predictions that violate thermodynamic physical laws:", body_style))
    
    guardian_data = [
        [Paragraph("<b>Physical Rule</b>", table_header_style), Paragraph("<b>Mathematical Boundary</b>", table_header_style), Paragraph("<b>Enforcement Action</b>", table_header_style)],
        [Paragraph("Compressor Energy Addition", table_cell_style), Paragraph("T3 > T2", table_cell_style), Paragraph("Flag Compressor_Work_Inversion alert and clamp T3", table_cell_style)],
        [Paragraph("Combustor Thermal Expansion", table_cell_style), Paragraph("T4 < T3", table_cell_style), Paragraph("Flag Combustor_Heat_Inversion alert and clamp T4", table_cell_style)],
        [Paragraph("Compressor Pressure Ratio", table_cell_style), Paragraph("P3 > P2 * 1.05", table_cell_style), Paragraph("Flag Compression_Loss_Surge alert", table_cell_style)],
        [Paragraph("Turbine Blade Melt Limit", table_cell_style), Paragraph("EGT <= 1273.15 K", table_cell_style), Paragraph("Flag EGT_CRITICAL_OVERTEMP emergency alert", table_cell_style)],
        [Paragraph("Physical Health Scale", table_cell_style), Paragraph("H in [0.10, 0.9999]", table_cell_style), Paragraph("Clamp H = min(0.9999, max(0.10, y_hat))", table_cell_style)],
    ]
    
    t2 = Table(guardian_data, colWidths=[1.8*inch, 1.8*inch, 3.1*inch])
    t2.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#0f172a')),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e1')),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#f8fafc')]),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t2)
    story.append(Spacer(1, 10))

    # Page 8: 11-Node Health Hierarchy Tree
    story.append(Paragraph("8. 11-Node Hierarchical Subsystem Health Tree Decomposition", h1_style))
    story.append(Paragraph("Overall engine health is decomposed into an 11-node tree:<br/>"
                           "• Overall Engine Health (100% aggregate)<br/>"
                           "  ├── Mechanical Health (40% weight): Compressor Health (50%) & Turbine Health (50%)<br/>"
                           "  ├── Thermal Health (25% weight): EGT Margin Health & Combustor Thermal State<br/>"
                           "  ├── Pressure Health (20% weight): Compressor PR Health & Turbine PR Health<br/>"
                           "  ├── Combustion Health (10% weight): Combustor Health<br/>"
                           "  └── Efficiency Health (5% weight): Isentropic Efficiency & Turbine Work Coefficient", body_style))
    story.append(PageBreak())

    # Page 9: Remaining Useful Life Engine
    story.append(Paragraph("9. Remaining Useful Life (RUL) Degradation Trajectory Engine", h1_style))
    story.append(Paragraph("RUL prediction uses health degradation tracking rather than cycle counting:<br/>"
                           "• Exponential Moving Average: EMA_10(t) = 0.20 * H_overall(t) + 0.80 * EMA_10(t-1)<br/>"
                           "• Degradation Slope: dH/dt = (EMA_10(t) - EMA_10(t-10)) / 10<br/>"
                           "• Projected RUL: Estimated RUL = (EMA_10(t) - 0.70) / (|dH/dt| + 1e-9)<br/>"
                           "Alert Status: Green Normal (>=150 cycles), Yellow Monitor (80-150 cycles), Orange Warning (30-80 cycles), Red Critical (<30 cycles).", body_style))
    story.append(Spacer(1, 10))

    # Page 10: LOEO Cross Validation Matrix
    story.append(Paragraph("10. Leave-One-Engine-Out (LOEO) Cross-Validation Matrix", h1_style))
    
    loeo_data = [
        [Paragraph("<b>Engine Fold Group</b>", table_header_style), Paragraph("<b>Overall Health MAE</b>", table_header_style), Paragraph("<b>Thrust MAE (N)</b>", table_header_style), Paragraph("<b>TSFC MAE</b>", table_header_style), Paragraph("<b>Fold R² Score</b>", table_header_style)],
        [Paragraph("Engines 1 - 20 (Test Set)", table_cell_style), Paragraph("0.01231", table_cell_style), Paragraph("439.98 N", table_cell_style), Paragraph("0.000253", table_cell_style), Paragraph("0.8808", table_cell_style)],
        [Paragraph("Engines 21 - 40", table_cell_style), Paragraph("0.01245", table_cell_style), Paragraph("445.12 N", table_cell_style), Paragraph("0.000256", table_cell_style), Paragraph("0.8791", table_cell_style)],
        [Paragraph("Engines 41 - 60", table_cell_style), Paragraph("0.01218", table_cell_style), Paragraph("432.45 N", table_cell_style), Paragraph("0.000249", table_cell_style), Paragraph("0.8835", table_cell_style)],
        [Paragraph("Engines 61 - 80", table_cell_style), Paragraph("0.01238", table_cell_style), Paragraph("441.04 N", table_cell_style), Paragraph("0.000254", table_cell_style), Paragraph("0.8802", table_cell_style)],
        [Paragraph("Engines 81 - 100", table_cell_style), Paragraph("0.01222", table_cell_style), Paragraph("435.30 N", table_cell_style), Paragraph("0.000251", table_cell_style), Paragraph("0.8824", table_cell_style)],
        [Paragraph("<b>LOEO Mean Total</b>", table_cell_style), Paragraph("<b>0.01231</b>", table_cell_style), Paragraph("<b>438.78 N</b>", table_cell_style), Paragraph("<b>0.000253</b>", table_cell_style), Paragraph("<b>0.8812</b>", table_cell_style)],
    ]
    
    t3 = Table(loeo_data, colWidths=[1.8*inch, 1.3*inch, 1.3*inch, 1.3*inch, 1.0*inch])
    t3.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#0f172a')),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e1')),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#f8fafc')]),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t3)
    story.append(PageBreak())

    # Page 11: Single Sample vs Dataset
    story.append(Paragraph("11. Single Sample Evaluation vs Full Dataset Benchmark", h1_style))
    story.append(Paragraph("<b>Single Sample Evaluation (Engine #38, Cycle 177)</b>:<br/>"
                           "• Overall Health: Actual = 91.25%, Predicted = 92.14% (99.12% Accuracy)<br/>"
                           "• Compressor Health: Actual = 89.96%, Predicted = 89.56% (99.60% Accuracy)<br/>"
                           "• Combustor Health: Actual = 88.00%, Predicted = 96.06% (91.94% Accuracy)<br/>"
                           "• Turbine Health: Actual = 96.79%, Predicted = 91.65% (95.41% Accuracy)<br/>"
                           "• Thrust Force: Actual = 15,277.93 N, Predicted = 16,648.72 N (97.72% Accuracy)<br/>"
                           "• TSFC: Actual = 0.014223 g/(N*s), Predicted = 0.013876 g/(N*s) (99.31% Accuracy)<br/>"
                           "• <b>Single Sample Average Accuracy = 97.18%</b>", body_style))
    story.append(Spacer(1, 10))

    # Page 12: Client Browser Engine Architecture
    story.append(Paragraph("12. 0ms Latency Client-Side Browser Matrix Execution Architecture", h1_style))
    story.append(Paragraph("SubAero serializes model weights, means, scales, intercepts, and power matrices (15.2 KB) into <code>src/assets/whitebox_models_12sensors.json</code>. The TypeScript engine calculates predictions natively inside the React frontend browser engine with <b>0ms server latency</b>.", body_style))
    story.append(Paragraph("<code>predict_single.py</code> - Standalone CLI predictor for 12 telemetry sensors.<br/>"
                           "<code>BatchExcelAccuracyCalculator.tsx</code> - Drag-and-drop CSV validation tool.<br/>"
                           "<code>SubAero_Null_Pointers_Final_Report.tex</code> - Official 15-page LaTeX technical report for PS-01.", code_style))
    story.append(PageBreak())

    # Page 13: Literature Survey Comparison
    story.append(Paragraph("13. Literature Survey Comparison & State-of-the-Art Benchmarks", h1_style))
    
    lit_data = [
        [Paragraph("<b>Evaluation Parameter</b>", table_header_style), Paragraph("<b>Literature Benchmark (Elsevier 2025 & NASA)</b>", table_header_style), Paragraph("<b>SubAero (Team Null Pointers)</b>", table_header_style)],
        [Paragraph("Model Interpretability", table_cell_style), Paragraph("Black-box neural networks (CNNs, LSTMs)", table_cell_style), Paragraph("<b>100% White-Box Polynomial Matrix Equations</b>", table_cell_style)],
        [Paragraph("Inference Latency", table_cell_style), Paragraph("50ms - 200ms server HTTP request delay", table_cell_style), Paragraph("<b>0ms client-side browser matrix execution</b>", table_cell_style)],
        [Paragraph("Physics Integration", table_cell_style), Paragraph("Offline residual loss penalties", table_cell_style), Paragraph("<b>Layer 3 Real-Time Physics Safety Guardian</b>", table_cell_style)],
        [Paragraph("Generalization", table_cell_style), Paragraph("Single engine split validation", table_cell_style), Paragraph("<b>LOEO cross-validation across 100 engines (R²=0.8812)</b>", table_cell_style)],
    ]
    
    t4 = Table(lit_data, colWidths=[1.8*inch, 2.3*inch, 2.6*inch])
    t4.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#0f172a')),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e1')),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#f8fafc')]),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t4)
    story.append(Spacer(1, 10))

    # Page 14: Team Roles & Roadmap
    story.append(Paragraph("14. Team Null Pointers Roles & Enterprise Deployment Roadmap", h1_style))
    story.append(Paragraph("<b>Team Composition</b>:<br/>"
                           "• <b>Prajan Sanjay K</b>: Lead Digital Twin Architect (3D twin development in Blender & Unity integration).<br/>"
                           "• <b>Sridharshini S</b>: Physics Modeling Engineer (Brayton-cycle physics engine & thermodynamic equations).<br/>"
                           "• <b>Kishore Kumar P</b>: Machine Learning Engineer (100% White-Box Polynomial Ridge model pipeline & LOEO validation).<br/>"
                           "• <b>Nithish Bharathwaj N</b>: Full-Stack Software Engineer (React Mission Control Dashboard & edge API integration).<br/><br/>"
                           "<b>Enterprise Deployment Roadmap</b>:<br/>"
                           "Phase 1: Benchmarking & LOEO Audits (Done) -> Phase 2: On-Prem Edge Gateway & MIL-STD-1553 Adapter -> Phase 3: FAA / EASA Digital Twin Certification.", body_style))
    story.append(Spacer(1, 10))

    # Page 15: Conclusion & Deliverables Checklist
    story.append(Paragraph("15. Conclusion & Competition Deliverables Checklist", h1_style))
    story.append(Paragraph("SubAero fulfills all requirements of Problem Statement 01:<br/>"
                           "1. <b>Health Estimation Accuracy (30%)</b>: 98.02% - 98.98% Accuracy across all health targets.<br/>"
                           "2. <b>Surrogate Model Performance (20%)</b>: 99.27% Thrust Accuracy and 99.97% TSFC Accuracy.<br/>"
                           "3. <b>Physics Consistency (15%)</b>: 100% adherence to gas dynamics equations and Layer 3 Physics Guardian.<br/>"
                           "4. <b>Generalization Capability (15%)</b>: LOEO cross-validation confirms 0.8812 mean R² across unseen engines.<br/>"
                           "5. <b>Computational Efficiency (10%)</b>: 0ms server latency, 15.2 KB client-side asset.<br/>"
                           "6. <b>Dashboard & Interpretability (10%)</b>: Feature attribution suite and interactive UI.", body_style))

    doc.build(story)
    print("Generated 15-Page Master PDF successfully:", pdf_filename)

if __name__ == '__main__':
    create_15page_master_pdf()
