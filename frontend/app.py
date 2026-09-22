import streamlit as st
import requests


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="AI-Based Industrial Maintenance",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# =========================================================
# SESSION STATE
# =========================================================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "page" not in st.session_state:
    st.session_state.page = "login"


# =========================================================
# BACKEND URL
# =========================================================

BACKEND_URL = "http://127.0.0.1:5000"


# =========================================================
# CSS
# =========================================================

st.markdown(
    """
    <style>

    /* =====================================================
       MAIN BACKGROUND
       ===================================================== */

    .stApp {
        background:
        radial-gradient(
            circle at top left,
            #123c4a 0%,
            transparent 35%
        ),
        radial-gradient(
            circle at bottom right,
            #073b4c 0%,
            transparent 35%
        ),
        linear-gradient(
            135deg,
            #06141b,
            #0a2029,
            #06141b
        );

        color: white;
    }


    /* =====================================================
       HIDE STREAMLIT DEFAULT
       ===================================================== */

    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    header {
        visibility: hidden;
    }


    /* =====================================================
       GENERAL TEXT
       ===================================================== */

    h1,
    h2,
    h3,
    h4,
    h5,
    h6,
    p,
    label {
        color: white !important;
    }


    /* =====================================================
       LOGIN
       ===================================================== */

    .login-title {
        text-align: center;
        color: white;
        font-size: 42px;
        font-weight: 800;
        margin-top: 55px;
        margin-bottom: 10px;
    }

    .login-subtitle {
        text-align: center;
        color: #b7d1d8 !important;
        font-size: 18px;
        margin-bottom: 40px;
    }


    /* =====================================================
       INPUT
       ===================================================== */

    .stTextInput label {
        color: white !important;
        font-weight: 700 !important;
    }

    .stTextInput input {
        background-color: white !important;
        color: #111111 !important;
        border: 2px solid #20c7bd !important;
        border-radius: 10px !important;
    }


    /* =====================================================
       NORMAL BUTTONS
       ===================================================== */

    div.stButton > button {
        background: #102b35 !important;
        color: white !important;
        border: 1px solid #315967 !important;
        border-radius: 12px !important;
        font-weight: 700 !important;
    }

    div.stButton > button:hover {
        background: #174552 !important;
        color: white !important;
        border: 1px solid #20c7bd !important;
    }


    /* =====================================================
       LOGIN PRIMARY BUTTON
       ===================================================== */

    button[kind="primary"] {
        background: #10aaa5 !important;
        color: white !important;
        border: none !important;
    }

    button[kind="primary"]:hover {
        background: #0b8985 !important;
    }


    /* =====================================================
       DASHBOARD MODULES
       COMPACT SIZE
       ===================================================== */

    .dashboard-module {
        margin-bottom: 5px;
    }

    .dashboard-module div.stButton > button {
        height: 95px !important;

        background: #102b35 !important;
        color: white !important;

        border: 1px solid #315967 !important;
        border-radius: 16px !important;

        font-size: 18px !important;
        font-weight: 800 !important;

        padding: 8px !important;

        white-space: pre-line !important;
    }

    .dashboard-module div.stButton > button:hover {
        background: #174552 !important;
        border: 2px solid #20c7bd !important;
        color: white !important;
    }


    /* =====================================================
       PAGE TITLE
       ===================================================== */

    .page-title {
        color: white;
        font-size: 34px;
        font-weight: 800;
        margin-top: 15px;
        margin-bottom: 25px;
    }


    /* =====================================================
       INFORMATION CARD
       ===================================================== */

    [data-testid="stVerticalBlockBorderWrapper"] {
        background: #102b35 !important;
        border: 1px solid #315967 !important;
        border-radius: 16px !important;
    }


    /* =====================================================
       ROBOT INFORMATION
       ===================================================== */

    .robot-title {
        font-size: 27px;
        font-weight: 800;
        color: white !important;
        margin-bottom: 22px;
    }

    .robot-item {
        font-size: 18px;
        font-weight: 700;

        /* SAME COLOUR FOR ALL INFORMATION */
        color: #d9f3f5 !important;

        margin-bottom: 15px;
    }


    /* =====================================================
       NEXT BUTTON
       ===================================================== */

    .next-button div.stButton > button {
        width: auto !important;
        min-width: 150px !important;
        height: 38px !important;

        font-size: 13px !important;
        font-weight: 700 !important;

        padding: 4px 15px !important;
    }


    /* =====================================================
       SLIDER
       ===================================================== */

    .stSlider label {
        color: white !important;
        font-size: 17px !important;
        font-weight: 700 !important;
    }


    </style>
    """,
    unsafe_allow_html=True,
)


