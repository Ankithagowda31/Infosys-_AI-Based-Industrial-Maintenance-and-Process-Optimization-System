import streamlit as st
import requests


# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="AI-Based Industrial Maintenance", page_icon="🤖", layout="wide"
)


# =====================================================
# SESSION STATE
# =====================================================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "page" not in st.session_state:
    st.session_state.page = "login"


# =====================================================
# BACKEND URL
# =====================================================

BACKEND_URL = "http://127.0.0.1:5000"


# =====================================================
# CSS
# =====================================================

st.markdown(
    """
<style>

.stApp {
    background: linear-gradient(
        135deg,
        #07111f 0%,
        #0f2027 50%,
        #203a43 100%
    );
}

header {
    visibility: hidden;
}

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}


/* =====================================================
   TITLES
   ===================================================== */

.main-title {
    text-align: center;
    color: white;
    font-size: 34px;
    font-weight: 800;
    margin-top: 15px;
}

.sub-title {
    text-align: center;
    color: #9fb3c8;
    font-size: 16px;
    margin-bottom: 35px;
}

.welcome {
    text-align: center;
    color: white;
    font-size: 32px;
    font-weight: 800;
}

.dashboard-title,
.module-title {
    color: white;
    font-size: 32px;
    font-weight: 800;
}

.dashboard-description,
.module-description {
    color: #9fb3c8;
    font-size: 16px;
    margin-bottom: 25px;
}


/* =====================================================
   INPUT
   ===================================================== */

.stTextInput label,
.stTextInput label p,
.stNumberInput label,
.stSelectbox label,
.stTextArea label {
    color: white !important;
    font-weight: 700 !important;
}

.stTextInput input,
.stNumberInput input,
.stTextArea textarea {
    background-color: white !important;
    color: #111827 !important;
    border: 2px solid #14b8a6 !important;
    border-radius: 10px !important;
}


/* =====================================================
   BUTTON
   ===================================================== */

.stButton > button {
    width: 100%;
    min-height: 45px;
    background: #0ea5a4 !important;
    color: white !important;
    border: none !important;
    border-radius: 10px !important;
    font-weight: 700 !important;
}

.stButton > button:hover {
    background: #0f766e !important;
}


/* =====================================================
   MODULE CARD
   ===================================================== */

.module-card {
    background: rgba(255,255,255,0.07);
    border: 1px solid rgba(255,255,255,0.14);
    border-radius: 15px;
    padding: 18px;
    text-align: center;
    min-height: 130px;
    margin-bottom: 10px;
}

.card-icon {
    font-size: 35px;
}

.card-title {
    color: white;
    font-size: 19px;
    font-weight: 800;
}

.card-description {
    color: #9fb3c8;
    font-size: 13px;
}


/* =====================================================
   DATA CARD
   ===================================================== */

.data-card {
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(255,255,255,0.16);
    border-radius: 15px;
    padding: 25px;
    margin-top: 15px;
    margin-bottom: 20px;
}

.data-card-title {
    color: white;
    font-size: 23px;
    font-weight: 800;
    margin-bottom: 20px;
}

.info-label {
    color: #9fb3c8;
    font-size: 14px;
    margin-top: 8px;
}

.info-value {
    color: white;
    font-size: 18px;
    font-weight: 700;
    margin-bottom: 10px;
}


/* =====================================================
   METRIC CARD
   ===================================================== */

.metric-card {
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(255,255,255,0.15);
    border-radius: 15px;
    padding: 20px;
    text-align: center;
}

.metric-icon {
    font-size: 30px;
}

.metric-value {
    color: white;
    font-size: 28px;
    font-weight: 800;
}

.metric-label {
    color: #9fb3c8;
    font-size: 13px;
}


/* =====================================================
   LOGIN SIDE
   ===================================================== */

.side-heading {
    color: white;
    text-align: center;
    font-size: 21px;
    font-weight: 800;
}

.side-text {
    color: #9fb3c8;
    text-align: center;
    line-height: 2;
}

</style>
""",
    unsafe_allow_html=True,
)


# =====================================================
# LOGIN PAGE
# =====================================================


