"""Streamlit app."""

from importlib.metadata import version

import streamlit as st

st.title(f"LLM_apps v{version('llm-apps')}")  # type: ignore[no-untyped-call]
