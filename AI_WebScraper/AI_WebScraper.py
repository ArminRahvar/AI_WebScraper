import reflex as rx

from rxconfig import config
from AI_WebScraper.components import navbar, footer
from AI_WebScraper.backend.states import State




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
                rx.input(
                    placeholder="what do you want to scrape?",
                    value=State.prompt,
                    on_change=State.set_prompt,
                    width="200px"
                ),
                rx.button("Scrape", on_click=State.search),
                rx.text(State.result, font_size="xl", color="gray.700"),
                spacing="2",
            ),
            height="80vh",  # Leave room for navbar/footer
        ),
        footer.footer(),
        spacing="0",  # Adjust to remove default spacing if needed
        align="stretch",
    )


app = rx.App(
    theme=rx.theme(appearance="dark",
                   accent_color="violet")
                   )

app.add_page(index)