def login_page():

    st.markdown(
        '<div class="main-title">' "AI-Based Industrial Maintenance" "</div>",
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="sub-title">'
        "Process Optimization System for Industrial Robotics"
        "</div>",
        unsafe_allow_html=True,
    )

    left, center, right = st.columns([1, 1.3, 1])

    # =================================================
    # LEFT
    # =================================================

    with left:

        st.write("")
        st.write("")
        st.write("")

        st.markdown("<h1 style='text-align:center;'>🤖</h1>", unsafe_allow_html=True)

        st.markdown(
            '<div class="side-heading">' "Smart Industrial Monitoring" "</div>",
            unsafe_allow_html=True,
        )

        st.markdown(
            """
            <div class="side-text">
            ⚙️ Machine Monitoring<br>
            🔧 Predictive Maintenance<br>
            📊 Process Optimization<br>
            🚨 Early Failure Detection
            </div>
            """,
            unsafe_allow_html=True,
        )

    # =================================================
    # CENTER
    # =================================================

    with center:

        st.write("")
        st.write("")

        st.markdown(
            '<div class="welcome">Welcome Back 👋</div>', unsafe_allow_html=True
        )

        st.markdown(
            '<div class="sub-title">' "Login to access your dashboard" "</div>",
            unsafe_allow_html=True,
        )

        username = st.text_input("Username", placeholder="Enter your username")

        password = st.text_input(
            "Password", placeholder="Enter your password", type="password"
        )

        st.write("")

        if st.button("🔐 Login"):

            if username == "" or password == "":

                st.warning("Please enter username and password.")

            elif username == "admin" and password == "admin123":

                st.session_state.logged_in = True
                st.session_state.page = "dashboard"

                st.rerun()

            else:

                st.error("Invalid username or password.")

    # =================================================
    # RIGHT
    # =================================================

    with right:

        st.write("")
        st.write("")
        st.write("")

        st.markdown("<h1 style='text-align:center;'>⚙️</h1>", unsafe_allow_html=True)

        st.markdown(
            """
            <div class="side-text">
            Intelligent Machine<br>
            Monitoring &<br>
            Maintenance
            </div>
            """,
            unsafe_allow_html=True,
        )


# =====================================================
# DASHBOARD
# =====================================================


