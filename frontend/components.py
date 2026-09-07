import streamlit as st


# ============================================================
# HERO
# ============================================================

def hero():

    st.markdown(
        """
        <div class="hero-card">

            <div style="
                display:flex;
                align-items:center;
                gap:10px;
                margin-bottom:8px;
            ">

                <span style="
                    width:8px;
                    height:8px;
                    border-radius:50%;
                    background:#22C55E;
                    display:inline-block;
                    box-shadow:0 0 10px rgba(34,197,94,0.6);
                "></span>

                <span style="
                    color:#67E8F9;
                    font-size:12px;
                    font-weight:800;
                    letter-spacing:2px;
                ">
                    AI LOGISTICS COMMAND CENTER
                </span>

            </div>


            <h1 style="
                margin:6px 0 5px 0;
                font-size:40px;
                font-weight:800;
                color:#F8FAFC;
                line-height:1.15;
            ">
                NER Smart Logistics AI
            </h1>


            <p style="
                color:#94A3B8;
                font-size:16px;
                margin:0;
                max-width:750px;
                line-height:1.6;
            ">
                Risk-aware logistics intelligence for
                India's North Eastern Region.
            </p>


            <div style="
                display:flex;
                gap:10px;
                flex-wrap:wrap;
                margin-top:18px;
            ">

                <span class="status-online">
                    ● SYSTEM ONLINE
                </span>

                <span style="
                    display:inline-flex;
                    align-items:center;
                    padding:6px 11px;
                    border-radius:999px;
                    background:rgba(25,195,255,0.08);
                    border:1px solid rgba(25,195,255,0.22);
                    color:#67E8F9;
                    font-size:12px;
                    font-weight:700;
                ">
                    AI ENABLED
                </span>

                <span style="
                    display:inline-flex;
                    align-items:center;
                    padding:6px 11px;
                    border-radius:999px;
                    background:rgba(148,163,184,0.08);
                    border:1px solid rgba(148,163,184,0.18);
                    color:#94A3B8;
                    font-size:12px;
                    font-weight:700;
                ">
                    NER REGION
                </span>

            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# KPI CARD
# ============================================================

def kpi(title, value, subtitle, icon="📊"):

    st.markdown(
        f"""
        <div class="ner-card" style="
            min-height:125px;
            position:relative;
            overflow:hidden;
        ">

            <div style="
                position:absolute;
                right:-25px;
                top:-25px;
                width:90px;
                height:90px;
                border-radius:50%;
                background:rgba(25,195,255,0.05);
            ">
            </div>


            <div style="
                display:flex;
                justify-content:space-between;
                align-items:center;
                position:relative;
            ">

                <span style="
                    color:#94A3B8;
                    font-size:13px;
                    font-weight:700;
                    letter-spacing:0.3px;
                ">
                    {title}
                </span>


                <span style="
                    display:flex;
                    align-items:center;
                    justify-content:center;
                    width:38px;
                    height:38px;
                    border-radius:10px;
                    background:rgba(25,195,255,0.08);
                    border:1px solid rgba(25,195,255,0.15);
                    font-size:20px;
                ">
                    {icon}
                </span>

            </div>


            <div style="
                color:#F8FAFC;
                font-size:32px;
                font-weight:800;
                margin-top:12px;
                line-height:1;
            ">
                {value}
            </div>


            <div style="
                color:#64748B;
                font-size:12px;
                margin-top:8px;
            ">
                {subtitle}
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# ALERT CARD
# ============================================================

def alert_card(title, message, level="MEDIUM"):

    level = level.upper()

    level_map = {

        "LOW": (
            "🟢",
            "#22C55E",
            "LOW RISK"
        ),

        "MEDIUM": (
            "🟠",
            "#F59E0B",
            "MODERATE"
        ),

        "HIGH": (
            "🔴",
            "#EF4444",
            "HIGH RISK"
        ),

        "CRITICAL": (
            "🚨",
            "#EF4444",
            "CRITICAL"
        ),
    }


    icon, color, label = level_map.get(
        level,
        ("⚠️", "#F59E0B", level)
    )


    extra_class = ""

    if level == "CRITICAL" or level == "HIGH":
        extra_class = "alert-critical"

    elif level == "LOW":
        extra_class = "alert-success"


    st.markdown(
        f"""
        <div class="alert-card {extra_class}"
             style="border-left-color:{color};">

            <div style="
                display:flex;
                justify-content:space-between;
                align-items:center;
                gap:15px;
            ">

                <div style="
                    display:flex;
                    align-items:center;
                    gap:9px;
                ">

                    <span style="font-size:18px;">
                        {icon}
                    </span>

                    <strong style="
                        color:#F8FAFC;
                        font-size:14px;
                    ">
                        {title}
                    </strong>

                </div>


                <span style="
                    color:{color};
                    font-size:10px;
                    font-weight:800;
                    letter-spacing:0.7px;
                    white-space:nowrap;
                ">
                    {label}
                </span>

            </div>


            <div style="
                color:#94A3B8;
                margin-top:8px;
                font-size:13px;
                line-height:1.5;
            ">
                {message}
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# SECTION TITLE
# ============================================================

def section_title(title, subtitle=None):

    html = f"""
    <div style="
        margin-top:28px;
        margin-bottom:16px;
    ">

        <div style="
            display:flex;
            align-items:center;
            gap:9px;
        ">

            <div style="
                width:4px;
                height:22px;
                border-radius:5px;
                background:#19C3FF;
                box-shadow:
                    0 0 10px rgba(25,195,255,0.35);
            ">
            </div>


            <h2 style="
                margin:0;
                font-size:22px;
                font-weight:800;
                color:#F8FAFC;
            ">
                {title}
            </h2>

        </div>
    """


    if subtitle:

        html += f"""
        <p style="
            color:#64748B;
            margin:6px 0 0 13px;
            font-size:13px;
        ">
            {subtitle}
        </p>
        """


    html += "</div>"


    st.markdown(
        html,
        unsafe_allow_html=True
    )


# ============================================================
# STATUS BADGE
# ============================================================

def status_badge(status):

    status = str(status).upper()


    colors = {

        "DELIVERED": "#22C55E",

        "IN TRANSIT": "#19C3FF",

        "DELAYED": "#F59E0B",

        "CRITICAL": "#EF4444",

        "LOW": "#22C55E",

        "MEDIUM": "#F59E0B",

        "HIGH": "#EF4444",

        "ACTIVE": "#22C55E",

        "PENDING": "#F59E0B",

        "COMPLETED": "#22C55E",

        "CANCELLED": "#EF4444",
    }


    color = colors.get(
        status,
        "#94A3B8"
    )


    st.markdown(
        f"""
        <span style="
            display:inline-flex;
            align-items:center;
            gap:6px;

            background:{color}14;

            color:{color};

            border:1px solid {color}45;

            padding:5px 10px;

            border-radius:999px;

            font-size:11px;

            font-weight:800;

            letter-spacing:0.3px;

            white-space:nowrap;
        ">

            <span style="
                width:6px;
                height:6px;
                border-radius:50%;
                background:{color};
                display:inline-block;
            "></span>

            {status}

        </span>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# INFO CARD
# ============================================================

def info_card(title, value, description="", icon="ℹ️"):

    st.markdown(
        f"""
        <div class="ner-card">

            <div style="
                display:flex;
                align-items:center;
                gap:10px;
                margin-bottom:10px;
            ">

                <span style="font-size:20px;">
                    {icon}
                </span>

                <span style="
                    color:#94A3B8;
                    font-size:13px;
                    font-weight:700;
                ">
                    {title}
                </span>

            </div>


            <div style="
                color:#F8FAFC;
                font-size:24px;
                font-weight:800;
            ">
                {value}
            </div>


            <div style="
                color:#64748B;
                font-size:12px;
                margin-top:5px;
            ">
                {description}
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )