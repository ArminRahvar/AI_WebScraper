import reflex as rx
from AI_WebScraper.components.navbar import navbar
from AI_WebScraper.components.footer import footer

@rx.page(route="/about")
def about():
    return rx.vstack(
        navbar(),
        rx.box(height="2em"),

        rx.center(
            rx.vstack(
                rx.heading("About My Scraper App", size="3", color="purple.600"),
                rx.text(
                    "Welcome to the AI Web Scraper App! 🚀",
                    font_size="xl",
                    color="gray.600",
                    font_weight="medium",
                ),
                rx.box(height="1em"),
                rx.text(
                    "🔍 This app is designed to help you easily extract and analyze data from websites. Whether you're researching or automating data collection, this tool is made to save you time and effort.",
                    font_size="lg",
                    line_height="1.8",
                    color="gray.700",
                    padding_x="4",
                    max_width="800px",
                    text_align="center",
                ),
                rx.box(height="2em"),
                rx.heading("✨ Features", size="3", color="purple.500"),
                rx.unordered_list(
                    rx.list_item("⚙️ Simple and intuitive interface."),
                    rx.list_item("🐍 Powered by Python and Reflex."),
                    rx.list_item("🧩 Easily customizable scraping logic."),
                    rx.list_item("📊 Clean display of search results."),
                    spacing="2",
                    padding_left="6",
                    font_size="md",
                    color="gray.600",
                ),
                rx.box(height="2em"),
                rx.text(
                    "Built with ❤️ using Reflex & Python.",
                    font_size="md",
                    font_style="italic",
                    color="gray.500",
                ),
                spacing="4",
                align="center",
                padding="4",
            ),
            padding_y="7",
            width="100%",
        ),

        footer(),
        display="flex",
        flex_direction="column",
        justify_content="space-between",
    )
