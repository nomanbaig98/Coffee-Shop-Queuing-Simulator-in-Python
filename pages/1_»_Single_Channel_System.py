import streamlit as st
from utils import add_logo

st.set_page_config(
    page_title="CQC - SCS",
    page_icon="img/logo.png",
    layout="centered",
    initial_sidebar_state="auto",
    menu_items=None,
)
hide_streamlit_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Add logo to sidebar top
add_logo()

with st.sidebar:
    st.write("\n\n")
    st.caption("Single Server Queue, M/M/1")
    st.sidebar.info(
        "A single server serves customers one at a time from the front of the queue, according to a first-come, first-served discipline."
    )

st.caption("Queuing Simulator in Python")
st.markdown("### Model A: Single Server Queue, M/M/1")


lambda_val = st.number_input(
    "Enter mean number of arrivals per time period (λ) : ",
    value=1.0,
    step=1.0,
    format="%.2f",
)
mu_val = st.number_input(
    "Enter mean number of people or items served per time period (μ) : ",
    value=2.0,
    step=1.0,
    format="%.2f",
)

check = st.button("Calculate")
if check:
    # Calculations
    diff_mu_lambda = mu_val - lambda_val

    ls = lambda_val / diff_mu_lambda
    ws = 1 / diff_mu_lambda
    lq = (lambda_val**2) / (mu_val * diff_mu_lambda)
    wq = lambda_val / (mu_val * diff_mu_lambda)
    p0 = 1 - (lambda_val / mu_val)

    st.info("Output: Single Server Queue (M/M/1)")

    out_str = f"""

Average number of customers in the queue (Lq):            {round(lq, 4)}
Average wait in the queue (Wq):                           {round(wq, 4)}
Average number of customers in the system (Ls):           {round(ls, 4)}
Average wait in the system (Ws):                          {round(ws, 4)}
Idle time of the server:                                  {round(p0, 4)}"""
    st.code(out_str)

    with st.expander("See explanation"):
        st.write(
            "The following Queuing theory *formulas* for *Single Server Queue (M/M/1)* were used for calculations:"
        )
        st.latex(
            r"""
            \textup{Mean number of arrivals per time period:} \;  \lambda
            """
        )
        st.latex(
            r"""
            \textup{Average wait in the system:} \;  \mu
            """
        )
        st.latex(
            r"""
            \textup{Average number of customers in the system:} \; Ls = \frac{\lambda}{\mu - \lambda}
            """
        )
        st.latex(
            r"""
            \textup{Average wait in the system:} \; Ws = \frac{1}{\mu - \lambda}
            """
        )
        st.latex(
            r"""
            \textup{Average number of customers in the queue:} \; Lq = \frac{\lambda ^2}{\mu \left ( \mu - \lambda \right )}
            """
        )
        st.latex(
            r"""
            \textup{Average wait in the queue:} \; Wq = \frac{\lambda}{\mu \left ( \mu - \lambda \right )}
            """
        )
        st.latex(
            r"""
            \textup{Idle time of the server:} \; P_{0} = 1 - \frac{\lambda}{\mu}
            """
        )
