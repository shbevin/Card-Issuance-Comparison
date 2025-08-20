import streamlit as st

# --- Americas Country Requirements Dataset ---
requirements = {
    "United States": {
        "requirement": "BIN Sponsor + Processor",
        "note": "Multiple federal & state regulators; scheme membership typically via sponsor for fintechs.",
        "regulator": "Federal Reserve, OCC, FDIC, CFPB, FinCEN (plus state regulators)",
        "time_to_market": "6–18 months",
        "rails": ["ACH", "Fedwire"],
        "example_providers": ["Galileo", "Stripe Issuing"]
    },
    "Canada": {
        "requirement": "BIN Sponsor + Processor",
        "note": "OSFI oversight for banks/issuers; Payments Canada operates rails.",
        "regulator": "OSFI; provincial regulators as applicable",
        "time_to_market": "6–12 months",
        "rails": ["Interac", "Lynx"],
        "example_providers": ["Marqeta", "Adyen"]
    },
    "Mexico": {
        "requirement": "BIN Sponsor + Processor",
        "note": "CNBV & Banxico environment; CoDi/SPEI integrations common.",
        "regulator": "CNBV; Banco de México; CONDUSEF (consumer)",
        "time_to_market": "6–12 months",
        "rails": ["CoDi", "SPEI"],
        "example_providers": ["Evertec", "Pomelo"]
    },
    # ------- Central America -------
    "Belize": {
        "requirement": "BIN Sponsor + Processor",
        "note": "Local licensing and bank partnerships required.",
        "regulator": "Central Bank of Belize",
        "time_to_market": "6–12 months",
        "rails": ["ACH Belize"],
        "example_providers": ["Local banks"]
    },
    "Costa Rica": {
        "requirement": "BIN Sponsor + Processor",
        "note": "SUGEF supervision; SINPE is the national payments system.",
        "regulator": "SUGEF; Banco Central de Costa Rica",
        "time_to_market": "6–12 months",
        "rails": ["SINPE"],
        "example_providers": ["Local banks"]
    },
    "El Salvador": {
        "requirement": "BIN Sponsor + Processor",
        "note": "USD economy; SSF oversight; Bitcoin legal tender does not replace card regulation.",
        "regulator": "Superintendencia del Sistema Financiero (SSF); Banco Central de Reserva",
        "time_to_market": "6–12 months",
        "rails": ["ACH El Salvador"],
        "example_providers": ["Local banks"]
    },
    "Guatemala": {
        "requirement": "BIN Sponsor + Processor",
        "note": "SIB regulates credit cards and payments.",
        "regulator": "Superintendencia de Bancos (SIB); Banco de Guatemala",
        "time_to_market": "6–12 months",
        "rails": ["ACH Guatemala"],
        "example_providers": ["Local banks"]
    },
    "Honduras": {
        "requirement": "BIN Sponsor + Processor",
        "note": "CNBS supervision; local bank sponsorship typical.",
        "regulator": "Comisión Nacional de Bancos y Seguros (CNBS); Banco Central de Honduras",
        "time_to_market": "6–12 months",
        "rails": ["ACH Honduras"],
        "example_providers": ["Local banks"]
    },
    "Nicaragua": {
        "requirement": "BIN Sponsor + Processor",
        "note": "SIBOIF oversight; local settlement rails.",
        "regulator": "SIBOIF; Banco Central de Nicaragua",
        "time_to_market": "6–12 months",
        "rails": ["ACH Nicaragua"],
        "example_providers": ["Local banks"]
    },
    "Panama": {
        "requirement": "BIN Sponsor + Processor",
        "note": "Dollarized; banked via SBP; SMV for markets.",
        "regulator": "Superintendencia de Bancos de Panamá (SBP); Superintendencia del Mercado de Valores (SMV)",
        "time_to_market": "6–12 months",
        "rails": ["ACH Panama"],
        "example_providers": ["Evertec"]
    },
    # ------- South America -------
    "Argentina": {
        "requirement": "BIN Sponsor + Processor",
        "note": "BCRA licensing; Transferencias 3.0 ecosystem.",
        "regulator": "BCRA; CNV (markets)",
        "time_to_market": "9–18 months",
        "rails": ["CBU/DEBIN", "Transferencias 3.0"],
        "example_providers": ["Pomelo"]
    },
    "Bolivia": {
        "requirement": "BIN Sponsor + Processor",
        "note": "ASFI supervision; local bank sponsorship common.",
        "regulator": "ASFI; Banco Central de Bolivia",
        "time_to_market": "6–12 months",
        "rails": ["ACH Bolivia"],
        "example_providers": ["Local banks"]
    },
    "Brazil": {
        "requirement": "BIN Sponsor + Processor",
        "note": "PIX/instant payments; stringent BCB oversight.",
        "regulator": "Banco Central do Brasil; CVM (markets)",
        "time_to_market": "6–12 months",
        "rails": ["PIX", "TED"],
        "example_providers": ["Pomelo"]
    },
    "Chile": {
        "requirement": "BIN Sponsor + Processor",
        "note": "CMF-regulated; local issuer sponsorship via banks.",
        "regulator": "Comisión para el Mercado Financiero (CMF); Banco Central de Chile",
        "time_to_market": "6–9 months",
        "rails": ["ACH Chile"],
        "example_providers": ["Pomelo"]
    },
    "Colombia": {
        "requirement": "BIN Sponsor + Processor",
        "note": "SFC oversight; BIN sponsorship speeds scheme access.",
        "regulator": "Superintendencia Financiera de Colombia (SFC)",
        "time_to_market": "6–9 months",
        "rails": ["PSE", "ACH"],
        "example_providers": ["Paymentology", "Pomelo"]
    },
    "Ecuador": {
        "requirement": "BIN Sponsor + Processor",
        "note": "SB oversight; BCE operates national payment systems (SPI).",
        "regulator": "Superintendencia de Bancos; Banco Central del Ecuador (BCE)",
        "time_to_market": "6–12 months",
        "rails": ["SPI (BCE)", "ACH Ecuador"],
        "example_providers": ["Local banks", "Paymentology"]
    },
    "Guyana": {
        "requirement": "BIN Sponsor + Processor",
        "note": "Bank of Guyana oversight; local sponsorship typical.",
        "regulator": "Bank of Guyana",
        "time_to_market": "6–12 months",
        "rails": ["ACH Guyana"],
        "example_providers": ["Local banks"]
    },
    "Paraguay": {
        "requirement": "BIN Sponsor + Processor",
        "note": "BCP + SIPAP real-time/ACH system.",
        "regulator": "Banco Central del Paraguay",
        "time_to_market": "6–12 months",
        "rails": ["SIPAP"],
        "example_providers": ["Local banks"]
    },
    "Peru": {
        "requirement": "BIN Sponsor + Processor",
        "note": "SBS oversight; BCRP operates RTGS.",
        "regulator": "SBS; Banco Central de Reserva del Perú (BCRP)",
        "time_to_market": "6–12 months",
        "rails": ["ACH Perú", "CCI"],
        "example_providers": ["Pomelo"]
    },
    "Suriname": {
        "requirement": "BIN Sponsor + Processor",
        "note": "Central Bank oversight; local rails.",
        "regulator": "Central Bank of Suriname",
        "time_to_market": "6–12 months",
        "rails": ["ACH Suriname"],
        "example_providers": ["Local banks"]
    },
    "Uruguay": {
        "requirement": "BIN Sponsor + Processor",
        "note": "BCU/SSF oversight.",
        "regulator": "Banco Central del Uruguay; Superintendencia de Servicios Financieros",
        "time_to_market": "6–12 months",
        "rails": ["ACH Uruguay"],
        "example_providers": ["Paymentology"]
    },
    "Venezuela": {
        "requirement": "BIN Sponsor + Processor (subject to sanctions)",
        "note": "SUDEBAN oversight; significant restrictions and complexity.",
        "regulator": "SUDEBAN",
        "time_to_market": "12–24 months",
        "rails": ["Pago Móvil", "RTGS BCV"],
        "example_providers": ["Limited options"]
    },
    # ------- Caribbean -------
    "Antigua and Barbuda": {
        "requirement": "BIN Sponsor + Processor",
        "note": "ECCB monetary union; national FSRC supervises institutions.",
        "regulator": "ECCB; Financial Services Regulatory Commission (FSRC)",
        "time_to_market": "6–12 months",
        "rails": ["ECCU ACH"],
        "example_providers": ["Evertec", "Local banks"]
    },
    "Bahamas": {
        "requirement": "BIN Sponsor + Processor",
        "note": "CBoB oversight; digital currency (Sand Dollar) exists alongside card rails.",
        "regulator": "Central Bank of The Bahamas",
        "time_to_market": "6–12 months",
        "rails": ["ACH Bahamas", "Sand Dollar"],
        "example_providers": ["Local banks"]
    },
    "Barbados": {
        "requirement": "BIN Sponsor + Processor",
        "note": "CBB & FSC oversight.",
        "regulator": "Central Bank of Barbados; Financial Services Commission",
        "time_to_market": "6–12 months",
        "rails": ["ACH Barbados"],
        "example_providers": ["Local banks"]
    },
    "Cuba": {
        "requirement": "BIN Sponsor + Processor (heavily restricted)",
        "note": "Sanctions environment; BCC oversight.",
        "regulator": "Banco Central de Cuba (BCC)",
        "time_to_market": "Not typical",
        "rails": ["Local card networks"],
        "example_providers": ["N/A"]
    },
    "Dominica": {
        "requirement": "BIN Sponsor + Processor",
        "note": "ECCB monetary union; local FSRC.",
        "regulator": "ECCB; Financial Services Unit (FSU)/FSRC",
        "time_to_market": "6–12 months",
        "rails": ["ECCU ACH"],
        "example_providers": ["Local banks"]
    },
    "Dominican Republic": {
        "requirement": "BIN Sponsor + Processor",
        "note": "Banking overseen by SIB; Central Bank sets payments policy.",
        "regulator": "Superintendencia de Bancos; Banco Central de la República Dominicana",
        "time_to_market": "6–12 months",
        "rails": ["ACH DOP"],
        "example_providers": ["Evertec"]
    },
    "Grenada": {
        "requirement": "BIN Sponsor + Processor",
        "note": "ECCB monetary union; GARFIN supervises.",
        "regulator": "ECCB; GARFIN",
        "time_to_market": "6–12 months",
        "rails": ["ECCU ACH"],
        "example_providers": ["Local banks"]
    },
    "Haiti": {
        "requirement": "BIN Sponsor + Processor",
        "note": "BRH oversight; infrastructure evolving.",
        "regulator": "Banque de la République d’Haïti (BRH)",
        "time_to_market": "6–12+ months",
        "rails": ["BRH Payments"],
        "example_providers": ["Local banks"]
    },
    "Jamaica": {
        "requirement": "BIN Sponsor + Processor",
        "note": "Bank of Jamaica operates JamClear RTGS/ACH.",
        "regulator": "Bank of Jamaica",
        "time_to_market": "6–12 months",
        "rails": ["JamClear-RTGS", "JamClear-ACH"],
        "example_providers": ["Local banks"]
    },
    "Saint Kitts and Nevis": {
        "requirement": "BIN Sponsor + Processor",
        "note": "ECCB monetary union; FSRC supervises.",
        "regulator": "ECCB; Financial Services Regulatory Commission",
        "time_to_market": "6–12 months",
        "rails": ["ECCU ACH"],
        "example_providers": ["Local banks"]
    },
    "Saint Lucia": {
        "requirement": "BIN Sponsor + Processor",
        "note": "ECCB monetary union; FSRA supervises.",
        "regulator": "ECCB; Financial Services Regulatory Authority (FSRA)",
        "time_to_market": "6–12 months",
        "rails": ["ECCU ACH"],
        "example_providers": ["Local banks"]
    },
    "Saint Vincent and the Grenadines": {
        "requirement": "BIN Sponsor + Processor",
        "note": "ECCB monetary union; FSA supervises.",
        "regulator": "ECCB; Financial Services Authority (FSA)",
        "time_to_market": "6–12 months",
        "rails": ["ECCU ACH"],
        "example_providers": ["Local banks"]
    },
    "Trinidad and Tobago": {
        "requirement": "BIN Sponsor + Processor",
        "note": "CBTT oversight; fast payments via TTIPS.",
        "regulator": "Central Bank of Trinidad and Tobago",
        "time_to_market": "6–12 months",
        "rails": ["TTIPS", "ACH"],
        "example_providers": ["Local banks"]
    },
    "Aruba": {
        "requirement": "BIN Sponsor + Processor",
        "note": "CBA oversight.",
        "regulator": "Centrale Bank van Aruba (CBA)",
        "time_to_market": "6–12 months",
        "rails": ["ACH Aruba"],
        "example_providers": ["Local banks"]
    },
    "Curaçao and Sint Maarten": {
        "requirement": "BIN Sponsor + Processor",
        "note": "CBCS oversight across both territories.",
        "regulator": "Central Bank of Curaçao and Sint Maarten (CBCS)",
        "time_to_market": "6–12 months",
        "rails": ["ACH"],
        "example_providers": ["Local banks"]
    },
    "Bermuda": {
        "requirement": "BIN Sponsor + Processor",
        "note": "BMA oversight; strong international banking links.",
        "regulator": "Bermuda Monetary Authority (BMA)",
        "time_to_market": "6–12 months",
        "rails": ["ACH Bermuda"],
        "example_providers": ["Local banks"]
    },
    "Cayman Islands": {
        "requirement": "BIN Sponsor + Processor",
        "note": "CIMA oversight.",
        "regulator": "Cayman Islands Monetary Authority (CIMA)",
        "time_to_market": "6–12 months",
        "rails": ["ACH Cayman"],
        "example_providers": ["Local banks"]
    },
    "British Virgin Islands": {
        "requirement": "BIN Sponsor + Processor",
        "note": "FSC oversight.",
        "regulator": "BVI Financial Services Commission (FSC)",
        "time_to_market": "6–12 months",
        "rails": ["ACH"],
        "example_providers": ["Local banks"]
    },
    "Turks and Caicos Islands": {
        "requirement": "BIN Sponsor + Processor",
        "note": "TCIFSC oversight.",
        "regulator": "Turks and Caicos Islands Financial Services Commission",
        "time_to_market": "6–12 months",
        "rails": ["ACH"],
        "example_providers": ["Local banks"]
    },
    # ------- US Territories -------
    "Puerto Rico": {
        "requirement": "BIN Sponsor + Processor",
        "note": "USD rails; OCIF oversees local institutions; US federal rules may apply via partner banks.",
        "regulator": "OCIF (PR); relevant US federal regulators",
        "time_to_market": "6–12 months",
        "rails": ["ACH (US)", "Fedwire"],
        "example_providers": ["Evertec", "Payblr"]
    },
    "US Virgin Islands": {
        "requirement": "BIN Sponsor + Processor",
        "note": "US territory; local division of banking & insurance; US rails.",
        "regulator": "VIDE Banking/Insurance; relevant US federal regulators",
        "time_to_market": "6–12 months",
        "rails": ["ACH (US)", "Fedwire"],
        "example_providers": ["Local banks"]
    }
}

