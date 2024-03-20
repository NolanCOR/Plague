import tkinter.font as tkFont
import tkinter as tk
import tkinter.filedialog as filedialog
import tkinter.simpledialog as simpledialog
import tkinter.messagebox as messagebox
import controller as c
import models as m
import generator as g

range_list = []
sc_list = []
word_list = []

def add_element(listbox,name):
    print(f"{name}\n")
    if (name == "Ranges"):
            control = c.IntRangeChecker()
            new_element = simpledialog.askstring("Add ranges", "Enter a new range:")
            if new_element is not None:
                if(control.is_int_range(new_element)):
                    listbox.insert(tk.END, new_element)
                    aux = new_element[1:-1].split("...")
                    range_list.append(m.Range(int(aux[0]),int(aux[1])))
                else:
                    print("Syntax should be [start...end]")
                
                
                
    elif (name == "Special Characters"):
            control = c.SpecialCharChecker()
            new_element = simpledialog.askstring("Add special characters", "Enter a new special character:")
            if new_element is not None:
                if(control.is_special_char(new_element)):
                    listbox.insert(tk.END, new_element)
                    sc_list.append(m.SpecialCase(new_element))
                else:
                    print("This character is not a special one")
    else :
            control = c.WordChecker()
            new_element = simpledialog.askstring("Add words", "Enter a new word:")
            if new_element is not None:
                if(control.is_word(new_element)):
                    listbox.insert(tk.END, new_element)
                    
                    word_list.append(m.Word(new_element))
                else:
                    print("This is not a word")
    


def delete_element(listbox):
    selection = listbox.curselection()
    if selection:
        listbox.delete(selection[0])

def select_output_directory():
    try:
        output_path = filedialog.askdirectory(title="Select Output Directory",initialdir=".")            
        if not output_path:
            messagebox.showerror("Output Directory Not Selected", "No output directory selected.")
            
        # Create list of models
        model_list = range_list + word_list + sc_list
        generator = g.GeneratorWordRange(model_list)
        generator.generate(outputdir=output_path+'/pwd_list.txt')
        generator = g.GeneratorWordRangeSpe(model_list)
        generator.generate(outputdir=output_path+'/pwd_list.txt')
        generator = g.GeneratorWordSpeRange(model_list)
        generator.generate(outputdir=output_path+'/pwd_list.txt')

    except Exception as e:
        messagebox.showerror("Error Selecting Output Directory", f"An error occurred while selecting the output directory:\n{e}")

root = tk.Tk()
root.title("Tkinter Interface")
root.configure(bg="#222222")

frame = tk.Frame(root, bg="#222222")
frame.pack(fill=tk.BOTH, expand=True)

left_frame = tk.Frame(frame, width=200, bd=2, relief=tk.GROOVE, bg="#333333")
left_frame.pack(side=tk.LEFT, fill=tk.BOTH)

sections = [("Ranges", "listbox1"),
            ("Special Characters", "listbox2"),
            ("Words", "listbox3")]

for section_name, listbox_var in sections:
    section_frame = tk.LabelFrame(left_frame, text=section_name, bg="#333333", fg="#cccccc")
    section_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    listbox = tk.Listbox(section_frame, width=30, height=10, bg="#444444", fg="#cccccc", bd=0, highlightthickness=0)
    listbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    vars()[listbox_var] = listbox

    add_button = tk.Button(section_frame, text="+", command=lambda section_name=section_name,listbox=listbox :add_element(listbox,section_name), bg="#555555", fg="#cccccc")
    add_button.pack(side=tk.LEFT, padx=10, pady=5)

    delete_button = tk.Button(section_frame, text="🗑", command=lambda listbox=listbox:  delete_element(listbox), bg="#555555", fg="#cccccc")
    delete_button.pack(side=tk.LEFT, padx=10, pady=5)
    



summary_frame = tk.Frame(frame, bg="#333333")
summary_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

summary_label = tk.Label(summary_frame, text="Summary:", font=tkFont.Font(size=16, family="Helvetica"), bg="#333333", fg="#cccccc")
summary_label.pack(side=tk.TOP, padx=10, pady=10)

summary_text = tk.Text(summary_frame, width=50, height=20, bg="#444444", fg="#cccccc", bd=0, highlightthickness=0)
summary_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

bottom_frame = tk.Frame(root, bg="#333333")
bottom_frame.pack(side=tk.BOTTOM, fill=tk.X)

button = tk.Button(bottom_frame, text="Generate password list", bg="#555555", fg="#cccccc",command=select_output_directory)
button.pack(side=tk.RIGHT, padx=10, pady=10)

root.mainloop()