# =========================================================
# GET API DATA
# =========================================================


def get_api_data(endpoint):

    try:

        response = requests.get(BACKEND_URL + endpoint, timeout=10)

        if response.status_code == 200:
            return response.json()

        st.error(f"API Error: {response.status_code}")

    except requests.exceptions.ConnectionError:

        st.error("❌ Backend is not running.")

    except requests.exceptions.Timeout:

        st.error("❌ Backend request timed out.")

    except Exception as e:

        st.error(f"❌ Error: {e}")

    return None


# =========================================================
# DISPLAY API DATA
# =========================================================


def display_data(data):

    if data is None:
        return

    if isinstance(data, dict):
        data = [data]

    if not isinstance(data, list):

        st.json(data)
        return

    if len(data) == 0:

        st.info("📭 No data available.")

        return

    for index, item in enumerate(data):

        with st.container(border=True):

            if isinstance(item, dict):

                st.markdown(f"### Record {index + 1}")

                for key, value in item.items():

                    st.write(f"**{key.replace('_', ' ').title()}:** {value}")

            else:

                st.write(item)


# =========================================================
# PAGE HEADER
# =========================================================


def show_page_header(title):

    st.markdown(f'<div class="page-title">{title}</div>', unsafe_allow_html=True)


# =========================================================
# NEXT PAGE
# =========================================================


def next_page(page_name, button_text):

    st.write("")

    st.markdown('<div class="next-button">', unsafe_allow_html=True)

    clicked = st.button(button_text, key=f"next_{page_name}")

    st.markdown("</div>", unsafe_allow_html=True)

    if clicked:

        st.session_state.page = page_name
        st.rerun()


# =========================================================
# LOGIN PAGE
# =========================================================


def login_page():

    st.markdown(
        '<div class="login-title">' "AI-Based Industrial Maintenance" "</div>",
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="login-subtitle">'
        "Process Optimization System for Industrial Robotics"
        "</div>",
        unsafe_allow_html=True,
    )

    left, center, right = st.columns([1, 2, 1])

    with center:

        st.markdown("## 🔐 System Login")

        st.write("Login to access your dashboard")

        username = st.text_input(
            "Username", placeholder="Enter username", key="username"
        )

        password = st.text_input(
            "Password", placeholder="Enter password", type="password", key="password"
        )

        st.write("")

        if st.button("Login", key="login", type="primary", use_container_width=True):

            if username == "" or password == "":

                st.warning("Please enter username and password.")

            elif username == "admin" and password == "admin123":

                st.session_state.logged_in = True
                st.session_state.page = "dashboard"

                st.rerun()

            else:

                st.error("Invalid username or password.")


# =========================================================
# DASHBOARD
# =========================================================


