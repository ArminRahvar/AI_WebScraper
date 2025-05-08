import reflex as rx
from .. import components.navbar as navbar
from .. import components.footer as footer


def index():
    return rx.vstack(
        navbar.navbar(),
        rx.separator(color_scheme="gray", color="gray.200"),
        rx.center(
            rx.vstack(
                rx.hstack(
                    rx.text("AI Web Scraper", size="7", font_weight="bold"),
                    rx.image(
                        src="/spider.png",
                        width="100px",
                        object_fit="contain",
                        margin_left="2",
                    ),
                    align="center",
                    spacing="4",
                ),
                rx.input(
                    placeholder="Search something...",
                    value=State.query,
                    on_change=State.set_query,
                    width="300px",
                ),
                rx.button("Search", on_click=State.search),
                rx.text(State.result, font_size="xl", color="gray.700"),
                spacing="2",
            ),
            height="80vh",  # Leave room for navbar/footer
        ),
        footer.footer(),
        spacing="0",  # Adjust to remove default spacing if needed
        align="stretch",
    )