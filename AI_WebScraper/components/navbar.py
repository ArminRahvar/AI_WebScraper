import reflex as rx


def navbar():
    return rx.box(
        rx.hstack(
            rx.image(src="/spider.png", alt="Logo", width="60px", object_fit="contain"),
            rx.text("My Scraper App", font_size="2xl", font_weight="bold"),
            rx.hstack(
                rx.link("Home", href="/"),
                rx.link("About", href="/about"),
                spacing="4",
            ),
            spacing="4",
            align="center",
        ),
        top="0",
        left="0",
        padding="1em",
        bg="blue.600",
        color="white",
        z_index="1000",
    )