def dashboard():

    st.markdown(
        '<div class="page-title">' "📊 System Dashboard" "</div>",
        unsafe_allow_html=True,
    )

    # =====================================================
    # FIRST ROW
    # =====================================================

    col1, col2, col3, col4 = st.columns(4)

    # ROBOT
    with col1:

        st.markdown('<div class="dashboard-module">', unsafe_allow_html=True)

        if st.button(
            "🤖\nRobot Management", key="robot_module", use_container_width=True
        ):

            st.session_state.page = "robot"
            st.rerun()

        st.markdown("</div>", unsafe_allow_html=True)

    # SENSOR
    with col2:

        st.markdown('<div class="dashboard-module">', unsafe_allow_html=True)

        if st.button(
            "📡\nSensor Monitoring", key="sensor_module", use_container_width=True
        ):

            st.session_state.page = "sensor"
            st.rerun()

        st.markdown("</div>", unsafe_allow_html=True)

    # TELEMETRY
    with col3:

        st.markdown('<div class="dashboard-module">', unsafe_allow_html=True)

        if st.button("📊\nTelemetry", key="telemetry_module", use_container_width=True):

            st.session_state.page = "telemetry"
            st.rerun()

        st.markdown("</div>", unsafe_allow_html=True)

    # MAINTENANCE
    with col4:

        st.markdown('<div class="dashboard-module">', unsafe_allow_html=True)

        if st.button(
            "🔧\nMaintenance", key="maintenance_module", use_container_width=True
        ):

            st.session_state.page = "maintenance"
            st.rerun()

        st.markdown("</div>", unsafe_allow_html=True)

    st.write("")

    # =====================================================
    # SECOND ROW
    # =====================================================

    col5, col6, col7, col8 = st.columns(4)

    # INCIDENT
    with col5:

        st.markdown('<div class="dashboard-module">', unsafe_allow_html=True)

        if st.button(
            "🚨\nIncident Management", key="incident_module", use_container_width=True
        ):

            st.session_state.page = "incident"
            st.rerun()

        st.markdown("</div>", unsafe_allow_html=True)

    # INVENTORY
    with col6:

        st.markdown('<div class="dashboard-module">', unsafe_allow_html=True)

        if st.button("📦\nInventory", key="inventory_module", use_container_width=True):

            st.session_state.page = "inventory"
            st.rerun()

        st.markdown("</div>", unsafe_allow_html=True)

    # NOTIFICATIONS
    with col7:

        st.markdown('<div class="dashboard-module">', unsafe_allow_html=True)

        if st.button(
            "🔔\nNotifications", key="notification_module", use_container_width=True
        ):

            st.session_state.page = "notification"
            st.rerun()

        st.markdown("</div>", unsafe_allow_html=True)

    # AI PREDICTION
    with col8:

        st.markdown('<div class="dashboard-module">', unsafe_allow_html=True)

        if st.button(
            "🧠\nAI Prediction", key="prediction_module", use_container_width=True
        ):

            st.session_state.page = "prediction"
            st.rerun()

        st.markdown("</div>", unsafe_allow_html=True)

    st.write("")
    st.write("")

    # LOGOUT

    if st.button("🚪 Logout", key="logout"):

        st.session_state.logged_in = False
        st.session_state.page = "login"

        st.rerun()


# =========================================================
# ROBOT PAGE
# =========================================================


def robot_page():

    show_page_header("🤖 Robot Management")

    st.subheader("Robot Information")

    # =====================================================
    # ONE INFORMATION CARD
    # =====================================================

    with st.container(border=True):

        st.markdown(
            '<div class="robot-title">' "Industrial Robotic Arm" "</div>",
            unsafe_allow_html=True,
        )

        st.markdown(
            '<div class="robot-item">' "Location: Production Line 1" "</div>",
            unsafe_allow_html=True,
        )

        st.markdown(
            '<div class="robot-item">' "Machine Type: 6-Axis Robot" "</div>",
            unsafe_allow_html=True,
        )

        st.markdown(
            '<div class="robot-item">' "Robot ID: RA001" "</div>",
            unsafe_allow_html=True,
        )

        st.markdown(
            '<div class="robot-item">' "Robot Name: Industrial Robotic Arm" "</div>",
            unsafe_allow_html=True,
        )

        st.markdown(
            '<div class="robot-item">' "Status: Active" "</div>", unsafe_allow_html=True
        )

    next_page("sensor", "Next → Sensor")


# =========================================================
# SENSOR PAGE
# =========================================================


def sensor_page():

    show_page_header("📡 Sensor Monitoring")

    st.subheader("Sensor Data")

    data = get_api_data("/sensors")

    display_data(data)

    next_page("telemetry", "Next → Telemetry")


# =========================================================
# TELEMETRY PAGE
# =========================================================


def telemetry_page():

    show_page_header("📊 Telemetry")

    st.subheader("Telemetry Data")

    data = get_api_data("/telemetry")

    display_data(data)

    next_page("maintenance", "Next → Maintenance")


# =========================================================
# MAINTENANCE PAGE
# =========================================================