# --- Streamlit App ---
import json, io, csv, datetime as dt

st.title("💡 Ever curious how to launch a card program?")
st.write("Select your country to find out whether you need a BIN Sponsor, an Issuer Processor, or both. Then generate a brief, compare countries, and get a tailored next step.")

# Sidebar: Glossary & Notes
with st.sidebar:
    st.header("📖 Glossary")
    st.markdown("**BIN Sponsor** — A regulated institution with scheme membership (Visa/Mastercard) that lets you issue cards if you don't hold a BIN or license.")
    st.markdown("**Issuer Processor** — The tech platform that authorizes transactions, manages cards, and connects to networks.")
    st.markdown("**Time to market** — Indicative only; varies by partners, licensing, and scope.")
    st.caption("This tool is informational only. Not legal or regulatory advice. Sharing in a personal capacity. The views expressed here are mine alone and do not represent Mastercard. This is not an official communication or endorsement.")

# Controls
col1, col2 = st.columns([1.2, 1])
with col1:
    country = st.selectbox("Select a country:", ["-- Choose a country --"] + sorted(list(requirements.keys())))
    persona = st.selectbox("Your entity type:", ["Fintech (unlicensed)", "Licensed issuer / Bank", "Credit union / Cooperative"])
    program_type = st.selectbox("Program type:", ["Prepaid", "Debit", "Credit"])    

