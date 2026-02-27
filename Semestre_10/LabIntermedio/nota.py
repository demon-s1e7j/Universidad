class Contribution:
    def __init__(self, note: int | float, percentage: int | float) -> None:
        self.note = note
        self.percentage = percentage * (1/100)
        self.cont = self.note * self.percentage

notas = [
    Contribution(54.8, 12),
    Contribution(70.37, 12),
    Contribution(65.4, 42),
    Contribution(47.81, 6),
    Contribution(87.67, 15),
    Contribution(100, 3),
    Contribution(98.57, 10)
]

final_note = sum([x.cont for x in notas])
is_total = sum([x.percentage for x in notas]) == 1.0

print(final_note, is_total)
