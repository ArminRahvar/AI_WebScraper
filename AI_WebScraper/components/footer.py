import reflex as rx

def footer():
    return rx.box(
        "© 2025 My Scraper App",
        position="fixed",
        bottom="0",
        left="50%",
        transform="translateX(-50%)",
        padding="1em",
        bg="gray.800",
        color="white",
        text_align="center",
        width="fit-content",
    )