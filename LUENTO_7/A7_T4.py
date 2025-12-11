from dataclasses import dataclass

DELIMITER = ";"


@dataclass
class TIMESTAMP:
    weekday: str = ""
    hour: str = ""
    consumption: float = 0.0
    price: float = 0.0


def read_timestamps(filename: str) -> list[TIMESTAMP]:
    timestamps: list[TIMESTAMP] = []

    print(f'Reading file "{filename}".')

    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                row = line.rstrip()

                if row == "":
                    continue

                columns = row.split(DELIMITER)
                ts = TIMESTAMP()

                ts.weekday = columns[0]
                ts.hour = columns[1]
                ts.consumption = float(columns[2])
                ts.price = float(columns[3])

                columns.clear()
                timestamps.append(ts)

    except FileNotFoundError:
        print("Error: File not found.")
        return []

    return timestamps


def main():
    print("Program starting.")
    filename = input("Insert filename: ")

    timestamps = read_timestamps(filename)

    print("Electricity usage:")

    total_consumption = 0.0
    total_price = 0.0

    for ts in timestamps:
        total = ts.consumption * ts.price
        total_consumption += ts.consumption
        total_price += total

        print(
            f" - {ts.weekday} {ts.hour}, "
            f"price {ts.price:.2f}, "
            f"consumption {ts.consumption:.2f} kWh, "
            f"total {total:.2f} €"
        )

    print(f"Program ending.")


if __name__ == "__main__":
    main()
