import streamlit as st
import pandas as pd

# --- Sample Data ---
data = {
    'ID': [101, 102, 103, 104, 105],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Department': ['Sales', 'HR', 'Engineering', 'Sales', 'HR'],
    'Salary': [60000, 55000, 80000, 65000, 50000]
}
df = pd.DataFrame(data)

# Initialize session state for checkbox selection and submitted results
if 'data_with_checkbox' not in st.session_state:
    st.session_state.data_with_checkbox = df.copy()
    st.session_state.data_with_checkbox.insert(0, 'Select', False)

if 'submitted_results' not in st.session_state:
    st.session_state.submitted_results = pd.DataFrame()

st.title("Employee Selection Table")

# --- Display Data Editor ---
edited_df = st.data_editor(
    st.session_state.data_with_checkbox,
    column_config={
        "Select": st.column_config.CheckboxColumn(
            "Select",
            help="Select rows to process",
            default=False
        )
    },
    disabled=df.columns.tolist(),  # Only checkbox editable
    hide_index=True,
    use_container_width=True
)

# Update session state with the latest checkbox selections
st.session_state.data_with_checkbox = edited_df

# --- Submit Button ---
col1, col2 = st.columns([8, 2])  # Adjust to move button to the right
with col2:
    if st.button("Submit"):
        selected_rows = st.session_state.data_with_checkbox[
            st.session_state.data_with_checkbox['Select']
        ]
        final_selection = selected_rows.drop(columns=['Select'])
        
        st.session_state.submitted_results = final_selection

# --- Display Submitted Results ---
if not st.session_state.submitted_results.empty:
    st.markdown("---")
    st.subheader("Submitted Selection")
    st.dataframe(st.session_state.submitted_results)
    
    if len(st.session_state.submitted_results) == 1:
        row = st.session_state.submitted_results.iloc[0]
        st.markdown(f"**Selected Employee:** {row['Name']} from {row['Department']}, Salary: {row['Salary']}")
    else:
        st.info(f"You selected **{len(st.session_state.submitted_results)}** employees.")
