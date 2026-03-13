import tkinter as tk
from tkinter import messagebox

# [player] execVM "loadoutGenerated.sqf"
# file configs
output_file_end = "loadoutGenerated.sqf"

instructions = """1. generate file (loadoutGenerated.sqf) and place into mission folder\n2.In 3DEN editor, place down 
trigger and set it as radio alpha and mark as repeatable.\n3.In trigger onActivation box put this script: [player] 
execVM "loadoutGenerated.sqf"; """


def makeFile():
    imported_filepath = ent_import_filepath.get() + "\\" + output_file_end
    imported_loadout_raw = txt_import_str.get("1.0", "end-1c")
    imported_loadout = imported_loadout_raw.removeprefix("[").removesuffix("]") + ";"
    script = f"""
//removes existing gear
removeAllWeapons player;
removeAllItems player;
removeAllAssignedItems player;
removeUniform player;
removeVest player;
removeBackpack player;
removeHeadgear player;
removeGoggles player;

//sets players loadout
player setUnitLoadout {imported_loadout}
hint"loadout reset :)";
"""
    try:
        if imported_loadout == "" or imported_loadout == " " or imported_loadout == "" or imported_loadout == " ":
            messagebox.showwarning("empty text box", "please put loadout and filepath into textbox")
        else:
            with open(imported_filepath, 'w') as f:
                f.write(script)
                f.close()
                messagebox.showinfo("success", "loadout imported to file")
    except PermissionError as e:
        messagebox.showwarning("Permission error", "double check file path is correct and you have permissions")
# tkinter window


root = tk.Tk()

root.title("Export loadout to file")
root.geometry("600x600")
root.configure(bg="DarkOliveGreen4")

# elements
lbl_import = tk.Label(root, text="Paste mission filepath:", bg="DarkOliveGreen4")
lbl_import.pack()

ent_import_filepath = tk.Entry(root, width=98)
ent_import_filepath.pack()

lbl_import = tk.Label(root, text="Paste loadout:", bg="DarkOliveGreen4")
lbl_import.pack()

txt_import_str = tk.Text(root, width=35, height=10)
txt_import_str.pack()

btn_makeFile = tk.Button(root, text="generate loadout file", command=makeFile, width=35, height=5)
btn_makeFile.pack()

lbl_howTo = tk.Label(root, text=instructions, bg="DarkOliveGreen4")
lbl_howTo.pack()
root.mainloop()
