import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, HRFlowable
from reportlab.lib.units import inch

def create_executive_pdf():
    pdf_filename = r"c:\Users\praja\Downloads\AEROTHON2026-main (2)\AEROTHON2026-main\SubAero_Null_Pointers_Executive_9Min_Pitch_Script.pdf"
    
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
        textColor=colors.HexColor('#1e40af'),
        alignment=1,
        spaceAfter=10
    )

    meta_style = ParagraphStyle(
        'MetaStyle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=13.5,
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
        spaceBefore=12,
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

    speech_style = ParagraphStyle(
        'Speech_Custom',
        parent=styles['BodyText'],
        fontName='Helvetica-Oblique',
        fontSize=9,
        leading=13.5,
        textColor=colors.HexColor('#0f172a'),
        spaceAfter=8,
        leftIndent=10,
        rightIndent=10
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
    story.append(Paragraph("EXECUTIVE PROPULSION PITCH SCRIPT & PROTOTYPE DEMO", title_style))
    story.append(Paragraph("HAL × IIT Indore Aerothon 2026 — 9-Minute Executive Defence (No Math Recitation)", subtitle_style))
    story.append(Paragraph("<b>Problem Statement:</b> PS-01 (Physics-Informed Digital Twin for Real-Time Four-Stage Turbojet Health Monitoring)<br/>"
                           "<b>Team Name:</b> Null Pointers &nbsp;|&nbsp; <b>Engineers:</b> Prajan Sanjay K, Kishore Kumar P, Nithish Bharathwaj N, Sridharshini S", meta_style))
    story.append(Spacer(1, 8))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#1d4ed8'), spaceBefore=2, spaceAfter=10))

    # Section 1: Budget
    story.append(Paragraph("1. Executive 9-Minute Presentation Schedule", h1_style))
    
    timeline_data = [
        [Paragraph("<b>Time Budget</b>", table_header_style), Paragraph("<b>Defence Segment</b>", table_header_style), Paragraph("<b>High-Level Executive Focus (No Complex Math)</b>", table_header_style)],
        [Paragraph("0:00 - 0:30 (30s)", table_cell_style), Paragraph("1. Crisp Introduction", table_cell_style), Paragraph("HAL & IIT Indore greeting, PS-01 declaration, Team Null Pointers introduction.", table_cell_style)],
        [Paragraph("0:30 - 1:30 (60s)", table_cell_style), Paragraph("2. PS & Flight Anomaly", table_cell_style), Paragraph("Structural explanation of PS-01 with a real flight degradation example (Engine #38).", table_cell_style)],
        [Paragraph("1:30 - 2:15 (45s)", table_cell_style), Paragraph("3. Expected Outcomes", table_cell_style), Paragraph("Concise outcomes: 4-stage health indices, surrogate Thrust/TSFC, 0ms browser latency.", table_cell_style)],
        [Paragraph("2:15 - 3:15 (60s)", table_cell_style), Paragraph("4. Technical Methodology", table_cell_style), Paragraph("4-stage physics-informed pipeline: Telemetry -> Brayton Physics -> White-Box ML -> UI.", table_cell_style)],
        [Paragraph("3:15 - 4:30 (75s)", table_cell_style), Paragraph("5. Physics & White-Box ML", table_cell_style), Paragraph("Thermodynamic efficiency principles, transparent polynomial matrix, Physics Safety Guardian.", table_cell_style)],
        [Paragraph("4:30 - 6:00 (90s)", table_cell_style), Paragraph("6. Masterpiece Prototype Demo", table_cell_style), Paragraph("Live dashboard, 12-sensor calculation, CSV batch accuracy (98.02%-99.97%), RUL EMA trajectory.", table_cell_style)],
        [Paragraph("6:00 - 6:30 (30s)", table_cell_style), Paragraph("7. Literature & Conclusion", table_cell_style), Paragraph("Benchmark against NASA & Elsevier standards, defense-ready summary.", table_cell_style)],
        [Paragraph("6:30 - 9:30 (3m)", table_cell_style), Paragraph("8. Reserved Technical Q&A", table_cell_style), Paragraph("3-minute reserved buffer for HAL propulsion directors' questions.", table_cell_style)],
    ]
    
    t1 = Table(timeline_data, colWidths=[1.2*inch, 1.8*inch, 4.2*inch])
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

    # Section 2: Word-for-Word Script
    story.append(Paragraph("2. Executive Word-for-Word Speech Script", h1_style))

    # Segment 1
    story.append(Paragraph("SEGMENT 1: Crisp Introduction (0:00 - 0:30)", h2_style))
    story.append(Paragraph('"Good morning/afternoon, Evaluation Board, Chief Engineers from Hindustan Aeronautics Limited, and Faculty from IIT Indore.<br/><br/>'
                           'We are <b>Team Null Pointers</b>. I am <b>Prajan Sanjay K</b>, Lead Digital Twin Architect, alongside my teammates <b>Sridharshini S</b>, Physics Modeling Engineer; <b>Kishore Kumar P</b>, Machine Learning Engineer; and <b>Nithish Bharathwaj N</b>, Full-Stack Developer.<br/><br/>'
                           'We are proud to present <b>SubAero</b>—our solution for <b>Problem Statement 01</b>: a real-time, 100% transparent Physics-Informed Digital Twin for four-stage turbojet health monitoring."', speech_style))

    # Segment 2
    story.append(Paragraph("SEGMENT 2: Problem Statement Breakdown & Flight Anomaly Example (0:30 - 1:30)", h2_style))
    story.append(Paragraph('"To understand the core problem of PS-01: turbojet engines operate under severe temperature and pressure stress. Critical component states—such as internal compressor blade fouling, combustor thermal degradation, and turbine wear—cannot be measured directly during flight with sensors.<br/><br/>'
                           '<b>Consider a real flight scenario</b>: Engine #38 flying at cruise altitude. Sensor telemetry shows standard operating temperatures. However, hidden compressor fouling has silently reduced internal efficiency, causing net thrust force to drop by over 1,000 Newtons while burning significantly more fuel.<br/><br/>'
                           'Existing simulation software is too slow for real-time flight monitoring, while standard black-box AI models lack transparency, making them risky for mission-critical aerospace deployment."', speech_style))

    # Segment 3
    story.append(Paragraph("SEGMENT 3: Expected Outcomes (Concise & Quantified) (1:30 - 2:15)", h2_style))
    story.append(Paragraph('"Our system delivers four key operational outcomes:<br/>'
                           '1. <b>Real-Time Health Reconstruction</b>: Continuously estimates health across all 4 stages—Compressor, Combustor, Turbine, and Overall engine state with over 98% accuracy.<br/>'
                           '2. <b>Performance Surrogate Modeling</b>: Accurately predicts net Thrust force and Specific Fuel Consumption.<br/>'
                           '3. <b>Zero Latency Browser Execution</b>: Runs predictions instantly inside the cockpit or ground station UI without server delays.<br/>'
                           '4. <b>Predictive Maintenance & RUL</b>: Projects Remaining Useful Life to alert maintenance teams long before failure occurs."', speech_style))

    story.append(PageBreak()) # Clean page split

    # Segment 4
    story.append(Paragraph("SEGMENT 4: Technical Methodology & System Architecture (2:15 - 3:15)", h2_style))
    story.append(Paragraph('"Our methodology combines thermodynamics with data science across 4 seamless stages:<br/><br/>'
                           '1. <b>Telemetry Processing</b>: Ingests 12 raw operational telemetry streams including pressure, temperature, altitude, Mach number, shaft speed, and fuel flow.<br/>'
                           '2. <b>Thermodynamic Feature Engineering</b>: Applies fundamental gas turbine Brayton cycle principles to derive key efficiency, temperature, and work ratios.<br/>'
                           '3. <b>100% White-Box Machine Learning</b>: Uses transparent, regularized polynomial matrix models that eliminate hidden black-box decisions.<br/>'
                           '4. <b>Digital Twin Dashboard</b>: Connects predictions to a real-time React and 3D Unity interface for intuitive fleet monitoring."', speech_style))

    # Segment 5
    story.append(Paragraph("SEGMENT 5: Physics Implementation & White-Box ML (3:15 - 4:30)", h2_style))
    story.append(Paragraph('"Here is how our physics and machine learning work together cleanly:<br/><br/>'
                           '• <b>First-Principles Physics</b>: Instead of relying purely on statistical guessing, we calculate true compressor isentropic efficiency, combustor thermal ratios, and turbine work coefficients using thermodynamics.<br/>'
                           '• <b>100% Transparent White-Box ML</b>: We explicitly model operational parameters using clear linear, quadratic, and cross-sensor interaction terms. Every calculation is fully auditable and 100% explainable.<br/>'
                           '• <b>Physics Safety Guardian</b>: The system automatically enforces physical safety laws—ensuring temperatures and pressures follow thermodynamic rules. If sensor noise corrupts data, the Guardian flags anomalies and safely clamps predictions."', speech_style))

    # Segment 6
    story.append(Paragraph("SEGMENT 6: Masterpiece Prototype Demonstration Script (4:30 - 6:00)", h2_style))
    story.append(Paragraph('"Now, let us walk through our <b>Live Prototype Demonstration</b>:<br/><br/>'
                           '• <b>Step 1: Dashboard Viewport</b>: On our dashboard, you see our 3D Turbofan Twin rendering live thermal heatmaps on the engine casing.<br/>'
                           '• <b>Step 2: Instant 12-Sensor Calculation</b>: As we enter 12 raw telemetry values, SubAero calculates all health and performance metrics instantly with <b>0ms latency</b>—predicting Overall Health at 92.14%, Thrust at 16,648 Newtons, and TSFC fuel consumption accurately.<br/>'
                           '• <b>Step 3: CSV Batch Evaluation Matrix</b>: Uploading an evaluation dataset renders our verified accuracy report: <b>99.97% TSFC Accuracy</b>, <b>99.27% Thrust Accuracy</b>, and <b>98.02% to 98.98% Health Accuracy</b>.<br/>'
                           '• <b>Step 4: RUL & Safety Alerts</b>: The 11-node health tree tracks degradation trends, projecting remaining flight cycles and alerting engineers in Green Normal, Yellow Monitor, Orange Warning, or Red Critical zones."', speech_style))

    # Segment 7
    story.append(Paragraph("SEGMENT 7: Literature Survey & Conclusion (6:00 - 6:30)", h2_style))
    story.append(Paragraph('"<b>Literature Benchmarks</b>: Benchmarked against NASA C-MAPSS standards and recent 2025 Elsevier research, SubAero advances existing work by offering <b>instant browser execution</b>, <b>100% transparent white-box models</b>, and <b>strong generalizability across unseen engines</b>.<br/><br/>'
                           '<b>Conclusion</b>: SubAero provides HAL with a defense-ready, physics-validated digital twin that delivers accurate health estimation, zero latency, and complete engineering transparency."', speech_style))

    story.append(Spacer(1, 10))

    # Section 3: Q&A Reserve
    story.append(Paragraph("3. Reserved Q&A Executive Defense Strategy (6:30 - 9:30)", h1_style))
    
    qa_data = [
        [Paragraph("<b>Board Question</b>", table_header_style), Paragraph("<b>Executive Response (No Complex Formulas)</b>", table_header_style)],
        [Paragraph("Why use White-Box ML over Deep Learning?", table_cell_style), Paragraph("Deep learning neural networks are black boxes that cannot be certified for safety-critical aviation deployment. Our transparent polynomial matrix model provides 100% explainability, explicit feature weights, and high accuracy (98%-99%) while complying with flight safety standards.", table_cell_style)],
        [Paragraph("How do you handle sensor errors or noise?", table_cell_style), Paragraph("Our Physics Safety Guardian continuously verifies thermodynamic rules. If faulty telemetry shows unphysical readings—like temperature inversions—the Guardian immediately flags the sensor anomaly and clamps predictions within safe boundaries.", table_cell_style)],
        [Paragraph("How well does it work on new, unseen engines?", table_cell_style), Paragraph("We validated generalizability using Leave-One-Engine-Out testing across 100 engines. Testing on completely unseen engines proved strong consistency with zero overfitting, ensuring reliable real-world deployment.", table_cell_style)],
    ]
    
    t2 = Table(qa_data, colWidths=[2.2*inch, 4.8*inch])
    t2.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#0f172a')),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e1')),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#f8fafc')]),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t2)

    doc.build(story)
    print("Generated Executive PDF successfully:", pdf_filename)

if __name__ == '__main__':
    create_executive_pdf()
