from tkinter import *

window = Tk()
window.title("Invoice Generator")

medicines = {"medicine A": 10, "medicine B": 22, "medicine C": 22, "medicine D": 22}

invoice_items = []

def calculate_total():
    total = 0.0
    for item in invoice_items:
        total = total + item[2]
    return total

def update_invoice_text():
    invoice_text.delete(1.0, END)
    for item in invoice_items:
        invoice_text.insert(
            END, f"Medicine: {item[0]}, Quantity: {item[1]}, Total: {item[2]}\n")

def add_medicine():
    selected_medicine = medicine_listbox.get(ANCHOR)
    quantity = int(quantity_entry.get())
    price = medicines[selected_medicine]
    item_total= quantity * price
    invoice_items.append((selected_medicine, quantity, item_total))
    print(invoice_items)
    total_amount_entry.delete(0, END)
    total_amount_entry.insert(END,str(calculate_total()))
    update_invoice_text()

medicine_lable = Label(window, text="Medicine: ")
medicine_lable.pack()

medicine_listbox = Listbox(window, selectmode=SINGLE) # only one medicine can be selected
for medicine in medicines:
    medicine_listbox.insert(END, medicine)
medicine_listbox.pack()

quantity_label = Label(window, text="Quantity")
quantity_label.pack()

quantity_entry = Entry(window)
quantity_entry.pack()

add_button = Button(text="add medicine", command=add_medicine)
add_button.pack()

total_amount_label = Label(window, text="Total Amount")
total_amount_label.pack()

total_amount_entry = Entry(window)
total_amount_entry.pack()

customer_label = Label(window, text="Customer Name:")
customer_label.pack()

customer_entry = Entry(window)
customer_entry.pack()

generate_button = Button(window, text="Generate Invoice")
generate_button.pack()

invoice_text = Text(window, height=10, width=50)
invoice_text.pack()


window.mainloop()

#if __name__ == '__main__':
    #print_hi('PyCharm')