with col2:
    compare = st.multiselect("Compare countries (up to 4):", sorted(list(requirements.keys())), max_selections=4)

# Helper to compute recommendation based on persona
def compute_need(base_req: str, persona: str) -> str:
    if persona == "Licensed issuer / Bank":
        return "Issuer Processor (BIN sponsor not needed if you have scheme membership)"
    return base_req

# Display main selection result
if country and country != "-- Choose a country --":
    data = requirements[country]
    final_need = compute_need(data["requirement"], persona)

    top = st.container()
    with top:
        st.success(f"In **{country}**, you likely need: **{final_need}**")
        st.subheader(f"ℹ️ {data['note']}")
        if program_type == "Credit":
            st.info("Credit programs often require additional underwriting, capital, and consumer credit compliance.")
        st.subheader(f"**Regulator(s):** {data['regulator']}")
        m1, m2 = st.columns(2)
        m1.metric("Indicative time to market", data["time_to_market"])
        m2.metric("Local rails", ", ".join(data["rails"]))
        st.write(f"**Example providers:** {', '.join(data['example_providers'])}")
        st.markdown("---")

    # Country brief generator
    def make_brief(cntry: str, persona: str, program: str) -> str:
        d = requirements[cntry]
        need = compute_need(d["requirement"], persona)
        lines = [
            f"Country: {cntry}",
            f"Entity type: {persona}",
            f"Program type: {program}",
            f"Recommendation: {need}",
            f"Why: {d['note']}",
            f"Regulator(s): {d['regulator']}",
            f"Local rails: {', '.join(d['rails'])}",
            f"Indicative time to market: {d['time_to_market']}",
            f"Example providers: {', '.join(d['example_providers'])}",
            "Next step: Explore Mastercard Product Express to match with the right BIN sponsor and processor."
        ]
        return "".join(lines)

