# SuperPy Inventory Management System

This is the SuperPy Inventory Management System, a command-line tool for managing product inventory. It allows you to perform various operations related to buying and selling products, checking the inventory status, and manipulating the current date.

## Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/your_username/superpy.git
   ```

2. Change to the project directory:

   ```bash
   cd superpy
   ```

3. Install any required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

You can use this tool to interact with the SuperPy Inventory Management System through the following commands:

### Buy a Product

Use the `buy` command to add a new product to the inventory.

```bash
python superpy.py buy --product-name [name] --price [price] --expiration-date [expiration date]
```

- Replace `[name]` with the name of the product.
- Replace `[price]` with the price of the product.
- Replace `[expiration date]` with the expiration date of the product.

Example:

```bash
python superpy.py buy --product-name "Widget" --price 10.99 --expiration-date "2023-12-31"
```

### Sell a Product

Use the `sell` command to remove a product from the inventory when you sell it.

```bash
python superpy.py sell --product-name [name] --price [price]
```

- Replace `[name]` with the name of the product.
- Replace `[price]` with the price at which the product was sold.

Example:

```bash
python superpy.py sell --product-name "Widget" --price 12.99
```

### Report Inventory

You can check the current state of the inventory at a specific time using the `report_inventory` command.

```bash
python superpy.py report_inventory [time]
```

- Replace `[time]` with the date and time you want to check the inventory for (optional).

Example:

```bash
python superpy.py report_inventory "2023-09-05 12:00:00"
```

### Report Current Time

To get the current date and time, use the `report_time` command.

```bash
python superpy.py report_time
```

### Advance Time

Use the `advance_time` command to fast-forward the current date by a specified number of days.

```bash
python superpy.py advance_time [days]
```

- Replace `[days]` with the number of days you want to advance the current time.

Example:

```bash
python superpy.py advance_time 7
```

### Rewind Time

To go back in time, use the `rewind_time` command. This will rewind the current date by a specified number of days.

```bash
python superpy.py rewind_time [days]
```

- Replace `[days]` with the number of days you want to rewind the current time.

Example:

```bash
python superpy.py rewind_time 3
```

### Reset Time

The `reset_time` command allows you to reset the current time to the current date.

```bash
python superpy.py reset_time
```