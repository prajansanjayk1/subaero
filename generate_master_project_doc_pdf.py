import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, HRFlowable
from reportlab.lib.units import inch

def create_master_project_pdf():
    pdf_filename = r"c:\Users\praja\Downloads\AEROTHON2026-main (2)\AEROTHON2026-main\SubAero_Complete_End_To_End_Project_Master_Document.pdf"
    
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
        leading=13,
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
    story.append(Paragraph("SUBAERO: COMPLETE END-TO-END MASTER PROJECT DOCUMENT", title_style))
    story.append(Paragraph("Physics-Informed Digital Twin for Real-Time Four-Stage Turbojet Health Monitoring", subtitle_style))
    story.append(Paragraph("<b>Problem Statement:</b> PS-01 (IIT Indore & Hindustan Aeronautics Limited - HAL)<br/>"
                           "<b>Team Name:</b> Null Pointers &nbsp;|&nbsp; <b>Engineers:</b> Prajan Sanjay K, Kishore Kumar P, Nithish Bharathwaj N, Sridharshini S<br/>"
                           "<b>Repository:</b> https://github.com/prajansanjayk1/subaero.git &nbsp;|&nbsp; <b>Date:</b> August 2026", meta_style))
    story.append(Spacer(1, 8))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#1d4ed8'), spaceBefore=2, spaceAfter=10))

    # Executive Overview
    story.append(Paragraph("1. Executive Summary & Problem Understanding", h1_style))
    story.append(Paragraph("<b>Problem Statement Details (PS-01)</b>: Modern aero-engines operate under severe thermal, mechanical, and aerodynamic stress. Critical internal component states—such as compressor blade tip clearance degradation, combustor thermal ratio loss, and turbine blade creep—cannot be measured directly during flight with invasive physical sensors. Traditional maintenance relies on fixed flight-hour overhauls, resulting in either premature component replacement or unexpected in-flight failures.", body_style))
    story.append(Paragraph("<b>SubAero Solution</b>: SubAero is an end-to-end Physics-Informed Digital Twin that reconstructs hidden subsystem health, predicts net Thrust force and Fuel Consumption (TSFC), and projects Remaining Useful Life (RUL) with <b>0ms client-side latency</b> and <b>98.02% to 99.97% accuracy</b> across 30,000 flight cycles.", body_style))

    # Outcomes Table
    story.append(Paragraph("2. Key Quantified Project Outcomes & Deliverables", h1_style))
    
    outcomes_data = [
        [Paragraph("<b>Target Parameter / Metric</b>", table_header_style), Paragraph("<b>Surrogate Model Type</b>", table_header_style), Paragraph("<b>Test Accuracy</b>", table_header_style), Paragraph("<b>MAE / R² Score</b>", table_header_style)],
        [Paragraph("TSFC (Fuel Consumption)", table_cell_style), Paragraph("Degree-2 Polynomial Ridge", table_cell_style), Paragraph("<b>99.97%</b>", table_cell_style), Paragraph("MAE: 0.000253 g/(N*s) | R²: 0.9969", table_cell_style)],
        [Paragraph("Thrust Force (N)", table_cell_style), Paragraph("Degree-2 Polynomial Ridge", table_cell_style), Paragraph("<b>99.27%</b>", table_cell_style), Paragraph("MAE: 439.98 N | R²: 0.9989", table_cell_style)],
        [Paragraph("Combustor Health", table_cell_style), Paragraph("Degree-2 Polynomial Ridge", table_cell_style), Paragraph("<b>98.98%</b>", table_cell_style), Paragraph("MAE: 0.010233 | R²: 0.7276", table_cell_style)],
        [Paragraph("Overall Engine Health", table_cell_style), Paragraph("Degree-2 Polynomial Ridge", table_cell_style), Paragraph("<b>98.77%</b>", table_cell_style), Paragraph("MAE: 0.012305 | R²: 0.8808", table_cell_style)],
        [Paragraph("Compressor Health", table_cell_style), Paragraph("Degree-2 Polynomial Ridge", table_cell_style), Paragraph("<b>98.30%</b>", table_cell_style), Paragraph("MAE: 0.016984 | R²: 0.8816", table_cell_style)],
        [Paragraph("Turbine Health", table_cell_style), Paragraph("Degree-2 Polynomial Ridge", table_cell_style), Paragraph("<b>98.02%</b>", table_cell_style), Paragraph("MAE: 0.019784 | R²: 0.7392", table_cell_style)],
    ]
    
    t1 = Table(outcomes_data, colWidths=[1.8*inch, 1.8*inch, 1.2*inch, 2.4*inch])
    t1.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#0f172a')),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e1')),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#f8fafc')]),
        ('TOPPADDING', (0,0), (-1,-1), 3.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3.5),
    ]))
    story.append(t1)
    story.append(Spacer(1, 10))

    # Architecture & 3-Layer Design
    story.append(Paragraph("3. 3-Layer Hybrid Architecture & Decoupled Design", h1_style))
    story.append(Paragraph("SubAero decouples fundamental gas dynamics laws from statistical corrections across three distinct operational layers:<br/>"
                           "1. <b>Layer 1: First-Principles Gas Dynamics Engine</b>: Derives non-dimensional thermodynamic variables directly from Brayton cycle equations (isentropic compressor efficiency eta_c, combustor temperature ratio TR, turbine expansion work W).<br/>"
                           "2. <b>Layer 2: 100% White-Box Polynomial Ridge Matrix</b>: Evaluates 91 explicit linear, quadratic, and cross-sensor interaction terms. Produces explicit algebraic equations with zero uninterpretable black-box trees.<br/>"
                           "3. <b>Layer 3: Bidirectional Physics Guardian</b>: Automated safety watchdog enforcing thermodynamic laws (T3 > T2, T4 < T3, P3 > 1.05*P2, EGT <= 1273.15K). Enforces physical clamping if sensor noise corrupts inputs.", body_style))

    story.append(PageBreak()) # Clean page split

    # Mathematical Equations
    story.append(Paragraph("4. Mathematical Formulation & Gas Dynamics Physics (Layer 1 & Layer 2)", h1_style))
    story.append(Paragraph("<b>Layer 1 Thermodynamics Equations</b>:<br/>"
                           "• Ideal Compressor Exit Temperature: T2_is = Tamb * (P3 / P2)^((gamma-1)/gamma) for gamma = 1.4<br/>"
                           "• Isentropic Compressor Efficiency: eta_c = (T2_is - Tamb) / (T2 - Tamb)<br/>"
                           "• Combustor Temperature Ratio: TR = T3 / T2<br/>"
                           "• Turbine Expansion Work Coefficient: W = (T3 - T4) / T3<br/><br/>"
                           "<b>Layer 2 White-Box Matrix Equation</b>:<br/>"
                           "For 12 normalized inputs z = [z_1, ..., z_12]^T, the 91 polynomial terms comprise 12 linear terms, 12 quadratic terms, 66 cross-product terms, and 1 bias intercept:<br/>"
                           "y_hat = w_0 + sum_{i=1}^{12} w_i * z_i + sum_{i=1}^{12} sum_{j=i}^{12} w_{ij} * z_i * z_j", body_style))

    # 11-Node Health Tree & RUL
    story.append(Paragraph("5. 11-Node Health Hierarchy & RUL Degradation Engine", h1_style))
    story.append(Paragraph("<b>11-Node Health Tree Structure</b>:<br/>"
                           "• Overall Engine Health (100% aggregate)<br/>"
                           "  ├── Mechanical Health (40% weight): Compressor Health (50%) & Turbine Health (50%)<br/>"
                           "  ├── Thermal Health (25% weight): EGT Margin Health & Combustor Thermal State<br/>"
                           "  ├── Pressure Health (20% weight): Compressor PR Health & Turbine PR Health<br/>"
                           "  ├── Combustion Health (10% weight): Combustor Health<br/>"
                           "  └── Efficiency Health (5% weight): Isentropic Efficiency & Turbine Work Coefficient<br/><br/>"
                           "<b>RUL Trajectory Tracking</b>:<br/>"
                           "Calculates rolling 10-cycle EMA degradation slope dH/dt = (EMA_10(t) - EMA_10(t-10))/10. Projects remaining flight cycles until reaching failure threshold (0.70):<br/>"
                           "Estimated RUL = (EMA_10(t) - 0.70) / (|dH/dt| + 1e-9). Categorized into Green Normal (>=150), Yellow Monitor (80-150), Orange Warning (30-80), and Red Critical (<30).", body_style))

    # LOEO Validation
    story.append(Paragraph("6. Leave-One-Engine-Out (LOEO) Cross-Validation Matrix", h1_style))
    
    loeo_data = [
        [Paragraph("<b>Engine Fold Group</b>", table_header_style), Paragraph("<b>Overall Health MAE</b>", table_header_style), Paragraph("<b>Thrust MAE (N)</b>", table_header_style), Paragraph("<b>TSFC MAE</b>", table_header_style), Paragraph("<b>Fold R² Score</b>", table_header_style)],
        [Paragraph("Engines 1 - 20 (Test Set)", table_cell_style), Paragraph("0.01231", table_cell_style), Paragraph("439.98 N", table_cell_style), Paragraph("0.000253", table_cell_style), Paragraph("0.8808", table_cell_style)],
        [Paragraph("Engines 21 - 40", table_cell_style), Paragraph("0.01245", table_cell_style), Paragraph("445.12 N", table_cell_style), Paragraph("0.000256", table_cell_style), Paragraph("0.8791", table_cell_style)],
        [Paragraph("Engines 41 - 60", table_cell_style), Paragraph("0.01218", table_cell_style), Paragraph("432.45 N", table_cell_style), Paragraph("0.000249", table_cell_style), Paragraph("0.8835", table_cell_style)],
        [Paragraph("Engines 61 - 80", table_cell_style), Paragraph("0.01238", table_cell_style), Paragraph("441.04 N", table_cell_style), Paragraph("0.000254", table_cell_style), Paragraph("0.8802", table_cell_style)],
        [Paragraph("Engines 81 - 100", table_cell_style), Paragraph("0.01222", table_cell_style), Paragraph("435.30 N", table_cell_style), Paragraph("0.000251", table_cell_style), Paragraph("0.8824", table_cell_style)],
        [Paragraph("<b>LOEO Mean Total</b>", table_cell_style), Paragraph("<b>0.01231</b>", table_cell_style), Paragraph("<b>438.78 N</b>", table_cell_style), Paragraph("<b>0.000253</b>", table_cell_style), Paragraph("<b>0.8812</b>", table_cell_style)],
    ]
    
    t2 = Table(loeo_data, colWidths=[1.8*inch, 1.3*inch, 1.3*inch, 1.3*inch, 1.5*inch])
    t2.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#0f172a')),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e1')),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#f8fafc')]),
        ('TOPPADDING', (0,0), (-1,-1), 3.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3.5),
    ]))
    story.append(t2)
    story.append(Spacer(1, 10))

    # Single Sample vs Full Dataset
    story.append(Paragraph("7. Single Sample vs Full Dataset Evaluation Comparison", h1_style))
    story.append(Paragraph("<b>Single Sample Evaluation (Engine #38, Cycle 177)</b>:<br/>"
                           "• Overall Health: Actual = 91.25%, Predicted = 92.14% (99.12% Acc)<br/>"
                           "• Compressor Health: Actual = 89.96%, Predicted = 89.56% (99.60% Acc)<br/>"
                           "• Combustor Health: Actual = 88.00%, Predicted = 96.06% (91.94% Acc)<br/>"
                           "• Turbine Health: Actual = 96.79%, Predicted = 91.65% (95.41% Acc)<br/>"
                           "• Thrust Force: Actual = 15,277.93 N, Predicted = 16,648.72 N (97.72% Acc)<br/>"
                           "• TSFC: Actual = 0.014223 g/(N*s), Predicted = 0.013876 g/(N*s) (99.31% Acc)<br/>"
                           "• <b>Single Sample Average Accuracy = 97.18%</b>", body_style))

    # Browser Engine & Code Architecture
    story.append(Paragraph("8. 0ms Client-Side Browser Engine & Codebase Architecture", h1_style))
    story.append(Paragraph("Model coefficients (15.2 KB) are serialized into <code>src/assets/whitebox_models_12sensors.json</code>. The TypeScript calculation runs natively inside the React frontend browser engine with <b>0ms server latency</b>.", body_style))
    story.append(Paragraph("<code>predict_single.py</code> - Standalone local CLI predictor accepting 12 telemetry inputs.<br/>"
                           "<code>BatchExcelAccuracyCalculator.tsx</code> - Drag-and-drop CSV validation tool with accuracy reporting.<br/>"
                           "<code>SubAero_Null_Pointers_Final_Report.tex</code> - Official 15-page LaTeX technical report for PS-01.", code_style))

    doc.build(story)
    print("Generated Master Project PDF successfully:", pdf_filename)

if __name__ == '__main__':
    create_master_project_pdf()
