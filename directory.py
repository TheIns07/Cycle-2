import tkinter as tk

#Creación de la clase de contacto
class Contacto:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

class DirectoryApp:
    #Se instancia el constructor 
    def __init__(self):
        #Arreglo para objeto Contacto
        self.contacts = []

        #Creación del Frame
        self.root = tk.Tk()
        self.root.title("Directorio Telefónico")
        self.root.geometry("600x300")

        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(pady=2)

        #Input y labels para introducirdatos
        self.name_label = tk.Label(self.main_frame, text="Nombre:")
        self.name_label.grid(row=0, column=0, padx=10, pady=5)
        self.name_input = tk.Entry(self.main_frame)
        self.name_input.grid(row=0, column=1, padx=10, pady=5)

        self.phone_label = tk.Label(self.main_frame, text="Teléfono:")
        self.phone_label.grid(row=1, column=0, padx=10, pady=5)
        self.phone_input = tk.Entry(self.main_frame)
        self.phone_input.grid(row=1, column=1, padx=10, pady=5)

        #Boton de accion para agregar contacto
        self.add_button = tk.Button(self.main_frame, text="Agregar", command=self.add_contact)
        self.add_button.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

        self.contacts_listbox = tk.Listbox(self.root, width=50)
        self.contacts_listbox.pack(padx=10, pady=5)

        self.show_contacts()

        self.root.mainloop()

    def add_contact(self):
        #Obtener los datos de los inputs
        name = self.name_input.get()
        phone = self.phone_input.get()

        #Creación del objeto contacto
        contact = Contacto(name, phone)
        #Relleno del arreglo
        self.contacts.append(contact)

        #Limpiar los inputs principales
        self.name_input.delete(0, tk.END)
        self.phone_input.delete(0, tk.END)

        self.show_contacts()

    def show_contacts(self):
        #Limpieza de la lista de contactos (evitar acumulación de datos en el listbox)
        self.contacts_listbox.delete(0, tk.END)

        for contact in self.contacts:
            self.contacts_listbox.insert(tk.END, f"Nombre: {contact.name}, Teléfono: {contact.phone}")

app = DirectoryApp()

