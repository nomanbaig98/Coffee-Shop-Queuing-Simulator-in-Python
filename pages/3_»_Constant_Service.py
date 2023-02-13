import streamlit as st
from utils import add_logo

st.set_page_config(
    page_title="CQC - CS",
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

add_logo()

with st.sidebar:
    st.write("\n\n")
    st.caption("Constant Service, M/G/1")
    st.sidebar.info(
        "In queueing theory, an M/G/1 queue represents the queue length in a system having a single server, where arrivals are determined by a Poisson process, a deterministic service time distribution, and job service times are fixed."
    )

st.caption("Queuing Simulator in Python")
st.markdown("### Model C: Constant Service, M/G/1")

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

    lq = (lambda_val**2) / (2 * mu_val * diff_mu_lambda)
    wq = lambda_val / (2 * mu_val * diff_mu_lambda)
    ls = lq + (lambda_val / mu_val)
    ws = wq + (1 / mu_val)

    st.info("Output: Constant Service (M/G/1)")

    out_str = f"""
Average number of customers in the queue (Lq):                                      {round(lq, 4)}
Average wait in the queue (Wq):                                                     {round(wq, 4)}
Average number of customers in the system (Ls):                                     {round(ls, 4)}
Average wait in the system (Ws):                                                    {round(ws, 4)}"""
    st.code(out_str)

    with st.expander("See explanation"):
        st.write(
            "The following Queuing theory *formulas* for *Constant Service System (M/G/1)* were used for calculations:"
        )
        st.latex(
            r"""
            \textup{Average number of customers in the queue:} \; L_{q} = \frac{\lambda ^2}{2\mu \left ( \mu - \lambda \right )}
            """
        )
        st.latex(
            r"""
            \textup{Average wait in the queue:} \; W_{q} = \frac{\lambda}{2\mu \left ( \mu - \lambda \right )}
            """
        )
        st.latex(
            r"""
            \textup{Average number of customers in the system:} \; L_{s} = L_{q} + \frac{\lambda}{\mu}
            """
        )
        st.latex(
            r"""
            \textup{Average wait in the system:} \; W_{s} = W_{q} + \frac{1}{\mu}
            """
        )