def maintenance_page():

    show_page_header("🔧 Maintenance")

    st.subheader("Maintenance Records")

    data = get_api_data("/maintenance")

    display_data(data)

    st.divider()

    st.subheader("➕ Add Maintenance")

    robot_id = st.text_input("Robot ID", key="maintenance_robot_id")

    maintenance_type = st.text_input("Maintenance Type", key="maintenance_type")

    description = st.text_area("Description", key="maintenance_description")

    scheduled_date = st.text_input(
        "Scheduled Date", placeholder="YYYY-MM-DD", key="maintenance_date"
    )

    status = st.selectbox(
        "Status", ["Scheduled", "Pending", "Completed"], key="maintenance_status"
    )

    if st.button("Add Maintenance", key="add_maintenance"):

        payload = {
            "robot_id": robot_id,
            "maintenance_type": maintenance_type,
            "description": description,
            "scheduled_date": scheduled_date,
            "status": status,
        }

        try:

            response = requests.post(
                BACKEND_URL + "/maintenance", json=payload, timeout=10
            )

            if response.status_code in [200, 201]:

                st.success("✅ Maintenance added successfully.")

            else:

                st.error(f"API Error: {response.status_code}")

        except requests.exceptions.ConnectionError:

            st.error("❌ Backend is not running.")

        except Exception as e:

            st.error(f"❌ Error: {e}")

    next_page("incident", "Next → Incident")


# =========================================================
# INCIDENT PAGE
# =========================================================


def incident_page():

    show_page_header("🚨 Incident Management")

    st.subheader("Incident Records")

    data = get_api_data("/incidents")

    display_data(data)

    next_page("inventory", "Next → Inventory")


# =========================================================
# INVENTORY PAGE
# =========================================================


def inventory_page():

    show_page_header("📦 Inventory")

    st.subheader("Inventory Records")

    data = get_api_data("/inventory")

    display_data(data)

    next_page("notification", "Next → Notifications")


# =========================================================
# NOTIFICATION PAGE
# =========================================================


def notification_page():

    show_page_header("🔔 Notifications")

    st.subheader("Notification Records")

    data = get_api_data("/notifications")

    display_data(data)

    next_page("prediction", "Next → Prediction")


# =========================================================
# PREDICTION PAGE
# =========================================================


def prediction_page():

    show_page_header("🧠 AI Prediction")

    st.subheader("Machine Condition")

    # =====================================================
    # TEMPERATURE
    # =====================================================

    temperature = st.slider(
        "🌡️ Temperature",
        min_value=0.0,
        max_value=100.0,
        value=45.0,
        step=0.5,
        key="temperature_slider",
    )

    # =====================================================
    # VIBRATION
    # =====================================================

    vibration = st.slider(
        "📳 Vibration",
        min_value=0.0,
        max_value=10.0,
        value=2.0,
        step=0.1,
        key="vibration_slider",
    )

    st.write("")

    # =====================================================
    # PREDICT
    # =====================================================

    if st.button("🔮 Predict", key="predict_button", use_container_width=True):

        payload = {
            "temperature": temperature,
            "pressure": 0,
            "vibration": vibration,
            "speed": 0,
        }

        try:

            response = requests.post(BACKEND_URL + "/predict", json=payload, timeout=10)

            if response.status_code == 200:

                result = response.json()

                st.subheader("📊 Prediction Result")

                if isinstance(result, dict):

                    prediction = (
                        result.get("prediction")
                        or result.get("result")
                        or result.get("status")
                    )

                    if prediction is not None:

                        st.success(f"Prediction: {prediction}")

                    else:

                        st.json(result)

                else:

                    st.success(f"Prediction: {result}")

            else:

                st.error(f"Prediction API Error: " f"{response.status_code}")

        except requests.exceptions.ConnectionError:

            st.error("❌ Backend is not running.")

        except requests.exceptions.Timeout:

            st.error("❌ Prediction request timed out.")

        except Exception as e:

            st.error(f"❌ Prediction Error: {e}")

    next_page("dashboard", "Next → Dashboard")


# =========================================================
# PAGE ROUTING
# =========================================================

if not st.session_state.logged_in:

    login_page()

else:

    if st.session_state.page == "dashboard":

        dashboard()

    elif st.session_state.page == "robot":

        robot_page()

    elif st.session_state.page == "sensor":

        sensor_page()

    elif st.session_state.page == "telemetry":

        telemetry_page()

    elif st.session_state.page == "maintenance":

        maintenance_page()

    elif st.session_state.page == "incident":

        incident_page()

    elif st.session_state.page == "inventory":

        inventory_page()

    elif st.session_state.page == "notification":

        notification_page()

    elif st.session_state.page == "prediction":

        prediction_page()

    else:

        st.session_state.page = "dashboard"
        st.rerun()