# Comparison table
if compare:
    import pandas as pd

    st.markdown("### 🔍 Side‑by‑side comparison")
    view = st.radio("View", ["Cards", "Table"], index=0, key="compare_view")

    # Helper: pick a chip color by requirement
    def req_class(req: str) -> str:
        req = req.lower()
        if "both" in req or ("bin" in req and "processor" in req):
            return "req-both"
        if "processor" in req and "bin" not in req:
            return "req-proc"
        if "bin" in req and "processor" not in req:
            return "req-sponsor"
        return "req-both"

    # Minimal flag mapping (fallback 🌎)
    FLAG = {
        "United States": "🇺🇸", "Canada": "🇨🇦", "Mexico": "🇲🇽", "Brazil": "🇧🇷", "Argentina": "🇦🇷",
        "Chile": "🇨🇱", "Colombia": "🇨🇴", "Peru": "🇵🇪", "Ecuador": "🇪🇨", "Uruguay": "🇺🇾",
        "Paraguay": "🇵🇾", "Bolivia": "🇧🇴", "Venezuela": "🇻🇪", "Guatemala": "🇬🇹", "Honduras": "🇭🇳",
        "El Salvador": "🇸🇻", "Nicaragua": "🇳🇮", "Costa Rica": "🇨🇷", "Panama": "🇵🇦", "Belize": "🇧🇿",
        "Dominican Republic": "🇩🇴", "Haiti": "🇭🇹", "Jamaica": "🇯🇲", "Trinidad and Tobago": "🇹🇹",
        "Bahamas": "🇧🇸", "Barbados": "🇧🇧", "Guyana": "🇬🇾", "Suriname": "🇸🇷",
        "Puerto Rico": "🇵🇷", "US Virgin Islands": "🇻🇮"
    }

    # Shared CSS for cards & chips
    st.markdown(
        """
        <style>
        .card {border:1px solid #e5e7eb; border-radius:16px; padding:16px; background:#fafafa}
        .heading {font-weight:700; margin-bottom:6px}
        .sub {color:#475569; font-size:13px; margin-bottom:12px}
        .kv {font-size:13px; color:#1f2937; margin:8px 0}
        .chips {margin-top:6px}
        .chip {display:inline-block; padding:2px 10px; margin:2px 6px 2px 0; border-radius:999px; border:1px solid #e5e7eb; font-size:12px}
        .req-both {background:#fff7ed; border-color:#fdba74}
        .req-proc {background:#eff6ff; border-color:#93c5fd}
        .req-sponsor {background:#fef2f2; border-color:#fecaca}
        </style>
        """,
        unsafe_allow_html=True,
    )

    if view == "Cards":
        cols = st.columns(len(compare))
        for i, c in enumerate(compare):
            d = requirements[c]
            rclass = req_class(d["requirement"])
            rails_chips = "".join([f"<span class='chip'>{r}</span>" for r in d["rails"]])
            providers = ", ".join(d["example_providers"])
            with cols[i]:
                st.markdown(
                    f"""
                    <div class='card'>
                      <div class='heading' style='font-size:1.7em; line-height:1;'>{FLAG.get(c, '🌎')} <span style='font-size:1em'>{c}</span></div>
                      <div class='sub'>Regulator(s): {d['regulator']}</div>
                      <div class='kv'><strong>Time to market:</strong> {d['time_to_market']}</div>
                      <div class='kv'><strong>Rails:</strong> <span class='chips'>{rails_chips}</span></div>
                      <div class='kv'><strong>Providers:</strong> {providers}</div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
    else:
        # Table view with a bit of styling
        rows = []
        for c in compare:
            d = requirements[c]
            rows.append({
                "Country": f"{FLAG.get(c, '🌎')} {c}",
                "Requirement": d["requirement"],
                "Regulator(s)": d["regulator"],
                "Time to market": d["time_to_market"],
                "Rails": ", ".join(d["rails"]),
            })
        df = pd.DataFrame(rows)
        styler = (
            df.style
            .hide(axis="index")
            .set_properties(**{"border-color": "#e5e7eb"})
        )
        st.table(styler)

# CTA
st.markdown("---")
st.title("🚀 Ready to launch faster?")
st.markdown("[Learn more about Mastercard Product Express](https://www.mastercard.com/fintech-express/ui/public/)")

st.caption("This tool is for informational purposes only. Requirements may vary based on regulatory approvals and partnerships. Sharing in a personal capacity. The views expressed here are mine alone and do not represent Mastercard. This is not an official communication or endorsement.")
