import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, HRFlowable
from reportlab.lib.units import inch

def create_master_tech_pdf():
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
        fontSize=18,
        leading=22,
        textColor=colors.HexColor('#0f172a'),
        alignment=1,
        spaceAfter=6
    )
    
    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=15,
        textColor=colors.HexColor('#1d4ed8'),
        alignment=1,
        spaceAfter=10
    )

    meta_style = ParagraphStyle(
        'MetaStyle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        textColor=colors.HexColor('#334155'),
        alignment=1
    )
    
    h1_style = ParagraphStyle(
        'Heading1_Custom',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=12.5,
        leading=15,
        textColor=colors.HexColor('#0f172a'),
        spaceBefore=12,
        spaceAfter=5
    )

    h2_style = ParagraphStyle(
        'Heading2_Custom',
        parent=styles['Heading3'],
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=13.5,
        textColor=colors.HexColor('#1d4ed8'),
        spaceBefore=8,
        spaceAfter=4
    )
    
    body_style = ParagraphStyle(
        'Body_Custom',
        parent=styles['BodyText'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=12.5,
        textColor=colors.HexColor('#1e293b'),
        spaceAfter=5
    )

    code_style = ParagraphStyle(
        'Code_Custom',
        parent=styles['Normal'],
        fontName='Courier',
        fontSize=7.5,
        leading=10.5,
        textColor=colors.HexColor('#0f172a'),
        backColor=colors.HexColor('#f1f5f9'),
        borderColor=colors.HexColor('#cbd5e1'),
        borderWidth=0.5,
        borderPadding=5,
        spaceAfter=5
    )

    table_header_style = ParagraphStyle(
        'TableHeader',
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=10.5,
        textColor=colors.white,
        alignment=1
    )

    table_cell_style = ParagraphStyle(
        'TableCell',
        fontName='Helvetica',
        fontSize=7.5,
        leading=10.5,
        textColor=colors.HexColor('#1e293b')
    )

    story = []
    
    # Title Block
    story.append(Paragraph("SUBAERO: EXHAUSTIVE MASTER TECHNICAL & PHYSICS REFERENCE", title_style))
    story.append(Paragraph("End-to-End Documentation: Physics Formulas, ML Models & Detailed Tech Stack", subtitle_style))
    story.append(Paragraph("<b>Problem Statement:</b> PS-01 (IIT Indore & Hindustan Aeronautics Limited - HAL)<br/>"
                           "<b>Team Name:</b> Null Pointers &nbsp;|&nbsp; <b>Engineers:</b> Prajan Sanjay K, Kishore Kumar P, Nithish Bharathwaj N, Sridharshini S<br/>"
                           "<b>Repository:</b> https://github.com/prajansanjayk1/subaero.git &nbsp;|&nbsp; <b>Classification:</b> Master Technical Reference", meta_style))
    story.append(Spacer(1, 6))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#1d4ed8'), spaceBefore=2, spaceAfter=8))

    # Section 1: All Physics Formulas
    story.append(Paragraph("1. Complete List of 24 Physics & Thermodynamics Formulas Implemented", h1_style))
    
    physics_data = [
        [Paragraph("<b>Domain / Category</b>", table_header_style), Paragraph("<b>Physics Parameter / Formula Name</b>", table_header_style), Paragraph("<b>Mathematical Equation & Formulation</b>", table_header_style)],
        [Paragraph("Atmospheric Gas Dynamics", table_cell_style), Paragraph("Speed of Sound (a)", table_cell_style), Paragraph("a = sqrt(gamma * R * Tamb) where gamma=1.4, R=287.05 J/(kg*K)", table_cell_style)],
        [Paragraph("Atmospheric Gas Dynamics", table_cell_style), Paragraph("True Airspeed (V)", table_cell_style), Paragraph("V = Mach * a = Mach * sqrt(gamma * R * Tamb)", table_cell_style)],
        [Paragraph("Compressor Thermodynamics", table_cell_style), Paragraph("Compressor Pressure Ratio", table_cell_style), Paragraph("PR_comp = P3 / P2", table_cell_style)],
        [Paragraph("Compressor Thermodynamics", table_cell_style), Paragraph("Ideal Isentropic Exit Temp", table_cell_style), Paragraph("T2_is = Tamb * (P3 / P2)^((gamma-1)/gamma)", table_cell_style)],
        [Paragraph("Compressor Thermodynamics", table_cell_style), Paragraph("Isentropic Efficiency (eta_c)", table_cell_style), Paragraph("eta_c = (T2_is - Tamb) / (T2 - Tamb)", table_cell_style)],
        [Paragraph("Compressor Thermodynamics", table_cell_style), Paragraph("Compressor Temp Rise", table_cell_style), Paragraph("dT_comp = T3 - T2 [Kelvin]", table_cell_style)],
        [Paragraph("Compressor Thermodynamics", table_cell_style), Paragraph("Compressor Specific Work", table_cell_style), Paragraph("w_comp = cp * (T3 - T2) where cp=1005 J/(kg*K)", table_cell_style)],
        [Paragraph("Combustor Thermal State", table_cell_style), Paragraph("Combustor Temp Ratio", table_cell_style), Paragraph("TR_comb = T3 / T2", table_cell_style)],
        [Paragraph("Combustor Thermal State", table_cell_style), Paragraph("Heat Addition Rate (q_in)", table_cell_style), Paragraph("q_in = cp * (T3 - T2) [J/kg]", table_cell_style)],
        [Paragraph("Combustor Thermal State", table_cell_style), Paragraph("Fuel-Air Ratio Proxy (f)", table_cell_style), Paragraph("f = FuelFlow / (RPM * P2 / T2)", table_cell_style)],
        [Paragraph("Turbine Work Dynamics", table_cell_style), Paragraph("Turbine Temp Expansion Ratio", table_cell_style), Paragraph("TR_turb = T4 / T3", table_cell_style)],
        [Paragraph("Turbine Work Dynamics", table_cell_style), Paragraph("Turbine Pressure Expansion Ratio", table_cell_style), Paragraph("PR_turb = P3 / P4", table_cell_style)],
        [Paragraph("Turbine Work Dynamics", table_cell_style), Paragraph("Work Coefficient (W)", table_cell_style), Paragraph("W = (T3 - T4) / T3", table_cell_style)],
        [Paragraph("Turbine Work Dynamics", table_cell_style), Paragraph("Turbine Temp Drop", table_cell_style), Paragraph("dT_turb = T3 - T4 [Kelvin]", table_cell_style)],
        [Paragraph("Thermal Stress & Limits", table_cell_style), Paragraph("Thermal Stress Index (sigma)", table_cell_style), Paragraph("sigma_thermal = (T3 / T2) * (P3 / P2)", table_cell_style)],
        [Paragraph("Thermal Stress & Limits", table_cell_style), Paragraph("EGT Safety Margin", table_cell_style), Paragraph("EGT_margin = 1273.15 - T4 [Kelvin]", table_cell_style)],
        [Paragraph("Performance Surrogates", table_cell_style), Paragraph("Net Thrust Force (F_net)", table_cell_style), Paragraph("F_net = dot(phi(z), W_thrust) [Newtons]", table_cell_style)],
        [Paragraph("Performance Surrogates", table_cell_style), Paragraph("Fuel TSFC", table_cell_style), Paragraph("TSFC = FuelFlow / F_net [g/(N*s)]", table_cell_style)],
        [Paragraph("Physics Guardian Rules", table_cell_style), Paragraph("Compressor Work Rule", table_cell_style), Paragraph("T3 > T2 (Flag Compressor_Work_Inversion if violated)", table_cell_style)],
        [Paragraph("Physics Guardian Rules", table_cell_style), Paragraph("Combustor Expansion Rule", table_cell_style), Paragraph("T4 < T3 (Flag Combustor_Heat_Inversion if violated)", table_cell_style)],
        [Paragraph("Physics Guardian Rules", table_cell_style), Paragraph("Pressure Ratio Rule", table_cell_style), Paragraph("P3 > P2 * 1.05 (Flag Compression_Loss_Surge if violated)", table_cell_style)],
        [Paragraph("Physics Guardian Rules", table_cell_style), Paragraph("EGT Overheat Limit", table_cell_style), Paragraph("T4 <= 1273.15 K (Flag EGT_CRITICAL_OVERTEMP if violated)", table_cell_style)],
        [Paragraph("Health Tree & RUL", table_cell_style), Paragraph("11-Node Health Tree Aggregation", table_cell_style), Paragraph("H_overall = 0.40*H_mech + 0.25*H_thermal + 0.20*H_press + 0.10*H_comb + 0.05*H_eff", table_cell_style)],
        [Paragraph("Health Tree & RUL", table_cell_style), Paragraph("RUL Degradation Trajectory", table_cell_style), Paragraph("RUL = (EMA10(t) - 0.70) / (|dH/dt| + 1e-9) [Cycles]", table_cell_style)],
    ]
    
    t1 = Table(physics_data, colWidths=[1.5*inch, 1.8*inch, 3.7*inch])
    t1.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#0f172a')),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e1')),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#f8fafc')]),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
    ]))
    story.append(t1)
    story.append(PageBreak())

    # Section 2: ML Models Detailed Version
    story.append(Paragraph("2. Machine Learning Models Specification (Detailed Version)", h1_style))
    story.append(Paragraph("<b>Primary ML Architecture: 100% White-Box Regularized Polynomial Matrix Model Engine</b><br/>"
                           "• <b>Surrogate Class</b>: Scikit-Learn Degree-2 Regularized Polynomial Ridge Regression (alpha = 50.0).<br/>"
                           "• <b>Mathematical Matrix Formulation</b>: y_hat = w0 + sum_{k=1}^{91} w_k * phi_k(z_1, ..., z_12)<br/>"
                           "• <b>Polynomial Term Expansion (91 terms)</b>: 1 Bias Intercept, 12 Linear Terms, 12 Quadratic Terms (z_i^2), and 66 Cross-Sensor Interaction Terms (z_i * z_j).<br/>"
                           "• <b>Client Asset Serialization</b>: Compiled into lightweight JSON asset <code>src/assets/whitebox_models_12sensors.json</code> (15.2 KB) for 0ms browser inference.<br/>"
                           "• <b>Python Model Files</b>: Serialized Scikit-Learn pipelines stored in <code>trained_models_whitebox_12s/</code>.<br/>"
                           "• <b>RUL Predictor Engine</b>: Sensor-based 10-cycle Exponential Moving Average (EMA_10) degradation rate velocity extrapolator.<br/>"
                           "• <b>Black-Box Purge</b>: 0% Tree ensembles (LightGBM, XGBoost, CatBoost, ExtraTrees completely removed).", body_style))
    
    ml_models_table = [
        [Paragraph("<b>Target Parameter</b>", table_header_style), Paragraph("<b>ML Model Algorithm</b>", table_header_style), Paragraph("<b>Accuracy</b>", table_header_style), Paragraph("<b>MAE / RMSE Metric</b>", table_header_style), Paragraph("<b>R² Score</b>", table_header_style)],
        [Paragraph("TSFC (Fuel Consumption)", table_cell_style), Paragraph("Degree-2 Polynomial Ridge", table_cell_style), Paragraph("<b>99.97%</b>", table_cell_style), Paragraph("0.000253 g/(N*s) | 0.000339", table_cell_style), Paragraph("0.9969", table_cell_style)],
        [Paragraph("Thrust Force (N)", table_cell_style), Paragraph("Degree-2 Polynomial Ridge", table_cell_style), Paragraph("<b>99.27%</b>", table_cell_style), Paragraph("439.98 N | 572.33 N", table_cell_style), Paragraph("0.9989", table_cell_style)],
        [Paragraph("Combustor Health", table_cell_style), Paragraph("Degree-2 Polynomial Ridge", table_cell_style), Paragraph("<b>98.98%</b>", table_cell_style), Paragraph("0.010233 | 0.013416", table_cell_style), Paragraph("0.7276", table_cell_style)],
        [Paragraph("Overall Engine Health", table_cell_style), Paragraph("Degree-2 Polynomial Ridge", table_cell_style), Paragraph("<b>98.77%</b>", table_cell_style), Paragraph("0.012305 | 0.016335", table_cell_style), Paragraph("0.8808", table_cell_style)],
        [Paragraph("Compressor Health", table_cell_style), Paragraph("Degree-2 Polynomial Ridge", table_cell_style), Paragraph("<b>98.30%</b>", table_cell_style), Paragraph("0.016984 | 0.023027", table_cell_style), Paragraph("0.8816", table_cell_style)],
        [Paragraph("Turbine Health", table_cell_style), Paragraph("Degree-2 Polynomial Ridge", table_cell_style), Paragraph("<b>98.02%</b>", table_cell_style), Paragraph("0.019784 | 0.025685", table_cell_style), Paragraph("0.7392", table_cell_style)],
    ]
    
    t2 = Table(ml_models_table, colWidths=[1.5*inch, 1.6*inch, 1.0*inch, 1.6*inch, 0.8*inch])
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

    # Section 3: Technology Stack Detailed Version
    story.append(Paragraph("3. Complete Technology Stack Specification (Detailed Versions)", h1_style))
    
    tech_stack_data = [
        [Paragraph("<b>Tech Stack Component Layer</b>", table_header_style), Paragraph("<b>Framework / Technology Package</b>", table_header_style), Paragraph("<b>Exact Version</b>", table_header_style), Paragraph("<b>Engineering Purpose & Role</b>", table_header_style)],
        [Paragraph("Machine Learning & Data Science", table_cell_style), Paragraph("Python Language Runtime", table_cell_style), Paragraph("v3.11.7", table_cell_style), Paragraph("Core ML pipeline training, data processing, and CLI predictors.", table_cell_style)],
        [Paragraph("Machine Learning & Data Science", table_cell_style), Paragraph("Scikit-Learn", table_cell_style), Paragraph("v1.4.0", table_cell_style), Paragraph("PolynomialFeatures, Ridge regression, and StandardScaler pipelines.", table_cell_style)],
        [Paragraph("Machine Learning & Data Science", table_cell_style), Paragraph("NumPy", table_cell_style), Paragraph("v1.26.4", table_cell_style), Paragraph("High-performance matrix operations and polynomial term dot products.", table_cell_style)],
        [Paragraph("Machine Learning & Data Science", table_cell_style), Paragraph("Pandas", table_cell_style), Paragraph("v2.2.0", table_cell_style), Paragraph("Dataset manipulation, CSV telemetry parsing, and ground truth merging.", table_cell_style)],
        [Paragraph("Machine Learning & Data Science", table_cell_style), Paragraph("Joblib", table_cell_style), Paragraph("v1.3.2", table_cell_style), Paragraph("Serialization and deserialization of trained white-box ML models.", table_cell_style)],
        [Paragraph("Machine Learning & Data Science", table_cell_style), Paragraph("SciPy & CoolProp", table_cell_style), Paragraph("v1.12.0 / v6.4.3", table_cell_style), Paragraph("Thermodynamic fluid properties and Brayton cycle gas dynamics calculations.", table_cell_style)],
        [Paragraph("Frontend UI & Web App", table_cell_style), Paragraph("TypeScript", table_cell_style), Paragraph("v5.2.2", table_cell_style), Paragraph("Type-safe frontend logic and client-side 0ms matrix prediction engine.", table_cell_style)],
        [Paragraph("Frontend UI & Web App", table_cell_style), Paragraph("React Framework", table_cell_style), Paragraph("v18.2.0", table_cell_style), Paragraph("Component-driven Mission Control Dashboard UI.", table_cell_style)],
        [Paragraph("Frontend UI & Web App", table_cell_style), Paragraph("Vite Build Engine", table_cell_style), Paragraph("v6.4.3", table_cell_style), Paragraph("Lightning-fast HMR dev server and production bundling.", table_cell_style)],
        [Paragraph("Frontend UI & Web App", table_cell_style), Paragraph("Tailwind CSS", table_cell_style), Paragraph("v3.4.1", table_cell_style), Paragraph("Modern glassmorphism UI styling and responsive dashboard layout.", table_cell_style)],
        [Paragraph("Frontend UI & Web App", table_cell_style), Paragraph("Recharts & Lucide-React", table_cell_style), Paragraph("v2.12.2 / v0.344.0", table_cell_style), Paragraph("Telemetry sparklines, health accuracy charts, and aerospace UI icons.", table_cell_style)],
        [Paragraph("3D Digital Twin Engine", table_cell_style), Paragraph("Unity Engine & Blender", table_cell_style), Paragraph("2022.3 LTS / 4.0 LTS", table_cell_style), Paragraph("3D Turbojet CAD modeling and real-time casing thermal heatmap viewport.", table_cell_style)],
        [Paragraph("Backend & Database", table_cell_style), Paragraph("FastAPI & Uvicorn", table_cell_style), Paragraph("v0.109.0 / v0.27.0", table_cell_style), Paragraph("Asynchronous REST API gateway for edge telemetry streaming.", table_cell_style)],
        [Paragraph("Documentation & Publishing", table_cell_style), Paragraph("ReportLab & pdfLaTeX", table_cell_style), Paragraph("v4.1.0 / MiKTeX 24.1", table_cell_style), Paragraph("PDF document compilation and official 15-page LaTeX technical report.", table_cell_style)],
    ]
    
    t3 = Table(tech_stack_data, colWidths=[1.4*inch, 1.4*inch, 0.9*inch, 3.3*inch])
    t3.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#0f172a')),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e1')),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#f8fafc')]),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
    ]))
    story.append(t3)

    doc.build(story)
    print("Generated Master Tech & Physics PDF successfully:", pdf_filename)

if __name__ == '__main__':
    create_master_tech_pdf()
