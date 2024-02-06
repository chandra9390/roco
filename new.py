import tkinter as tk

def calculate_profit():
    try:
        selling_price = float(selling_price_entry.get())
        cost_price = float(cost_price_entry.get())
        amazon_referral_fee = float(amazon_referral_fee_entry.get())
        fba_fee = float(fba_fee_entry.get())
        shipping_cost = float(shipping_cost_entry.get())
        monthly_sales = int(monthly_sales_entry.get())

        total_revenue = selling_price * monthly_sales
        total_costs = (cost_price + shipping_cost) * monthly_sales
        total_fees = (amazon_referral_fee + fba_fee) * monthly_sales
        total_profit = total_revenue - total_costs - total_fees

        result_label.config(text=f"Estimated Profit: ${total_profit:.2f}")
    except ValueError:
        result_label.config(text="Invalid input. Please enter numbers.")

# Create the main window
root = tk.Tk()
root.title("Amazon FBA Profit Calculator")

# Create input fields and labels
tk.Label(root, text="Selling Price: $").pack()
selling_price_entry = tk.Entry(root)
selling_price_entry.pack()

tk.Label(root, text="Cost Price: $").pack()
cost_price_entry = tk.Entry(root)
cost_price_entry.pack()

tk.Label(root, text="Amazon Referral Fee: $").pack()
amazon_referral_fee_entry = tk.Entry(root)
amazon_referral_fee_entry.pack()

tk.Label(root, text="FBA Fee: $").pack()
fba_fee_entry = tk.Entry(root)
fba_fee_entry.pack()

tk.Label(root, text="Shipping Cost: $").pack()
shipping_cost_entry = tk.Entry(root)
shipping_cost_entry.pack()

tk.Label(root, text="Monthly Sales: ").pack()
monthly_sales_entry = tk.Entry(root)
monthly_sales_entry.pack()

calculate_button = tk.Button(root, text="Calculate Profit", command=calculate_profit)
calculate_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
