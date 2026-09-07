import streamlit as st


def load_css():

    st.markdown(
        """
        <style>

        /* =========================================================
           NER SMART LOGISTICS AI
           GLOBAL DESIGN SYSTEM
        ========================================================= */

        :root {
            --bg: #07111F;
            --bg-secondary: #081522;
            --card: #0D1B2A;
            --card-hover: #112438;

            --primary: #19C3FF;
            --primary-dark: #0EA5E9;

            --success: #22C55E;
            --warning: #F59E0B;
            --danger: #EF4444;

            --text: #F8FAFC;
            --text-secondary: #CBD5E1;
            --muted: #94A3B8;

            --border: #1E3A52;
            --border-light: #24465E;
        }


        /* =========================================================
           GLOBAL APP
        ========================================================= */

        .stApp {

            background:
                radial-gradient(
                    circle at 10% 0%,
                    rgba(25,195,255,0.09),
                    transparent 30%
                ),
                radial-gradient(
                    circle at 90% 20%,
                    rgba(14,165,233,0.05),
                    transparent 25%
                ),
                linear-gradient(
                    135deg,
                    #07111F 0%,
                    #081522 50%,
                    #07111F 100%
                );

            color: var(--text);

            min-height: 100vh;
        }


        /* =========================================================
           MAIN CONTAINER
        ========================================================= */

        .main .block-container {

            padding-top: 1.8rem;
            padding-bottom: 4rem;

            max-width: 1500px;

            animation: pageFade 0.45s ease;
        }


        /* =========================================================
           PAGE ANIMATION
        ========================================================= */

        @keyframes pageFade {

            from {
                opacity: 0;
                transform: translateY(8px);
            }

            to {
                opacity: 1;
                transform: translateY(0);
            }

        }


        /* =========================================================
           REMOVE STREAMLIT DEFAULT UI
        ========================================================= */

        #MainMenu {
            visibility: hidden;
        }

        footer {
            visibility: hidden;
        }

        header {
            visibility: hidden;
        }


        /* =========================================================
           SIDEBAR
        ========================================================= */

        section[data-testid="stSidebar"] {

            background:
                linear-gradient(
                    180deg,
                    #081522 0%,
                    #07111F 100%
                );

            border-right: 1px solid var(--border);

            box-shadow:
                8px 0 30px rgba(0,0,0,0.18);
        }


        section[data-testid="stSidebar"] > div {

            padding-top: 1rem;
            padding-left: 0.8rem;
            padding-right: 0.8rem;
        }


        /* =========================================================
           SIDEBAR TEXT
        ========================================================= */

        section[data-testid="stSidebar"] h1,
        section[data-testid="stSidebar"] h2,
        section[data-testid="stSidebar"] h3 {

            color: var(--text) !important;
        }


        /* =========================================================
           TYPOGRAPHY
        ========================================================= */

        h1,
        h2,
        h3,
        h4 {

            color: var(--text) !important;

            letter-spacing: -0.5px;

            font-weight: 750;
        }


        p,
        label {

            color: var(--text-secondary) !important;
        }


        /* =========================================================
           LINKS
        ========================================================= */

        a {

            color: var(--primary) !important;

            text-decoration: none;

            transition: 0.2s ease;
        }

        a:hover {

            color: #67D9FF !important;

            text-decoration: none;
        }


        /* =========================================================
           BUTTONS
        ========================================================= */

        .stButton > button {

            width: 100%;

            min-height: 42px;

            border-radius: 10px;

            border: 1px solid #1E4863;

            background:
                linear-gradient(
                    135deg,
                    #0EA5E9,
                    #06B6D4
                );

            color: white;

            font-weight: 700;

            padding: 0.65rem 1rem;

            transition:
                transform 0.2s ease,
                box-shadow 0.2s ease,
                border-color 0.2s ease;
        }


        .stButton > button:hover {

            transform: translateY(-2px);

            border-color: var(--primary);

            box-shadow:
                0 8px 25px rgba(14,165,233,0.25);
        }


        .stButton > button:active {

            transform: translateY(0);
        }


        /* =========================================================
           SECONDARY BUTTON
        ========================================================= */

        .secondary-button {

            background: var(--card);

            border: 1px solid var(--border);

            color: var(--text);

            border-radius: 10px;

            padding: 10px 18px;
        }


        /* =========================================================
           INPUTS
        ========================================================= */

        div[data-baseweb="select"] > div,
        .stTextInput input,
        .stNumberInput input,
        .stTextArea textarea {

            background: var(--card) !important;

            color: var(--text) !important;

            border: 1px solid var(--border-light) !important;

            border-radius: 10px !important;

            transition:
                border-color 0.2s ease,
                box-shadow 0.2s ease;
        }


        .stTextInput input:focus,
        .stNumberInput input:focus,
        .stTextArea textarea:focus {

            border-color: var(--primary) !important;

            box-shadow:
                0 0 0 2px rgba(25,195,255,0.12) !important;
        }


        /* =========================================================
           SELECTBOX
        ========================================================= */

        div[data-baseweb="select"] > div {

            min-height: 42px;
        }


        /* =========================================================
           CHECKBOX
        ========================================================= */

        div[data-testid="stCheckbox"] label {

            color: var(--text-secondary) !important;
        }


        /* =========================================================
           RADIO BUTTON
        ========================================================= */

        div[data-testid="stRadio"] label {

            color: var(--text-secondary) !important;
        }


        /* =========================================================
           METRICS
        ========================================================= */

        div[data-testid="stMetric"] {

            position: relative;

            background:
                linear-gradient(
                    145deg,
                    rgba(13,27,42,0.96),
                    rgba(17,36,56,0.90)
                );

            border: 1px solid var(--border);

            padding: 18px;

            border-radius: 14px;

            box-shadow:
                0 8px 25px rgba(0,0,0,0.15);

            transition:
                transform 0.2s ease,
                border-color 0.2s ease,
                box-shadow 0.2s ease;
        }


        div[data-testid="stMetric"]:hover {

            transform: translateY(-3px);

            border-color: #2A6587;

            box-shadow:
                0 12px 30px rgba(0,0,0,0.25);
        }


        div[data-testid="stMetricLabel"] {

            color: var(--muted) !important;
        }


        div[data-testid="stMetricValue"] {

            color: var(--text) !important;

            font-weight: 800;
        }


        /* =========================================================
           CUSTOM CARDS
        ========================================================= */

        .ner-card {

            background:
                linear-gradient(
                    145deg,
                    rgba(13,27,42,0.96),
                    rgba(17,36,56,0.92)
                );

            border: 1px solid var(--border);

            border-radius: 16px;

            padding: 20px;

            margin-bottom: 16px;

            box-shadow:
                0 10px 30px rgba(0,0,0,0.16);

            transition:
                transform 0.2s ease,
                border-color 0.2s ease;
        }


        .ner-card:hover {

            transform: translateY(-2px);

            border-color: #285773;
        }


        /* =========================================================
           HERO CARD
        ========================================================= */

        .hero-card {

            background:
                radial-gradient(
                    circle at 85% 20%,
                    rgba(25,195,255,0.16),
                    transparent 30%
                ),
                linear-gradient(
                    135deg,
                    #0B1D2E,
                    #0D263A
                );

            border: 1px solid #214761;

            border-radius: 20px;

            padding: 28px;

            margin-bottom: 24px;

            box-shadow:
                0 15px 45px rgba(0,0,0,0.22);
        }


        /* =========================================================
           STATUS BADGES
        ========================================================= */

        .status-online {

            display: inline-flex;

            align-items: center;

            gap: 7px;

            padding: 6px 11px;

            border-radius: 999px;

            background: rgba(34,197,94,0.10);

            border: 1px solid rgba(34,197,94,0.25);

            color: #4ADE80;

            font-size: 12px;

            font-weight: 700;
        }


        .status-warning {

            display: inline-flex;

            align-items: center;

            gap: 7px;

            padding: 6px 11px;

            border-radius: 999px;

            background: rgba(245,158,11,0.10);

            border: 1px solid rgba(245,158,11,0.25);

            color: #FBBF24;

            font-size: 12px;

            font-weight: 700;
        }


        .status-danger {

            display: inline-flex;

            align-items: center;

            gap: 7px;

            padding: 6px 11px;

            border-radius: 999px;

            background: rgba(239,68,68,0.10);

            border: 1px solid rgba(239,68,68,0.25);

            color: #F87171;

            font-size: 12px;

            font-weight: 700;
        }


        /* =========================================================
           ALERT CARDS
        ========================================================= */

        .alert-card {

            padding: 16px 18px;

            border-radius: 12px;

            margin: 10px 0;

            background: var(--card);

            border-left: 4px solid var(--warning);
        }


        .alert-critical {

            border-left-color: var(--danger);

            background:
                rgba(239,68,68,0.06);
        }


        .alert-success {

            border-left-color: var(--success);

            background:
                rgba(34,197,94,0.06);
        }


        /* =========================================================
           DATAFRAME
        ========================================================= */

        div[data-testid="stDataFrame"] {

            border-radius: 14px;

            overflow: hidden;

            border: 1px solid var(--border);
        }


        /* =========================================================
           TABLE
        ========================================================= */

        table {

            border-radius: 12px;

            overflow: hidden;
        }


        /* =========================================================
           TABS
        ========================================================= */

        button[data-baseweb="tab"] {

            color: var(--muted) !important;

            font-weight: 600;
        }


        button[data-baseweb="tab"][aria-selected="true"] {

            color: var(--primary) !important;

            border-bottom-color: var(--primary) !important;
        }


        /* =========================================================
           EXPANDER
        ========================================================= */

        div[data-testid="stExpander"] {

            background: var(--card);

            border: 1px solid var(--border);

            border-radius: 12px;
        }


        /* =========================================================
           PROGRESS BAR
        ========================================================= */

        div[data-testid="stProgressBar"] {

            background: #12263A;

            border-radius: 999px;
        }


        /* =========================================================
           DIVIDERS
        ========================================================= */

        hr {

            border-color: var(--border) !important;

            opacity: 0.7;
        }


        /* =========================================================
           SPINNER
        ========================================================= */

        div[data-testid="stSpinner"] {

            color: var(--primary);
        }


        /* =========================================================
           SUCCESS / WARNING / ERROR
        ========================================================= */

        div[data-testid="stAlert"] {

            border-radius: 12px;

            border: 1px solid var(--border);
        }


        /* =========================================================
           SCROLLBAR
        ========================================================= */

        ::-webkit-scrollbar {

            width: 8px;

            height: 8px;
        }


        ::-webkit-scrollbar-track {

            background: var(--bg);
        }


        ::-webkit-scrollbar-thumb {

            background: #1E4863;

            border-radius: 10px;
        }


        ::-webkit-scrollbar-thumb:hover {

            background: #2A6587;
        }


        /* =========================================================
           TEXT SELECTION
        ========================================================= */

        ::selection {

            background: rgba(25,195,255,0.25);

            color: white;
        }


        /* =========================================================
           MOBILE / SMALL SCREEN
        ========================================================= */

        @media (max-width: 768px) {

            .main .block-container {

                padding-left: 1rem;

                padding-right: 1rem;
            }


            .hero-card {

                padding: 20px;

                border-radius: 15px;
            }


            .ner-card {

                padding: 16px;
            }

        }

        </style>
        """,
        unsafe_allow_html=True
    )