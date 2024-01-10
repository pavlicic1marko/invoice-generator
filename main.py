from tkinter import *

window = Tk()
window.title("Invoice Generator")

medicines = {"medicine A": 10, "medicine B": 22}

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

add_button = Button(text="add medicine")
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


