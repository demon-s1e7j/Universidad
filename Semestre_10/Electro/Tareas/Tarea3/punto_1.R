library(ggplot2)

elements <- read.csv("./punto_1.csv")

calculate_n <- function(element) {
  space <- seq(0.4, 0.7, length.out = 100)
  n_values <- element$A + (element$B / space^2)
  data.frame(wavelength = space, n = n_values, element = element$name)
}


plot_data <- calculate_n(elements)

plot_data |>
ggplot(aes(x = wavelength, y = n, color = element)) +
  geom_line() +
  labs(
    x = "Longitud de onda (μm)",
    y = "Índice de refracción n(λ)",
    title = "Índice de refracción según la ecuación de Cauchy"
  ) +
  theme_minimal() +
  theme(legend.title = element_blank())

ggsave("punto_1.png")