def dashboard():

    st.markdown(
        '<div class="dashboard-title">' "📊 System Dashboard" "</div>",
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="dashboard-description">'
        "Monitor and manage your industrial robotic system"
        "</div>",
        unsafe_allow_html=True,
    )

    # =================================================
    # ROW 1
    # =================================================

    col1, col2, col3, col4 = st.columns(4)

    # ROBOT

    with col1:

        st.markdown(
            """
            <div class="module-card">
            <div class="card-icon">🤖</div>
            <div class="card-title">Robot</div>
            <div class="card-description">
            Manage robotic machines
            </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        if st.button("Open Robot", key="robot_btn"):

            st.session_state.page = "robot"
            st.rerun()

    # SENSOR

    with col2:

        st.markdown(
            """
            <div class="module-card">
            <div class="card-icon">📡</div>
            <div class="card-title">Sensor</div>
            <div class="card-description">
            Monitor sensor data
            </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        if st.button("Open Sensor", key="sensor_btn"):

            st.session_state.page = "sensor"
            st.rerun()

    # TELEMETRY

    with col3:

        st.markdown(
            """
            <div class="module-card">
            <div class="card-icon">📊</div>
            <div class="card-title">Telemetry</div>
            <div class="card-description">
            View machine telemetry
            </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        if st.button("Open Telemetry", key="telemetry_btn"):

            st.session_state.page = "telemetry"
            st.rerun()

    # MAINTENANCE

    with col4:

        st.markdown(
            """
            <div class="module-card">
            <div class="card-icon">🔧</div>
            <div class="card-title">Maintenance</div>
            <div class="card-description">
            Manage maintenance
            </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        if st.button("Open Maintenance", key="maintenance_btn"):

            st.session_state.page = "maintenance"
            st.rerun()

    st.write("")

    # =================================================
    # ROW 2
    # =================================================

    col5, col6, col7, col8 = st.columns(4)

    # INCIDENT

    with col5:

        st.markdown(
            """
            <div class="module-card">
            <div class="card-icon">🚨</div>
            <div class="card-title">Incident</div>
            <div class="card-description">
            Track machine incidents
            </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        if st.button("Open Incident", key="incident_btn"):

            st.session_state.page = "incident"
            st.rerun()

    # INVENTORY

    with col6:

        st.markdown(
            """
            <div class="module-card">
            <div class="card-icon">📦</div>
            <div class="card-title">Inventory</div>
            <div class="card-description">
            Manage spare parts
            </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        if st.button("Open Inventory", key="inventory_btn"):

            st.session_state.page = "inventory"
            st.rerun()

    # NOTIFICATION

    with col7:

        st.markdown(
            """
            <div class="module-card">
            <div class="card-icon">🔔</div>
            <div class="card-title">Notification</div>
            <div class="card-description">
            View system alerts
            </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        if st.button("Open Notification", key="notification_btn"):

            st.session_state.page = "notification"
            st.rerun()

    # PREDICTION

    with col8:

        st.markdown(
            """
            <div class="module-card">
            <div class="card-icon">🔮</div>
            <div class="card-title">Prediction</div>
            <div class="card-description">
            AI-based predictions
            </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        if st.button("Open Prediction", key="prediction_btn"):

            st.session_state.page = "prediction"
            st.rerun()

    st.write("")
    st.write("")

    if st.button("🚪 Logout", key="logout_btn"):

        st.session_state.logged_in = False
        st.session_state.page = "login"

        st.rerun()


# =====================================================
# MODULE HEADER
# =====================================================


def module_header(title, description):

    st.markdown(
        f'<div class="module-title">' f"{title}" f"</div>", unsafe_allow_html=True
    )

    st.markdown(
        f'<div class="module-description">' f"{description}" f"</div>",
        unsafe_allow_html=True,
    )

    st.divider()


# =====================================================
# METRIC CARD
# =====================================================


def metric_card(icon, value, label):

    st.markdown(
        f"""
        <div class="metric-card">

        <div class="metric-icon">
        {icon}
        </div>

        <div class="metric-value">
        {value}
        </div>

        <div class="metric-label">
        {label}
        </div>

        </div>
        """,
        unsafe_allow_html=True,
    )


# =====================================================
# BACK BUTTON
# =====================================================


def back_to_dashboard():

    st.write("")

    if st.button("⬅ Back to Dashboard", key=f"back_{st.session_state.page}"):

        st.session_state.page = "dashboard"

        st.rerun()


# =====================================================
# ROBOT PAGE
# =====================================================


def robot_page():

    module_header("🤖 Robot", "View and manage industrial robotic machines.")

    try:

        response = requests.get(BACKEND_URL + "/robots", timeout=10)

        if response.status_code == 200:

            data = response.json()

            if isinstance(data, dict):
                data = [data]

            st.success("✅ Robot data loaded successfully.")

            if len(data) == 0:

                st.info("No robot data available.")

            for robot in data:

                st.markdown(
                    f"""
                    <div class="data-card">

                    <div class="data-card-title">
                    🤖 {robot.get(
                        "robot_name",
                        "Industrial Robot"
                    )}
                    </div>

                    <div class="info-label">
                    Robot ID
                    </div>

                    <div class="info-value">
                    {robot.get(
                        "robot_id",
                        "N/A"
                    )}
                    </div>

                    <div class="info-label">
                    Machine Type
                    </div>

                    <div class="info-value">
                    {robot.get(
                        "machine_type",
                        "N/A"
                    )}
                    </div>

                    <div class="info-label">
                    Location
                    </div>

                    <div class="info-value">
                    {robot.get(
                        "location",
                        "N/A"
                    )}
                    </div>

                    <div class="info-label">
                    Status
                    </div>

                    <div class="info-value">
                    🟢 {robot.get(
                        "status",
                        "N/A"
                    )}
                    </div>

                    </div>
                    """,
                    unsafe_allow_html=True,
                )

        else:

            st.error(f"Robot API Error: " f"{response.status_code}")

    except Exception as e:

        st.error(f"Robot Error: {e}")

    back_to_dashboard()


# =====================================================
# SENSOR PAGE
# =====================================================


def sensor_page():

    module_header("📡 Sensor", "Monitor sensor values and machine conditions.")

    try:

        response = requests.get(BACKEND_URL + "/sensors", timeout=10)

        if response.status_code == 200:

            data = response.json()

            if isinstance(data, dict):
                data = [data]

            st.success("✅ Sensor data loaded successfully.")

            if len(data) == 0:

                st.info("No sensor data available.")

            for sensor in data:

                st.markdown(
                    f"""
                    <div class="data-card">

                    <div class="data-card-title">
                    📡 Sensor Information
                    </div>

                    <div class="info-label">
                    Temperature
                    </div>

                    <div class="info-value">
                    🌡️ {sensor.get(
                        "temperature",
                        "N/A"
                    )}
                    </div>

                    <div class="info-label">
                    Pressure
                    </div>

                    <div class="info-value">
                    💨 {sensor.get(
                        "pressure",
                        "N/A"
                    )}
                    </div>

                    <div class="info-label">
                    Vibration
                    </div>

                    <div class="info-value">
                    📈 {sensor.get(
                        "vibration",
                        "N/A"
                    )}
                    </div>

                    <div class="info-label">
                    Status
                    </div>

                    <div class="info-value">
                    🟢 {sensor.get(
                        "status",
                        "N/A"
                    )}
                    </div>

                    </div>
                    """,
                    unsafe_allow_html=True,
                )

        else:

            st.error(f"Sensor API Error: " f"{response.status_code}")

    except Exception as e:

        st.error(f"Sensor Error: {e}")

    back_to_dashboard()


# =====================================================
# TELEMETRY PAGE
# =====================================================


def telemetry_page():

    module_header("📊 Telemetry", "View machine telemetry and operational data.")

    try:

        response = requests.get(BACKEND_URL + "/telemetry", timeout=10)

        if response.status_code == 200:

            data = response.json()

            if isinstance(data, dict):
                telemetry_list = [data]

            elif isinstance(data, list):
                telemetry_list = data

            else:
                telemetry_list = []

            st.success("✅ Telemetry data loaded successfully.")

            if len(telemetry_list) == 0:

                st.info("No telemetry data available.")

            else:

                for item in telemetry_list:

                    st.markdown(
                        f"""
                        <div class="data-card">

                        <div class="data-card-title">
                        📊 Machine Telemetry
                        </div>

                        <div class="info-label">
                        Temperature
                        </div>

                        <div class="info-value">
                        🌡️ {item.get(
                            "temperature",
                            "N/A"
                        )}
                        </div>

                        <div class="info-label">
                        Pressure
                        </div>

                        <div class="info-value">
                        💨 {item.get(
                            "pressure",
                            "N/A"
                        )}
                        </div>

                        <div class="info-label">
                        Vibration
                        </div>

                        <div class="info-value">
                        📈 {item.get(
                            "vibration",
                            "N/A"
                        )}
                        </div>

                        <div class="info-label">
                        Speed
                        </div>

                        <div class="info-value">
                        ⚡ {item.get(
                            "speed",
                            "N/A"
                        )}
                        </div>

                        <div class="info-label">
                        Status
                        </div>

                        <div class="info-value">
                        🟢 {item.get(
                            "status",
                            "N/A"
                        )}
                        </div>

                        </div>
                        """,
                        unsafe_allow_html=True,
                    )

        else:

            st.error(f"Telemetry API Error: " f"{response.status_code}")

    except requests.exceptions.ConnectionError:

        st.error("❌ Backend is not running.")

    except Exception as e:

        st.error(f"Telemetry Error: {e}")

    back_to_dashboard()


# =====================================================
# MAINTENANCE PAGE
# =====================================================


def maintenance_page():

    module_header(
        "🔧 Maintenance Management", "Schedule and manage industrial robot maintenance."
    )

    try:

        response = requests.get(BACKEND_URL + "/maintenance", timeout=10)

        if response.status_code == 200:

            data = response.json()

            if isinstance(data, list):
                records = data

            elif isinstance(data, dict):
                records = [data]

            else:
                records = []

        else:

            records = []

            st.error(f"Maintenance API Error: " f"{response.status_code}")

    except Exception as e:

        records = []

        st.error(f"Maintenance Error: {e}")

    total = len(records)

    scheduled = sum(
        1 for r in records if str(r.get("status", "")).lower() == "scheduled"
    )

    pending = sum(1 for r in records if str(r.get("status", "")).lower() == "pending")

    completed = sum(
        1 for r in records if str(r.get("status", "")).lower() == "completed"
    )

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        metric_card("🔧", total, "Total")

    with c2:
        metric_card("📅", scheduled, "Scheduled")

    with c3:
        metric_card("⏳", pending, "Pending")

    with c4:
        metric_card("✅", completed, "Completed")

    st.write("")

    tab1, tab2, tab3, tab4 = st.tabs(["📋 View", "➕ Add", "✏️ Update", "🗑️ Delete"])

    # =================================================
    # VIEW
    # =================================================

    with tab1:

        if len(records) == 0:

            st.info("📭 No maintenance records available.")

        else:

            for record in records:

                status = record.get("status", "N/A")

                if str(status).lower() == "scheduled":
                    status_display = "🟡 Scheduled"

                elif str(status).lower() == "completed":
                    status_display = "🟢 Completed"

                elif str(status).lower() == "pending":
                    status_display = "🟠 Pending"

                else:
                    status_display = f"🔵 {status}"

                st.markdown(
                    f"""
                    <div class="data-card">

                    <div class="data-card-title">
                    🔧 Maintenance #
                    {record.get(
                        "maintenance_id",
                        "N/A"
                    )}
                    </div>

                    <div class="info-label">
                    🤖 Robot ID
                    </div>

                    <div class="info-value">
                    {record.get(
                        "robot_id",
                        "N/A"
                    )}
                    </div>

                    <div class="info-label">
                    🛠️ Maintenance Type
                    </div>

                    <div class="info-value">
                    {record.get(
                        "maintenance_type",
                        "N/A"
                    )}
                    </div>

                    <div class="info-label">
                    📝 Description
                    </div>

                    <div class="info-value">
                    {record.get(
                        "description",
                        "N/A"
                    )}
                    </div>

                    <div class="info-label">
                    📅 Scheduled Date
                    </div>

                    <div class="info-value">
                    {record.get(
                        "scheduled_date",
                        "N/A"
                    )}
                    </div>

                    <div class="info-label">
                    📌 Status
                    </div>

                    <div class="info-value">
                    {status_display}
                    </div>

                    </div>
                    """,
                    unsafe_allow_html=True,
                )

    # =================================================
    # ADD
    # =================================================

    with tab2:

        st.subheader("➕ Add Maintenance")

        robot_id = st.text_input("Robot ID", placeholder="RA002", key="add_robot")

        maintenance_type = st.selectbox(
            "Maintenance Type",
            [
                "Preventive Maintenance",
                "Corrective Maintenance",
                "Predictive Maintenance",
            ],
            key="add_type",
        )

        description = st.text_area("Description", key="add_description")

        scheduled_date = st.text_input(
            "Scheduled Date", placeholder="YYYY-MM-DD", key="add_date"
        )

        status = st.selectbox(
            "Status", ["Scheduled", "Pending", "Completed"], key="add_status"
        )

        if st.button("➕ Add Maintenance", key="add_maintenance"):

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

                if response.status_code == 201:

                    st.success("✅ Maintenance added successfully!")

                    st.rerun()

                else:

                    st.error(f"API Error: " f"{response.status_code}")

            except Exception as e:

                st.error(f"Error: {e}")

    # =================================================
    # UPDATE
    # =================================================

    with tab3:

        st.subheader("✏️ Update Maintenance")

        update_id = st.number_input(
            "Maintenance ID", min_value=1, step=1, key="update_id"
        )

        update_robot = st.text_input("Robot ID", key="update_robot")

        update_type = st.selectbox(
            "Maintenance Type",
            [
                "Preventive Maintenance",
                "Corrective Maintenance",
                "Predictive Maintenance",
            ],
            key="update_type",
        )

        update_description = st.text_area("Description", key="update_description")

        update_date = st.text_input("Scheduled Date", key="update_date")

        update_status = st.selectbox(
            "Status", ["Scheduled", "Pending", "Completed"], key="update_status"
        )

        if st.button("✏️ Update Maintenance", key="update_maintenance"):

            payload = {
                "robot_id": update_robot,
                "maintenance_type": update_type,
                "description": update_description,
                "scheduled_date": update_date,
                "status": update_status,
            }

            try:

                response = requests.put(
                    BACKEND_URL + f"/maintenance/{update_id}", json=payload, timeout=10
                )

                if response.status_code == 200:

                    st.success("✅ Maintenance updated successfully!")

                    st.rerun()

                elif response.status_code == 404:

                    st.error("❌ Maintenance not found.")

                else:

                    st.error(f"API Error: " f"{response.status_code}")

            except Exception as e:

                st.error(f"Error: {e}")

    # =================================================
    # DELETE
    # =================================================

    with tab4:

        st.subheader("🗑️ Delete Maintenance")

        delete_id = st.number_input(
            "Maintenance ID", min_value=1, step=1, key="delete_id"
        )

        if st.button("🗑️ Delete Maintenance", key="delete_maintenance"):

            try:

                response = requests.delete(
                    BACKEND_URL + f"/maintenance/{delete_id}", timeout=10
                )

                if response.status_code == 200:

                    st.success("✅ Maintenance deleted successfully!")

                    st.rerun()

                elif response.status_code == 404:

                    st.error("❌ Maintenance not found.")

                else:

                    st.error(f"API Error: " f"{response.status_code}")

            except Exception as e:

                st.error(f"Error: {e}")

    back_to_dashboard()


# =====================================================
# INCIDENT PAGE
# =====================================================


def incident_page():

    module_header(
        "🚨 Incident Management", "Monitor and manage industrial robot incidents."
    )

    try:

        response = requests.get(BACKEND_URL + "/incidents", timeout=10)

        if response.status_code == 200:

            data = response.json()

            if isinstance(data, dict):
                incidents = [data]

            elif isinstance(data, list):
                incidents = data

            else:
                incidents = []

            if len(incidents) == 0:

                st.info("📭 No incidents available.")

            else:

                total = len(incidents)

                open_count = sum(
                    1
                    for item in incidents
                    if str(item.get("status", "")).lower() == "open"
                )

                high_count = sum(
                    1
                    for item in incidents
                    if str(item.get("severity", "")).lower() == "high"
                )

                resolved_count = sum(
                    1
                    for item in incidents
                    if str(item.get("status", "")).lower() in ["resolved", "closed"]
                )

                c1, c2, c3, c4 = st.columns(4)

                with c1:
                    metric_card("🚨", total, "Total Incidents")

                with c2:
                    metric_card("🔴", open_count, "Open")

                with c3:
                    metric_card("⚠️", high_count, "High Severity")

                with c4:
                    metric_card("✅", resolved_count, "Resolved")

                st.write("")

                for incident in incidents:

                    incident_id = incident.get("incident_id", "N/A")

                    robot_id = incident.get("robot_id", "N/A")

                    incident_type = incident.get("incident_type", "N/A")

                    description = incident.get("description", "N/A")

                    severity = incident.get("severity", "N/A")

                    status = incident.get("status", "N/A")

                    if str(severity).lower() == "high":

                        severity_display = "🔴 HIGH"

                    elif str(severity).lower() == "medium":

                        severity_display = "🟠 MEDIUM"

                    elif str(severity).lower() == "low":

                        severity_display = "🟢 LOW"

                    else:

                        severity_display = f"🔵 {severity}"

                    if str(status).lower() == "open":

                        status_display = "🔴 OPEN"

                    elif str(status).lower() in ["resolved", "closed"]:

                        status_display = "🟢 RESOLVED"

                    elif str(status).lower() == "investigating":

                        status_display = "🟡 INVESTIGATING"

                    else:

                        status_display = f"🔵 {status}"

                    st.markdown(
                        f"""
                        <div class="data-card">

                        <div class="data-card-title">
                        🚨 Incident #{incident_id}
                        </div>

                        <div class="info-label">
                        🤖 Robot ID
                        </div>

                        <div class="info-value">
                        {robot_id}
                        </div>

                        <div class="info-label">
                        ⚠️ Incident Type
                        </div>

                        <div class="info-value">
                        {incident_type}
                        </div>

                        <div class="info-label">
                        📝 Description
                        </div>

                        <div class="info-value">
                        {description}
                        </div>

                        <div class="info-label">
                        🔥 Severity
                        </div>

                        <div class="info-value">
                        {severity_display}
                        </div>

                        <div class="info-label">
                        📌 Status
                        </div>

                        <div class="info-value">
                        {status_display}
                        </div>

                        </div>
                        """,
                        unsafe_allow_html=True,
                    )

        else:

            st.error(f"Incident API Error: " f"{response.status_code}")

    except requests.exceptions.ConnectionError:

        st.error("❌ Backend is not running.")

    except Exception as e:

        st.error(f"Incident Error: {e}")

    back_to_dashboard()


# =====================================================
# NOTIFICATION PAGE
# =====================================================


def notification_page():

    module_header(
        "🔔 Notifications", "View important alerts and machine notifications."
    )

    try:

        response = requests.get(BACKEND_URL + "/notifications", timeout=10)

        if response.status_code == 200:

            notifications = response.json()

            if isinstance(notifications, dict):

                notifications = [notifications]

            if len(notifications) == 0:

                st.info("📭 No notifications available.")

            else:

                st.success(
                    f"🔔 {len(notifications)} " "notifications loaded successfully."
                )

                for notification in notifications:

                    notification_id = notification.get("notification_id", "N/A")

                    robot_id = notification.get("robot_id", "N/A")

                    notification_type = notification.get("type", "Information")

                    message = notification.get("message", "No message")

                    status = notification.get("status", "N/A")

                    date = notification.get("date", "N/A")

                    if str(notification_type).lower() == "alert":

                        icon = "🚨"

                    elif str(notification_type).lower() == "warning":

                        icon = "⚠️"

                    else:

                        icon = "ℹ️"

                    if str(status).lower() == "unread":

                        status_display = "🔴 Unread"

                    else:

                        status_display = "🟢 Read"

                    st.markdown(
                        f"""
                        <div class="data-card">

                        <div class="data-card-title">
                        {icon} Notification #{notification_id}
                        </div>

                        <div class="info-label">
                        🤖 Robot ID
                        </div>

                        <div class="info-value">
                        {robot_id}
                        </div>

                        <div class="info-label">
                        📢 Type
                        </div>

                        <div class="info-value">
                        {notification_type}
                        </div>

                        <div class="info-label">
                        💬 Message
                        </div>

                        <div class="info-value">
                        {message}
                        </div>

                        <div class="info-label">
                        📅 Date
                        </div>

                        <div class="info-value">
                        {date}
                        </div>

                        <div class="info-label">
                        📌 Status
                        </div>

                        <div class="info-value">
                        {status_display}
                        </div>

                        </div>
                        """,
                        unsafe_allow_html=True,
                    )

        else:

            st.error(f"Notification API Error: " f"{response.status_code}")

    except requests.exceptions.ConnectionError:

        st.error("❌ Backend is not running.")

    except Exception as e:

        st.error(f"Notification Error: {e}")

    back_to_dashboard()


# =====================================================
# PREDICTION PAGE
# =====================================================


def prediction_page():

    module_header("🔮 Prediction", "AI-based machine maintenance prediction.")

    # =================================================
    # INTRO CARD
    # =================================================

    st.markdown(
        """
        <div class="data-card">

        <div class="data-card-title">
        🤖 Machine Health Prediction
        </div>

        <div style="color:#9fb3c8;">
        Enter the machine sensor values to predict
        the maintenance condition.
        </div>

        </div>
        """,
        unsafe_allow_html=True,
    )

    # =================================================
    # INPUTS
    # =================================================

    col1, col2 = st.columns(2)

    with col1:

        temperature = st.number_input(
            "🌡️ Temperature",
            min_value=0.0,
            value=45.0,
            step=1.0,
            key="prediction_temperature",
        )

    with col2:

        vibration = st.number_input(
            "📈 Vibration",
            min_value=0.0,
            value=5.0,
            step=0.1,
            key="prediction_vibration",
        )

    st.write("")

    # =================================================
    # PREDICT BUTTON
    # =================================================

    if st.button("🔮 Predict Maintenance Status", key="predict_button"):

        payload = {"temperature": temperature, "vibration": vibration}

        try:

            # IMPORTANT:
            # Backend /predict accepts POST
            # NOT GET

            response = requests.post(BACKEND_URL + "/predict", json=payload, timeout=10)

            # =================================================
            # SUCCESS
            # =================================================

            if response.status_code == 200:

                result = response.json()

                prediction = result.get("prediction", "Unknown")

                st.success("✅ Prediction completed successfully!")

                # =================================================
                # RESULT CARD
                # =================================================

                st.markdown(
                    f"""
                    <div class="data-card">

                    <div class="data-card-title">
                    🔮 Prediction Result
                    </div>

                    <div class="info-label">
                    🌡️ Temperature
                    </div>

                    <div class="info-value">
                    {result.get(
                        "temperature",
                        "N/A"
                    )}
                    </div>

                    <div class="info-label">
                    📈 Vibration
                    </div>

                    <div class="info-value">
                    {result.get(
                        "vibration",
                        "N/A"
                    )}
                    </div>

                    <div class="info-label">
                    🤖 Maintenance Prediction
                    </div>

                    <div class="info-value">
                    🔮 {prediction}
                    </div>

                    </div>
                    """,
                    unsafe_allow_html=True,
                )

            # =================================================
            # BAD REQUEST
            # =================================================

            elif response.status_code == 400:

                try:

                    error_data = response.json()

                    st.error("❌ " + error_data.get("error", "Invalid input"))

                except:

                    st.error("❌ Invalid prediction input.")

            # =================================================
            # OTHER ERROR
            # =================================================

            else:

                try:

                    error_data = response.json()

                    st.error(
                        "Prediction API Error: "
                        + error_data.get("error", str(response.status_code))
                    )

                except:

                    st.error(f"Prediction API Error: " f"{response.status_code}")

        except requests.exceptions.ConnectionError:

            st.error("❌ Backend is not running. " "Please start Flask backend first.")

        except requests.exceptions.Timeout:

            st.error("⏱️ Prediction request timed out.")

        except Exception as e:

            st.error(f"Prediction Error: {e}")

    back_to_dashboard()


# =====================================================
# GENERIC MODULE PAGE
# =====================================================


def generic_module_page(title, icon, description, endpoint):

    module_header(f"{icon} {title}", description)

    try:

        response = requests.get(BACKEND_URL + endpoint, timeout=10)

        if response.status_code == 200:

            data = response.json()

            st.success(f"✅ {title} data loaded successfully.")

            # =================================================
            # LIST
            # =================================================

            if isinstance(data, list):

                if len(data) == 0:

                    st.info(f"No {title.lower()} data available.")

                else:

                    for index, item in enumerate(data):

                        st.markdown(
                            f"""
                            <div class="data-card">

                            <div class="data-card-title">
                            {icon} {title} #{index + 1}
                            </div>

                            """,
                            unsafe_allow_html=True,
                        )

                        if isinstance(item, dict):

                            for key, value in item.items():

                                label = key.replace("_", " ").title()

                                st.markdown(
                                    f"""
                                    <div class="info-label">
                                    {label}
                                    </div>

                                    <div class="info-value">
                                    {value}
                                    </div>
                                    """,
                                    unsafe_allow_html=True,
                                )

                        st.markdown("</div>", unsafe_allow_html=True)

            # =================================================
            # DICT
            # =================================================

            elif isinstance(data, dict):

                st.markdown(
                    f"""
                    <div class="data-card">

                    <div class="data-card-title">
                    {icon} {title} Information
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

                for key, value in data.items():

                    label = key.replace("_", " ").title()

                    st.markdown(
                        f"""
                        <div class="info-label">
                        {label}
                        </div>

                        <div class="info-value">
                        {value}
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )

                st.markdown("</div>", unsafe_allow_html=True)

            else:

                st.info("No data available.")

        elif response.status_code == 404:

            st.warning(f"⚠️ {title} endpoint is not " f"available in the backend.")

        else:

            st.error(f"{title} API Error: " f"{response.status_code}")

    except requests.exceptions.ConnectionError:

        st.error("❌ Backend is not running. " "Please start Flask backend first.")

    except Exception as e:

        st.error(f"{title} Error: {e}")

    back_to_dashboard()


# =====================================================
# MAIN ROUTING
# =====================================================

if not st.session_state.logged_in:

    login_page()

else:

    # =================================================
    # DASHBOARD
    # =================================================

    if st.session_state.page == "dashboard":

        dashboard()

    # =================================================
    # 1. ROBOT
    # =================================================

    elif st.session_state.page == "robot":

        robot_page()

    # =================================================
    # 2. SENSOR
    # =================================================

    elif st.session_state.page == "sensor":

        sensor_page()

    # =================================================
    # 3. TELEMETRY
    # =================================================

    elif st.session_state.page == "telemetry":

        telemetry_page()

    # =================================================
    # 4. MAINTENANCE
    # =================================================

    elif st.session_state.page == "maintenance":

        maintenance_page()

    # =================================================
    # 5. INCIDENT
    # =================================================

    elif st.session_state.page == "incident":

        incident_page()

    # =================================================
    # 6. INVENTORY
    # =================================================

    elif st.session_state.page == "inventory":

        generic_module_page(
            "Inventory",
            "📦",
            "Manage spare parts and inventory information.",
            "/inventory",
        )

    # =================================================
    # 7. NOTIFICATION
    # =================================================

    elif st.session_state.page == "notification":

        notification_page()

    # =================================================
    # 8. PREDICTION
    # =================================================

    elif st.session_state.page == "prediction":

        prediction_page()
